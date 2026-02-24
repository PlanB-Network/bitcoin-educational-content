---
name: Introdução ao Bitcoin mining
goal: Compreender o Bitcoin mining e o proof-of-work a partir do zero
objectives: 


  - Compreender a proof-of-work e o seu papel na Bitcoin.
  - Analisar o mecanismo de ajustamento da dificuldade.
  - Saber o que significam os termos técnicos associados ao mining.
  - Descrever os passos envolvidos na construção de um bloco Bitcoin e dos seus componentes.
  - Identificar os principais desenvolvimentos no sector do mining.


---

# Descobrir os fundamentos do Bitcoin mining



Compreender o proof of work é compreender o funcionamento do Bitcoin. Sem essa invenção e seu uso engenhoso, o Bitcoin simplesmente não poderia ter existido. Este curso fornece-lhe toda a teoria do mining de que necessita para a sua viagem no bitcoin.



O MIN 101 destina-se principalmente a principiantes, uma vez que explica todos os conceitos precisamente a partir do zero. No entanto, se já possui um nível intermédio de conhecimentos, este curso permitir-lhe-á consolidar a sua compreensão, corrigir algumas intuições aproximadas e explorar pormenores frequentemente ausentes das explicações habituais.



No final deste curso, será capaz de explicar o funcionamento do proof-of-work de uma forma simples e rigorosa. O MIN 101 é também uma introdução ideal a todos os outros cursos mais avançados dedicados ao Bitcoin, mining e Plan ₿ Academy, quer sejam teóricos ou práticos.



+++


# Introdução


<partId>041ff0fa-53c3-4d55-9888-d7840de283e9</partId>



## Descrição geral do curso


<chapterId>a82d49dc-d68a-4e3f-985e-bcef6643677e</chapterId>



Bem-vindo ao curso MIN 101, no qual descobrirá os conceitos teóricos fundamentais do mining e do Proof-of-Work dentro do sistema Bitcoin. Este curso é o primeiro passo na sua viagem de bitcoiner para compreender como funciona o mining. Depois de o concluir, poderá avançar para cursos teóricos mais avançados, ou pôr mãos à obra e tornar-se um mineiro de bitcoin!



Neste curso MIN 101, não voltaremos a rever os conceitos básicos de Bitcoin, pois iremos diretamente ao cerne da questão: mining. Se nunca ouviu falar do Bitcoin, ou se os seus fundamentos ainda não são muito claros para si, recomendo vivamente que comece com o nosso curso introdutório BTC 101. Assim que tiver adquirido estes fundamentos, será capaz de abordar o MIN 101 com confiança:



https://planb.academy/courses/2b7dc507-81e3-4b70-88e6-41ed44239966


### Parte 1 - Introdução



Vamos começar este curso com um primeiro capítulo opcional, no qual apresento uma explicação muito simplificada do mining, para lhe dar uma imagem mental clara antes de entrar nos mecanismos técnicos.



O objetivo aqui não é fornecer todos os detalhes técnicos (eles virão mais tarde no curso), mas dar-lhe um fio condutor. Uma vez criada esta estrutura, cada conceito mais avançado introduzido posteriormente enquadrar-se-á naturalmente nesta estrutura.



### Parte 2 - Como funciona o proof of work



Após a introdução, a Parte 2 é a base técnica do programa de formação. O seu objetivo é explicar, passo a passo, como o Bitcoin produz blocos válidos. Começaremos por descobrir a estrutura de um bloco, antes de entrar no mecanismo do proof-of-work: o papel do alvo, o nonce e a função hash. Finalmente, veremos como o Bitcoin consegue manter uma taxa de produção de blocos estável apesar das variações no poder do hash, graças ao mecanismo de ajuste de dificuldade. No final desta secção, terá uma compreensão completa dos princípios fundamentais do Bitcoin do proof-of-work.



### Parte 3 - O sistema de incentivos Bitcoin mining



Na terceira parte, veremos porque é que os mineiros são encorajados a participar honestamente no mining. Detalharemos o princípio da recompensa do bloco, a sua composição e método de cálculo, a sua evolução ao longo do tempo através de halvings e o papel específico da transação coinbase.



### Parte 4 - A indústria Bitcoin mining



A quarta parte coloca o mining de volta à sua realidade operacional. Traça a evolução das máquinas mining, desde o início do Bitcoin até ao moderno ASIC, de modo a compreender as actuais restrições de hardware. Também analisamos os princípios básicos dos pools do mining, para compreender como os mineiros conseguem reduzir a variação dos seus rendimentos.



### Parte 5 - Secção final



Na parte final do curso, pode testar os seus conhecimentos sobre o mining, obtendo o seu diploma.



O objetivo deste curso MIN 101 é, portanto, permitir-lhe sair com uma compreensão clara, estruturada e duradoura do Bitcoin mining, tanto técnica como economicamente.



Pronto para descobrir o Bitcoin mining? Vamos lá começar!




## Bitcoin mining fácil


<chapterId>278577a6-98bb-4659-86c7-f6c4f6d5fa3e</chapterId>



