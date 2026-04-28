---
name: Configurando seu primeiro nó do Lightning
goal: Compreender, instalar, configurar e utilizar um nó do Lightning
objectives: 


  - Compreender a função e a finalidade de um nó do Lightning.
  - Identificar as diferentes soluções de software disponíveis.
  - Instalar e configurar um nó Lightning (LND).
  - Ligar uma conta de despesas.
  - Conhecer os riscos da utilização de um nó de relâmpago.


---

# O seu primeiro passo para a autonomia no Lightning



Já adquiriu o seu primeiro sats, assegurou os seus fundos de auto-custódia e implementou um nó Bitcoin para ser soberano na sua utilização do on-chain. O próximo passo é ganhar a mesma autonomia no Lightning: é precisamente esse o objetivo deste curso.



O LNP202 destina-se a utilizadores intermédios e orienta-o passo a passo através da implementação do seu primeiro nó Lightning, sem competências técnicas avançadas.



Aprenderá a instalar o LND no Umbrel, a abrir e gerir os seus canais, a supervisionar o seu nó e a ligar um wallet móvel, para que possa usufruir de uma experiência comparável à de um wallet de custódia, mantendo um controlo total sobre os seus fundos.



+++


# Introdução


<partId>5e77c17a-0853-4f36-a988-1b4a956f49e4</partId>



## Descrição geral do curso


<chapterId>e0871abf-af6d-4221-9389-1a996aea9b79</chapterId>



O LNP202 é um curso prático concebido para o tornar autónomo no Lightning, operando o seu próprio nó. O objetivo é simples: começar com um nó Bitcoin já instalado, implementar o LND no Umbrel, protegê-lo adequadamente, abrir e gerir os seus primeiros canais e, em seguida, utilizar o seu nó diariamente a partir de um wallet móvel. Este curso pressupõe que já tenha feito o BTC 202, uma vez que estou a assumir que o seu nó Bitcoin no Umbrel está instalado e sincronizado. Não voltaremos a falar sobre como configurar um nó Bitcoin aqui.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Para uma melhor compreensão da mecânica interna do Lightning, o curso LNP 201 também é altamente recomendado, embora não seja um pré-requisito para este curso:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Na primeira parte deste curso LNP202, veremos o que é realmente um nó Lightning, como ele difere de um simples wallet e por que operar um nó pessoal é a única maneira de usar o Lightning sem delegar seu sats a um terceiro confiável. Esta secção termina com uma escolha estratégica: qual a solução mais adequada para si, desde as abordagens mais simples até ao nó Lightning clássico, o que iremos implementar neste curso.



Na Parte 2 do curso, instalará o LND no Umbrel e, em seguida, colocará em prática os elementos que evitam os erros mais dispendiosos: uma estratégia de backup realista e proteção contra batota através de uma torre de vigia. Quando estes elementos básicos estiverem implementados, abrirá o seu primeiro canal, para que possa começar a pagar no Lightning com a sua própria infraestrutura.



Como vê: neste curso LNP202, vamos configurar um nó Lightning em modo plug-and-play através do Umbrel, em vez da abordagem clássica de linha de comandos, para o tornar adequado a utilizadores intermédios. Se preferir uma instalação de linha de comando, recomendo que siga o tutorial abaixo. Outros cursos de Lightning mais avançados, orientados por linha de comando, também estão em preparação.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

A Parte 3 irá levá-lo de um nó que funciona para um que sabe como controlar. Começará por determinar o perfil do operador do seu nó Lightning (consumidor, comerciante ou router), depois irá familiarizar-se com um software de gestão completo, a fim de seguir os seus canais e atuar de forma limpa na sua topologia. Por fim, abordará um ponto muito importante do Lightning: como obter liquidez de entrada, seja através de soluções pagas ou cooperativas.



A Parte 4 centrar-se-á na utilização quotidiana. Irá estabelecer uma ligação entre o seu nó e um cliente móvel, para que possa pagar e receber simplesmente a partir do seu smartphone, sem abdicar da auto-custódia. Começaremos por analisar uma abordagem de rede através do *Tailscale* e, em seguida, uma abordagem de protocolo através do *Nostr Wallet Connect*, com as respectivas vantagens e desvantagens. O curso terminará com um capítulo final que lhe dará os hábitos certos para manter a sua auto-custódia, tanto a nível operacional como pedagógico.



Se seguir este curso LNP202 na ordem correta, no final terá uma configuração completa para o seu nó Lightning, funcional para a utilização diária e, acima de tudo, sob controlo.




## Compreender os nós do Lightning


<chapterId>8275dfd8-7a72-48cc-bf7f-bc2a46063003</chapterId>