Antes de passar a uma explicação detalhada e mais técnica do Bitcoin [mining](https://planb.academy/resources/glossary/mining), gostaria de lhe dar uma visão geral do princípio, que é deliberadamente simples e esquemático. Se já tem alguns conhecimentos básicos, pode ir diretamente ao cerne da questão no próximo capítulo, depois de responder às perguntas do questionário. Este capítulo destina-se principalmente a principiantes, para lhe dar um bom começo.



Imagine o Bitcoin como um grande caderno público, partilhado por todos, onde anotamos quem enviou bitcoins a quem. Este caderno chama-se "[blockchain](https://planb.academy/resources/glossary/blockchain)". Não pode ser guardado por uma só pessoa, caso contrário teria de ser de confiança. Em vez disso, o Bitcoin funciona coletivamente: milhares de computadores verificam e mantêm a mesma versão deste caderno.



![Image](assets/fr/049.webp)



No Bitcoin, quando efectua um pagamento, cria uma [transação](https://planb.academy/resources/glossary/transaction-tx). Esta transação não é imediatamente adicionada à caderneta. É primeiro enviada para a rede e depois espera para ser integrada no pacote de transação seguinte. Este pacote é designado por [bloco](https://planb.academy/resources/glossary/block).



![Image](assets/fr/050.webp)



Um bloco é simplesmente um conjunto de transacções agrupadas. Quando um bloco está pronto, não basta publicá-lo. É preciso provar à rede que o bloco é digno de ser adicionado à pool. É aqui que entra o mining.



Mining é o trabalho de validação de um bloco através do consumo de energia. Os actores chamados [mineiros](https://planb.academy/resources/glossary/miner) utilizam computadores especializados. Estas máquinas consomem eletricidade para realizar um número muito elevado de testes, em ciclo, até encontrarem uma prova que a rede aceite. Quando um mineiro encontra esta prova, o seu bloco é considerado válido.



Uma vez validado, o bloco é transmitido para a rede. Os outros [nós](https://planb.academy/resources/glossary/node) verificam rapidamente se está em conformidade com as regras e adicionam-no à sequência de blocos anteriores. É por isso que se chama "blockchain": cada novo bloco vem depois dos outros, por ordem sequencial, e esta cadeia cresce pouco a pouco.



![Image](assets/fr/051.webp)



Em suma, as transacções são primeiro criadas. Depois, são agrupadas num bloco. Depois, um mineiro valida este bloco consumindo eletricidade. Finalmente, este bloco é adicionado à cadeia de blocos e as transacções que contém são [confirmadas](https://planb.academy/resources/glossary/confirmation).



Se os mineiros consomem eletricidade, não é por serem voluntários. Fazem-no porque há uma recompensa. Quando um mineiro valida um bloco, recebe dois tipos de rendimento. Por um lado, recebe bitcoins recém-criados. Por outro, recolhe as [taxas](https://planb.academy/resources/glossary/transaction-fees) pagas pelos utilizadores pelas transacções incluídas no bloco. Por outras palavras, o mineiro é compensado tanto pela emissão monetária programada como pelas taxas de transação determinadas por um mercado.



Nesta fase, é-lhe dada deliberadamente uma visão muito simples do mining. Ainda não explica como o bloco é construído em detalhe, ou como funciona exatamente a prova que os mineiros procuram, ou como o Bitcoin mantém um ritmo constante, ou como a recompensa é calculada com precisão, ou como é reclamada. Não faz mal, isso é tudo o que vamos ver no resto deste curso MIN 101!



O objetivo deste capítulo era simplesmente dar-lhe uma estrutura mental clara: transacções → blocos → mining → blockchain → recompensa. Tenha em mente esta cadeia de ideias. No resto do curso, cada capítulo adicionará uma camada de detalhes técnicos sobre um desses elementos, até que você entenda não apenas o que está acontecendo, mas como e por que ele funciona de forma confiável, em escala, sem um chefe e sem precisar de confiança.



# Como funciona o proof of work


<partId>e917e8e3-37f2-46fb-91b2-6a5ce6f0f5c3</partId>



## O caminho da transação Bitcoin


<chapterId>3b7a3502-4814-4554-8de1-86ac961a2958</chapterId>



Para entender o que é o Bitcoin mining, precisamos primeiro seguir o caminho de uma transação típica do Bitcoin. Isto irá mostrar-lhe exatamente onde é que o bloco entra em jogo e porque é que está no centro do sistema. É isso que eu gostaria que você descobrisse neste primeiro capítulo.



No Bitcoin, uma transação é uma estrutura de dados que transfere a propriedade de bitcoins de um utilizador para outro. Em termos concretos, consome `outputs` de transacções passadas (as chamadas [UTXOs](https://planb.academy/resources/glossary/utxo)), referindo-se a elas como `inputs`, e depois cria novos `outputs` que definem a quem pertencem agora esses bitcoins e em que condições podem ser gastos mais tarde.



![Image](assets/fr/001.webp)



Um ponto importante sobre o Bitcoin é a autorização para gastar. Os Bitcoin não estão numa conta, como o seu dinheiro no banco, mas estão bloqueados por condições de despesa. Quando um [wallet](https://planb.academy/resources/glossary/wallet) quer utilizar um UTXO como [entrada](https://planb.academy/resources/glossary/input), deve fornecer uma prova criptográfica de que tem o direito de o desbloquear. Essa prova geralmente assume a forma de uma [assinatura digital](https://planb.academy/resources/glossary/digital-signature) generated de uma [chave privada](https://planb.academy/resources/glossary/private-key). É por isso que os bitcoiners insistem em proteger as suas chaves privadas: são elas que desbloqueiam o acesso aos seus bitcoins e, consequentemente, permitem-lhe gastá-los.



![Image](assets/fr/002.webp)



A assinatura digital no Bitcoin desempenha duas funções importantes:




- Autorizar despesas: prova que o utilizador possui a chave privada prevista na condição de despesas UTXO;
- Proteção da integridade: liga a autorização aos detalhes exactos da transação (destinatários, montantes, taxas, etc.). Se alguém alterar a transação posteriormente, a assinatura deixará de ser válida.



Depois de a transação ter sido corretamente construída e assinada pelo Bitcoin wallet do utilizador, deve ser difundida na rede Bitcoin.



### O papel do nó Bitcoin na distribuição



O Bitcoin é uma rede [peer-to-peer](https://planb.academy/resources/glossary/peertopeer-p2p): não existe um servidor central que receba e processe todas as transacções. Este papel é desempenhado coletivamente pelos nós. Um nó Bitcoin é uma peça de software (por exemplo, [Bitcoin Core](https://planb.academy/resources/glossary/bitcoin-core)) ligada a outros nós na rede Bitcoin, cuja principal missão é verificar, armazenar e retransmitir transacções e blocos.



Quando envia uma transação a partir de um wallet, o wallet encaminha-a para um nó (o seu próprio nó ou o de um serviço). Este nó verifica primeiro se a transação está em conformidade com várias regras, tais como:




- as assinaturas são válidas;
- as entradas referem UTXOs existentes (ou seja, bitcoins que existem);
- estes UTXO não tenham já sido gastos noutro local;
- a quantidade de [outputs](https://planb.academy/resources/glossary/output) é menor ou igual à quantidade de inputs (os bitcoins não são criados a partir do nada);
- etc.



Se a transação passar em todas estas verificações, o nó propaga a transação aos outros nós da rede a que está ligado. Estes, por sua vez, verificam-na e retransmitem-na, e assim sucessivamente. Numa questão de segundos, a transação é propagada e torna-se conhecida por toda, ou pelo menos por uma grande parte, da rede Bitcoin.



![Image](assets/fr/003.webp)



### O mempool: a sala de espera das transacções



Entre o momento em que uma transação é transmitida e o momento em que é confirmada em um bloco, ela deve esperar. Esta área de espera é chamada de **[mempool](https://planb.academy/resources/glossary/mempool)** (contração de `memory` e `pool`). Um mempool é, portanto, um espaço de armazenamento temporário para transacções válidas, mas ainda não confirmadas.



Ponto importante: não existe um único mempool, apenas mempools. Cada nó mantém o seu próprio mempool, com as suas próprias restrições locais. Isto significa que, num dado momento, dois nós podem ter conteúdos de mempool ligeiramente diferentes (dependendo do que receberam, do que rejeitaram ou do que purgaram).



![Image](assets/fr/004.webp)



Nesta fase, a rede tem conhecimento da transação, verificou-a e mantém-na em memória até ser confirmada. Mas a confirmação desta transação só ocorrerá quando um mineiro a inserir num bloco e este bloco for aceite pela rede.



### Blockchain: um registo público de marcação de tempo



Como a bitcoin é uma moeda intangível, tem de resolver um problema: evitar a [duplicação de gastos](https://planb.academy/resources/glossary/double-spending-attack) sem uma autoridade central. Se duas transacções tentarem gastar o mesmo UTXO, todos devem ser capazes de convergir para um estado único e coerente. O Satoshi Nakamoto resume esta questão com esta famosa frase:



> A única forma de confirmar a ausência de uma transação é estar atento a todas as transacções.

Por outras palavras, para saber se um bitcoin ainda não foi gasto, é necessário um registo comum de gastos anteriores.



É este o papel da blockchain: um registo público que contém o histórico das transacções. Mas, em vez de escrever cada transação à medida que ela acontece, o Bitcoin agrupa-as em blocos. Cada bloco funciona como uma página de histórico, e o sistema funciona assim como um servidor de carimbo de tempo: ordena as transacções ao longo do tempo de uma forma verificável.



Este registo não pode ser reescrito, graças a um princípio simples: cada bloco inclui a impressão digital criptográfica ([hash](https://planb.academy/resources/glossary/hash-function)) do bloco anterior. Assim, os blocos estão ligados entre si: se modificarmos um bloco do passado, o seu hash altera-se, o que quebra a ligação com o bloco seguinte, que quebra a ligação com o bloco seguinte, e assim por diante. É esta cadeia de dependências que dá o nome à "*blockchain*".



![Image](assets/fr/005.webp)



Uma vez compreendidos estes princípios básicos do Bitcoin, podemos descrever o objetivo de um mineiro em termos mais concretos: construir um novo bloco que amplie a cadeia existente, inscrevendo transacções pendentes, e depois tentar torná-lo válido (este é o famoso "[proof of work](https://planb.academy/resources/glossary/proof-of-work)" que estudaremos num capítulo posterior). Mas primeiro, vamos descobrir juntos, no próximo capítulo, como se constrói um bloco candidato.



## Construção de um bloco Bitcoin


<chapterId>2b5cd04b-d400-4865-b0a0-e70fa7e67c17</chapterId>



Já percebeu como funciona uma transação Bitcoin e o papel da cadeia de blocos. No entanto, antes de analisarmos mais pormenorizadamente o funcionamento do proof-of-work, há ainda um passo essencial que o mineiro deve executar: a construção de um [bloco candidato](https://planb.academy/resources/glossary/candidate-block). Vamos descobrir juntos o que é um bloco candidato e como o mineiro o constrói, antes de embarcarmos na busca de uma prova válida.



### O bloco candidato



Os Miner têm de construir eles próprios os seus blocos antes de os tentarem minerar. Cada mineiro, por sua vez, constrói o que é conhecido como um bloco candidato a partir das transacções pendentes no seu mempool. A construção de um bloco candidato consiste, portanto, em:




- escolher as transacções a incluir;
- organizar estas transacções de uma forma compatível com as regras Bitcoin;
- produzem os metadados do bloco, armazenados no seu [cabeçalho](https://planb.academy/resources/glossary/block-header).



A escolha das transacções obedece a uma lógica económica simples: um bloco tem uma capacidade limitada pelo protocolo Bitcoin, pelo que o mineiro procura maximizar o que ganha por esse espaço. O mineiro seleciona prioritariamente as transacções que oferecem as taxas mais elevadas em relação ao espaço que ocupam no bloco (é a chamada "taxa de taxa", expressa em sats/vB). Os pormenores das taxas serão tratados mais tarde; basta recordar a ideia de ordenar por eficiência de espaço.



Por conseguinte, um bloco Bitcoin é composto por duas partes principais:




- uma lista de transacções;
- um cabeçalho de bloco, que serve, de certa forma, como bilhete de identidade do bloco.



![Image](assets/fr/006.webp)



O cabeçalho é essencial, uma vez que é utilizado como base para o proof-of-work: no Bitcoin, não se extrai diretamente um bloco inteiro; extrai-se apenas o cabeçalho de um bloco, que resume a informação necessária para ligar o bloco à cadeia e comprometer o seu conteúdo. Para permitir que o cabeçalho represente todas as transacções, o Bitcoin utiliza uma ferramenta criptográfica: a [árvore de Merkle](https://planb.academy/resources/glossary/merkle-tree).



### A árvore de Merkle: resumir um grande conjunto de transacções



Listar todas as transacções no cabeçalho seria impossível: um bloco pode conter milhares de transacções, enquanto o cabeçalho tem um tamanho fixo (80 bytes). A solução é, portanto, calcular um hash único que depende de todas as transacções do bloco: é a [raiz de Merkle](https://planb.academy/resources/glossary/merkle-root).



O princípio é o seguinte:




- é calculada a impressão digital criptográfica (hash) de cada transação;
- estes hashes são emparelhados, concatenados e, em seguida, submetidos a um novo hash para formar uma nova camada de hashes;
- este processo é repetido até se obter um único hash final: a raiz de Merkle.



![Image](assets/fr/007.webp)



Assim, se uma única transação for alterada, mesmo que seja por um único bit, o resultado é uma modificação da sua impressão digital, que se propaga para a raiz Merkle. Esta raiz está incluída no cabeçalho do bloco. Assim, modificar uma transação passada significa modificar o cabeçalho do bloco em que está incluída e, por conseguinte, a pegada do bloco e, depois, a ligação com os blocos subsequentes.



Desde o [SegWit](https://planb.academy/resources/glossary/segwit), separámos as assinaturas do resto. Assim, na realidade, existem 2 árvores de Merkle aninhadas em cada bloco. Esta separação tem consequências para a forma como contamos o tamanho de um bloco e para certos compromissos criptográficos, mas a ideia básica continua a ser a mesma: o cabeçalho deve comprometer, de forma compacta, todo o conteúdo do bloco.



### Cabeçalho do bloco



O cabeçalho do bloco tem 80 bytes de comprimento e contém exatamente 6 campos. São estes seis elementos que serão submetidos a um processo de hash aquando da pesquisa de um proof of work (ver capítulo seguinte):





- A versão (`version`): Indica quais as regras ou sinais de atualização a que o bloco obedece. Serve como um mecanismo para manter a compatibilidade e a evolução do protocolo.




- Hash do bloco anterior (`previousblockhash`): Este é o hash do cabeçalho do bloco anterior. É o que liga os blocos entre si. Sem este campo, teríamos blocos independentes. Ao incluir o hash do cabeçalho do bloco anterior, obtemos uma cadeia, onde cada novo bloco se baseia no anterior.





- Raiz Merkle (`merkleroot`): Esta é a impressão digital de todas as transacções no bloco (através da árvore Merkle). Liga o cabeçalho ao conteúdo: se o mineiro modificar a seleção ou a ordem das transacções, a raiz muda.





- [Carimbo de tempo](https://planb.academy/resources/glossary/timestamp): Este é um carimbo de tempo (hora Unix) escolhido pelo mineiro (com restrições de validade), que deve indicar quando o bloco foi extraído. Não tem de ser perfeitamente exato ao segundo, mas deve cumprir determinadas condições para permanecer aceitável para a rede.





- Objetivo de dificuldade codificado (`nbits`): Este campo codifica o [alvo de dificuldade](https://planb.academy/resources/glossary/difficulty-target) atual. Nós entraremos em mais detalhes no capítulo sobre dificuldade, mas lembre-se que este parâmetro é parte do cabeçalho.





- [Nonce](https://planb.academy/resources/glossary/nonce) (`nonce`): Este é um valor que o mineiro pode modificar livremente. Serve como uma variável ajustável durante o proof-of-work. Explicarei o seu papel com mais pormenor no próximo capítulo, mas é importante compreender que o nonce faz parte do cabeçalho do bloco e foi concebido para permitir tentativas sucessivas.



Para facilitar a visualização, eis um exemplo de um cabeçalho de bloco em formato hexadecimal (80 bytes):



```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```



Segue-se uma análise campo a campo:



```text
version: 00e0ff3f
previousblockhash: 5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
merkleroot: 206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
time: bcb13a64
nbits: b2e00517
nonce: 43f09a40
```



Este cabeçalho de bloco candidato, construído pelo mineiro, constitui a base do seu trabalho. Quando se procura um proof-of-work válido, não é a lista completa de transacções que é diretamente hash num loop, mas sim este bloco de 80 bytes, que contém tudo o que é necessário para ligar o bloco ao passado e confirmar o seu conteúdo, incluindo também os parâmetros necessários para o mecanismo mining, que exploraremos no próximo capítulo.



## O hash, o alvo e o nonce


<chapterId>d054323b-16bd-4556-bac5-4878654e59a3</chapterId>



Nos capítulos anteriores, seguiu o caminho de uma transação Bitcoin: criada e assinada por um wallet, retransmitida por nós, armazenada em mempools, depois confirmada quando um mineiro a inclui num bloco aceite pela rede. Mas ainda não vimos como um mineiro pode adicionar seu bloco ao blockchain. Qual é o processo por trás do mining?



Compreender o processo mining é bastante simples. Resume-se a 3 conceitos que andam de mãos dadas: uma função hash, um valor alvo e uma variável que o mineiro pode modificar. Vejamos como tudo isto funciona.



### A função de hash



Uma função de hash é uma ferramenta que recebe uma mensagem como entrada e produz uma saída de tamanho fixo, denominada "*fingerprint*" ou "*hash*".



![Image](assets/fr/010.webp)



A função hash é interessante em sistemas informáticos porque tem certas propriedades:





- Se alterarmos um único bit da entrada, o hash de saída resultante altera-se completamente e de forma imprevisível;



![Image](assets/fr/011.webp)





- É impossível passar do output para o input: a função é irreversível;



![Image](assets/fr/012.webp)





- É impossível encontrar duas mensagens diferentes que dêem exatamente o mesmo hash.



![Image](assets/fr/013.webp)



A função hash utilizada no Bitcoin para o mining é o `SHA256`, aplicado duas vezes seguidas. Isto é conhecido como duplo [SHA256](https://planb.academy/resources/glossary/sha256), ou `SHA256d`. É este duplo hashing que produz a impressão digital do bloco.



```text
hash = SHA256(SHA256(message))
```



No nosso caso, a `mensagem` corresponde de facto ao cabeçalho do bloco, que viu no capítulo anterior. Como lembrete, o cabeçalho é uma pequena estrutura que resume tudo no bloco.



![Image](assets/fr/014.webp)



### Prova de trabalho: encontrar um hash mais pequeno do que o objetivo



O Proof-of-Work é frequentemente descrito como a resolução de um problema complexo. Na realidade, não é tanto um problema quanto uma busca por tentativa e erro: o minerador deve encontrar uma versão do cabeçalho cujo hash (depois de passar pela função hash `SHA256d`) respeite uma condição simples: deve ser menor que um determinado alvo.



Esta condição é formulada da seguinte forma:




- o hash do cabeçalho do bloco é calculado utilizando uma função de hash;
- interpretamos este hash como um número;
- para que o bloco seja válido, este número deve ser inferior ou igual a um valor denominado "*alvo de dificuldade*".



Por outras palavras, um bloco é válido se:



```text
SHA256d(block_header) <= target
```



![Image](assets/fr/015.webp)



O alvo é um número de 256 bits. Como o hash produzido pelo `SHA256d` também tem 256 bits, eles podem ser comparados como dois números. Quanto menor o alvo, mais difícil é a condição, pois há menos resultados possíveis abaixo desse limite. Inversamente, quanto maior o objetivo, mais fácil é satisfazer a condição e mais fácil se torna minerar um bloco. Iremos analisar mais detalhadamente a forma como este objetivo é determinado em capítulos posteriores.



Neste sistema, a função hash é interessante. Lembre-se que é fácil calcular a saída a partir da entrada, mas é impossível encontrar uma entrada conhecendo apenas a saída da função. No mining, os mineiros não são solicitados a encontrar um hash preciso, mas sim a encontrar um hash abaixo de um valor alvo. A única forma de o conseguir é fazer um grande número de tentativas, até que um determinado cabeçalho do seu bloco candidato, quando submetido a hash, produza um hash inferior a este objetivo.



Quando o objetivo é suficientemente baixo, este processo torna-se dispendioso. O mineiro calcula o hash do cabeçalho do seu bloco candidato, verifica o resultado e, se a condição não for cumprida, modifica o cabeçalho e repete o cálculo. Este ciclo repete-se até ser encontrado um cabeçalho válido. Quando o hash do cabeçalho satisfaz finalmente a condição, o proof of work é estabelecido, o bloco é considerado válido e pode ser difundido na rede Bitcoin para que os nós o adicionem à sua cadeia de blocos. O mineiro vencedor recebe então a recompensa associada (detalharemos a sua composição mais tarde), enquanto todos os mineiros partem imediatamente em busca de um novo cabeçalho válido para o bloco seguinte.



A vantagem fundamental deste mecanismo reside na sua assimetria. Produzir um proof of work é dispendioso para os mineiros, pois requer um grande número de cálculos de hash. Por outro lado, para os verificadores, ou seja, os nós da rede, a verificação é extremamente simples: basta fazer o hash do cabeçalho do bloco fornecido pelo mineiro e verificar se o hash resultante é efetivamente inferior ao objetivo. Encontrar uma prova requer, portanto, muito trabalho e recursos, ao passo que verificar a sua validade é rápido e pouco dispendioso. É precisamente esta propriedade que define um sistema proof-of-work eficiente.



### O nonce



Subsiste uma questão prática: se o cabeçalho do bloco candidato construído pelo mineiro não fornecer um hash válido, como é que o mineiro pode tentar novamente? Ele precisa de modificar algo no cabeçalho para obter um hash diferente. É precisamente este o papel do nonce.



Lembre-se da primeira propriedade de uma função de hash: basta alterar um único bit da entrada para produzir um hash de saída totalmente diferente e imprevisível. Cada cálculo de hash é, portanto, semelhante a um sorteio aleatório.



![Image](assets/fr/016.webp)



Para tentar a sua sorte novamente, o mineiro não precisa de modificar todo o cabeçalho do seu bloco candidato: só precisa de alterar uma pequena parte, porque mesmo um único bit diferente resultará num hash completamente novo, potencialmente válido se for mais pequeno do que o objetivo.



É exatamente por isso que o cabeçalho do bloco contém um nonce. O nonce é um valor de 32 bits, utilizado uma vez e depois substituído. Em termos práticos, para o mesmo bloco candidato, um mineiro pode testar cerca de 4,29 mil milhões de valores possíveis (de `0` a `2^32 - 1`). Cada variação do nonce modifica o cabeçalho do bloco e, consequentemente, altera completamente o hash produzido após a aplicação da função hash `SHA256d`.



O processo do mining é muito simples:




- o mineiro constrói um bloco candidato (transacções + cabeçalho);
- calcula então o hash do `SHA256d(header)`;
- se o resultado for maior do que o objetivo, altera o nonce;
- começa de novo;
- etc.



![Image](assets/fr/017.webp)



De facto, o nonce não é o único campo que pode ser modificado. Qualquer modificação nas transacções de um bloco resulta numa alteração da raiz da árvore de Merkle e, por conseguinte, numa modificação do cabeçalho desse bloco. Com o poder de computação moderno, percorrer os 4,29 mil milhões de valores possíveis do nonce pode ser feito de forma relativamente rápida. É por isso que existe um outro campo, geralmente designado por "*[extra-nonce](https://planb.academy/resources/glossary/extra-nonce)*", que multiplica ainda mais as possibilidades de variação do cabeçalho. Voltaremos a este mecanismo com mais pormenor num capítulo posterior.



### Qual é o objetivo do proof of work?



Chamamos-lhe "prova" porque o resultado é imediatamente verificável: uma vez produzido um bloco, qualquer nó pode verificar, numa fração de segundo, que o hash criptográfico do seu cabeçalho está efetivamente abaixo do objetivo exigido. Chamamos-lhe "trabalho" porque a obtenção deste hash requer uma multiplicidade de tentativas e, por conseguinte, um custo real em termos de computação e energia.



No [Livro Branco](https://planb.academy/resources/glossary/white-paper) sobre o Bitcoin, o Satoshi Nakamoto apresenta duas vantagens da utilização de um sistema proof-of-work no Bitcoin:





- Seal: a história económica:**



Uma vez gasta a carga computacional, o bloco fica bloqueado: modificá-lo exigiria refazer o proof of work desse bloco. E, como os blocos estão encadeados, alterar um bloco antigo significaria também recalcular todos os blocos subsequentes e, em seguida, alcançar e ultrapassar o trabalho em curso da cadeia honesta.



Por outras palavras, o proof-of-work serve como espinha dorsal do sistema de registo de tempo, tornando cada vez mais dispendiosa a falsificação do passado à medida que os blocos se acumulam. Quando um novo bloco é extraído, a segurança fornecida pelo proof of work é aplicada simultaneamente e uniformemente a todos os UTXOs existentes. Com cada bloco adicionado, cada UTXO acumula assim uma quantidade adicional de segurança do Proof-of-Work.





- Definir a regra da maioria ([consenso](https://planb.academy/resources/glossary/consensus)) e neutralizar a Sybil:**



O Proof-of-Work também permite que o Bitcoin chegue a um consenso sem se basear na regra de votação "um ID = um voto", que poderia ser facilmente falseada pela criação maciça de identidades (IPs, nós, chaves...).



No Bitcoin, a "*maioria*" não é o maior número de participantes, mas a **cadeia que acumula mais trabalho**. Como diz o Satoshi, este é um princípio de "uma CPU = um voto", ou seja, um voto ponderado pelo poder de computação real gasto para produzir blocos válidos. Assim, a implantação de milhares de nós não traz qualquer vantagem em relação ao Bitcoin. Sem poder de computação adicional, não são acumuladas mais provas de trabalho e o [ataque Sybil](https://planb.academy/resources/glossary/sybil-attack) torna-se inútil, enquanto a regra de decisão permanece objetiva e não exige a identificação dos participantes.



![Image](assets/fr/018.webp)



[Nakamoto, S. (2008). *Bitcoin: Um sistema de dinheiro eletrónico peer-to-peer.*](https://bitcoin.org/bitcoin.pdf)



Os princípios relativos à utilidade e aos poderes dos menores são um assunto muito complexo, que não vou aprofundar neste curso. No entanto, voltaremos a abordar este tema em profundidade em futuras acções de formação MIN 201.



De momento, pode resumir o funcionamento do mining da seguinte forma: os mineiros constroem um bloco candidato com as transacções pendentes nos mempools e, em seguida, procuram um hash do seu cabeçalho (através do `SHA256d`) que seja menor ou igual a um objetivo. Eles conseguem isso testando nonces por tentativa e erro.



No próximo capítulo, faremos um breve desvio histórico do princípio proof-of-work para compreender os seus antecedentes e, em seguida, analisaremos a forma como o objetivo de dificuldade é determinado pelo sistema.



## A história do proof of work


<chapterId>919d9f3e-8b3b-41d9-b45a-54df4f3c31a3</chapterId>



A prova de trabalho não foi inventada para o Bitcoin. O [Satoshi Nakamoto](https://planb.academy/resources/glossary/nakamoto-satoshi) retomou e reuniu várias ideias mais antigas, já exploradas em diferentes contextos.



### Hashcash



No final da década de 1990, o problema do spam por correio eletrónico tornou-se significativo. De facto, se enviar uma mensagem de correio eletrónico não custa quase nada, um spammer pode enviar milhões. Mas se cada mensagem exigir um pequeno esforço computacional, o envio de uma única mensagem legítima continua a ser fácil para um utilizador normal, ao passo que o envio de milhões de mensagens se torna muito dispendioso.



Este é o objetivo do [Hashcash](https://planb.academy/resources/glossary/hashcash), proposto pelo Adam Back em 1997, que é considerado a invenção do princípio proof-of-work. O princípio do Hashcash é muito semelhante ao do mining: produzir um hash que respeite uma condição (ter um certo número de zeros no início do hash). A prova acompanha então a mensagem e pode ser verificada muito rapidamente pelo destinatário. Se for recebida uma mensagem de correio eletrónico que não contenha esta prova, pode ser imediatamente considerada como spam e, por conseguinte, filtrada. Os spammers são então obrigados a despender uma quantidade considerável de energia para enviar milhões de mensagens, o que reduz drasticamente (ou mesmo anula completamente) a rentabilidade deste tipo de operação, seja ela de marketing ou fraudulenta.



Atualmente, o Hashcash não é utilizado para correio eletrónico. A filtragem de spam baseia-se atualmente em sistemas centralizados. A vantagem do Hashcash em relação às soluções actuais reside no facto de não necessitar de uma filtragem centralizada: qualquer pessoa pode ajustar os parâmetros de acordo com os seus próprios critérios. Também não requer identificação, uma vez que a pesquisa de hash pode ser efectuada de forma anónima. Acima de tudo, não depende de um sistema de reputação, que tende a introduzir formas subjectivas de filtragem.



O Hashcash não tinha como objetivo criar dinheiro. Procurava impor um custo marginal a uma ação digital facilmente automatizável.



![Image](assets/fr/008.webp)



### Bit Gold



No final dos anos 90 e início dos anos 2000, Nick Szabo explorou a ideia de escassez digital baseada no proof of work. O seu projeto concetual, denominado Bit Gold, prevê a criação de unidades de valor através da resolução de um proof of work dispendioso, registando depois essas provas num registo para estabelecer uma forma de propriedade.



O Bit Gold não resultou num sistema implementado como o Bitcoin, mas contém várias ideias importantes: a ideia de que a computação pode produzir escassez e a ideia de registar elementos ao longo do tempo para criar uma história difícil de reescrever.



### RPOW



Em 2004, o Hal Finney propôs o RPOW (*Reusable Proofs of Work*). A ideia era produzir provas de trabalho que pudessem ser trocadas, em vez de simplesmente consumidas. O objetivo do RPOW era criar token digitais baseados no proof of work, com um sistema para verificar e transferir esses token sem os duplicar. O RPOW, mais uma vez, não resolveu satisfatoriamente o problema de um registo totalmente descentralizado como o Bitcoin faria mais tarde, mas continua a ser um dos grandes precursores do Bitcoin.



![Image](assets/fr/009.webp)



O Hashcash, o Bit Gold e o RPOW utilizam o proof-of-work para impor um custo e criar uma forma de escassez. A Bitcoin retoma este mecanismo, mas atribui-lhe um papel central e coletivo: O proof-of-work não é apenas utilizado para criar algo, é também utilizado para decidir quem tem o direito de escrever a página seguinte do registo (o bloco seguinte) e para tornar este registo difícil de falsificar.



## Ajustar o objetivo de dificuldade


<chapterId>528bcaa8-351e-4eae-887a-426a78a223e3</chapterId>



Nos capítulos anteriores, viu o coração do proof-of-work: os mineiros fazem o hash do cabeçalho do seu bloco candidato com o `SHA256d`, e o bloco só é considerado válido se o hash resultante for numericamente menor ou igual a um valor de referência chamado alvo. A questão que se coloca é: de onde vem esse objetivo e como é que o sistema garante que ele se mantém consistente ao longo do tempo?



O Bitcoin tem como objetivo uma taxa média de um bloco encontrado a cada 10 minutos. Obviamente, este ritmo não é garantido ao segundo. Na prática, alguns blocos são encontrados alguns segundos após o anterior, enquanto outros são encontrados após mais de uma hora. O que importa aqui é a média durante um período suficientemente longo.



![Image](assets/fr/019.webp)



Esta variabilidade resulta da natureza probabilística do mining: cada hash é uma tentativa independente, com uma probabilidade constante (assumindo que o objetivo se mantém inalterado) de produzir um resultado inferior ao objetivo. Pode, portanto, ser comparado a uma lotaria com um sorteio contínuo: quanto mais hashes os mineiros fizerem por segundo, menor será o atraso esperado até ao aparecimento de um bloco válido, mas sem nunca eliminar a aleatoriedade de um sorteio para o seguinte.



### Porquê tentar fazer um intervalo de 10 minutos entre blocos?



Embora não haja provas deste facto, o Satoshi Nakamoto escolheu certamente 10 minutos como um compromisso prático entre eficiência e segurança. Um intervalo mais curto daria confirmações mais frequentes, mas causaria mais divisões temporárias na rede. Para compreender este ponto, precisamos de voltar à forma como um bloco se propaga.



Quando um mineiro encontra um bloco válido, distribui-o imediatamente aos seus pares. Os nós que o recebem verificam a sua validade (transacções, proof of work, regras de consenso, etc.) e depois retransmitem-no. Esta propagação demora um certo tempo, limitado pela latência da Internet, pela largura de banda e pela capacidade de cada nó para verificar o bloco.



![Image](assets/fr/020.webp)



Se, durante este atraso na difusão, outro mineiro também descobrir um bloco válido à mesma altura, a rede pode ficar temporariamente dividida: uma parte dos nós e dos mineiros depende do bloco A, enquanto a outra depende do bloco B. Trata-se de uma divisão temporária da rede.



![Image](assets/fr/021.webp)



Estas divisões não são catastróficas. O consenso Nakamoto prevê que, a longo prazo, apenas um ramo prevalecerá: aquele que acumula mais trabalho. De facto, assim que um novo bloco é extraído sobre o bloco A, por exemplo, toda a rede se ressincroniza com este ramo e abandona o bloco B, que se torna então um "*[stale block](https://planb.academy/resources/glossary/stale-block)*", por vezes erradamente chamado "*orphan block*" na linguagem corrente.



![Image](assets/fr/022.webp)



Por outro lado, têm um custo: durante alguns minutos, uma fração dos mineiros trabalha num ramo que será abandonado. Este trabalho é então desperdiçado do ponto de vista da segurança global, uma vez que não contribuiu para a cadeia final. Quanto mais rápido for o intervalo entre cada bloco, maior será a probabilidade de tais divisões, uma vez que o tempo de propagação representa uma proporção maior do tempo entre cada bloco.



O intervalo de 10 minutos geralmente permite tempo suficiente para que o bloco vencedor se propague amplamente antes que um bloco concorrente na mesma altura seja encontrado. É um compromisso que limita as divisões, reduz o desperdício de poder de computação e ajuda a rede a manter-se sincronizada a uma escala global.



### Compreender o hashrate



*"[Hashrate](https://planb.academy/resources/glossary/hashrate)*" refere-se à quantidade de computação de hash produzida por segundo, seja por um único minerador, um grupo de mineradores ou todos os mineradores no Bitcoin. É expresso em `H/s` (hashes por segundo), com múltiplos como `TH/s` (terahashes por segundo) ou `EH/s` (exahashes por segundo). Isso representa o número de tentativas que os mineradores podem fazer a cada segundo para tentar obter um hash menor que o alvo.



Se o objetivo se mantiver fixo, então:




- cada tentativa tem uma probabilidade fixa de sucesso;
- fazer mais tentativas por segundo aumenta a probabilidade de uma tentativa vencedora aparecer rapidamente


Por outras palavras, se a rede Bitcoin de amanhã duplicar a sua capacidade de cálculo, ligando o dobro das máquinas mining, sem um mecanismo de correção, os blocos serão encontrados, em média, duas vezes mais depressa. O objetivo deve, portanto, ser ajustado para compensar as variações do hashrate.



### Ajustar o objetivo de dificuldade



O Bitcoin resolve este problema com um mecanismo de ajustamento periódico do objetivo, que ajusta a dificuldade do mining. O princípio é o seguinte: a cada 2016 blocos (aproximadamente a cada 2 semanas), cada nó recalcula o objetivo de dificuldade observando quanto tempo foi realmente necessário para produzir esses 2016 blocos.



O objetivo deste mecanismo é reduzir o tempo médio de produção de um bloco para cerca de 10 minutos, enquanto o hashrate global da rede está em constante mudança, devido à desconexão de máquinas ou, pelo contrário, à adição de novas máquinas.



![Image](assets/fr/023.webp)



O cálculo baseia-se no tempo observado para o período decorrido:




- se os últimos blocos de 2016 foram encontrados demasiado depressa, isso significa que o hashrate aumentou durante esse período; o Bitcoin torna então a condição mais difícil, baixando o objetivo para o período seguinte;
- se os blocos de 2016 foram encontrados demasiado lentamente, isso significa que o hashrate diminuiu; o Bitcoin alivia a situação aumentando o objetivo.



A fórmula é a seguinte:



```txt
Tn = To * (Ta / Tt)
```



Com:




- `tn`: novo objetivo
- `to`: destino antigo
- `Ta`: tempo real decorrido para os últimos 2016 blocos
- `Tt`: tempo do objetivo (em segundos)



Com um tempo alvo de duas semanas, ou seja, `Tt = 1.209.600` segundos:



```txt
Tn = To * (Ta / 1 209 600)
```



Para compreender como ajustar a dificuldade do Bitcoin mining, eis um exemplo com valores fictícios:



```txt
Tn = To * (Ta / 1 209 600)
Tn = 18 045 755 102 * (1 000 000 / 1 209 600)
Tn = 14 918 779 020
```


Com:



- `**To = 18.045.755.102**`: Objetivo antigo, ou seja, o valor de referência antes do ajustamento.
- `**ta = 1.000.000 segundos**`: Tempo efetivamente gasto a produzir os últimos 2016 blocos. Uma vez que este tempo é inferior ao tempo alvo, a rede extraiu demasiado rapidamente.
- 1.209.600 segundos: Tempo alvo correspondente a 10 minutos por bloco para blocos de 2016, utilizado como referência para o ajustamento.
- `**tn = 14,918,779,020**`: Novo objetivo calculado após o [ajustamento de dificuldade](https://planb.academy/resources/glossary/difficulty-adjustment).



Neste caso, o novo objetivo é mais baixo do que o anterior, o que significa que o mining se torna mais difícil para abrandar a produção de blocos no período seguinte.


*Os valores alvo neste exemplo são simplificados e escalados para fins didácticos; o alvo real utilizado no Bitcoin é um inteiro de 256 bits de uma ordem de grandeza completamente diferente.*



Este cálculo é efectuado localmente por cada nó, com base nos carimbos de data e hora introduzidos nos blocos. Como todos os nós aplicam as mesmas regras, chegam ao mesmo resultado, e o novo objetivo torna-se a referência comum para os próximos blocos de 2016.



Há um pormenor importante a ter em conta sobre este ajustamento: **é limitado**. O Bitcoin limita a variação da dificuldade por período, a fim de evitar alterações demasiado bruscas que poderiam bloqueá-la. De facto, o tempo real tido em conta é limitado a um intervalo equivalente a um fator de 4 (mínimo um quarto do objetivo antigo, máximo quatro vezes o objetivo antigo). Isto evita uma reorientação extrema se as marcas de tempo forem altamente atípicas ou manipuladas.



### Representação do alvo



No cabeçalho do bloco, o alvo não aparece na sua forma completa de 256 bits, pois isso ocuparia demasiado espaço. Em vez disso, o campo `nBits` de 32 bits codifica o alvo num formato compacto, comparável à notação científica de base 256: um expoente (1 byte) e um coeficiente (3 bytes). O alvo completo é então reconstruído a partir destes dois valores. Não entraremos em pormenores aqui, uma vez que o assunto é relativamente complexo e não acrescenta nada à compreensão do mining. Lembre-se apenas que o alvo não é armazenado em bruto no cabeçalho do bloco, mas em formato compacto.



Com este último capítulo da Parte I, fizemos uma visita guiada ao funcionamento do proof-of-work no Bitcoin: o mineiro constrói um bloco candidato selecionando transacções do seu mempool, calcula o cabeçalho do bloco candidato, faz o hash, compara o hash resultante com o objetivo do período, depois recomeça modificando o nonce até obter um hash válido. Finalmente, a cada 2016 blocos, a rede recalcula um novo objetivo de modo a manter um tempo médio de cerca de 10 minutos por bloco, apesar das constantes variações no hashrate.




# O sistema de incentivos Bitcoin mining


<partId>27fb10c1-d53b-4dc2-90fa-3cb0309b74c1</partId>



## Block reward


<chapterId>b316fb89-9c18-417e-917b-ab98f1722646</chapterId>



Como se pode imaginar, o Bitcoin mining não é uma atividade altruísta. Os Miner têm custos reais: eletricidade para fazer funcionar os seus computadores mining, compra de equipamento especializado, salários para manutenção, por vezes instalações e sistemas de refrigeração. Para que o sistema Bitcoin funcione, os interesses privados dos mineiros devem estar alinhados com os interesses colectivos da rede. É exatamente este o papel da recompensa mining. Incentiva os mineiros a investirem no proof of work, a incluírem transacções válidas e a respeitarem as regras do protocolo em vez de tentarem corrompê-lo.



Esta lógica baseia-se na teoria dos jogos: o protocolo torna a honestidade racional. Um mineiro ganha dinheiro quando produz um bloco válido aceite pelos nós. Por outro lado, se tentar fazer batota, o seu bloco será rejeitado pelos nós e não receberá nada. Uma vez que a produção de um bloco tem um custo, um bloco rejeitado representa uma perda direta. Num ambiente competitivo em que milhares de jogadores procuram simultaneamente um bloco válido, a estratégia mais rentável, na maioria das vezes, é, portanto, seguir rigorosamente as regras e maximizar o seu rendimento de forma honesta.



Para tal, o protocolo Bitcoin estipula que o mineiro que encontrar um bloco válido ganha o direito de incluir uma determinada transação no mesmo, o que lhe atribui uma determinada soma de BTC. Isto é conhecido como **[recompensa do bloco](https://planb.academy/resources/glossary/block-reward)**. Neste primeiro capítulo desta secção, o objetivo é compreender em que consiste e como é determinada. Mais tarde, veremos como a parte da criação de dinheiro evolui ao longo do tempo (com halvings) e como é efetivamente cobrada tecnicamente (através da transação coinbase).



### Em que consiste a recompensa por bloco?



Nos capítulos anteriores, vimos como os mineiros conseguem encontrar um bloco válido. Quando um mineiro encontra um cabeçalho cujo hash é mais pequeno do que o objetivo, o seu bloco candidato é considerado válido. Ele pode então distribuí-lo para toda a rede Bitcoin. O bloco é adicionado ao resto da cadeia de blocos, confirmando as transacções que contém.



É precisamente este evento (a adição efectiva do bloco à cadeia de blocos) que desencadeia a atribuição de uma recompensa ao mineiro vencedor. Esta recompensa é composta por dois elementos distintos que são somados:




- [subsídio por bloco](https://planb.academy/resources/glossary/block-subsidy)**;
- taxas de transação**.



![Image](assets/fr/024.webp)



Vejamos a que correspondem estas duas partes da recompensa.



### Subvenção por categoria



O subsídio por bloco corresponde à parte da recompensa relativa à criação monetária. Quando um mineiro produz um bloco válido, o protocolo autoriza-o a criar um determinado número de novos bitcoins e a atribuí-los a si próprio como recompensa. Estes bitcoins são criados ex nihilo. Não existiam antes.



No entanto, a quantidade de bitcoins recém-criados não é de forma alguma arbitrária. É estritamente definida pelas regras do protocolo Bitcoin e é idêntica para todos os mineiros. Analisaremos mais detalhadamente este mecanismo no próximo capítulo, uma vez que o subsídio não é um valor fixo indefinidamente: é dividido periodicamente de acordo com um calendário preciso. Para já, basta lembrarmo-nos disso:




- o subsídio por bloco é uma das duas componentes do prémio por bloco;
- é limitado e determinado pelo protocolo, não pelo mineiro (embora o mineiro possa tecnicamente pedir menos do que o montante máximo);
- cria bitcoins a partir do nada.



Este subsídio desempenha dois papéis principais no âmbito do protocolo Bitcoin. A primeira é incentivar os jogadores a participarem do mining. Nos primeiros anos do Bitcoin (e por vezes ainda hoje), as taxas de transação eram muito baixas. Por conseguinte, o subsídio garantiu uma compensação suficiente para atrair mineiros e manter um nível de segurança para o sistema.



O segundo papel está relacionado com a distribuição da moeda. Qualquer nova moeda enfrenta a questão de como distribuir equitativamente as unidades monetárias pela população. O subsídio por bloco dá uma resposta a este problema. Ao criar bitcoins através do mining, permite a sua distribuição inicial de uma forma aberta e neutra: qualquer pessoa pode obtê-los, desde que participe no mining, sem necessidade de autorização ou identificação prévia.



Por outro lado, uma vez que estes bitcoins são criados a partir do nada, o seu valor não é desprovido de uma base. Ao aumentar a quantidade de dinheiro em circulação, a subvenção dilui mecanicamente o valor dos bitcoins existentes. Introduz, portanto, uma forma de inflação monetária. No entanto, veremos no próximo capítulo que este subsídio está destinado a desaparecer gradualmente e que a inflação acabará por cessar.



![Image](assets/fr/025.webp)



### Taxas de transação



A segunda componente da recompensa por bloco está ligada à utilização do sistema: quando um utilizador lança uma transação, pretende que esta seja confirmada. No entanto, o espaço em bloco é limitado e os blocos aparecem, em média, apenas de 10 em 10 minutos. O espaço dos blocos é, portanto, um recurso escasso. Quando a procura excede a oferta, o preço sobe: este é o mercado das taxas de transação. Cada mineiro que consegue produzir um bloco válido obtém o direito de cobrar, por sua própria conta, a totalidade das taxas de transação associadas a todas as transacções que incluiu no seu bloco.



Pode pensar-se nisto como um sistema de leilão: cada transação propõe um montante de taxa, e os mineiros dão prioridade àquelas que maximizam o seu rendimento, sob restrições de espaço. Este mecanismo alinha naturalmente os interesses:




- os utilizadores com pressa pagam mais para serem incluídos rapidamente;
- os mineiros são encorajados a incluir transacções que pagam as taxas mais elevadas pelo espaço do bloco.
- a rede evita o spam, porque a publicação de uma transação tem um custo.



#### Como são calculadas as taxas de transação?



Contrariamente à crença popular, as taxas não são um resultado de uma transação Bitcoin. Na verdade, uma transação gasta inputs e cria outputs. As entradas representam a origem dos bitcoins utilizados, enquanto as saídas representam o destino dos pagamentos. As taxas de transação são simplesmente **a diferença entre o total de entradas e o total de saídas**.



Por outras palavras, os inputs de bitcoin do utilizador, que lhe pertencem, criam outputs para os destinatários, mas não reproduzem o montante total consumido pelos inputs. A diferença entre os dois representa as taxas de transação que o mineiro pode cobrar.



Vejamos um exemplo. Uma transação consome dois inputs, um de `100.000 sats` e outro de `150.000 sats`, e cria três outputs de `35.000 sats`, `42.000 sats` e `170.000 sats`.



![Image](assets/fr/027.webp)



A soma das entradas é, por conseguinte, de 250 000 sats, enquanto a soma das saídas é de 247 000 sats. Isto significa que `3.000 sats` foram consumidos nos inputs sem serem recriados nos outputs: este montante corresponde às taxas propostas por esta transação.



![Image](assets/fr/028.webp)



Se um mineiro incluir esta transação num bloco válido, terá direito a recuperar estes `3.000 sats`, para além das taxas de todas as outras transacções incluídas no bloco. No entanto, não existe uma ligação direta entre a transação que paga a taxa e os sats efetivamente cobrados pelo mineiro. Tecnicamente, os `3.000 sats` em taxas são destruídos e, em troca, o mineiro obtém o direito de recriar o mesmo montante para si próprio.



#### O rácio da taxa



Um bloco não é limitado pelo número de transacções, mas pela sua capacidade total (hoje, na prática, pelo peso do bloco). Algumas transacções ocupam mais espaço do que outras: uma transação com muitos inputs e outputs será maior do que uma simples transação com um único input e dois outputs. Os scripts utilizados também influenciam o tamanho.



![Image](assets/fr/026.webp)



Duas transacções podem, portanto, pagar o mesmo montante de taxas em termos absolutos, mas não serem economicamente equivalentes do ponto de vista do mineiro. Se uma é duas vezes maior, custa o dobro do espaço no bloco. O espaço é escasso, pelo que o mineiro procura maximizar as suas receitas por unidade de espaço.



É por isso que, na prática, expressamos a competitividade de uma transação com um rácio de taxa, normalmente em `sats/vB` ([satoshis](https://planb.academy/resources/glossary/satoshi-sat) por byte virtual). O cálculo deste rácio é simples:



```text
fee rate = fee / weight (in vB)
```



Por exemplo, se tivermos uma transação com um peso de `141 vB` e uma taxa de `1.974 sats`, esta terá uma taxa de `14 sats/vB`.



```text
1 974 / 141 ≈ 14 sats/vB
```



Este rácio explica as escolhas económicas feitas pelos mineiros: com uma capacidade fixa, a inclusão de transacções de elevada taxa maximiza as taxas totais do bloco e, por conseguinte, a compensação do mineiro. Também explica porque é que as transacções de baixo custo permanecem em fila de espera nos mempools durante longos períodos: competem com outras transacções que pagam mais por unidade de espaço.



### Proteção da rede contra spam



As taxas também servem um objetivo de segurança operacional: introduzem um custo na multiplicação das transacções. Se a publicação de uma transação fosse gratuita, seria fácil inundar a rede com transacções inúteis e saturar os mempools, aumentando a carga nos nós.



Na prática, os nós aplicam políticas locais de retransmissão (regras de mempool) e frequentemente definem um limite mínimo de taxa abaixo do qual eles não retransmitem uma transação (por padrão, `0.1 sat/vB` no Bitcoin Core via `minRelayTxFee`). Uma transação pode ser válida no sentido estrito das regras de consenso, mas não ser retransmitida pela maioria dos nós se suas taxas forem muito baixas. Como resultado, ela não circula, não chega aos mineradores e tem muito pouca chance de ser confirmada.



Nesta altura, já tem uma ideia geral da recompensa do bloco: corresponde à compensação para o mineiro vencedor e é composta por dois elementos distintos. Por um lado, um subsídio de bloco, definido pelas regras do protocolo, que cria novos bitcoins ex nihilo. E, por outro lado, as taxas das transacções incluídas no bloco minerado.



No próximo capítulo, iremos debruçar-nos mais detalhadamente sobre o subsídio por bloco, para compreender exatamente como é calculado e como evolui ao longo do tempo de acordo com as regras do protocolo Bitcoin.



## Halving


<chapterId>7cdca211-7300-48f8-a1e4-53e5c2678cd8</chapterId>



No capítulo anterior, vimos que os mineiros que produzem um bloco válido recebem uma recompensa que consiste nas taxas das transacções incluídas no bloco, mais um subsídio ao bloco. No entanto, ainda não explicámos como é determinado o montante deste subsídio. O mecanismo que define e faz evoluir este valor é conhecido como ***[halving](https://planb.academy/resources/glossary/halving)***.



### O que é reduzir para metade?



O Halving é um evento programado no protocolo Bitcoin que reduz para metade o subsídio por bloco, ou seja, o montante máximo de novos bitcoins que o mineiro vencedor pode criar em cada bloco. Não afecta as taxas de transação: as taxas existem independentemente e continuam a ser determinadas pela atividade dos utilizadores e pela concorrência pelo espaço do bloco.



Quando o Bitcoin foi lançado em 2009, o subsídio por bloco foi fixado em 50 BTC por cada bloco extraído. Desde então, este subsídio foi reduzido várias vezes para metade.



![Image](assets/fr/029.webp)



O Halving não é acionado por uma data, mas pela altura do bloco. Ele é executado **a cada 210.000 blocos**. Uma vez que o Bitcoin tem como objetivo um intervalo médio de cerca de 10 minutos por bloco, 210.000 blocos correspondem a cerca de quatro anos.



```cpp
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
// Force block reward to zero when right shift is undefined.
if (halvings >= 64)
return 0;

CAmount nSubsidy = 50 * COIN;
// Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
nSubsidy >>= halvings;
return nSubsidy;
}
```



Assim, se anotarmos `n` o número de metades já ocorridas, o subsídio de bloco no BTC pode ser calculado da seguinte forma



```text
subsidy(n) = 50 / 2^n
```



### Metades passadas



Segue-se um quadro recapitulativo das metades que já ocorreram, com a altura do bloco, a data e o novo subsídio de bloco aplicável após o evento:



| Event               |   Height  | Date                        | Subsidy    |
| ------------------- | --------: | --------------------------- | ---------: |
| Halving 1           |   210 000 | 28 novembre 2012            |     25 BTC |
| Halving 2           |   420 000 | 9 july 2016                 |   12,5 BTC |
| Halving 3           |   630 000 | 11 may 2020                 |   6,25 BTC |
| Halving 4           |   840 000 | 20 april 2024               |  3,125 BTC |
| Halving 5 (upcoming) | 1 050 000 | Spring   2028 (estimation) | 1,5625 BTC |

### Quando e como termina a subvenção?



Halving repete-se desde que a subvenção possa ser expressa na unidade mínima do sistema: satoshi.



```text
1 BTC = 100 000 000 sats
```



À medida que o subsídio é reduzido para metade, acabamos por atingir fracções de um bitcoin tão pequenas que se tornam inferiores a 1 satoshi. Nesta altura, já não é possível criar meia unidade de satoshi. A criação de dinheiro através do subsídio por bloco pára, e os mineiros são compensados apenas com base nas taxas de transação. A partir deste momento, todos os bitcoins estarão em circulação e já não será possível produzir novas unidades.



O fim definitivo dos subsídios de bloco ocorrerá no nível de bloco 6.930.000, ou seja, na 33ª e última redução para metade. Prevê-se que este evento ocorra por volta do ano 2140, embora seja impossível indicar uma data exacta, pois dependerá da velocidade a que os blocos forem encontrados até lá.



Uma vez que o subsídio por bloco segue uma sequência geométrica com um rácio de 1/2 em cada redução para metade, a criação de dinheiro foi extremamente elevada nos primeiros dias do Bitcoin, diminuindo depois muito rapidamente. Na sétima redução para metade, mais de 99% dos bitcoins já terão sido postos em circulação. Prevê-se que o limiar de 99% seja ultrapassado entre 2032 e 2036. Isto significa que serão necessários mais de 100 anos para extrair os últimos 1% de bitcoins. Embora a inflação monetária fosse muito elevada aquando do lançamento do Bitcoin, para permitir a distribuição generalizada da moeda, é agora muito baixa e continuará a baixar, até atingir o nível de uma verdadeira moeda forte, cuja oferta circulante já não pode aumentar.



![Image](assets/fr/030.webp)



### Porque é que nunca haverá 21 milhões de BTC?



A oferta monetária máxima do Bitcoin é frequentemente apresentada como 21 milhões de BTC. Esta é uma boa aproximação para compreender a sua política monetária, mas de um ponto de vista estritamente técnico, a oferta total nunca atingirá exatamente 21.000.000 bitcoins.



A principal razão é de ordem mecânica. Através de halvings sucessivos, o subsídio por bloco acaba por cair abaixo do valor mínimo de 1 sat, o que acaba por ser emitido antes de atingir o total teórico exato. Em resultado desta granularidade mínima e das regras de arredondamento, o número total de bitcoins criados pelo subsídio é ligeiramente inferior a 21 milhões.



Além disso, os desvios marginais relacionados com o protocolo também podem contribuir para este facto. Por exemplo, em casos raros, alguns mineiros podem não ter reclamado a totalidade do seu subsídio, o que reduz definitivamente a quantidade de bitcoins efetivamente emitidos. Podemos também mencionar o [bloco genesis](https://planb.academy/resources/glossary/genesis-block), produzido pelo Satoshi em 3 de janeiro de 2009, cujos bitcoins criados não fazem parte do [UTXO set](https://planb.academy/resources/glossary/utxo-set), bem como certos eventos históricos ligados a bugs, como identificadores de transacções coinbase duplicados.



Por último, há que ter em conta todos os bitcoins que foram destruídos ou bloqueados:




- bitcoins trancados em scripts insolúveis;
- os deliberadamente destruídos pelos guiões `OP_RETURN`;
- ou perda de chaves privadas a nível da aplicação.



Em teoria, a oferta do Bitcoin está, portanto, limitada a 21 milhões. Na prática, porém, nunca haverá de facto 21 milhões de bitcoins em circulação.



## A transação da coinbase


<chapterId>69476700-3616-4aab-b006-367aba059de9</chapterId>



Nos capítulos anteriores, apresentámos dois pontos importantes. Em primeiro lugar, o mineiro que consegue produzir e distribuir um bloco válido recebe uma recompensa. Por outro lado, vimos que esta recompensa é composta por dois elementos distintos:




- um subsídio de bloco (bitcoins criados ex nihilo, cujo montante máximo é fixado pelo protocolo e reduzido gradualmente através de halvings);
- todas as taxas de transação pagas pelos utilizadores cujas transacções tenham sido incluídas no bloco.



No entanto, resta uma questão: através de que mecanismo é que o mineiro recebe esta recompensa em Bitcoin? É precisamente este o papel de uma determinada transação designada por "coinbase".



### Como funciona a transação com a coinbase



Como vimos na primeira parte do curso, cada bloco Bitcoin contém uma lista de transações pendentes que serão confirmadas. A primeira delas é sempre a [transação coinbase](https://planb.academy/resources/glossary/coinbase-transaction). É o que permite que o minerador vencedor receba sua recompensa.



![Image](assets/fr/031.webp)



À primeira vista, parece uma transação Bitcoin clássica: tem um [TXID](https://planb.academy/resources/glossary/txid-transaction-identifier), saídas e está incluída na árvore Merkle do bloco. No entanto, ela difere num aspeto importante: não gasta nenhum UTXO existente.



Numa transação Bitcoin clássica, os "inputs" referem outputs anteriores não gastos (UTXOs), que fornecem o valor de input. As saídas redistribuem então esse valor para novos UTXOs, com novas condições de gasto. Por outras palavras, para enviar bitcoins, é necessário já os possuir. A transação coinbase, por outro lado, não consome bitcoins no input: cria bitcoins no output diretamente a partir do zero.



É precisamente este mecanismo que permite a introdução de novos bitcoins em circulação através do subsídio do bloco e que credita ao mineiro as taxas associadas às transacções incluídas no bloco. A transação coinbase não pode fazer referência a um UTXO real existente (na verdade, faz referência a um UTXO fictício), uma vez que o seu papel é precisamente criar parte do valor (o subsídio) e recuperar a outra parte (as taxas), sem as receber de uma transação anterior. Para que todo o sistema se mantenha consistente, a parte correspondente às taxas deve ser exatamente igual à soma dos bitcoins consumidos em inputs mas não recriados em outputs nas outras transacções do bloco.



![Image](assets/fr/032.webp)



Esta transação não é opcional. Um bloco que não contenha uma transação coinbase é inválido e será sistematicamente rejeitado pelos nós da rede.



⚠️ Atenção: o termo "*coinbase*" não tem qualquer relação com a plataforma de troca com o mesmo nome. No Bitcoin, "*coinbase*" refere-se historicamente à transação que cria a recompensa do bloco. A empresa simplesmente adoptou este termo para o seu nome.



A transação coinbase desempenha, de facto, várias funções em simultâneo:




- A primeira é a que acabámos de descrever: atribui ao mineiro a recompensa a que tem direito por ter produzido um bloco válido.
- O seu segundo papel, mais técnico, é o de ancorar o compromisso criptográfico com as testemunhas (assinaturas) das transacções SegWit incluídas no bloco.
- Um terceiro papel, desta vez não diretamente relacionado com o protocolo mas ligado à industrialização moderna do mining, é que a base de moedas é agora frequentemente utilizada para ancorar dados técnicos arbitrários. Estes dados estão geralmente ligados ao funcionamento dos pools do mining e à sua organização interna.



Para o ajudar a compreender estas diferentes utilizações, vamos agora analisar mais detalhadamente a estrutura da transação coinbase.



### A estrutura básica da transação coinbase



Uma transação coinbase deve conter exatamente um input. Para simplificar, às vezes dizemos que não tem entrada, porque essa entrada não gasta nenhum UTXO real. Na realidade, existe um input com uma fonte referenciada, mas que aponta deliberadamente para um UTXO inexistente.



Como já vimos, cada transação Bitcoin deve consumir UTXOs como entrada para criar saídas válidas. Na transação Bitcoin, este consumo assume a forma de referência a um UTXO existente como entrada. Esta referência é feita simplesmente através da indicação do identificador da transação anterior (aquela em que o UTXO foi criado), bem como do seu índice entre os outputs desta transação. Em termos concretos, um UTXO é definido por um hash (o TXID anterior) e um índice.



Mas no caso da transação coinbase, em vez de fazer referência a um UTXO real existente, a entrada deve necessariamente apontar para este UTXO falso em particular, com um TXID cheio de zeros, que não corresponde a nenhum TXID real:



```text
0000000000000000000000000000000000000000000000000000000000000000
```


Diretamente seguido do índice falso:


```text
0xffffffff
```


![Image](assets/fr/033.webp)



No protocolo básico Bitcoin, tal como descrito no Satoshi Nakamoto, esta entrada falsa é a única restrição imposta à transação coinbase.



Como qualquer UTXO referenciado na entrada de uma transação, ele está associado a um campo `scriptSig`. Numa transação convencional, este campo `scriptSig` contém os elementos necessários para satisfazer a `scriptPubKey` e assim desbloquear o UTXO gasto. Mas no caso particular da coinbase, como o UTXO referenciado é deliberadamente fictício, o campo `scriptSig` é totalmente livre. Os Miners podem, portanto, inserir qualquer dado que desejarem. Veremos mais tarde como esta liberdade é utilizada.


Além dessa entrada falsa, há uma ou mais saídas perfeitamente padrão, que permitem ao minerador coletar os bitcoins da recompensa em um de seus endereços Bitcoin. Essas saídas são UTXOs bloqueados por uma `scriptPubKey` (por exemplo, um script apontando para um endereço controlado pelo minerador ou pelo pool). A única particularidade aqui reside na regra de cálculo do seu valor: a soma total dos outputs da coinbase nunca deve exceder o subsídio máximo permitido, ao qual são adicionadas as taxas de bloco.



Historicamente, portanto, a transação coinbase resume-se a este esquema simples: uma entrada falsa referenciando um UTXO inexistente, e uma ou mais saídas concebidas para distribuir a recompensa do bloco ao mineiro vencedor. Atualmente, porém, a coinbase já não se limita a este papel de distribuição. A sua posição especial no bloco e a grande flexibilidade da sua estrutura conduziram a novas utilizações, tanto no próprio protocolo como nos mecanismos de gestão do pool de mining.



### Outras utilizações da coinbase



Ao longo do tempo, a transação coinbase tornou-se um ponto de inserção particularmente conveniente para integrar uma variedade de informações úteis para o mining e para a própria estrutura do bloco. Vamos dar uma olhada nelas para entender melhor a organização geral da coinbase.



#### O BIP-34



O [BIP-34](https://planb.academy/resources/glossary/bip0034) é um fork soft implantado em março de 2013, começando com o bloco 227.930, que introduziu a versão 2 dos blocos Bitcoin. Esta nova versão exige que cada bloco inclua, no `scriptSig` da transação coinbase, a altura do bloco que está sendo criado.



Por um lado, esta evolução clarifica a forma como a rede concorda em desenvolver a estrutura dos blocos e as regras de consenso. Por outro lado, garante a unicidade de cada bloco e de cada transação coinbase.



Assim, o `scriptSig` da coinbase não é totalmente livre. Desde a ativação do BIP-34, está simplesmente limitado a começar com a altura do bloco em que esta transação da coinbase está incluída.



![Image](assets/fr/035.webp)



#### O extra-nonce



Como vimos nos primeiros capítulos deste curso, o minerador tem um campo nonce de 32 bits no cabeçalho do bloco, que ele modifica por tentativa e erro para encontrar um hash menor ou igual ao alvo. Esse espaço de 32 bits já permite que um número muito grande de combinações seja explorado, mas quando a dificuldade do mining é alta, esse intervalo pode ser totalmente esgotado em um tempo relativamente curto e, portanto, pode não produzir nenhuma combinação que produza um hash válido. Se todos os valores possíveis do `nonce` tiverem sido testados sem sucesso, o minerador deve então modificar outro elemento para alterar o cabeçalho do bloco e iniciar uma nova série de tentativas.



Como a transação coinbase oferece um campo livre através do `scriptSig` da sua entrada, a solução utilizada para alargar o espaço do nonce é explorar parte deste `scriptSig`. Isso é geralmente chamado de extra-nonce. Ao modificar o extra-nonce, o mineiro modifica o `scriptSig` da coinbase, ou seja, o identificador da transação, depois a raiz Merkle do bloco e, finalmente, o próprio cabeçalho do bloco. Desta forma, obtém um novo espaço de pesquisa de hashes para explorar, sem ter de modificar os outros componentes do seu bloco candidato.



![Image](assets/fr/036.webp)



#### Identificação de pools e mineradores



Atualmente, uma grande parte do hashrate do mundo está organizada em pools de mining. Estas estruturas reúnem mineiros individuais para combinar o seu trabalho e reduzir a variação dos seus rendimentos.



Por razões operacionais, os pools do mining também exploram o campo livre do `scriptSig` da entrada da coinbase para inserir várias informações. Estas variam de pool para pool e de protocolo de rede para protocolo de rede, mas geralmente incluem um identificador único (muitas vezes um nonce extra estruturado em várias sub-partes) atribuído a cada mineiro, para evitar a duplicação de trabalho dentro do pool. É normalmente adicionada uma etiqueta de identificação do pool, utilizada para a atribuição pública de blocos encontrados, estatísticas mining e outros objectivos de rastreio.



![Image](assets/fr/037.webp)



#### Compromisso do SegWit



Desde que o SegWit soft fork foi ativado em 2017, os dados das testemunhas (ou seja, geralmente as assinaturas) foram separados dos dados principais da transação, nomeadamente para corrigir o problema de [maleabilidade das transacções Bitcoin](https://planb.academy/resources/glossary/malleability-transaction). Esta separação introduz, por conseguinte, um novo elemento a ser objeto de autorização no bloco.



Para fazer isso, as testemunhas são agrupadas em outra árvore Merkle dedicada, cuja raiz é então comprometida com a transação coinbase através de uma saída `OP_RETURN`.



![Image](assets/fr/038.webp)



Não vou entrar em mais detalhes sobre este mecanismo neste curso, pois está além do escopo deste artigo, mas lembre-se que desde a introdução do SegWit, a transação coinbase serve como um veículo para ancorar no bloco uma impressão digital resumindo todas as testemunhas do SegWit. As testemunhas são colocadas numa árvore Merkle independente, a raiz desta árvore é escrita numa saída da transação coinbase, e esta transação coinbase é ela própria incluída na árvore Merkle principal, juntamente com todas as outras transacções, cuja raiz aparece no cabeçalho do bloco. É assim que os testemunhos, armazenados separadamente dos dados da transação principal, continuam a ser inscritos no cabeçalho do bloco.



![Image](assets/fr/039.webp)



#### Mensagens arbitrárias



Como o `scriptSig` permite a inserção livre de informações arbitrárias escolhidas pelo minerador, alguns aproveitaram a oportunidade para adicionar mensagens de natureza mais pessoal, em vez de técnicas. O caso mais famoso é, obviamente, o do Satoshi Nakamoto, com a sua mensagem agora icónica:



> The Times 03/Jan/2009 Chanceler à beira de um segundo resgate aos bancos

Esta mensagem, presente no bloco Genesis (o primeiro bloco do Bitcoin), está de facto codificada em hexadecimal no `scriptSig` da transação coinbase:



```text
5468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73
```


![Image](assets/fr/034.webp)



### O período de maturidade


Depois de o bloco ter sido extraído e distribuído, a transação coinbase aparece na cadeia de blocos como qualquer outra transação. Ela cria UTXOs para o minerador vencedor, permitindo que ele receba sua recompensa. No entanto, esses UTXOs não são imediatamente gastáveis: eles estão sujeitos a um [período de maturidade](https://planb.academy/resources/glossary/maturity-period). Esta maturidade é fixada em 100 blocos após o bloco que contém a coinbase. Em termos concretos, a transação coinbase deve, portanto, totalizar 101 confirmações para que os seus outputs se tornem passíveis de serem gastos pelo mineiro vencedor.


![Image](assets/fr/040.webp)


O objetivo desta regra é limitar o impacto das reorganizações da cadeia na economia. Como vimos nos capítulos anteriores, pode acontecer que, na mesma altura, dois blocos válidos distintos sejam encontrados quase simultaneamente por mineiros diferentes. Por um breve momento, a rede pode dividir-se: alguns nós recebem primeiro o bloco A, enquanto outros vêem primeiro o bloco B. Depois, no decurso dos blocos seguintes, um dos dois ramos acumula mais trabalho e torna-se o ramo de referência. O outro ramo é abandonado e os seus blocos tornam-se obsoletos. As transacções que continha podem então, em teoria, regressar aos mempools que aguardam confirmação.



Na prática, isto raramente acontece, porque o mercado de taxas resulta frequentemente em que quase as mesmas transacções apareçam em dois blocos concorrentes à mesma altura. Esta é uma das razões pelas quais uma transação Bitcoin é geralmente considerada imutável após seis confirmações: as reorganizações de mais de seis blocos são tão improváveis que podem ser razoavelmente consideradas impossíveis.



![Image](assets/fr/041.webp)



O problema com estas reorganizações no caso da transação coinbase é que não se trata de uma transação normal. Introduz novos bitcoins em circulação. Se a recompensa do bloco pudesse ser gasta imediatamente, poderia surgir uma situação problemática em cascata:




- um mineiro gasta bitcoins de uma base de moedas,
- estes bitcoins circulam na economia,
- depois o bloco original foi finalmente abandonado durante uma reorganização.



Os bitcoins em circulação nunca teriam existido na cadeia final e uma série de transacções que eram válidas no momento da emissão tornar-se-iam inválidas a posteriori.



O prazo de vencimento impõe um período de tempo suficientemente longo para tornar este cenário irrealista. Uma reorganização de 101 blocos é considerada, na prática, impossível (mesmo que haja uma probabilidade infinitesimal). Não sabemos exatamente porque é que o Satoshi escolheu um valor tão elevado para a maturidade, mas é provável que tenha sido escolhido para que o mecanismo permaneça funcional, mesmo em caso de grandes avarias na rede.



Esta regra evita que o dinheiro recém-criado para a recompensa do bloco comece a circular antes de o bloco que o generated tenha sido enterrado de forma segura sob uma grande quantidade de trabalho acumulado.



---

Chegámos ao fim da nossa explicação sobre o funcionamento do Bitcoin mining. Agora já deve ter uma ideia clara dos mecanismos básicos envolvidos.



Na última parte do curso, voltaremos a aspectos mais concretos, para mostrar como o Bitcoin mining se materializa no mundo real: a sua industrialização, as máquinas utilizadas, o agrupamento de jogadores, etc. O objetivo será dar uma visão global do Bitcoin mining, tanto do ponto de vista teórico e protocolar que acabámos de ver, como do seu lado prático e operacional.



# A indústria Bitcoin mining


<partId>906a6e18-4718-4a1f-85f5-18854cebdf7c</partId>



## A evolução das máquinas mining


<chapterId>2d2f9055-75fd-4630-b493-a577d708a39f</chapterId>



Nos primeiros tempos do Bitcoin, o mining não era uma atividade industrial. Fazia parte do software Bitcoin, lançado num computador pessoal, muitas vezes por curiosidade, outras vezes para apoiar a rede e, em segundo lugar, para obter bitcoins que, na altura, não tinham praticamente nenhum valor de mercado.



Ao longo dos anos, esta atividade sofreu uma transformação: as máquinas mudaram, a dificuldade explodiu e a mining tornou-se uma indústria de pleno direito. Vejamos os aspectos operacionais do Bitcoin mining.



### Como começar: mining com uma CPU



Em 2009 e nos primeiros anos, o mining era realizado principalmente usando a CPU de um computador convencional. O Bitcoin era então apenas um simples software, servindo como um wallet, um nó e um mineiro. Bastava lançar o software do Satoshi Nakamoto no seu computador pessoal para participar no processo do mining e, em muitos casos, encontrar blocos.



Uma CPU pode fazer tudo, mas não está optimizada para nada. Ela executa instruções muito gerais, com lógica complexa. Para uma tarefa como o hashing repetitivo de cabeçalhos de blocos, não é a ferramenta ideal, mas no arranque da rede, a dificuldade é tão baixa que é mais do que suficiente para encontrar blocos.



Este período é importante, pois recorda-nos um ponto importante: O proof of work não depende de uma categoria particular de equipamento. O que conta é a capacidade de calcular hashes mais rapidamente do que outros, a um determinado custo. Assim que surge uma vantagem técnica, esta transforma-se automaticamente numa vantagem económica. Mas, em termos absolutos, ainda hoje é possível tentar encontrar blocos Bitcoin usando um CPU convencional. Esta é a abordagem adoptada pelo projeto NerdMiner, por exemplo. As chances de encontrar um bloco são praticamente nulas, mas ainda há uma probabilidade infinitesimal.



https://planb.academy/tutorials/mining/hardware/nerdminer-c9826fd9-c2b4-4d1e-8c78-809122de1654

### Mudança para GPUs



Em breve, os mineiros aperceberam-se de que o estrangulamento não era a potência, mas a capacidade de efetuar um grande número de operações semelhantes em paralelo. Era exatamente isso que as unidades de processamento gráfico (GPUs) podiam fazer. Originalmente, uma GPU tinha sido concebida para efetuar as mesmas operações em grandes quantidades de dados. Esta arquitetura era perfeitamente adequada para uma tarefa como o hashing repetido: em vez de ter alguns núcleos altamente versáteis, tem centenas, ou mesmo milhares de unidades capazes de executar as mesmas instruções em simultâneo.



Com um consumo de energia comparável, uma GPU pode produzir muito mais hashes por segundo do que uma CPU. Ao mesmo tempo, o bitcoin tinha uma taxa de câmbio em relação ao dólar, o seu valor estava a aumentar e estavam a surgir plataformas de troca. A partir daí, a natureza do mining começou a mudar. Já não se tratava apenas de participar, mas de ganhar dinheiro. Apareceram configurações dedicadas: máquinas construídas em torno de várias placas gráficas, por vezes sem ecrãs, com um sistema mínimo e software especializado, cujo único objetivo era a mineração.



Foi nesta altura que a dificuldade do mining começou a explodir. Entre meados de 2010 e meados de 2011, aumentou até por um fator de 1.000. Mecanicamente, a especialização começa, tal como as primeiras formas de industrialização, e os utilizadores comuns - que se contentam em executar o software Bitcoin nos seus computadores pessoais - têm agora apenas uma hipótese muito pequena de encontrar um bloco válido.



![Image](assets/fr/044.webp)



*Fonte: [CoinWarz.com](https://www.coinwarz.com/mining/bitcoin/hashrate-chart)*



Entre a era da GPU e a era moderna do [ASIC](https://planb.academy/resources/glossary/asic), houve uma fase intermédia: a utilização de FPGAs. Uma FPGA é um componente reprogramável: pode ser configurada para implementar diretamente um circuito lógico dedicado a um cálculo específico, neste caso o `SHA256d`. A ideia era afastar-se ainda mais do hardware de uso geral (CPU/GPU) para ganhar em eficiência energética. Mas, em breve, as melhorias efectuadas virtualmente nos FPGAs seriam aplicadas fisicamente aos próprios chips: é a chegada do ASIC.



### A chegada do ASIC



A fase final da especialização do hardware mining foi o aparecimento dos ASICs (*Application-Specific Integrated Circuits*). Um ASIC é um chip concebido para uma única tarefa. No caso do Bitcoin mining, esta tarefa é precisamente a execução do `SHA256d` à velocidade máxima e com uma eficiência energética óptima. Ao contrário de um GPU, um ASIC não é utilizado para executar jogos, renderização 3D ou IA. Serve para fazer hashing, e mais nada.



![Image](assets/fr/045.webp)



*ASIC S21 XP fabricado pela Bitmain*



Esta especialização tem duas consequências importantes:




- O primeiro é um salto em termos de desempenho e eficiência. Para dispositivos de geração comparável, um ASIC produz muito mais hashes por segundo do que uma GPU, consumindo menos energia. O Mining com uma GPU tornou-se rapidamente não competitivo: embora funcionasse tecnicamente, o custo da eletricidade ultrapassava largamente as receitas esperadas na maioria dos contextos;
- A segunda é uma mudança de modelo: o investimento deslocou-se principalmente para hardware de nível industrial. O Mining implica agora a compra de máquinas concebidas para o efeito, a sua alimentação contínua, a sua refrigeração, a sua manutenção e a absorção da sua obsolescência. Porque um ASIC não é economicamente eterno: quando uma nova geração mais eficiente chega ao mercado, as máquinas antigas tornam-se progressivamente menos rentáveis, mesmo que se mantenham funcionais.



A partir daí, já não estamos a falar apenas de um passatempo. Estamos a falar de um sector em que a competitividade depende de uma equação:




- custo da eletricidade;
- custo do equipamento e amortizações;
- capacidade de arrefecimento e de funcionamento em grande escala;
- disponibilidade e fiabilidade da máquina;
- velocidade das comunicações;
- etc.



### Explorações agrícolas Mining



Uma máquina isolada pode minerar, mas ao agrupar centenas, depois milhares de ASICs num único local, partilhamos custos fixos, optimizamos a logística e aproximamo-nos de um modelo de centro de dados especializado.



Uma [quinta mining](https://planb.academy/resources/glossary/mining-farm), na sua forma mais simples, é um edifício (ou conjunto de contentores) cheio de ASICs a funcionar 24/7. O desafio agora é manter condições de funcionamento estáveis:




- fornecer grandes quantidades de energia eléctrica estável e de baixo custo;
- gerir o calor para evitar o estrangulamento, uma vez que a densidade energética é considerável;
- filtrar o pó, controlar a humidade, limpar;
- monitorização em tempo real do desempenho da máquina (temperaturas, erros de hardware, quedas de hashrate, etc.).



![Image](assets/fr/043.webp)



*Um dos sete edifícios dedicados ao Bitcoin mining nas instalações da Riot Platforms em Rockdale, perto de Austin, Texas. Este é especificamente dedicado à imersão mining*



O Mining é agora impulsionado por operadores industriais, alguns dos quais cotados na bolsa, que estão a construir e a explorar explorações agrícolas em grande escala. Entre estes contam-se a MARA Holdings (Nasdaq: `MARA`) e a Riot Platforms (Nasdaq: `RIOT`).



![Image](assets/fr/042.webp)



Mesmo sem entrar nos pormenores dos modelos de rentabilidade, é importante compreender porque é que o mining assumiu esta forma. A prova de trabalho é um mecanismo competitivo: a probabilidade de encontrar um bloco e, por conseguinte, de ganhar dinheiro, é proporcional à quota de hashrate que se utiliza. Consequentemente, existe uma pressão constante para aumentar o poder de computação, reduzir o custo por unidade de computação e limitar as perdas. Consequentemente, os ambientes que oferecem eletricidade mais barata, um clima propício ao arrefecimento ou uma infraestrutura energética abundante tornam-se naturalmente mais atractivos.



O Mining Bitcoin evoluiu assim de uma atividade acessível a qualquer pessoa nos seus primórdios para uma atividade dominada por equipamentos especializados e operações profissionais. Este facto não altera as regras do protocolo. Em teoria, qualquer pessoa pode minerar com qualquer máquina. Mas, na prática, o nível de dificuldade e de eficiência da ASIC tornou a mining doméstica largamente não competitiva na maioria dos contextos.



É claro que ainda há situações em que o mining doméstico pode ser interessante, por exemplo, se beneficiar de eletricidade muito barata ou se utilizar o calor generated do seu mineiro para aquecer a sua casa no inverno. Mas, em qualquer dos casos, terá de comprar uma máquina equipada com um chip ASIC. Além disso, uma vez que a sua potência mining continuará a ser extremamente pequena em relação à rede Bitcoin, terá de encontrar uma forma de reduzir a variância dos seus rendimentos: é precisamente este o papel dos pools mining, de que falaremos no próximo capítulo.



Se quiser explorar soluções domésticas mining com recuperação de calor, temos tutoriais sobre várias ferramentas, tanto prontas a utilizar como de bricolage:



https://planb.academy/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

https://planb.academy/tutorials/mining/hardware/canaan-avalon-nano-3f6ac96e-ea8a-4dee-9b9b-13875824c9a6

https://planb.academy/tutorials/mining/hardware/attakai-0d177e6b-e167-4b25-8e38-4ec74213d1fb

## Agrupamento em pools mining


<chapterId>c871bece-eebe-4ef4-9789-d47251f16c8b</chapterId>



Mining O Bitcoin implica custos contínuos e inevitáveis, entre os quais se destaca o consumo de energia das máquinas. Estas despesas são efectuadas independentemente dos resultados, embora as receitas do mining sejam, pela sua própria natureza, raras e aleatórias. A descoberta de um bloco depende exclusivamente da quota-parte do mineiro no hashrate, o que torna os ganhos tanto mais imprevisíveis quanto menor for essa quota-parte. É precisamente este problema prático que levou rapidamente à utilização generalizada de [pools de mining](https://planb.academy/resources/glossary/pool-mining). Neste capítulo final do curso MIN 101, apresento uma introdução aos princípios e ao funcionamento dos pools mining no Bitcoin.



### O que é uma piscina mining?



Um pool mining é uma organização (muitas vezes um serviço online) que agrega o poder de computação de muitos mineiros independentes, a fim de aumentar a frequência com que o seu grupo encontra blocos. Quando a pool encontra um bloco, a recompensa do bloco é então redistribuída entre os participantes de acordo com as regras internas da pool (que serão abordadas no curso MIN 201, uma vez que são demasiado complexas para o MIN 101).



Os participantes numa pool mining são então muitas vezes referidos como "[hashers](https://planb.academy/resources/glossary/hasher)", em vez de "mineiros", uma vez que já não realizam todo o trabalho mining, mas simplesmente fazem o hash dos dados que lhes são transmitidos pela pool.



Tenha cuidado para não confundir o pool mining com o farm mining. São dois conceitos diferentes. Como vimos no capítulo anterior, uma farm é um local físico onde uma única entidade opera várias máquinas mining. Uma pool, por outro lado, é sobretudo um agrupamento virtual: milhares de máquinas, muitas vezes dispersas geograficamente, trabalham sob uma coordenação comum. No entanto, uma quinta pode participar, e muitas vezes participa, numa pool.



![Image](assets/fr/048.webp)



### Reduzir a variação do rendimento



Então, porquê juntar-se a uma pool? Muito simplesmente porque o resultado da atividade do mining é probabilístico: com cada tentativa de hash, há uma hipótese muito pequena de atingir o objetivo de dificuldade e, portanto, produzir um bloco válido.



A muito longo prazo, os seus ganhos médios devem ser proporcionais à sua quota do hashrate global. Este princípio decorre diretamente das leis da probabilidade: cada cálculo de hash constitui um sorteio aleatório independente e, pela lei dos grandes números, a frequência com que descobre blocos converge matematicamente para a sua fração do total de hashrate da rede. No entanto, a curto e médio prazo, os seus ganhos reais podem ser extremamente irregulares. É a esta discrepância entre a média teórica e a realidade aleatória que chamamos **variância** em matemática.



Eis um exemplo simples para ilustrar o princípio:




- A rede Bitcoin produz uma média de 144 blocos por dia (aproximadamente um bloco a cada 10 minutos);
- Se tiver `0,0001 %` do total de hashrate, a sua expetativa é `144 × 0,000001`, ou `0,000144` bloco/dia;
- Por outras palavras, deverá encontrar um bloco, em média, a cada `1 / 0,000144` dias, ou seja, a cada 6.944 dias, ou cerca de 19 anos.



Mas este valor corresponde apenas a uma expetativa matemática: a distribuição dos tempos de descoberta segue uma lei aleatória, pelo que é perfeitamente possível, na prática, nunca descobrir um único bloco, mesmo durante um período muito longo. É possível ter azar e não encontrar nada durante muito tempo, pagando simultaneamente custos recorrentes (eletricidade, manutenção, depreciação do equipamento...).



A pool mining altera a natureza deste problema: ao combinar hashrates, a pool encontra blocos com mais frequência. Cada participante concorda então em receber apenas uma fração de cada bloco encontrado, mas com muito mais frequência. Trata-se de uma transformação de um rendimento altamente volátil e muito espaçado para um rendimento mais regular, à custa da partilha dos prémios e do pagamento de taxas de serviço.



### Porque é que a variância diminui quando se agrupa?



Quanto maior for o seu poder de computação, maior será a frequência esperada de blocos encontrados. Mais importante ainda, quanto mais frequentes forem os eventos, mais os resultados observados se aproximam da média estatística num determinado período.



Numa base individual, um mineiro de pequena escala pode passar anos sem um único bloco, receber um grande pagamento num dia e depois nada. Num pool, a mesma realidade probabilística continua a aplicar-se, mas é suavizada à escala colectiva: o pool encontra blocos com mais frequência e a redistribuição converte estes eventos em pagamentos mais regulares para cada participante. **O pool do mining vende, portanto, previsibilidade na atividade do mining**.



### Marcos históricos



Como vimos no capítulo anterior, no início, o mining podia ser feito a solo com um computador convencional, pois a dificuldade era muito baixa. Mas à medida que o hashrate global explodiu (GPU, depois ASIC), o mining a solo tornou-se uma aposta muito demorada para a maioria dos participantes.



As primeiras pools foram criadas precisamente em resposta a esta nova realidade. O Braiins Pool (anteriormente Slush Pool / Bitcoin.cz) é o primeiro pool Bitcoin mining: extraiu o seu primeiro bloco a 16 de dezembro de 2010. O sucesso deste primeiro pool mining foi rápido, pois em apenas alguns dias capturou quase 3,5% do hashrate global.



![Image](assets/fr/047.webp)



Do ponto de vista técnico, os pools foram então estruturados em torno de protocolos de comunicação especializados entre o pool e os mineiros (por exemplo, [Stratum](https://planb.academy/resources/glossary/stratum), depois Stratum V2), a fim de orquestrar eficientemente o trabalho distribuído. Iremos analisar mais detalhadamente estes conceitos no nosso curso de formação MIN 201.



### A situação atual



No momento em que escrevo (início de 2026), o Bitcoin hashrate global está numa ordem de grandeza de zetta-hash por segundo (= 1.000 EH/s = 1.000.000.000.000.000.000.000.000 hashes por segundo), e quase todos os blocos encontrados vêm de pools mining.



Eis uma classificação, até à data, dos principais pools de mining e da sua respectiva quota de hashrate. É provável que esta classificação se altere na altura em que ler este curso. Para obter dados actualizados, visite [mempool.space] (https://mempool.space/graphs/mining/pools).



![Image](assets/fr/046.webp)



| Ranking    | Pool           | Blocks found  | Hashrate share   |
| ---------: | -------------- | ------------: | ---------------: |
|          1 | Foundry USA    |          1297 |           29.57% |
|          2 | AntPool        |           755 |           17.21% |
|          3 | ViaBTC         |           514 |           11.72% |
|          4 | F2Pool         |           467 |           10.65% |
|          5 | SpiderPool     |           349 |            7.96% |
|          6 | MARA Pool      |           229 |            5.22% |
|          7 | SECPOOL        |           197 |            4.49% |
|          8 | Luxor          |           128 |            2.92% |
|          9 | Binance Pool   |           105 |            2.39% |
|         10 | OCEAN          |            78 |            1.78% |
|         11 | SBI Crypto     |            70 |            1.60% |
|         12 | Braiins Pool   |            54 |            1.23% |
|         13 | WhitePool      |            33 |            0.75% |
|         14 | Mining Squared |            26 |            0.59% |
|         15 | BTC.com        |            16 |            0.36% |
|         16 | Poolin         |            14 |            0.32% |
|         17 | ULTIMUSPOOL    |            14 |            0.32% |
|         18 | GDPool         |            12 |            0.27% |
|         19 | Innopolis Tech |            11 |            0.25% |
|         20 | NiceHash       |             8 |            0.18% |
|         21 | RedRock Pool   |             8 |            0.18% |
|         22 | Unknown        |             2 |            0.05% |
|         23 | Public Pool    |             1 |            0.02% |

*Fonte [mempool.space](https://mempool.space/graphs/mining/pools), dados de um mês, 16 de dezembro de 2025 a 16 de janeiro de 2025.*



Num curso mais avançado, aprofundaremos o funcionamento interno dos pools (partilhas, protocolos de rede, métodos de pagamento...), porque é aqui que entram os pormenores que determinam tanto a rentabilidade do mineiro como as potenciais implicações para o Bitcoin.



---

Chegámos agora ao fim do MIN 101. Obrigado por o ter seguido até ao fim. Se quiser avaliar as competências que adquiriu ao longo do curso, tem à sua espera um exame final na próxima secção.



Com os conhecimentos básicos que acabaste de adquirir, podes agora fazer cursos mais avançados sobre o mining no Plan ₿ Academy, quer teóricos, como este, quer mais práticos, para que também tu possas começar a participar no Bitcoin mining!



# Parte final


<partId>eced8ca1-971d-4a22-9254-dbf8bce15d1b</partId>



## Comentários e classificações


<chapterId>dc005a96-f4b4-42be-ab72-d4624c110716</chapterId>


<isCourseReview>true</isCourseReview>

## Exame final


<chapterId>959f06cf-fd66-4f29-b7ee-665bfedfea0d</chapterId>


<isCourseExam>true</isCourseExam>

## Conclusão


<chapterId>f16a4e42-c16e-466b-ad16-f42b5360f510</chapterId>


<isCourseConclusion>true</isCourseConclusion>