Antes de lançar seu próprio nó, este capítulo faz uma breve revisão da teoria básica por trás do [Lightning Network](https://planb.academy/resources/glossary/lightning-network). De facto, é importante compreender os mecanismos envolvidos, uma vez que isso lhe permitirá identificar os riscos e adotar boas práticas para os limitar. No entanto, não entrarei em detalhes aqui, pois este não é o objetivo principal deste curso. Se quiser aprofundar o assunto, recomendo vivamente que consulte o curso LNP 201 de Fanis Michalakis, que é uma referência na matéria:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### O que é um nó de relâmpago?



Vamos voltar ao básico: antes de definir o que é um nó, precisamos entender o que é Lightning Network. É um protocolo de camada superior, construído sobre o Bitcoin, concebido para permitir transacções BTC [offchain](https://planb.academy/resources/glossary/offchain) que são rápidas (com finalização quase instantânea) e geralmente baratas. "Offchain" significa que as transacções efectuadas no Lightning não se destinam a aparecer na [blockchain](https://planb.academy/resources/glossary/blockchain) principal do Bitcoin. O Lightning é também uma resposta parcial à crescente utilização do Bitcoin e ao congestionamento na cadeia, que está a levantar preocupações sobre a [escalabilidade](https://planb.academy/resources/glossary/scalability) do sistema.



Para funcionar, a Lightning baseia-se na abertura de [canais de pagamento](https://planb.academy/resources/glossary/payment-channel) entre os participantes, nos quais as transacções podem ser realizadas quase instantaneamente, muitas vezes com taxas mínimas, sem a necessidade de as registar uma a uma na cadeia de blocos Bitcoin. Estes canais podem permanecer abertos durante muito tempo, exigindo transacções [onchain](https://planb.academy/resources/glossary/onchain) apenas quando são abertos e fechados.



Um [nó Lightning](https://planb.academy/resources/glossary/lightning-node) é um participante na rede Lightning, abrindo canais e efectuando pagamentos com outros nós. Em termos concretos, um nó Lightning é uma peça de software que corre num computador e implementa o protocolo Lightning Network. Exemplos incluem LND, Core Lightning ou Eclair. O principal papel deste software é:




- ligar-se a um [nó Bitcoin](https://planb.academy/resources/glossary/full-node) para obter informações da cadeia de blocos principal;
- criar e gerir canais de pagamento bidireccionais com outros nós;
- trocar mensagens com toda a rede Lightning.



![Image](assets/fr/001.webp)



### Nó vs. Lightning Wallet: uma distinção importante



No Bitcoin (onchain), "*[wallet](https://planb.academy/resources/glossary/wallet)*" refere-se ao software que gere as suas [chaves privadas](https://planb.academy/resources/glossary/private-key), calcula o seu saldo a partir dos seus [UTXOs](https://planb.academy/resources/glossary/utxo) e constrói as suas transacções. Este wallet pode ser baseado no seu próprio nó Bitcoin ou no de outra pessoa, mas atualmente, o papel do nó e o do wallet onchain são claramente distintos.



No Lightning, é mais difícil reutilizar este tipo de vocabulário sem criar confusão. O termo "*Lightning wallet*" é bastante vago, porque na realidade não existe um wallet Lightning verdadeiramente auto-custodial, a menos que seja baseado num nó. Assim, apenas duas situações são possíveis:



- Para ter um nó Lightning real (ou seja, não custodial): o software que está a usar (por exemplo, uma aplicação móvel como o Phoenix ou uma instância LND no Umbrel) está realmente a executar um nó, e você realmente detém as chaves para recuperar os seus bitcoins. Neste caso, o seu "*Lightning wallet*" é, na realidade, apenas uma interface de utilizador sobre um nó Lightning, seja ele incorporado ou remoto.



- Para utilizar um serviço de custódia: utiliza uma aplicação que lhe mostra um saldo em [sats](https://planb.academy/resources/glossary/satoshi-sat) no Lightning, mas em segundo plano, os fundos estão num nó de um fornecedor (por exemplo, Wallet of Satoshi). O utilizador não tem nem as chaves nem o controlo dos canais. O seu saldo é apenas um registo contabilístico na base de dados da empresa. É comparável a deixar os seus bitcoins numa plataforma de troca, com todos os riscos associados. Neste caso, o seu "*Lightning wallet*" é apenas um acesso a uma conta gerida por um operador que, por sua vez, gere um verdadeiro nó Lightning.



Portanto, não há meio termo no Lightning: ou você tem um nó (mesmo um incorporado) e está em autocustódia, ou não tem, então uma empresa possui seu sats. Mas, como veremos nos próximos capítulos, esses dois usos às vezes podem ser difíceis de distinguir. Por exemplo, o Phoenix é uma aplicação móvel que incorpora um nó Lightning real, mas o utilizador não está necessariamente consciente disso, uma vez que a complexidade total do seu funcionamento está quase totalmente escondida.



### Uma recordação do funcionamento do Lightning Network



Nesta secção, vou relembrar rapidamente como funciona o Lightning. Mais uma vez, se desejar uma apresentação mais aprofundada dos conceitos teóricos, convido-o a dar uma vista de olhos no curso dedicado LNP 201.



#### Canais de pagamento: abrir, atualizar e fechar



O coração da rede Lightning baseia-se em canais de pagamento bidireccionais. Um canal pode ser aberto (ou seja, criado), atualizado à medida que as transações Lightning ocorrem e, finalmente, fechado. Do ponto de vista da onchain, um canal nada mais é do que uma [saída](https://planb.academy/resources/glossary/output) 2/2 [multisignature](https://planb.academy/resources/glossary/multisig).



![Image](assets/fr/002.webp)



Do ponto de vista da Lightning, trata-se de um canal de pagamento com [liquidez](https://planb.academy/resources/glossary/liquidity-lightning) dividida entre os dois participantes.



![Image](assets/fr/003.webp)





- Abrir um canal:**



Dois nós decidem abrir um canal. Um deles compromete bitcoins numa transação onchain chamada *transação de financiamento*. Esta transação cria uma saída baseada num [script](https://planb.academy/resources/glossary/script) 2-of-2 multisignature, o que significa que gastar estes fundos no Bitcoin requer a [assinatura](https://planb.academy/resources/glossary/digital-signature) de ambos os nós no canal. Antes de emitir esta transação, a parte que fornece os fundos pede à outra que assine uma *transação de levantamento*, que não é emitida na cadeia, mas que lhe permite recuperar os seus fundos em caso de problema.



![Image](assets/fr/004.webp)





- Transacções Commitment:**



O estado do canal (ou seja, a distribuição de sats entre A e B) é representado por um *[commitment transaction](https://planb.academy/resources/glossary/commitment-transaction)*, conhecido por ambos os nós, mas não imediatamente transmitido na blockchain. Esta transação descreve como redistribuir os fundos do canal na cadeia de acordo com os pagamentos efectuados no Lightning.



Com cada pagamento relâmpago, os dois nós assinam um novo estado que substitui o anterior. O estado antigo é revogado graças a um mecanismo de chave de revogação: se um dos participantes tentar transmitir um estado antigo, o outro pode recuperar o montante total dos fundos como penalização.



A ideia importante aqui é que há sempre uma transação Bitcoin assinada, não transmitida na cadeia, mantida pelos nós, e que permite a redistribuição dos sats uns dos outros de acordo com os pagamentos efectuados no Lightning Network.



![Image](assets/fr/005.webp)





- Encerramento do canal:**



Um canal pode ser fechado de forma limpa através de um encerramento cooperativo, quando ambas as partes concordam com o estado final do canal, ou unilateralmente (um encerramento forçado) se um dos participantes deixar de cooperar ou se tornar inacessível. Em todos os casos, o encerramento assume a forma de uma transação onchain que gasta a saída 2/2 e distribui os fundos entre os participantes de acordo com o último estado válido do canal.



![Image](assets/fr/006.webp)



O Lightning funciona assim como uma camada secundária ancorada no Bitcoin: apenas determinados eventos (a abertura e o fecho de canais) aparecem na blockchain principal. Os pagamentos intermédios permanecem fora da cadeia.



Antes de prosseguir, aqui estão dois conceitos essenciais para entender como gerenciar um canal Lightning:




- Liquidity*: a quantidade de sats disponível num dos lados do canal;
- A *[capacidade](https://planb.academy/resources/glossary/lightning-channel-capacity)*: é o montante total bloqueado na saída 2/2 multisig, ou seja, a soma da liquidez em ambos os lados do canal.



#### Uma rede de canais e de liquidez



Um canal não serve apenas para pagamentos entre dois nós: ele faz parte de uma rede global de canais interconectados. O seu nó pode encaminhar pagamentos para outros utilizadores através dos seus próprios canais, e pode enviar sats para um nó Lightning com o qual não tenha um canal direto, desde que seja possível encontrar um caminho válido entre os seus dois nós.



Cada nó conhece, através do protocolo [gossip](https://planb.academy/resources/glossary/gossip), um mapa desta rede: que canais existem, que nós estão ligados por um canal bidirecional e que capacidades estão publicadas. Para enviar um pagamento a um destinatário sem canal direto, o seu nó calcula uma rota composta por vários saltos: o seu nó → nó X → nó Y → nó destinatário. Em cada salto, o pagamento transita por um canal que deve ter liquidez suficiente no sentido do pagamento.



![Image](assets/fr/007.webp)



A liquidez de um canal não é, portanto, simétrica: um lado pode estar muito carregado, enquanto o outro está quase vazio. Gerir esta liquidez, ou seja, saber onde estão os sats e em que direção podem fluir, é um dos aspectos mais importantes da exploração de um nó Lightning. Iremos analisá-lo com mais pormenor nos capítulos práticos que se seguem.



#### HTLC: Transportar o pagamento sem ser roubado



Para permitir que os pagamentos passem por nós intermediários sem a necessidade de confiança, o Lightning usa [contratos inteligentes](https://planb.academy/resources/glossary/smart-contract) chamados *[HTLC](https://planb.academy/resources/glossary/htlc)* (*Hashed Time-Locked Contracts*). Em termos simples, um HTLC condiciona a transferência de fundos à revelação de um segredo e incorpora uma restrição de tempo para proteger o remetente em caso de falha da transação. Assim, cada pagamento está sujeito à apresentação de uma pré-imagem (um segredo cujo [hash](https://planb.academy/resources/glossary/hash-function) corresponde a um valor acordado). Se o destinatário final fornecer esta pré-imagem, pode reclamar os fundos, o que, por sua vez, permite a cada nó intermediário recuperar os seus próprios fundos.



![Image](assets/fr/008.webp)



Vou poupar-vos aos pormenores técnicos do funcionamento dos HTLC, uma vez que não são essenciais para os objectivos deste curso. Encontrará uma explicação pormenorizada no curso teórico LNP 201. Lembre-se apenas que os HTLCs permitem trocas atómicas: ou a transferência é concluída e ninguém é prejudicado no encaminhamento, ou falha e cada participante recupera os seus fundos iniciais. Não existe um meio termo.



### As principais implementações do nó do Lightning



Tal como acontece com o Bitcoin, existem várias implementações do protocolo Lightning. Várias equipas independentes estão a desenvolver as suas próprias versões, todas elas interoperáveis, uma vez que seguem as mesmas especificações (as [BOLT](https://planb.academy/resources/glossary/bolt)). Eis as principais implementações atualmente em uso.



#### LND (*Lightning Network Daemon*)



O LND é uma implementação completa do protocolo Lightning, escrito em Go e desenvolvido pela Lightning Labs.



![Image](assets/fr/009.webp)



#### Núcleo Relâmpago (*CLN*)



Core Lightning (anteriormente *C-Lightning*) é a implementação desenvolvida pela Blockstream. Ela é escrita em C, com alguns componentes em Rust.



![Image](assets/fr/010.webp)



#### Eclair



Eclair é uma implementação escrita em Scala e desenvolvida pela empresa francesa ACINQ. A ACINQ opera um dos nós de encaminhamento mais importantes da rede Lightning com o Eclair e utiliza esta implementação como base de software para os seus próprios produtos, como a aplicação Phoenix.



![Image](assets/fr/011.webp)



#### LDK (*Lightning Development Kit*)



LDK (*Lightning Development Kit*) é um kit de desenvolvimento Rust, mantido pela Spiral (Block, ex-Square). Não é um daemon pronto a usar, como o LND ou o CLN, mas uma biblioteca para programadores que pretendam integrar o Lightning diretamente nas suas aplicações.



![Image](assets/fr/012.webp)



Neste curso LNP202, vamos concentrar-nos principalmente no LND: a implementação mais comummente utilizada em soluções chave-na-mão para clientes privados, como o Umbrel.



E assim se vai esta breve recordação de como funciona o Lightning. Mais uma vez, se houver algum conceito que não compreenda, ou se quiser aprofundar um pouco mais antes de o pôr em prática, o curso de Fanis Michalakis é a referência essencial sobre o assunto:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb


## Porquê gerir o seu próprio Lightning node?


<chapterId>421db24e-511c-41ed-ad68-69b0662042ea</chapterId>



A resposta a esta pergunta é bastante simples, uma vez que é retórica: sem o seu próprio nó, já não está realmente a utilizar o Lightning, mas apenas a ilusão do Lightning na infraestrutura de uma empresa.



Usar um wallet de custódia Lightning significa que os bitcoins pertencem tecnicamente à empresa que opera o nó. O utilizador não detém as chaves privadas e não controla os canais. O seu saldo wallet é apenas uma linha na base de dados de um fornecedor de serviços. Esta situação é certamente muito conveniente para os principiantes, e a experiência do utilizador é muitas vezes fluida, mas a questão fundamental é: qual é a vantagem de utilizar o Bitcoin e o Lightning se acabar por abdicar dos aspectos que os distinguem das moedas e bancos tradicionais?



As duas principais propostas de valor do Bitcoin são a soberania monetária (não depender mais de uma autoridade central para emitir e manter) e a resistência à censura (impossibilidade de um terceiro impedir ou filtrar pagamentos). Um sistema de custódia na Lightning vai de encontro a estes dois objectivos: não é possível verificar a oferta monetária interna da plataforma e, por definição, um operador que detenha todos os fundos e todos os canais pode censurar, atrasar, priorizar ou bloquear os seus pagamentos. Nestas condições, podemos legitimamente perguntar-nos: **de que serve utilizar a bitcoin via Lightning se esta vai reproduzir os mesmos padrões de confiança e dependência que os sistemas monetários estatais tradicionais**.



> O que é necessário é um sistema de pagamento eletrónico baseado na prova criptográfica em vez da confiança, permitindo que duas partes dispostas a transacionar diretamente entre si sem necessidade de um terceiro de confiança.
*Livro Branco Satoshi Nakamoto, Bitcoin


Filosofia à parte, as desvantagens mais concretas para si são as seguintes. Em primeiro lugar, não tem qualquer possibilidade de verificar se a empresa detém efetivamente os bitcoins correspondentes aos saldos apresentados. Pode funcionar com reservas fraccionadas, ser pirateada, ir à falência ou simplesmente desaparecer. Neste caso, é apenas mais um credor, sem qualquer garantia real de que receberá o seu dinheiro de volta.



Em segundo lugar, a empresa está sujeita a riscos regulamentares: injunções, congelamento de fundos, pedidos de bloqueio de utilizadores ou transacções, vigilância reforçada ou mesmo proibição total de atividade em determinadas jurisdições. Todas as restrições que pesam sobre o prestador de serviços reflectem-se mecanicamente em si.



Em termos de confidencialidade, a situação não é melhor. Um operador de custódia vê todos os seus fluxos: montantes, frequências, destinatários, saldos, hábitos de consumo. Combinadas com as informações fornecidas pela aplicação e, eventualmente, com a análise da cadeia subjacente ao Bitcoin, estas informações podem fornecer um perfil muito preciso da sua atividade financeira. Mais uma vez, isto está muito longe do objetivo do Bitcoin de reduzir o controlo financeiro.



A boa notícia é que, hoje em dia, operar seu próprio nó Lightning não é mais exclusividade de especialistas técnicos, como pode ter sido no final dos anos 2010. Soluções relativamente simples estão disponíveis para usuários domésticos, que explicaremos em detalhes no próximo capítulo.




## Escolher a solução certa para o trabalho


<chapterId>615870e3-741d-4ec1-875d-a483e70f39d4</chapterId>



Hoje em dia, é possível ter uma experiência de utilização muito próxima da de um wallet de custódia Lightning, mantendo-se em autocustódia. O objetivo deste capítulo é ajudá-lo a escolher o caminho mais adequado ao seu perfil.



### Opção 1: Não utilizar diretamente o Lightning



A primeira solução é simplesmente não utilizar o Lightning nativamente, mas utilizar um Bitcoin ou [Liquid](https://planb.academy/resources/glossary/liquid-network) wallet que incorpore [atomic swaps](https://planb.academy/resources/glossary/atomic-swap). Por exemplo, as aplicações Aqua ou Bull Bitcoin Wallet utilizam este método, permitindo-lhe pagar [facturas Lightning](https://planb.academy/resources/glossary/invoice-lightning) sem operar um nó Lightning, mantendo-se em autocustódia.



O princípio é simples: os seus fundos permanecem no Bitcoin, no on-chain ou no Liquid, e acede aos mesmos através de um wallet onde detém as chaves da forma tradicional. Quando digitaliza uma fatura Lightning, o seu wallet inicia uma transação (on-chain ou Liquid) para um serviço de troca atómica. Este serviço gere então o pagamento Lightning através do seu próprio nó, utilizando os bitcoins que forneceu através do on-chain ou do Liquid. Como resultado, não tem de gerir quaisquer canais Lightning, mas pode liquidar facturas Lightning sem problemas.



![Image](assets/fr/013.webp)



A principal vantagem desta abordagem, em comparação com um wallet de custódia Lightning convencional, é que o utilizador permanece sempre na posse de 100% dos seus fundos. Os bitcoins estão na sua onchain ou Liquid wallet, com a sua própria [frase mnemónica](https://planb.academy/resources/glossary/seed). Mesmo durante a troca, o utilizador permanece na posse dos seus fundos, porque a troca é atómica. Baseia-se num mecanismo criptográfico que garante que só há dois resultados possíveis: ou a troca é totalmente bem sucedida, ou falha e o serviço não pode apropriar-se dos seus fundos.



A maior parte das carteiras que oferecem este tipo de funcionalidade baseiam-se no [Boltz](https://boltz.exchange/) para a parte técnica da troca.



Esta solução também oferece vantagens interessantes em termos de confidencialidade, especialmente quando associada ao Liquid. Para um principiante, é também muito fácil de configurar e guardar: uma frase mnemónica clássica, sem canais, sem liquidez para equilibrar...



Por outro lado, esta abordagem tem as suas limitações. Em primeiro lugar, não é incensurável: depende da disponibilidade e da boa vontade do serviço de swap. Se este deixar de querer processar a sua conta ou deixar de funcionar, já não poderá pagar as facturas Lightning através dele. Depois, há as taxas não negligenciáveis: paga tanto as [taxas de transação](https://planb.academy/resources/glossary/transaction-fees) onchain ou Liquid, como a comissão do serviço de swap. Além disso, se as taxas onchain aumentarem drasticamente, pode tornar-se muito caro utilizar o Lightning.



Assim, para uma utilização ocasional, ainda é aceitável, mas para um utilizador muito ativo do Lightning, é melhor fazer as coisas como deve ser com um verdadeiro nó Lightning.



### Opção 2: Nós Lightning integrados



A segunda categoria de soluções baseia-se em nós Lightning integrados diretamente numa aplicação móvel. O Phoenix Wallet foi pioneiro neste modelo e continua a ser uma referência. Atualmente, outros projectos oferecem abordagens comparáveis, como o Zeus (em modo incorporado) ou o BitKit.



A ideia é simples: a aplicação executa efetivamente um nó Lightning, mas todas as operações complexas são tratadas automaticamente em segundo plano. O utilizador tem uma interface "*Lightning wallet*" com uma frase mnemónica para backup, vê o saldo e paga facturas, mas não gere canais, liquidez ou a maioria dos parâmetros.



![Image](assets/fr/014.webp)



Estas soluções são sempre auto-custodiais. As chaves que controlam os fundos são generated e armazenadas no seu telemóvel, e o backup é feito através de um seed ou mecanismo equivalente. Não se trata apenas de ter uma conta num fornecedor de serviços, mas sim de possuir bitcoins bloqueados em canais que lhe pertencem e que não podem ser roubados.



As vantagens dos nós de bordo LN são numerosas:




- extremamente fácil de instalar e utilizar;
- experiência de utilizador próxima da de um Lightning wallet com custódia, mas com auto-custódia;
- sem gestão manual dos canais ou da liquidez;
- backup relativamente simples.



Mas estes wallet incorporados apresentam também limitações significativas. Em primeiro lugar, em termos de confidencialidade, o operador do serviço (por exemplo, a ACINQ no caso do Phoenix) tem uma visão bastante detalhada dos fluxos que passam pelo seu nó: quantidades, frequências, destinatários, ainda que isso deva melhorar, nomeadamente com a adoção progressiva dos *Nós Trampolim*. Em segundo lugar, o utilizador está fortemente dependente deste operador como o seu principal par Lightning. Se o nó ACINQ ficar indisponível (no caso do Phoenix), se a empresa sofrer pressões regulamentares ou alterar o seu modelo de negócio, a sua experiência de utilizador pode ser gravemente degradada ou mesmo comprometida.



Por último, esta simplicidade tem um preço. Os serviços do nó LN incorporado cobram geralmente taxas específicas sobre os depósitos, os levantamentos ou certas operações de gestão do canal. Na minha opinião, este modelo faz sentido em termos do serviço oferecido, mas para uma utilização intensiva, pode ser muito mais caro do que um nó Lightning convencional bem gerido.



### Opção 3: o nó Lightning clássico



A terceira solução, que será analisada em maior profundidade neste curso LNP202, é operar um nó Lightning convencional num servidor ou dispositivo dedicado.



Por "clássico" quero dizer que o utilizador instala e configura uma implementação Lightning (por exemplo, LND) em cima do seu próprio nó Bitcoin. Escolhe os seus pares, abre os seus canais, gere a sua [liquidez de entrada e saída](https://planb.academy/resources/glossary/inbound-capacity) e define as suas políticas de taxas de encaminhamento.



Em termos de soberania, é a melhor solução. Já não está dependente de uma empresa específica para os seus canais ou pagamentos: se um par o censurar ou fechar um canal, pode abrir outro com um nó diferente. Se um serviço desaparecer, os seus sats permanecem nos canais que controla e pode repatriá-los onchain. Também pode otimizar os seus custos a longo prazo: quando os seus canais são corretamente dimensionados e geridos, o custo global dos pagamentos pode tornar-se muito baixo.



Em termos de confidencialidade, está obviamente sujeito às limitações do próprio modelo da Lightning, mas não está a entregar todo o seu negócio a um único operador.



Em contrapartida, a criação de um nó Lightning clássico é obviamente mais complexa: é necessário instalar, configurar, manter, monitorizar as actualizações, compreender a lógica dos canais e das políticas de cobrança, gerir os canais e o fluxo de caixa, etc. Uma configuração incorrecta, uma cópia de segurança desleixada ou uma gestão descuidada podem levar mais facilmente à perda do sats. O nó também deve funcionar continuamente.



É precisamente este o caminho que lhe proponho seguir neste curso, acompanhando-o em todas as etapas para limitar os riscos e estruturar a sua abordagem.



### Que solução para que perfil de utilizador?



Para escolher a solução certa para o seu perfil de usuário do Lightning, é preciso considerar dois fatores: a frequência com que você usa o Lightning e seu apetite por gerenciamento técnico.



Se não efetuar muitos pagamentos Lightning numa base ocasional, mas ainda assim quiser poder liquidar facturas LN a partir do seu telefone de vez em quando, sem renunciar à auto-custódia: um Bitcoin ou Liquid wallet com funcionalidade de troca é provavelmente a melhor opção. Mantém a propriedade dos seus fundos, não gere nós e aceita taxas ligeiramente mais elevadas em troca de simplicidade.



https://planb.academy/tutorials/wallet/mobile/bull-bitcoin-2c72127c-a228-4f50-b833-c6183d56aaf6

https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

Se utiliza o Lightning com bastante regularidade e pretende obter as vantagens de um nó real, mas não quer perder tempo a gerir canais, taxas ou infra-estruturas, um nó Lightning móvel incorporado é uma boa solução. Mantém a custódia dos seus fundos, a experiência de utilizador permanece muito acessível e toda a complexidade é ocultada, ao preço de uma dependência acentuada de um operador.



https://planb.academy/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

https://planb.academy/tutorials/wallet/mobile/bitkit-a7224674-85c4-4045-9baf-37018d89550c

https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

Se é um utilizador intermédio ou avançado, está disposto a investir tempo na compreensão e gestão da sua infraestrutura e pretende obter o máximo controlo sobre os seus canais, liquidez e custos: um nó Lightning clássico baseado em servidor é o caminho a seguir. É a solução mais exigente, mas também a mais consistente com a ideia de soberania do Bitcoin.




# Criando seu primeiro nó do Lightning


<partId>b6db225e-61ab-437a-bccb-33d07503da15</partId>



## Instalação do LND com o Umbrel


<chapterId>a0014bf3-1bd3-4311-b15b-5ef2354ec744</chapterId>



Agora que revisamos os conceitos básicos do Lightning e as soluções disponíveis, é hora de ir direto ao assunto. Para fazer este curso, você precisará de um nó Bitcoin sincronizado com o Umbrel. Este curso de treinamento LNP202 é uma continuação do BTC 202; se ainda não tiver um nó Bitcoin, convido-o a fazer esse outro curso de treinamento antes de voltar aqui quando seu nó tiver sido sincronizado. Recomendo vivamente que o consulte, pois não entrarei em pormenores sobre o seu funcionamento, configuração e medidas de segurança.



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

Neste primeiro capítulo, veremos como instalar o LND no seu Umbrel. A forma como o Umbrel funciona torna este passo muito simples, uma vez que tudo o que tem de fazer é instalar uma aplicação.



Na página inicial, abra a `App Store` na parte inferior da interface.



![Image](assets/fr/015.webp)



Na barra de pesquisa, introduza `Lightning Node` e, em seguida, clique na aplicação.



![Image](assets/fr/016.webp)



Em seguida, clique no botão `Instalar` para iniciar a instalação.



![Image](assets/fr/017.webp)



Na página inicial, clique na aplicação para a abrir e, em seguida, selecione "Configurar um novo nó".



![Image](assets/fr/018.webp)



É-lhe dada uma frase mnemónica de 24 palavras. Guarde-a num lugar seguro. Veremos com mais detalhes no próximo capítulo como recuperar o acesso ao seu Lightning node (este é um processo muito mais complexo do que para um simples Bitcoin wallet), mas lembre-se por enquanto que esta frase desempenha um papel crucial e deve ser guardada com o máximo cuidado.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Guarde esta frase da mesma forma que uma frase mnemónica convencional: num suporte físico (papel ou metal) guardado num local seguro, depois clique no botão `NEXT`.



![Image](assets/fr/019.webp)



Em seguida, introduza as palavras da sua frase para verificar se as escreveu corretamente.



![Image](assets/fr/020.webp)



Uma mensagem de aviso lembrar-lhe-á que a aplicação está em versão beta e que o Lightning Network continua a ser uma tecnologia experimental. Obviamente, nunca coloque valores no seu Lightning node que não esteja preparado para perder.



Em seguida, você chegará à interface principal do seu Lightning node. À esquerda, você encontrará seu Bitcoin onchain wallet hospedado no seu nó. Este é o generated da frase de 24 palavras que acabou de guardar.



No centro, encontrarás o teu Lightning wallet. Na verdade, representa o seu [dinheiro de saída](https://planb.academy/resources/glossary/outbound-capacity), ou seja, os bitcoins que possui nos seus canais Lightning.



À direita, são apresentadas várias informações importantes sobre o seu nó:




- O número de ligações e canais abertos;
- O seu fluxo de caixa total de saída, ou seja, o que pode teoricamente gastar no Lightning;
- A sua liquidez total de entrada, ou seja, o que pode teoricamente receber na Lightning.



![Image](assets/fr/021.webp)



Vamos começar por personalizar o nosso nó. Clique nos três pequenos pontos no canto superior direito da interface e depois em `Configurações avançadas`. No submenu `Personalização`, pode definir um nome público para o seu nó (evite usar o seu nome verdadeiro) e escolher a sua cor.



![Image](assets/fr/046.webp)



Em seguida, clique no botão verde `SAVE AND RESTART` para reiniciar o nó e aplicar as alterações.



O seu Lightning node está agora pronto para abrir os seus primeiros canais para efetuar pagamentos. Mas primeiro, vamos ver como proteger o seu sats!



## Salvando seu Lightning node


<chapterId>638fa75d-62af-4bf3-ab4a-b7d10ea75815</chapterId>



Antes de enviar o seu primeiro sats para o seu nó, é importante entender como funciona o seu backup e quais são os riscos associados. Ao contrário de um simples portfólio Bitcoin onchain, o backup de um nó Lightning é bastante complexo: a estratégia errada pode levar à perda permanente de seus fundos. Neste capítulo, veremos o que realmente precisa ser feito no backup e como o Umbrel lida com esse processo com o LND.



Neste curso, vamos utilizar a implementação LND (*Lightning Network Daemon*). Embora os princípios sejam semelhantes nas outras implementações, os ficheiros de recuperação e os procedimentos de que vou falar são específicos do LND.



### O que devo poupar num nó de luz?



Num nó Lightning, não basta salvar o seed e esperar que tudo volte ao normal. Vários elementos desempenham papéis diferentes, pelo que é importante distingui-los.



#### O seed (*aezeed*)



Quando se inicializa o LND, recebe-se um seed de 24 palavras. Este é um formato específico do LND chamado "*aezeed*". Não é um seed BIP39 clássico, embora se pareça muito com um. A partir deste seed, o LND deriva as chaves privadas do seu wallet onchain associado ao nó Lightning, ou seja, os endereços nos quais pode receber ou para os quais pode repatriar bitcoins após o encerramento do canal.



![Image](assets/fr/019.webp)



Este seed pode, portanto, ser usado para recriar o wallet onchain associado ao seu nó e para recuperar fundos que já foram repatriados onchain (por exemplo, após o fechamento de um canal). Por outro lado, o seed por si só não é suficiente para restaurar os seus canais Lightning que ainda estão abertos, uma vez que não contém as informações necessárias sobre o estado dos seus canais.



#### A base de dados do canal (`channel.db`)



O LND armazena o status detalhado dos seus canais em um banco de dados chamado `channel.db`. Esta base de dados contém:




- a lista dos seus canais abertos;
- os seus pares e os seus identificadores;
- os últimos commitment transactions para cada canal (os estados sucessivos que definem quem possui o quê no canal e permitem que os fundos onchain sejam recuperados em caso de problema);
- a informação necessária para punir um par que tenta transmitir um relatório antigo.



O problema com esta base de dados é que ela está em constante mudança: cada pagamento, cada roteamento, cada abertura ou fechamento de um canal modifica o seu conteúdo. É por isso que um backup convencional (por exemplo, uma cópia periódica do seu `channel.db`) é perigoso. Se você restaurar uma versão muito antiga do `channel.db` e remontar o nó com este estado obsoleto, seus pares podem considerar que você está transmitindo um estado antigo do canal. Neste caso, o protocolo prevê uma penalização: o seu par pode recuperar a totalidade dos fundos do canal, como se tivesse tentado fazer batota.



Na prática, então, `channel.db` não é um meio de backup como tal. Ele é o estado vivo do seu nó. A única situação em que faz sentido usá-lo para restaurar seu nó é quando você recupera esse banco de dados diretamente de uma máquina que acabou de falhar (por exemplo, um disco que ainda é legível). Neste caso, recupera o estado mais recente e pode reiniciar o LND noutra máquina com base nesta base de dados, com a certeza de que este estado está o mais atualizado possível, uma vez que a máquina antiga já não está a funcionar. Outra situação em que este método pode servir como um backup relevante é numa configuração de dois discos, com uma cópia dinâmica e permanente de um para o outro. No entanto, este tipo de configuração é mais complexo de implementar.



Mas fazer cópias periódicas do `channel.db` e guardá-las como backups para serem restauradas mais tarde é uma péssima ideia: no dia em que as usar, corre o risco de se penalizar e perder todo o seu sats.



#### Reserva de canal estático (SCB)



Para tornar possível a recuperação de desastres, o LND introduziu o mecanismo *Static Channel Backup* (SCB). Este é um arquivo especial, muitas vezes chamado de `channel.backup`, que contém informações estáticas sobre seus canais: quem são seus pares, como contactá-los e quais são seus canais.



Esse arquivo não contém o status detalhado do canal ou o histórico de atualizações. Não permite reabrir canais no estado exato em que se encontravam, nem continuar a operar este Lightning node. Em vez disso, o seu papel é agir como um ponto de ancoragem para pedir aos seus pares para ajudá-lo a fechar todos os seus canais de forma limpa, e assim receber o seu sats onchain, em chaves que você pode recuperar graças ao seed. Assim, ao contrário do ficheiro `channel.db`, que é modificado a cada pagamento ou encaminhamento, o ficheiro SCB só é atualizado quando um canal é aberto ou fechado.



Quando a recuperação é efectuada através do SCB, o processo é o seguinte




- Restauras o teu seed (*aezeed*), que recria o teu wallet onchain associado ao nó Lightning;
- Fornecer ao LND o seu SCB mais recente;
- O LND utiliza o SCB para encontrar a lista dos seus pares e os canais que tem com eles;
- Contacta cada par, diz-lhes que sofreu uma perda de dados e pede-lhes que "forcem o fecho" do seu canal com eles, para que possa recuperar a sua partilha onchain.



A ideia é que os seus pares, percebendo que está a reportar uma perda de dados, transmitam o seu último commitment transaction e fechem o canal de força. Uma vez que estas transacções tenham sido confirmadas, os seus fundos reaparecem na sua carteira onchain (ligada ao seed).



Este mecanismo de recuperação não é perfeito, no entanto. Em primeiro lugar, ele não restaura realmente seu Lightning node, pois todos os canais serão fechados. Terá então de construir um novo Lightning node a partir do zero. Em segundo lugar, não garante 100% de recuperação, embora aumente consideravelmente as hipóteses de recuperar os seus saldos onchain em caso de problema. De facto, este protocolo de recuperação depende da cooperação e da disponibilidade dos seus pares: se um deles estiver offline, tiver perdido os seus próprios dados ou se recusar a cooperar, os seus fundos podem ficar bloqueados ou mesmo perder-se definitivamente. É por isso que é importante não manter canais abertos no seu Lightning node com pares inacessíveis por longos períodos de tempo. Se sofrer uma perda de dados nesse momento e o par permanecer inacessível, a recuperação via SCB será impossível e os seus fundos permanecerão perdidos até que esse par volte a estar online (talvez para sempre).



Em suma, uma boa estratégia de backup do Lightning no LND assenta em três pilares:




- O vosso seed (*aezeed*), para a camada onchain;
- Backup automático fiável do SCB;
- Boa gestão dos canais, escolhendo pares fiáveis e encerrando preventivamente os que são frequentemente inacessíveis.



### Como é que o Umbrel gere a cópia de segurança do seu nó LND?



O Umbrel oferece um mecanismo de cópia de segurança simplificado para o nó LND, baseado precisamente no SCB. A ideia é poupar-lhe o trabalho de manipular este ficheiro, fazer uma cópia de segurança do mesmo e automatizar o processo na medida do possível.



Quando cria o seu nó no Umbrel, recebe um seed que desempenha um papel duplo:




- deriva o seu Bitcoin onchain wallet associado ao seu Lightning node;
- é utilizado para obter um identificador de cópia de segurança e uma chave de encriptação utilizados para cópias de segurança remotas do SCB.



Graças a este mecanismo, o Umbrel faz automaticamente uma cópia de segurança encriptada do seu SCB e guarda-a nos seus servidores via Tor. O SCB é guardado encriptado, graças a uma chave derivada do seu seed. Assim, em caso de perda de dados, basta recriar um Bitcoin e um nó Lightning no Umbrel, na mesma ou noutra máquina, e depois entrar no seu seed. Poderá então recuperar o último estado do SCB dos servidores Umbrel, desencriptá-lo e iniciar o processo de recuperação dos seus fundos.



Estas cópias de segurança são encriptadas localmente pelo seu nó antes de serem enviadas, o que garante a confidencialidade dos seus dados: O Umbrel não pode ler o conteúdo do SCB. A transmissão é efectuada através do Tor, o que impede que o seu endereço IP seja divulgado. Além disso, o seu Umbrel adiciona ruído ao tráfego (preenchimento aleatório e falsos backups enviados em intervalos irregulares) para evitar que o servidor deduza exatamente quando abre ou fecha um canal.



A principal vantagem deste método é que ele simplifica consideravelmente o backup do seu nó Lightning: você só precisa fazer o backup do seu seed uma vez durante a inicialização do nó. Isto implica algum risco, uma vez que se trata apenas de um backup do SCB, mas para quantidades razoáveis é um compromisso aceitável.



### Melhores práticas para limitar o risco de perda



Mesmo com o backup do Umbrel, algumas boas práticas simples podem reduzir bastante o risco de perder o sats:





- Monitorizar a disponibilidade dos seus pares:



Se um canal importante está frequentemente associado a um par inacessível ou instável, é mais seguro fechá-lo de forma limpa enquanto o seu nó ainda está a funcionar. Um encerramento preventivo cooperativo ou forçado elimina uma potencial fonte de problemas no caso de recuperação do SCB.





- Evitar concentrar demasiada liquidez em pares desconhecidos:



Quanto maior for o canal que um par tem consigo, mais importante é ser fiável. Escolha nós sérios, bem conectados e activos, para que qualquer recuperação futura através do SCB possa decorrer sem problemas.





- Completar o Umbrel com cópias de segurança locais:



Para além do backup automático do Umbrel, pode também manter uma cópia encriptada do seu ficheiro SCB (`channel.backup`) num suporte externo e actualizá-lo periodicamente. O ideal é renová-lo sempre que abrir ou fechar um canal. Isto dá-lhe uma solução de backup se, por qualquer razão, o serviço de backup automático do Umbrel ficar indisponível.





- Gerir o seu seed da forma correta



O seu seed Umbrel não só restaura o seu wallet onchain, como também obtém a chave de encriptação para as cópias de segurança. Um atacante com acesso a ele poderia, portanto, lançar uma recuperação e transferir os seus fundos para o seu próprio wallet, sem sequer ter acesso físico ao seu nó.



Assim, se precisar de restaurar o seu nó mas já não tiver o seu seed, não conseguirá recuperar nada: todo o seu sats se perderá. Por isso, é muito importante guardar o seu seed com o máximo cuidado, apenas em suportes físicos (papel ou metal), e mantê-lo num local seguro. Para mais informações sobre a gestão de um seed, consulte este tutorial:



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

### Como é que guardo o meu nó do Lightning no Umbrel?



Agora que você entendeu como a teoria funciona, vamos ao que interessa. No seu aplicativo Lightning Node (que na verdade é o LND), clique nos três pequenos pontos no canto superior direito.



![Image](assets/fr/022.webp)



Há aqui três elementos de interesse para o apoio:




- Verifique se a opção "Backups automáticos" está activada. Isto irá enviar automaticamente o seu SCB encriptado para os servidores do Umbrel.
- Você pode então escolher se quer enviar via Tor ou clearnet, usando a opção `Backup over Tor`. Como explicado nas secções anteriores, recomendo vivamente que utilize o Tor para preservar a sua confidencialidade.
- Finalmente, existe um botão `Download channel backup file`, que lhe permite fazer o download de um ficheiro `channel.backup`, ou seja, um snapshot encriptado do seu SCB, para o seu computador. Isto permite-lhe fazer backups locais adicionais de tempos a tempos, para além dos que são enviados automaticamente para os servidores do Umbrel.



Agora você sabe como proteger o sats do seu Lightning node contra perda de dados. No próximo capítulo, veremos como proteger seu nó contra tentativas de trapaça.




## Watchtower: papel e configuração


<chapterId>e6c654dd-26c5-4e4d-8d11-a215bac37812</chapterId>



No Lightning, cada canal é baseado numa sequência de estados sucessivos, representados por commitment transactions não publicados. Com cada pagamento ou encaminhamento Lightning, os 2 participantes no canal constroem um novo par de commitment transactions, reflectindo a atual distribuição de fundos no canal. Os commitment transactions antigos tornam-se obsoletos.



Se uma das partes publicar um estado desatualizado, a outra tem o direito de o sancionar e recuperar o montante total dos fundos do canal. Neste capítulo, vamos dar uma breve olhada em como esse mecanismo funciona e, em seguida, explicar como configurar uma ***watchtower***: um sistema para proteger seu nó Lightning de possíveis tentativas de trapaça.



### Compreender o funcionamento das torres de vigia


A qualquer momento, cada parte no canal tem um commitment transaction que, se publicado, lhe permitirá fechar o canal e recuperar a sua parte dos fundos. Este processo é conhecido como *fecho forçado*. No entanto, se tentarem publicar um commitment transaction mais antigo, correspondente a um estado anterior do canal em que este tinha mais sats, esta transação será considerada uma tentativa de batota. Neste caso, a contraparte pode utilizar a chave de revogação associada a este estado mais antigo para recuperar o montante total de fundos no canal, enquanto o batoteiro é temporariamente bloqueado pelo timelock.


Este sistema significa que publicar um estado antigo, ou seja, tentar fazer batota, é muito arriscado: se a outra parte vir esta transação no mempool ou na blockchain antes de o timelock expirar, pode usar a chave de revogação e recuperar todos os fundos. **Portanto, a segurança do seu canal Lightning depende da sua capacidade de detetar uma tentativa de batota dentro da janela de tempo imposta pelo timelock**.



#### Porque é que as torres de vigia são necessárias?



O mecanismo de sanções só funciona se a pessoa lesada puder fazê-lo:




- monitorizar cada novo bloco Bitcoin para ver se foi publicado um canal commitment transaction;
- determinar se esta transação corresponde ao último estado válido ou a um estado revogado;
- no caso de um estatuto revogado, transmitir a transação legal em tempo útil, utilizando a chave de revogação para recuperar todos os fundos antes de expirar o bloqueio temporal.



![Image](assets/fr/023.webp)



Num cenário ideal, o seu nó Lightning está online 24 horas por dia, 7 dias por semana, está sincronizado e monitoriza continuamente a blockchain. Por esta razão, ele pode detetar sozinho uma tentativa de batota e reagir. Na prática, no entanto, um nó Lightning pessoal pode desligar-se, particularmente no caso de um corte de energia prolongado ou de uma falha na ligação à Internet.



É precisamente durante estes períodos de inatividade que o risco se torna real: se um peer desonesto publica um estado antigo enquanto o seu nó está offline, e o timelock se esgota sem qualquer reação da sua parte, a batota torna-se efectiva. Perde parte ou a totalidade dos seus fundos no canal.



Os Watchtower foram introduzidos para reduzir este risco. Uma torre de vigia é um serviço externo que monitoriza a cadeia de blocos em seu nome, procurando a possível publicação de um estado antigo num dos seus canais e, se necessário, transmite automaticamente a transação de penalização em seu nome. Assim, mesmo que o seu nó Lightning permaneça offline durante um longo período, desde que a torre de vigia que está a utilizar esteja operacional, será capaz de proteger os seus fundos, monitorizando quaisquer tentativas de batota e aplicando a penalização correspondente, assim que a detetar.



#### Como funciona uma torre de vigia



Uma torre de vigia foi concebida para minimizar a informação que obtém sobre os seus canais, ao mesmo tempo que lhe dá os meios para atuar em caso de problema:




- Para cada novo estado do canal com um par, o seu nó prepara antecipadamente uma potencial transação de penalização. No caso de este par fazer batota, esta transação permitir-lhe-ia recuperar todos os fundos do canal;
- O seu nó encripta então esta transação de penalização usando o TXID do commitment transaction correspondente (aquele que seria usado se o batoteiro tentasse uma fraude). Enquanto não houver encerramento, a torre de vigia não pode desencriptar esta transação, uma vez que não conhece totalmente o TXID da transação fraudulenta;
- O seu nó envia à torre de vigia um pacote contendo a transação de penalização encriptada e metade do TXID da potencial transação de batota.



Como o TXID transmitido à torre de vigia está incompleto, esta não pode desencriptar a transação de justiça. No entanto, pode monitorizar a blockchain em busca de um TXID que corresponda à parte que lhe pertence. Se detetar uma tal transação, tenta então utilizar o TXID completo dessa transação para desencriptar a sua transação de penalização. Se a desencriptação for bem sucedida, sabe que se trata de uma tentativa de batota e publica imediatamente a transação de penalização para si.



![Image](assets/fr/024.webp)



A torre de vigia não tem, portanto, qualquer visibilidade dos detalhes dos seus canais: nem a identidade dos seus pares, nem os saldos, nem a estrutura das transacções. Apenas vê os pacotes encriptados. A única informação que pode deduzir é a taxa de atualização dos seus canais, uma vez que recebe um pacote para cada novo estado, mas não pode conhecer o seu conteúdo. Em caso de batota, descobrirá certamente a informação sobre o canal decifrando a transação de penalização, mas pelo menos o seu sats será salvo.



Este mecanismo baseia-se num compromisso: você delega a capacidade de publicar uma transação de penalização pré-assinada à torre de vigia, mas esta transação permanece totalmente opaca para a torre de vigia até que ocorra alguma batota. A torre de vigia não pode modificar os destinatários nem desviar os fundos, uma vez que apenas dispõe de uma transação que já foi assinada, com os resultados congelados a seu favor. Também não pode conhecer os detalhes de um canal num fecho forçado ou cooperativo legítimo, uma vez que os TXIDs não coincidem. Por outro lado, a watchtower continua a ser uma terceira parte minimamente confiável: você precisa de contar com ela para estar online e para transmitir corretamente a sua transação de justiça quando precisar dela.



#### Tornar-se uma torre de vigia



Em teoria, qualquer nó Lightning pode atuar como uma torre de vigia para outros nós (se eles usarem a mesma implementação, por exemplo, LND), enquanto ele próprio é protegido por outros nós que desempenham esse papel para ele. Nas secções práticas seguintes, vou mostrar-lhe como configurar este mecanismo simples no seu LND sob o Umbrel.


Consequentemente, uma estratégia interessante pode ser combinar com amigos bitcoiners de confiança para actuarem como torre de vigia uns dos outros. Você vigia os canais deles e eles vigiam os seus.



### Encontrar uma torre de vigia altruísta



Se não conhece ninguém à sua volta que possa fornecer um serviço de torre de vigia, há uma série de torres de vigia públicas altruístas às quais se pode ligar. Por exemplo, neste curso LNP202, sugiro que se ligue ao serviço de torre de vigia oferecido conjuntamente por LN+ e Voltage, que é uma torre de vigia para LND.


Aqui tem os dados de início de sessão:



- Via Tor:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



- Via clearnet:


```txt
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@34.216.52.158:9911
```

Para lhes agradecer por fornecerem este serviço gratuito da Torre de Vigia, [pode fazer um donativo através do Lightning](https://lightningnetwork.plus/donation).


Agora que estamos a utilizar um serviço de torre de vigia altruísta, vamos ver como o configurar no nosso nó LND sob Umbrel.


### Instalação de uma torre de vigia


A partir da aplicação `Lightning Node`, clique nos três pontos no canto superior direito da interface e selecione `Advanced Settings`.


![Image](assets/fr/025.webp)


Em seguida, aceda ao menu `Watchtower`.


![Image](assets/fr/026.webp)



Ativar a opção `Cliente Watchtower`, em seguida clicar no botão `SALVAR E REINICIAR NODO`. Aguardar a reinicialização do LND.


![Image](assets/fr/027.webp)


Quando a reinicialização estiver concluída, volte ao mesmo menu e introduza o ID da torre de vigia altruísta da sua escolha no campo fornecido. Depois clique no botão `ADD` para confirmar. Pode também ajustar o parâmetro `Watchtower Client Sweep Fee Rate`: esta é a taxa que está disposto a pagar por uma possível transação de justiça transmitida pela torre de vigia. Não há necessidade de escolher uma taxa excessivamente alta, mas também deve evitar uma taxa demasiado baixa, caso contrário a transação legal não será confirmada a tempo.


Reinicie o seu nó utilizando o botão `SAVE AND RESTART NODE` para aplicar estas alterações.


![Image](assets/fr/028.webp)



Se voltar a este mesmo menu, verá que o seu nó Raio está agora protegido pela torre de vigia que acabou de adicionar.



![Image](assets/fr/029.webp)



Uma torre de vigia altruísta é geralmente suficiente, especialmente se não colocar grandes quantias de dinheiro no seu nó de iluminação e se gerir bem o seu nó (não o deixe desligado durante muito tempo). Para uma segurança ainda maior, podes também adicionar várias, repetindo o mesmo processo.



## Abrir o seu primeiro canal Lightning


<chapterId>00642af7-8f3d-4a25-96d7-34e85de7bd5d</chapterId>



Se chegou até aqui, já sabe que um nó Lightning sem um canal é um pouco como um wallet vazio: existe, mas é inútil. Para poder enviar ou receber pagamentos, o seu nó deve estar ligado a pelo menos um outro nó na rede Lightning através de um canal. No futuro, recomendamos vivamente a abertura de vários canais, por razões de resiliência e de eficácia de encaminhamento. Nos capítulos seguintes, veremos também como gerir os seus activos líquidos, otimizar a topologia do seu canal e utilizar ferramentas mais avançadas do que a interface básica LND no Umbrel.



Mas neste capítulo introdutório, o objetivo é simplesmente compreender como escolher um bom par Lightning, onde encontrar as informações necessárias para selecionar os seus pares e, finalmente, como abrir o seu primeiro canal através da interface básica do LND.



### Como escolher um bom par do Lightning?



Ao abrir um canal, é necessário escolher um par: outro nó do Lightning ao qual seu nó estará diretamente conectado, através de um canal. Essa escolha de par é importante, pois terá um impacto direto sobre:




- a facilidade com que os seus pagamentos são encaminhados;
- a fiabilidade dos seus canais ao longo do tempo;
- os seus custos de encaminhamento.



Não existe um par perfeito para toda a gente, mas há uma série de critérios fiáveis para identificar bons candidatos.



#### 1. Conectividade de nós



Um bom par é um nó que está bem ligado à rede Lightning. Isto significa não só ter um grande número de canais (embora isso possa ser um indicador), mas sobretudo estar ligado a outros nós fiáveis e ocupar uma posição suficientemente central no gráfico da rede.



Um nó bem ligado aumenta as suas hipóteses de encontrar uma rota eficiente para a maioria dos destinos de pagamento. Também reduz o número de nós intermediários necessários, o que mantém os custos baixos.



Por outro lado, abrir o seu primeiro canal a um nó isolado ou fracamente ligado pode restringir as suas possibilidades: poderá pagar a esse par, mas será muito mais difícil pagar ao resto da rede.



#### 2. Capitalização e capacidade do canal



Um bom par é também um nó suficientemente capitalizado. Isto é demonstrado pela sua capacidade total de canal (a soma de sats comprometidos com todos os seus canais) e a sua capacidade média de canal (muitas vezes é melhor ter apenas alguns canais bem capitalizados do que muitos pequenos).



Um nó com uma capacidade ridícula, ou cujos canais são todos minúsculos, não conseguirá encaminhar pagamentos com montantes elevados, o que resultará em falhas de encaminhamento para o utilizador.



#### 3. Políticas de despesas



Cada nó define as suas próprias taxas de encaminhamento (`taxa base` e `taxa de taxa`). Um bom par não cobrará taxas exorbitantes para canais estratégicos. Para um primeiro canal, é melhor escolher um nó com taxas moderadas, de modo a não prejudicar os seus próprios pagamentos.



Lembre-se que as suas próprias taxas de encaminhamento também influenciam a forma como os outros o vêem como um par: um nó que muda constantemente as suas taxas ou impõe custos absurdos raramente é apreciado.



#### 4. Estabilidade e antiguidade



A estabilidade dos pares é um critério muito importante. Um bom nó tem um tempo de atividade elevado (raramente está offline), mantém os seus canais abertos durante muito tempo e não abre/fecha canais constantemente sem motivo.



Canais antigos e ainda activos são um bom sinal: sugerem que a relação é rentável para o par, que o nó sabe como gerir o seu capital e que não fecha a qualquer momento, pelo que não tem de continuar a pagar taxas onchain para fechar e reabrir.



Por outro lado, um colega que esteja frequentemente offline, ou que feche rapidamente os canais, pode ser uma fonte de problemas para si e de custos adicionais para a abertura de novos canais.



Mesmo com estes critérios, não fará uma escolha perfeita à primeira. É normal: a verdadeira qualidade de um par é revelada pela sua utilização. Por isso, é importante:




- monitorizar a atividade do canal (volumes encaminhados, disponibilidade, etc.);
- fechar canais que não servem para nada ou cujos pares estão demasiadas vezes offline;
- reafectar o seu capital a melhores pares ao longo do tempo.



A ideia não é abrir e fechar canais todos os dias (o que seria dispendioso em termos de custos onchain), mas sim fazer evoluir gradualmente a sua topologia para convergir para um conjunto de pares fiáveis e bem ligados, compatíveis com as suas necessidades.



### Como é que posso encontrar um par?



Para aplicar esses critérios, você precisará de ferramentas que forneçam visibilidade da rede Lightning. Há vários exploradores e serviços disponíveis para fazer isso. Entre os exploradores Lightning mais conhecidos estão [1ML](https://1ml.com/) e [Amboss](https://amboss.space/).



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017

https://planb.academy/tutorials/node/lightning-network/1ml-37ada2ab-7a24-4473-87fd-007cb7640e7b

Neste caso, no entanto, sugiro que utilize [a ferramenta Terminal Lightning da Lightning Labs](https://terminal.lightning.engineering/), que fornece uma classificação (reconhecidamente baseada em critérios parcialmente subjectivos) dos nós Lightning considerados mais relevantes para a abertura de um canal.



![Image](assets/fr/030.webp)



O problema com os nós Lightning muito grandes no topo deste ranking é que a maioria não aceita aberturas de canal abaixo de quantias muito altas. Muitos também aplicam políticas rigorosas de gestão de pares, o que pode levar ao encerramento do seu canal. Por outro lado, esses nós geralmente não precisam de liquidez de entrada, dado o número de conexões.



Por isso, aconselho-o a descer na classificação para encontrar um nó que esteja bem ligado, seja fiável e suficientemente central no grafo da rede, sem ser excessivamente grande. Por exemplo, aqui identifiquei o nó Lightning em stacker.news, que está muito bem ligado, tem uma capacidade elevada e ocupa uma posição central no grafo da rede.



![Image](assets/fr/031.webp)



Outra abordagem interessante é abrir um canal para um nó que necessite de liquidez, como um comerciante conhecido, uma associação ou uma comunidade. Esta estratégia tem três vantagens:




- Uma vez que a entidade escolhida necessita de liquidez de entrada, terá logicamente menos incentivos para fechar o seu canal sem motivo;
- A sua atividade económica aumenta as possibilidades de encaminhamento neste canal e, por conseguinte, de cobrança de taxas;
- Está a fazer um favor ao ecossistema e a dar um contributo valioso a outros bitcoiners.



Uma vez identificado um nó relevante, é possível obter o seu Node ID. Isso é simplesmente uma concatenação da chave pública do nó, um separador `@`, seu endereço IP ou Tor e a porta usada. Este ID é facilmente acessível a partir do perfil do nó em qualquer explorador Lightning.



### Abra o seu primeiro canal através do LND



Agora que identificámos o nó com o qual abriremos o nosso primeiro canal, precisamos que o sats o bloqueie. Para isso, é necessário alimentar o Bitcoin onchain wallet associado ao LND.



Na interface principal do LND, localize o seu `Bitcoin Wallet` e clique no botão `Depositar`. Um endereço de receção onchain é então generated: envie sats para ele. A quantidade que você precisa transferir depende da capacidade que você deseja alocar para o seu primeiro canal, mas tenha em mente que você precisa enviar um pouco mais do que a capacidade desejada. Por exemplo, se quiseres abrir um canal de 500.000 sats, não envies exatamente 500.000 sats, mas uma quantidade superior.



![Image](assets/fr/032.webp)



Uma vez transmitida a transação, esta aparece na interface. Aguarde a confirmação antes de abrir o canal. Verá uma seta verde ao lado da transação quando esta for confirmada.



![Image](assets/fr/033.webp)



Desça até à interface principal e clique em `+ OPEN CHANNEL`.



![Image](assets/fr/034.webp)



Introduza o `Node ID` do nó com o qual deseja abrir um canal, indique o montante que deseja bloquear e, em seguida, ajuste a taxa de transação de abertura de acordo com o estado do mercado de taxas onchain. Claro, certifique-se de que você tem fundos suficientes em sua carteira LND onchain de antemão.



Uma vez definidos todos os parâmetros, clicar no botão `OPEN CHANNEL`.



![Image](assets/fr/035.webp)



Aguarde que a transação de abertura seja confirmada onchain. O teu primeiro canal está agora oficialmente operacional: parabéns!



Pode ver que, de momento, 100% da liquidez do canal está do meu lado: é normal, uma vez que fui eu que abri o canal. À medida que os pagamentos e o encaminhamento evoluírem, esta distribuição alterar-se-á, mas a capacidade total do canal permanecerá sempre a mesma.



![Image](assets/fr/036.webp)



Agora que tem um canal, pode fazer os seus primeiros pagamentos Lightning, desde que o nó escolhido esteja corretamente ligado à rede. É claro que, em capítulos posteriores, veremos como configurar um método mais conveniente de pagar faturas Lightning a partir do seu telemóvel. Mas, por agora, vamos tentar fazer um primeiro pagamento diretamente do LND para o Umbrel.



Para tal, na secção `Lightning Wallet`, clicar no botão `ENVIAR` e, em seguida, colar a fatura a definir.



![Image](assets/fr/037.webp)



O montante da fatura é apresentado. Confirmar o pagamento clicando no botão "ENVIAR".



![Image](assets/fr/038.webp)



Se for encontrada uma rota válida, o primeiro pagamento do Lightning deverá ser bem sucedido.



![Image](assets/fr/039.webp)



Se olharmos para a distribuição da liquidez no canal, vemos que o meu par tem agora 5.002 sats do seu lado. Isto corresponde aos 5.000 sats do pagamento que acabei de efetuar e que ele encaminhou para o nó do destinatário. Os 2 sats adicionais representam as taxas de encaminhamento que paguei, uma vez que o destinatário recebeu exatamente 5.000 sats.



![Image](assets/fr/040.webp)



Para melhorar a fiabilidade dos nossos pagamentos, será obviamente necessário abrir outros canais. Em função dos nossos objectivos, será também necessário encontrar uma forma de disponibilizar a liquidez de entrada para poder receber os pagamentos no Lightning. Este será o tema da próxima secção.



# Gerenciando seu nó do Lightning


<partId>e27c3e1e-487b-4414-ad6b-d67bdb91c7c5</partId>



## Definir o perfil do operador de nó


<chapterId>d3b2e163-50f6-4d1d-a5fc-8fd177dfac76</chapterId>



Agora que seu Lightning node está instalado e funcionando, a próxima etapa é definir seu perfil de negociador. Esta é uma escolha importante, pois determina a sua estratégia de abertura de canais, o tipo de pares que prefere e a forma como gere a liquidez.



No Lightning, para que isto funcione, é necessária liquidez na direção certa. A liquidez de saída corresponde à sua capacidade de pagar (sats disponível no seu lado dos canais). A liquidez de entrada corresponde à sua capacidade de receber (sats disponível do lado dos seus pares). Por outras palavras, o seu perfil resume-se a uma simples questão: na maior parte do tempo, os seus sats estão a sair do seu nó ou a entrar nele?



### O consumidor



Este é o perfil da grande maioria dos utilizadores. Utiliza o seu nó para efetuar pagamentos Lightning: para comprar bens e serviços, pagar contas, enviar gorjetas - em suma, para utilizar o Lightning como meio de pagamento rápido. Por outro lado, recebe pouco de Lightning, ou apenas marginalmente, por exemplo, alguns donativos, reembolsos entre amigos ou alguns micro-pagamentos.



Este perfil é o mais fácil de gerir, porque a sua principal necessidade é ser capaz de pagar. Em termos práticos, isto significa que precisa de liquidez de saída. Depois de abrir um ou mais canais corretamente dimensionados para nós estáveis e bem conectados, os seus pagamentos de saída moverão mecanicamente a liquidez para o outro lado dos seus canais. É precisamente este movimento que cria naturalmente uma quantidade razoável de liquidez de entrada. Como resultado, mesmo que não pretenda receber regularmente, poderá receber de vez em quando sem implementar uma estratégia complexa. Assim, não precisa de se preocupar com a sua liquidez de entrada.



Neste curso LNP202, vamos concentrar-nos neste perfil de operador de nó "consumidor", pois é o que corresponde à quase totalidade dos utilizadores do Bitcoin no Lightning.



### O retalhista



O comerciante é, de certa forma, o oposto do consumidor. Aqui, o objetivo principal não é pagar, mas cobrar. Uma empresa, um prestador de serviços, uma loja online ou um ponto de venda que aceite Lightning receberá muitos pagamentos e efectuará relativamente poucos pagamentos a partir deste nó.



Este perfil é mais exigente, uma vez que uma recusa de pagamento no Lightning representa potencialmente uma venda perdida. Assim, a prioridade passa a ser a liquidez de entrada. Se o seu nó não tiver liquidez de entrada suficiente, os seus clientes verão os seus pagamentos falharem, mesmo que tenham os fundos, simplesmente porque não existe um caminho para que a liquidez chegue até si na direção certa.



O maior desafio para o comerciante advém também da evolução natural dos canais. Se tudo o que faz é receber, os seus canais encher-se-ão gradualmente do seu lado. Assim, são necessários mecanismos para manter e renovar a sua liquidez de entrada.



Há, no entanto, um caso mais simples: o perfil misto de consumidor/comerciante. Se a cobrança é feita no Lightning, mas as despesas também são feitas no Lightning (despesas comerciais, pagamentos a fornecedores ou mesmo despesas pessoais), os pagamentos de saída recriam naturalmente os de entrada. A gestão torna-se mais fácil, uma vez que os fluxos se compensam mutuamente, e é menos necessário recorrer a mecanismos artificiais concebidos apenas para recuperar a liquidez de entrada.



### O router



O router é um perfil específico. Não utiliza o seu nó Lightning para pagar ou cobrar, mas para encaminhar os pagamentos de outras pessoas e cobrar taxas. O objetivo é ser uma rota útil, fiável e economicamente competitiva dentro do gráfico Lightning.



Para ser sincero, ser um router na Lightning é um negócio mais complexo do que parece, e a rentabilidade é difícil de alcançar. Antes de mais, abrir e fechar canais é dispendioso em termos de custos onchain. Para rotear com eficiência, muitas vezes é necessário ajustar a topologia, testar, fechar canais com baixo desempenho, abrir novos canais e reequilibrar regularmente a liquidez. Em segundo lugar, a concorrência é feroz: nós grandes e estabelecidos capturam naturalmente uma grande parte do tráfego, e é difícil ganhar uma posição sem imobilizar um capital significativo em canais de boa dimensão.



Existe também um elevado requisito operacional. Um nó de encaminhamento deve ser extremamente estável, monitorizado, ter cópias de segurança adequadas e ser gerido com rigor. É necessário monitorizar o desempenho do canal, adaptar a política de taxas, manter a liquidez equilibrada, gerir os pares e resolver rapidamente os problemas técnicos. Este nível de envolvimento pode ser interessante como um passatempo técnico ou como uma contribuição para a infraestrutura, mas se o seu objetivo for simplesmente utilizar a Lightning de forma soberana, entrar no encaminhamento para ganhar dinheiro raramente é relevante. É por isso que este curso LNP202 não aborda esse perfil em profundidade.



### Situe-se claramente antes de avançar



Se se enquadra no perfil de consumidor, a sua prioridade será poder pagar de forma fiável com uma gestão simples. Se for um comerciante, a sua prioridade será fazer dinheiro sem falhas, o que implica uma estratégia de aquisição de liquidez de entrada. Se está a considerar o encaminhamento, deve encará-lo como uma atividade exigente, economicamente incerta e morosa.



A definição deste perfil ajudará a evitar uma armadilha clássica: aplicar uma estratégia de canal concebida para um comerciante ou um router, quando o utilizador é simplesmente um utilizador que quer pagar.



## Usando um gerenciador de nós do Lightning


<chapterId>02eb4c09-d14b-4ff0-8b04-b90de3307d34</chapterId>



Na parte anterior deste curso de formação LNP202, utilizámos a interface básica da aplicação `Lightning Node` do Umbrel. Esta interface é suficiente para as operações essenciais (verificação de saldos, visualização da distribuição de dinheiro, abertura e fecho de canais), mas é deliberadamente muito simplificada. Esta simplicidade limita as opções disponíveis e não dá acesso a muitas das funcionalidades avançadas do seu nó LND. Por esta razão, vamos utilizar um outro software de gestão do nó Lightning, mais completo.



Este software adicional será simplesmente uma interface de gestão complementar para o seu nó. Isso significa que você pode continuar a usar a interface `Lightning Node` em paralelo, e até mesmo usar várias interfaces diferentes, se desejar. Estas são simplesmente formas diferentes de interagir com o mesmo nó Lightning.



Entre os programas de software mais conhecidos estão:




- [Alby Hub](https://albyhub.com/);
- [Ride The Lightning](https://www.ridethelightning.info/);
- [ThunderHub](https://thunderhub.io/).



Todas as três são boas soluções. Se desejar, pode testar as três com o seu nó antes de escolher a que mais lhe convém. Pessoalmente, utilizo o ThunderHub por hábito e porque me parece mais completo do que os outros. Esta é a ferramenta que vou apresentar nesta formação, mas também pode escolher uma das outras duas alternativas. Temos um tutorial dedicado a cada um destes programas no Plan ₿ Academy.



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

https://planb.academy/tutorials/node/lightning-network/ride-the-lightning-ca007688-0653-490c-8349-81d330d744b5

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

### Instalar o ThunderHub



Todos esses programas podem ser instalados facilmente a partir da App Store do Umbrel. Como disse, vamos usar o ThunderHub aqui, mas se quiser testar outro mais tarde, o procedimento será semelhante.



![Image](assets/fr/041.webp)



O Umbrel fornece-lhe uma palavra-passe predefinida para aceder ao ThunderHub. Copie-a: vai precisar dela imediatamente. Lembre-se também de a guardar no seu gestor de senhas, pois ser-lhe-á pedida sempre que abrir o software.



![Image](assets/fr/042.webp)



Clique em `Login`, depois cole a palavra-passe fornecida pelo Umbrel para iniciar a sessão.



![Image](assets/fr/043.webp)



Em seguida, você será levado para a página inicial do ThunderHub, que exibe as principais informações sobre o seu Lightning node.



![Image](assets/fr/044.webp)



Para começar, recomendo que active a autenticação de dois factores (2FA). Nas definições, basta clicar em "Ativar" ao lado de "Ativar 2FA" e, em seguida, seguir o processo habitual.



![Image](assets/fr/045.webp)



### Utilizar o ThunderHub



O ThunderHub é relativamente fácil de aprender. Todos os menus são acessíveis a partir da coluna da esquerda da interface. Para resumir, eis o que cada um faz:




- home: visão geral do nó, saldos e acções rápidas;
- painel de controlo: painel de controlo personalizável com widgets e métricas;
- pares: visualizar e gerenciar conexões com outros nós do Lightning;
- canais": gestão completa dos canais (liquidez, taxas, encerramento, etc.);
- rebalance": um instrumento para reequilibrar os canais através de pagamentos circulares;
- transacções: histórico dos pagamentos Lightning enviados e recebidos;
- forwards`: estatísticas de encaminhamento e custos generated pelo seu nó;
- `Chain`: Carteira onchain Bitcoin (UTXOs e transacções);
- integração do gW-201 para monitorização e cópia de segurança;
- `Tools`: ferramentas avançadas (cópias de segurança, relatórios, macarons, assinaturas, etc.);
- troca: Trocas relâmpago/em cadeia via Boltz;
- `Stats`: estatísticas gerais e desempenho do seu Lightning node.



Com esse conjunto de funções, você tem todas as ferramentas necessárias para gerenciar seu Lightning node com eficiência. Não é essencial dominar todas as opções em detalhes imediatamente: nós as exploraremos progressivamente ao longo deste curso. No entanto, se você quiser se familiarizar com o software com mais profundidade, dê uma olhada no nosso tutorial ThunderHub:



https://planb.academy/tutorials/node/lightning-network/thunderhub-16909a39-2484-408e-a118-4e34e249bb9a

O menu que mais nos interessa aqui é o `Canais`. Oferece uma visão detalhada de todos os canais no seu nó, com a sua distribuição de liquidez. Em particular, pode ver quais os canais que estão abertos em `Aberto`, quais estão à espera de serem abertos ou fechados em `Pendente`, e quais já estão fechados em `Fechado`.



![Image](assets/fr/047.webp)



Para um determinado canal, é possível clicar no nome do par ou no ID do canal para abrir a página do Amboss e obter mais informações. Também pode clicar no ícone de lápis para modificar os parâmetros do canal, incluindo a política de taxas aplicada a esse canal se o seu nó encaminhar pagamentos para o nó do seu par.



![Image](assets/fr/048.webp)



Se estiver usando seu nó do Lightning principalmente como um "consumidor", não precisa alterar essas cobranças: pode manter os valores padrão. Por outro lado, se quiser entender melhor como funcionam as taxas de roteamento no Lightning, recomendo o treinamento LNP 201 e, em particular, o capítulo 4.1:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Ao clicar na pequena cruz ao lado de um par, pode iniciar o fecho de um canal. Se notar, por exemplo, que um par está regularmente inativo, pode ser apropriado fechar este canal para realocar o seu capital para um par mais fiável.



Nesse caso, há duas opções. A primeira, e sempre preferível, é o fecho cooperativo. Ao confirmar esta ação, o seu nó pede ao seu par que feche o canal em conjunto. Se ele aceitar, você pode transmitir a transação de fechamento onchain e recuperar sua parte dos fundos. As vantagens deste método são que você escolhe as taxas onchain para a transação, evitando assim custos desnecessários, e que os fundos são recuperados mais rapidamente, sem qualquer timelock.



![Image](assets/fr/049.webp)



A segunda opção é o encerramento forçado. Neste caso, não se pede o acordo do par e transmite-se diretamente o último commitment transaction na nossa posse. Não recomendo este método a menos que seja um último recurso, por exemplo, se o par recusar sistematicamente encerramentos cooperativos ou deixar de responder. O encerramento forçado tem duas grandes desvantagens: as taxas são muitas vezes muito elevadas, uma vez que foram definidas antecipadamente para antecipar um aumento nas taxas onchain, e há um atraso na recuperação dos fundos, uma vez que eles são bloqueados por um timelock. Este bloqueio dá ao seu par o tempo necessário para reagir no caso de uma tentativa de batota (o que obviamente não é o caso aqui, mas mesmo assim tem de esperar).



![Image](assets/fr/050.webp)



Finalmente, para abrir um novo canal, vá ao menu `Home` e clique em `Open a Channel` na secção `Liquidity`. Poderá então introduzir o ID do nó escolhido, a capacidade do canal, a taxa de encaminhamento Lightning desejada e a taxa onchain para a transação de abertura.



![Image](assets/fr/051.webp)



Estas são as principais acções que terá de realizar no ThunderHub. Iremos descobrir outras funcionalidades à medida que avançamos neste curso LNP202.



## Obtenção de liquidez de entrada


<chapterId>b740c656-a897-4d95-af4b-116b718447cd</chapterId>



Como pode ver, ter liquidez de saída para efetuar pagamentos no Lightning não é particularmente complexo. Basta abrir canais por sua própria iniciativa para outros nós e começar a enviar sats. Por outro lado, ter liquidez de entrada para receber pagamentos no Lightning é mais complicado, uma vez que ou precisa que outros nós abram canais para si, ou precisa de movimentar a liquidez você mesmo, efectuando pagamentos.



Se adotar um perfil de "consumidor", geralmente não há necessidade de se preocupar com a liquidez de entrada. A sua utilização do nó Lightning será predominantemente orientada para o pagamento, e não para o recebimento de dinheiro. Ao efetuar simplesmente alguns pagamentos Lightning, criará naturalmente liquidez ao longo do tempo.



Por outro lado, se tiver um perfil de "comerciante", a situação é inversa: vai sobretudo cobrar pagamentos e efetuar poucos. Assim, não pode contar apenas com os seus próprios pagamentos para obter liquidez. Assim, torna-se necessário que outros nós Lightning abram canais para o seu. Mas como é que isso pode ser feito? Como é que se consegue que os outros operadores mobilizem capital para si? É precisamente isso que vamos explorar neste capítulo.



### Compra de liquidez de entrada



Como seria de esperar, a forma mais eficaz de conseguir que alguém actue é pagando-lhe. Para a entrada de liquidez no seu nó Lightning, o princípio é exatamente o mesmo. A maneira mais simples de obter canais para o seu nó é pagar pelo serviço e pela ligação de capital envolvida.



Se é uma empresa ou um retalhista, esta abordagem significa que pode obter rapidamente canais fiáveis para recolher pagamentos dos seus clientes sem fricção.



Há muitas formas de comprar liquidez de entrada. A que eu pessoalmente utilizo e recomendo é a plataforma [Magma](https://magma.amboss.tech/) da Amboss. É muito fácil de utilizar, a abertura de um canal é rápida e as taxas são geralmente razoáveis. A Magma funciona como um mercado, com criadores e compradores, mas a versão 2 simplificou bastante a experiência: basta criar um pedido, pagar o preço através do Lightning e a Magma combina-o automaticamente com a melhor oferta disponível. Após seis confirmações onchain, seu canal com liquidez de entrada está pronto e funcionando. Veja como funciona:



Ir para [o sítio Web da Magma](https://magma.amboss.tech/buy), na secção `Comprar canais`.



![Image](assets/fr/052.webp)



Se desejar, pode criar uma conta para acompanhar as suas compras, mas tal não é obrigatório. Se não criar uma conta, a Magma limitar-se-á a fornecer-lhe um ID de sessão, que lhe permitirá recuperar as suas compras numa data posterior.



Uma vez no site, preencha as informações necessárias para comprar liquidez. Selecione `Uma Vez` para uma compra única, depois introduza o montante que está disposto a pagar pela liquidez recebida. Quanto maior for o valor pago, maior será a capacidade do canal aberto para o seu nó. Uma estimativa da capacidade do canal aparece abaixo: esta é uma aproximação, pois o valor final dependerá da melhor oferta encontrada pelo Magma, que às vezes é maior, às vezes menor.



![Image](assets/fr/053.webp)



Depois introduza o seu ID de nó. Pode encontrá-lo, por exemplo, no menu `Node ID` da aplicação `Lightning Node` no Umbrel.



![Image](assets/fr/054.webp)



Quando todas as informações tiverem sido preenchidas, clique no botão "Rever e abrir a encomenda".



![Image](assets/fr/055.webp)



Se não tiver criado uma conta, a Magma fornecer-lhe-á uma chave de sessão e um ficheiro de cópia de segurança. Guarde estes dois elementos num local seguro, pois permitir-lhe-ão recuperar a encomenda numa data posterior ou seguir o seu estado em caso de problema. Depois de ter guardado o ficheiro, clique no botão `Pagar com o Lightning`.



![Image](assets/fr/056.webp)



A Magma em seguida generates uma fatura Lightning no valor que escolheu. O utilizador deve pagá-la. Se já tiver canais no seu nó Lightning, pode pagar diretamente a partir dele ou utilizar outro wallet Lightning externo.



![Image](assets/fr/057.webp)



Uma vez efectuado o pagamento, a transação aparece como tendo sido processada na interface Magma.



![Image](assets/fr/058.webp)



Após alguns minutos, o pedido é processado: um canal com sats está a ser aberto para o seu nó Lightning. Assim que a transação de abertura for confirmada onchain, terá acesso à liquidez de entrada correspondente.



![Image](assets/fr/059.webp)



O Magma também está integrado diretamente no ThunderHub. No separador `Home`, desça até à secção `Liquidity` e clique em `Buy Inbound Liquidity`. Tudo o que tem de fazer é introduzir o montante pretendido e confirmar. Não precisa de pagar nenhuma fatura manualmente, pois o ThunderHub encarrega-se automaticamente do pagamento do seu nó.



![Image](assets/fr/060.webp)



Se é um comerciante, este tipo de serviço é particularmente adequado, pois permite-lhe obter rapidamente uma grande quantidade de liquidez de entrada de nós fiáveis, garantindo que os seus clientes poderão pagar-lhe sem dificuldade. Por outro lado, se for um particular, ou se não quiser pagar pela entrada de liquidez, existem também soluções gratuitas. Vamos dar uma olhadela.



### Liquidez de entrada cooperativa



Se não for um comerciante, mas ainda assim precisar de alguma liquidez de entrada (por exemplo, para preparar o seu nó no arranque, enquanto espera que alguns pagamentos sejam efectuados), não tem necessariamente de a pagar. Uma das minhas soluções preferidas é cooperar com outros operadores de nós que também precisam de liquidez de entrada, para abrir canais Lightning uns para os outros. Desta forma, a abertura de um canal traz-lhe liquidez de saída e, ao mesmo tempo, fornece-lhe liquidez de entrada, gratuitamente (modulo de taxas onchain para abertura).



Pode, evidentemente, organizar isto diretamente com outros bitcoiners. No entanto, existe uma plataforma dedicada a este tipo de abertura circular: [Lightning Network +](https://lightningnetwork.plus/). O princípio não é abrir dois canais entre as mesmas pessoas, mas criar aberturas circulares que envolvam um mínimo de três participantes, ou mesmo mais.



Vejamos um exemplo para compreender o funcionamento do Lightning Network+:




- Um operador de nó, chamado `A`, publica um anúncio afirmando que deseja abrir um canal de 1 milhão de sats com duas outras pessoas;
- O anúncio permanece ativo até que sejam adicionados mais participantes;
- Mais tarde, dois operadores, `B` e `C`, juntam-se ao anúncio do nó `A`. O triângulo está agora completo, e a fase de abertura pode começar.
- O nó `A` abre um canal para o nó `B`;
- O nó `B` abre um canal para o nó `C`;
- O nó `C` abre um canal para o nó `A`.



No final da operação, cada nó tem 1 milhão de sats de liquidez de saída e 1 milhão de sats de liquidez de entrada. Este esquema pode ser alargado a quatro ou cinco participantes.



É claro que não existe um mecanismo técnico que garanta que um participante abrirá efetivamente o canal que se comprometeu a criar. É por isso que a plataforma criou um sistema de reputação, baseado em críticas positivas quando os operadores cumprem os seus compromissos. E, no pior dos casos, se se deparar com alguém que não coopera, não terá perdido dinheiro: terá simplesmente perdido uma oportunidade de entrada de liquidez.



Esta solução é particularmente adequada a um perfil de "consumidor", pois permite-lhe obter liquidez de entrada gratuitamente, ligando o seu nó a outros pequenos operadores. Por outro lado, se for um operador, esta abordagem não é geralmente pertinente: cada sat de entrada de liquidez requer o bloqueio de um sat de saída de liquidez, e as suas grandes necessidades de entrada de liquidez implicariam então a imobilização de demasiado capital.



Para utilizar o Lightning Network +, tem duas opções: ou utiliza a aplicação integrada no Umbrel, ou utiliza o sítio Web clássico e cria uma conta iniciando sessão a partir do seu nó. Recomendo a segunda opção, pois a aplicação integrada não oferece todas as funções disponíveis.



Aceder ao sítio Web [Lightning Network +](https://lightningnetwork.plus/) e clicar no botão `Login` no canto superior direito da interface.



![Image](assets/fr/061.webp)



Para se autenticar, é necessário assinar a mensagem fornecida utilizando a chave privada do seu Lightning node. Com o ThunderHub, esta operação é muito simples. Comece por copiar a mensagem apresentada pelo LN+.



![Image](assets/fr/062.webp)



No ThunderHub, aceda ao separador `Ferramentas` e, em seguida, clique no botão `Assinar` na secção `Mensagens`.



![Image](assets/fr/063.webp)



Cole a mensagem de autenticação fornecida pelo LN+ e, em seguida, clique em `Sign`.



![Image](assets/fr/064.webp)



ThunderHub então assina esta mensagem usando a chave privada do seu nó. Copie a assinatura do generated.



![Image](assets/fr/065.webp)



Cole esta assinatura no campo correspondente no site do LN+ e clique em `Sign in`.



![Image](assets/fr/066.webp)



Está agora ligado ao LN+ com o seu Lightning node. Este processo permite ao LN+ verificar se é o legítimo proprietário do nó que está a reivindicar na sua plataforma.



![Image](assets/fr/067.webp)



Se desejar, pode personalizar o seu perfil LN+, por exemplo, acrescentando uma pequena biografia.



Para participar na sua primeira abertura de canal circular, vá ao menu `Swaps` no topo da interface. Aqui encontrará todos os swaps atualmente disponíveis, de acordo com as caraterísticas do seu nó.



![Image](assets/fr/068.webp)



Para aderir a uma oferta de troca existente, basta clicar na mesma e registar-se. No entanto, no LN+, o criador de uma troca pode impor certas condições aos participantes, tais como um número mínimo de canais ou uma capacidade total mínima do nó. Por conseguinte, é possível, especialmente nos primeiros dias, que poucas ofertas estejam disponíveis para o seu nó. No meu caso, apesar de alguns canais já estarem abertos, não havia ofertas disponíveis para o meu nó. Por isso, criei a minha própria troca e podes fazer o mesmo se estiveres na mesma situação.



Clique em `Start Liquidity Swap` e, em seguida, introduza os parâmetros da sua oferta:




- Escolha o número total de participantes (3, 4 ou 5);
- Indique a quantidade de canais a abrir (certifique-se de que tem pelo menos esta quantidade no seu wallet onchain);
- Definir o tempo de abertura do canal. Este é o período durante o qual os participantes concordam em não os fechar;
- À direita, pode definir restrições para os participantes: número mínimo de canais, capacidade total mínima e tipo de ligação aceite.



Uma vez definidos todos os parâmetros, clique no botão `Iniciar troca de Liquidity`.



![Image](assets/fr/069.webp)



A sua oferta de troca já foi criada. Agora tudo o que tens de fazer é esperar que outros operadores de nós se inscrevam. Se as suas condições não forem demasiado restritivas, isto não deve demorar muito tempo. Lembre-se de monitorizar o estado da sua troca nas horas ou dias seguintes.



![Image](assets/fr/070.webp)



Todos os lugares de troca foram ocupados: passamos agora à fase de abertura do canal. Cada participante pode ver, a partir da sua interface LN+, para que nó tem de abrir um canal Lightning.



![Image](assets/fr/084.webp)



Do seu lado, abra o canal usando o Node ID fornecido pelo LN+ e respeitando a quantidade indicada. Como vimos nos capítulos anteriores, pode fazê-lo através do ThunderHub, com outro gestor de nós Lightning ou diretamente a partir da interface básica da aplicação Nó Lightning.



![Image](assets/fr/085.webp)



Quando a abertura tiver sido lançada, pode vê-la aparecer na secção de canais em espera. No meu caso, é o canal com o nó `Plebian_fr`.



![Image](assets/fr/086.webp)



Pode então voltar ao LN+ para confirmar que iniciou a abertura de canais. Basta clicar no botão `Abertura de canal iniciada`.



![Image](assets/fr/087.webp)



Quando todos os outros participantes também tiverem aberto o canal a que se comprometeram, lembre-se de lhes deixar um comentário positivo.



![Image](assets/fr/088.webp)



Em caso de dificuldades ou atrasos, pode contactar diretamente os seus pares através da secção de comentários no final da página.



![Image](assets/fr/089.webp)



Alguns participantes podem desejar reequilibrar os canais circulares desde o início, efectuando um pagamento a si próprios. Isto garante uma distribuição equilibrada do dinheiro em cada canal. Se estiver num perfil de "consumidor", isto não é essencial, mas pode fazer este reequilíbrio você mesmo se quiser, ou definir temporariamente as suas taxas de canal para zero para facilitar o trabalho do colega que o quiser fazer. Por vezes, ninguém o quer fazer.



![Image](assets/fr/090.webp)




# Libertar o potencial do seu Lightning node


<partId>8dcc24b1-6eb9-4a5f-a56b-8a823e5ac0fd</partId>



## Ligar um wallet móvel através do Tailscale


<chapterId>5fefb222-3f50-4f9d-a170-2ea628be4437</chapterId>



É isso, agora você tem um nó Lightning bem conectado, com liquidez de entrada e saída. Assim, está pronto para utilizar o seu Lightning node na vida real. Até agora, sempre utilizámos interfaces diretamente no Umbrel, quer a aplicação `Lightning Node` quer a interface `ThunderHub`. Estas ferramentas funcionam para enviar e receber pagamentos, mas não estão claramente optimizadas para os pagamentos Lightning do dia a dia. A interface foi concebida para ser utilizada num computador, o que não é prático num smartphone, e requer também uma ligação à mesma rede para funcionar corretamente (embora seja tecnicamente possível ligar-se remotamente através do Tor).



Na prática, o que procuramos como bitcoiners é uma interface clássica Lightning wallet num smartphone: a capacidade de digitalizar facturas através de código QR e uma interface simples para pagar e levantar sats. É precisamente isso que vamos implementar neste capítulo e no próximo. A ideia geral é ter uma aplicação móvel Lightning wallet no seu smartphone, que pode ser utilizada em qualquer lugar (não apenas na sua rede local) mas que, em segundo plano, depende do seu próprio nó Lightning para enviar e receber pagamentos.



### Quais são as soluções para ligar um cliente móvel?



Atualmente, existem várias formas de o fazer, tanto em termos da aplicação móvel como do tipo de ligação entre o seu nó e esta aplicação. Os três principais modos de ligação são:




- via ***Tor***;
- via VPN ***Tailscale***;
- via ***Nostr Wallet Connect***.



Há alguns anos, costumava ligar-me através do ***Tor***, mas rapidamente deixei de o fazer: o número de falhas e os atrasos de comunicação eram demasiado grandes. Em teoria, funciona, mas, na prática, a experiência do utilizador era catastrófica. Por conseguinte, desaconselho esta abordagem.



A alternativa que adoptei foi a utilização de uma VPN ***Tailscale*** para assegurar a comunicação entre a aplicação móvel e o nó. Esta solução funciona muito bem: mesmo em redes móveis com baixa taxa de transferência, os meus pagamentos são sempre efectuados sem dificuldade. É este o método que vou apresentar em primeiro lugar neste capítulo, com a aplicação Zeus.



No próximo capítulo, veremos outra solução mais recente, que também funciona muito bem: ***Nostr Wallet Connect***. Desta vez, vamos utilizar a aplicação Alby Go para lhe apresentar uma alternativa, embora o Zeus também seja compatível com o NWC, se assim o desejar.



### Instalação e configuração do Tailscale



Para este primeiro método, vamos precisar do Tailscale. Trata-se de uma solução VPN baseada no WireGuard, que permite ligar de forma segura dispositivos espalhados pela Internet, gerindo automaticamente a encriptação, a autenticação e a passagem NAT. Em termos simples, é como se todos os seus dispositivos estivessem ligados à mesma LAN do seu router, embora possam estar em qualquer parte da Internet.



Para o utilizar, comece por criar uma conta. Aceda ao sítio Web do Tailscale e clique no botão `Get Started`.



![Image](assets/fr/071.webp)



Em seguida, escolha um provedor de identidade para sua conta Tailscale. Pessoalmente, utilizei uma das minhas contas GitHub para iniciar sessão.



![Image](assets/fr/072.webp)



Depois de iniciar sessão, ser-lhe-ão feitas algumas perguntas sobre a sua utilização. Responda-as brevemente para continuar.



![Image](assets/fr/073.webp)



O Tailscale oferece-se então para instalar um cliente na sua máquina. De momento, não é isso que nos interessa: vá diretamente para o Umbrel e instale a aplicação Tailscale a partir da App Store.



![Image](assets/fr/074.webp)



Quando a aplicação abrir, clique em "Iniciar sessão" e siga o processo de autenticação, utilizando o mesmo método que utilizou quando criou a sua conta.



![Image](assets/fr/075.webp)



Clique em `Connect` para confirmar. O seu Umbrel está agora ligado à sua rede VPN.



![Image](assets/fr/076.webp)



Em seguida, descarregue a aplicação Tailscale para o seu smartphone e inicie sessão utilizando a mesma conta. Atenção: no Android, não é possível utilizar duas VPNs em simultâneo. Para que o Tailscale funcione, é necessário desativar qualquer outra VPN ativa. Além disso, sempre que quiser utilizar o seu nó Lightning através do Zeus, terá de ativar a VPN Tailscale, caso contrário a ligação não será estabelecida.



![Image](assets/fr/077.webp)



No site do Tailscale, agora que pelo menos dois clientes estão ligados, pode aceder à consola de administração com uma lista de todos os seus dispositivos ligados à rede e os respectivos endereços IP do Tailscale.



![Image](assets/fr/078.webp)



### Ligar o Zeus



Instale a aplicação Zeus no seu telemóvel. Quando abrir, selecione `Advanced Setup` e, em seguida, `Create or connect a wallet`.



![Image](assets/fr/079.webp)



Na secção `Interface Wallet`, escolher `LND (REST)`. Em seguida, introduza o endereço Tailscale do seu Umbrel, que pode encontrar no seu painel de controlo Tailscale ou diretamente na aplicação Tailscale no Umbrel. Para a porta, introduza `8080`.



![Image](assets/fr/080.webp)



O Zeus pede-lhe então que forneça um `Macaroon`. Trata-se de uma autorização token que permite definir com precisão os direitos concedidos a uma aplicação (neste caso Zeus) para interagir com seu Lightning node. É possível criar um macaroon a partir do menu `Tools`, sub-menu `Bakery`, mas para este propósito, a maneira mais fácil é obtê-lo diretamente da aplicação `Lightning Node`.



Clique nos três pequenos pontos no canto superior direito da interface e depois em `Connect Wallet`. Escolha `REST (Rede Local)`. Poderá então copiar um macaroon com os direitos apropriados.



![Image](assets/fr/081.webp)



Cole-o no campo correspondente em Zeus e clique no botão `SAVE WALLET CONFIG`.



![Image](assets/fr/082.webp)



Agora pode aceder ao seu nó Lightning a partir da aplicação Zeus. Isto significa que pode receber pagamentos de facturas generate diretamente no seu nó Lightning a partir do seu smartphone e também pagar facturas Lightning onde quer que esteja.



![Image](assets/fr/083.webp)



Dica: O Tailscale não se limita a usar seu Lightning node remotamente. Permite-lhe aceder a todas as ferramentas do seu Umbrel a partir de outro software, mesmo remotamente. Por exemplo, pode usar o endereço IP Tailscale do seu Umbrel para ligar o seu nó Bitcoin (via Electrs ou Fulcrum) ao Sparrow Wallet, sem passar pelo Tor. Mais uma vez, isto evita a lentidão inerente ao Tor. Basta instalar o cliente Tailscale no seu computador e ligá-lo à sua rede.



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

No próximo capítulo, veremos outra maneira igualmente eficaz de conectar um cliente móvel ao seu nó Lightning: Nostr Wallet Connect. Utilizaremos uma aplicação diferente do Zeus (embora o Zeus também seja compatível com o NWC), nomeadamente o Alby Go.



## Ligar um wallet móvel através de NWC


<chapterId>f5c97e43-e66e-4ba3-bcc9-fee1a04fc7f4</chapterId>



Se não estiver convencido com a ligação Tailscale, ou se a gestão de uma VPN dupla parecer demasiado incómoda, este capítulo sugere outra forma de utilizar um cliente móvel remoto para pagar e receber sats através do seu nó Lightning: ***Nostr Wallet Connect***.



Para este exemplo, vamos utilizar a aplicação móvel Alby Go, que está muito bem concebida e é particularmente fácil de aprender. Dito isto, também pode utilizar o Zeus ou qualquer outra aplicação móvel compatível com o NWC. Encontrará uma lista de aplicações compatíveis no [repositório `awesome-nwc` do GitHub](https://github.com/getAlby/awesome-nwc).



### Como é que o Nostr Wallet Connect funciona?



O Nostr Wallet Connect é um protocolo normalizado que permite a uma aplicação ou a um sítio Web desencadear acções num nó Lightning remoto, sem estabelecer uma ligação de rede direta a esse nó (sem API LND exposição, sem VPN, sem serviço `.onion`...). O NWC define como um aplicativo formula uma intenção (por exemplo, `pay_intece`) e recebe o resultado.



O seu funcionamento é muito simples. Inicializa-se uma sessão digitalizando um código QR ou através de uma ligação profunda `nostr+walletconnect:`. Esta cadeia contém os parâmetros da sessão e um segredo de autorização. Depois, quando a aplicação pretende pagar, serializa o pedido, encripta-o e publica-o como um evento num relé Nostr. O nó lê o evento no relé, desencripta-o, verifica se o autor está autorizado para esta sessão, executa o pagamento e devolve uma resposta encriptada (sucesso com pré-imagem ou erro). O relé actua apenas como um intermediário de transporte: não pode ler o conteúdo, mas pode observar o tempo e a frequência dos pedidos.



Em comparação com uma ligação via Tailscale ou Tor, a principal vantagem do NWC é que o seu nó não é diretamente acessível a partir do exterior. Isto simplifica muito a utilização móvel: o seu nó não precisa de aceitar ligações de entrada, apenas precisa de ser capaz de comunicar com um retransmissor. Por outro lado, introduz-se uma dependência funcional dos retransmissores Nostr: se estes não estiverem disponíveis, a experiência deteriora-se. Além disso, mesmo que as mensagens sejam encriptadas, o retransmissor pode observar um certo nível de metadados de atividade.



A diferença nos modelos de segurança também é importante. Com o Tailscale ou Tor, expõe o acesso direto ao seu nó (via API ou LND) protegido por segredos altamente sensíveis. Isto é poderoso, porque se pode administrar tudo, mas é também uma superfície de ataque de camada inferior. Com o NWC, o acesso é mais aplicativo: delega-se uma sessão token que autoriza apenas determinadas acções.



### Instalar o Alby Hub no nó do Lightning



Anteriormente, existia uma aplicação especificamente dedicada às ligações NWC na App Store do Umbrel, mas infelizmente esta já não está disponível. Agora é necessário utilizar o Alby Hub para estabelecer este tipo de ligação. Para tal, comece por instalar a aplicação Alby Hub diretamente a partir da loja.



![Image](assets/fr/091.webp)



Ao abrir, pule as telas introdutórias e clique no botão `Get Started (LND)`. É importante verificar se está escrito `LND`, e não `LDK`, entre parênteses. Se aparecer `LND`, significa que o Alby Hub detectou corretamente o seu Lightning node existente e irá se configurar como interface para ele. Por outro lado, se `LDK` for exibido, isso indica que o Alby Hub não detectou seu nó e está prestes a criar um novo, o que não é o objetivo aqui.



![Image](assets/fr/092.webp)



Ser-lhe-á então pedido que crie uma conta Alby. Para uma utilização limitada ao NWC, isto não é necessário, mas poderá querer fazê-lo se pretender tirar partido dos serviços específicos do Alby. Caso contrário, clique em "Talvez mais tarde" para continuar.



![Image](assets/fr/093.webp)



Em seguida, escolha uma palavra-passe forte e única. Esta protegerá o acesso ao Alby Hub no seu nó. Não se esqueça de a guardar no seu gestor de palavras-passe.



![Image](assets/fr/094.webp)



Isto leva-o à interface do Alby Hub. Não é necessário passar por todo o processo de configuração, a menos que você queira usá-lo como o principal gerenciador do seu nó Lightning. Como vimos anteriormente, o Alby Hub pode, de facto, substituir a utilização do ThunderHub para a administração do seu nó. Se quiser saber mais sobre as opções do Alby Hub, dê uma olhada no nosso tutorial dedicado:



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Aceder ao menu "Ligações".



![Image](assets/fr/095.webp)



Aqui você pode ver todos os aplicativos que podem se conectar ao seu nó Lightning via NWC. Isso inclui o Zeus, já mencionado no capítulo anterior. Aqui, usaremos o Alby Go. Clique em Alby Go e, em seguida, no botão `Connect to Alby Go` para iniciar o processo de conexão.



![Image](assets/fr/096.webp)



### Instalação e ligação do Alby Go



No seu smartphone, instale a aplicação Alby Go:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Apple App Store](https://apps.apple.com/us/app/alby-go/id6471335774);
- [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq3jhml5fvklgnq9fxpete767txn9zfzqdkc0sxfptmnchfrexje7qqfxxmmd9enk2arpd338jtndda3xjmr9pzj5tk).



No Alby Hub, configure os direitos que deseja conceder ao aplicativo Alby Go no seu nó do Lightning. Pode, por exemplo, definir limites de despesas por período, uma data de expiração para a ligação NWC ou deixar o controlo total. Depois de definir os parâmetros, clique no botão "Seguinte".



![Image](assets/fr/097.webp)



O Alby Hub então generates um código QR para estabelecer a conexão NWC entre seu Lightning node e o Alby Go.



![Image](assets/fr/098.webp)



Na aplicação Alby Go, quando aberta pela primeira vez, clicar em `Connect Wallet`, depois digitalizar o código QR fornecido pelo Alby Hub.



![Image](assets/fr/099.webp)



Escolha um nome para identificar este wallet. Tem agora acesso remoto ao seu nó Lightning via Alby Go. Pode receber facturas generate no seu nó sats ou definir facturas Lightning diretamente com ele.



![Image](assets/fr/100.webp)



Por exemplo, enviei 1543 sats a partir da interface Alby Go.



![Image](assets/fr/101.webp)



Se eu for à interface básica do meu nó Lightning no Umbrel, posso ver que este pagamento foi efetivamente efectuado pelo meu nó.



![Image](assets/fr/102.webp)



Agora já sabe como utilizar facilmente o seu Lightning node a partir de qualquer lugar.



## Autonomia de longa duração no Lightning


<chapterId>691a0942-b46d-482a-8fbc-fe19b3814992</chapterId>



Chegámos ao fim deste curso prático sobre o LNP202. Tem agora as noções básicas necessárias para utilizar o Lightning Network de forma soberana: compreende o verdadeiro papel de um nó, as vantagens e desvantagens das diferentes abordagens e configurou uma instância LND no Umbrel com uma estratégia de backup e proteção consistente. Também abriu os seus primeiros canais, aprendeu a gerir a liquidez, a tornar os seus pagamentos fiáveis diariamente.



De um ponto de vista operacional, o seu nó deve agora entrar num ritmo de manutenção. O principal é monitorizá-lo (tempo de funcionamento, sincronização, estado dos canais, falhas de pagamento, etc.), aplicar as actualizações oferecidas pelo Umbrel quando estiverem disponíveis versões estáveis e verificar periodicamente se as suas cópias de segurança e a configuração da torre de vigia ainda estão activas.



No que diz respeito aos canais, adopte uma abordagem pragmática: mantenha os que lhe são úteis, feche os que estão permanentemente inactivos ou associados a pares instáveis e reafecte gradualmente o seu capital para uma topologia mais robusta.



**Uma das armadilhas mais comuns nesta fase é atribuir demasiado capital ao seu nó Lightning. Tenha em conta que o seu nó Lightning é muito menos seguro do que um hardware wallet e que a disponibilidade dos fundos afectados aos seus canais depende de mecanismos de backup que continuam a ser imperfeitos. Por isso, é muito importante manter quantias razoáveis, que você pode se dar ao luxo de perder no caso de um problema, e sempre manter a maior parte do seu sats em um hardware wallet onchain.



No que diz respeito às ferramentas, recomendo que se mantenha curioso e atento aos novos desenvolvimentos. Nesta sessão de formação, descobrimos várias delas, seja para gerir o seu nó, a sua conetividade ou a sua utilização remota para efetuar pagamentos. No entanto, o Lightning é um domínio particularmente dinâmico. Todos os anos, surgem ferramentas novas e pertinentes, e muitas aplicações novas surgem também no Umbrel. Acompanhar estes novos desenvolvimentos pode permitir-lhe descobrir soluções mais poderosas ou mais práticas do que as apresentadas neste curso.



No plano educativo, se ainda não o fez, aconselho-o vivamente a frequentar o curso teórico LNP 201 de Fanis Michalakis, dedicado ao funcionamento do Lightning Network. Ajudá-lo-á a compreender melhor as manipulações efectuadas neste curso LNP202 e dar-lhe-á mais confiança na gestão diária do seu nó.



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Num sentido diferente, mas igualmente essencial para o seu percurso com a bitcoin, recomendo também o excelente curso de Ludovic Lars sobre a história da criação do Bitcoin.



https://planb.academy/courses/a51c7ceb-e079-4ac3-bf69-6700b985a082

Mas antes de avançar, pode fazer uma avaliação deste curso LNP202 e, evidentemente, obter o diploma para confirmar que compreendeu todo o seu conteúdo.



# Parte final


<partId>683c998f-ba0a-4ffb-a7e8-4cd8369cb9b3</partId>



## Comentários e classificações


<chapterId>aec048c7-7130-425d-8eca-9cd7f90c27f3</chapterId>



<isCourseReview>true</isCourseReview>

## Exame final


<chapterId>3951ccbb-14a3-4322-b81b-8dd2a6da19cb</chapterId>



<isCourseExam>true</isCourseExam>

## Conclusão


<chapterId>30cd6309-5139-40d9-8927-92de0f76414a</chapterId>



<isCourseConclusion>true</isCourseConclusion>