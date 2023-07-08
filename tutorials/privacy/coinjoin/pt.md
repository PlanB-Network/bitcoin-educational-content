---
name: Coinjoin
description: Compreender e utilizar o CoinJoin no Bitcoin.
---

![Legenda](assets/1.jpeg)

# Compreender e usar o CoinJoin no Bitcoin.

_**Texto fornecido por Loïc Morel como parte dos seus escritos em Pandul. Texto original [aqui](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin)**_

## Introdução

Um dos problemas iniciais de qualquer sistema de pagamento peer-to-peer é o gasto duplo. Como podemos evitar que actores maliciosos abusem da rede de pagamentos gastando as mesmas unidades várias vezes sem depender de uma autoridade central?

Satoshi Nakamoto encontrou uma solução para este problema com o seu protocolo Bitcoin, uma rede de pagamentos eletrónica peer-to-peer que funciona sem a intervenção de qualquer autoridade central. No seu Livro Branco, explica que a única forma de confirmar a ausência de uma transação e, portanto, de verificar que não há tentativa de despesa dupla, é ter conhecimento de todas as transacções efectuadas na rede de pagamentos distribuída.

Para que cada utilizador seja informado das transacções, estas devem ser anunciadas publicamente. O sistema de pagamento peer-to-peer proposto pelo protocolo Bitcoin foi, portanto, possibilitado por uma infraestrutura totalmente transparente e distribuída. Assim, qualquer pessoa com um nó pode verificar a cadeia de assinaturas electrónicas e a história de cada moeda, desde a sua criação por um mineiro.

> Este princípio de distribuição do livro-razão e de anúncio público de novas transacções é utilizado na mais recente criptomoeda (bitcoin), mas já era utilizado em criptomoedas anteriores, como a b-money, inventada por Wei Dai em 1998.
>
> Esta transparência e distribuição implicam que cada utilizador da rede Bitcoin pode seguir e observar as transacções de todos os outros utilizadores. A privacidade é, portanto, impossível ao nível do pagamento. Em vez disso, é feita ao nível da identificação pessoal.

Em vez de associar cada unidade de conta a uma identidade (nome, apelido...), como no sistema bancário tradicional, as bitcoins estão associadas a um par de chaves. Os utilizadores são assim representados anonimamente por um identificador criptográfico.

Assim, a perda de privacidade na Bitcoin ocorre quando um observador consegue associar certos UTXO a certos utilizadores. Quando esta ligação é feita entre um utilizador e as suas unidades de conta, é então possível seguir os seus pagamentos e analisar o histórico dos seus bitcoins.

A CoinJoin é uma prática que permite quebrar o histórico de UTXOs, a fim de proporcionar um certo nível de privacidade ao utilizador de Bitcoin.

Neste artigo, vamos estudar juntos o que é o CoinJoin, como ele funciona e como usá-lo corretamente. Vamos falar principalmente sobre o Whirlpool, a implementação do CoinJoin mais eficiente hoje na minha opinião, mas também abordaremos outras implementações existentes. Também vou falar sobre os indicadores que permitem calcular precisamente o nível de privacidade de seus bitcoins. Para não ficarmos apenas na teoria, vou mostrar concretamente como realizar uma transação CoinJoin de diferentes maneiras. Por fim, vamos estudar as boas práticas a serem observadas para não perder a privacidade conquistada após uma série de CoinJoin, e vou apresentar as diferentes ferramentas da carteira Samourai Wallet que permitem isso.

Se você gostou deste artigo, compartilhe nas redes sociais e com as pessoas que precisam.

> Sumário:
>
> - CoinJoin e mistura de bitcoins.
> - As diferentes implementações do CoinJoin.
> - Funcionamento teórico do Whirlpool.
> - Tutorial: Whirlpool no Sparrow Wallet.
> - Tutorial: Whirpool CLI no Dojo e Whirlpool GUI.
> - Boas práticas pós-mistura.
> - Ferramentas de gastos.
> - É errado misturar bitcoins?

Se você é um usuário iniciante de Bitcoin, antes de poder abordar este artigo, recomendo fortemente que você entenda a estrutura de uma transação Bitcoin (UTXO, inputs e outputs) lendo este breve artigo sobre o assunto: Mecanismo de uma transação Bitcoin: UTXO, inputs e outputs.

O uso do CoinJoin pode apresentar riscos indiretos para o usuário. Alguns provedores potencialmente bloquearão seus fundos e/ou sua conta como resultado de suas ações e solicitarão justificativas sobre a origem desses fundos. As informações contidas neste artigo não constituem aconselhamento em sistemas e software de computador, nem qualquer tipo de incentivo para realizar CoinJoin. A realização de um CoinJoin envolve o uso de uma carteira de software conectada à internet (chamada de "quente"). É possível que seus fundos sejam perdidos e/ou roubados. Recomendo que você faça suas próprias pesquisas sobre os diferentes riscos existentes. Este artigo não pode, de forma alguma, ser uma única fonte de informação sobre esses assuntos.

## CoinJoin e mistura de bitcoins.

Antes de começar, é importante entender a diferença entre o CoinJoin e a mistura.

A mistura (em inglês: "mixing", "blender" ou "tumbler") é uma técnica que permite misturar UTXOs, ou seja, misturar bitcoins, para quebrar seus históricos e embaralhar os rastros de rastreamento. O objetivo desse tipo de operação é pseudonimizar UTXOs para que o usuário ganhe em privacidade. A pseudonimização ocorre quando o UTXO está dentro de um grupo de vários outros UTXOs indistinguíveis.
O mixagem e o CoinJoin são inicialmente duas técnicas com o mesmo objetivo, mas que não funcionam da mesma maneira. A mixagem é baseada em uma terceira parte confiável a quem confiamos nossos bitcoins para serem misturados, enquanto o CoinJoin se baseia apenas em um coordenador que sincroniza a ação dos usuários, mas que nunca terá controle sobre os fundos.

Com a chegada do CoinJoin, a mixagem rapidamente se tornou obsoleta e os usuários a abandonaram. Ainda existem alguns serviços de mixagem como o ChipMixer. No entanto, hoje essa técnica existe apenas marginalmente, enquanto o CoinJoin é usado por cada vez mais pessoas.
Consequentemente, na linguagem comum dos usuários de bitcoin, muitos usam a palavra "mixagem" para se referir, no final das contas, a um CoinJoin. Embora essa semântica seja inicialmente incorreta, ela é amplamente aceita pelos usuários. Então falamos de "bitcoins misturados" para nos referirmos a UTXOs resultantes de uma transação CoinJoin.

![Legenda](assets/1.jpeg)

Portanto, o CoinJoin é uma técnica que permite que o histórico de UTXOs seja quebrado. Ele se baseia em uma transação colaborativa com a mesma estrutura: a transação CoinJoin. Esse tipo de transação foi inicialmente proposto por Gregory Maxwell em 2013 no fórum Bitcoin Talk: https://bitcointalk.org/index.php?topic=279249.0
O funcionamento geral é o seguinte: diferentes usuários que desejam misturar depositam uma quantia como entrada de uma transação. Essas entradas serão transformadas em diferentes saídas com o mesmo valor (possivelmente com troco, mas vamos estudar isso mais adiante). Na saída da transação, é impossível determinar qual saída pertence a qual usuário. Não há tecnicamente nenhuma ligação entre as entradas e saídas da transação CoinJoin. A ligação entre cada usuário e cada UTXO é quebrada, da mesma forma que o histórico de cada moeda.

Para permitir o CoinJoin sem que nenhum usuário perca o controle de seus fundos em nenhum momento, a transação é primeiro construída pelo coordenador e depois transmitida a cada usuário. Cada usuário então assina a transação por conta própria, verificando se ela está correta, e todas as assinaturas são adicionadas à transação. Se um usuário ou o coordenador tentar roubar os fundos dos outros modificando as saídas da transação CoinJoin, as assinaturas serão inválidas e a transação será rejeitada pelos nós.

Se me permitir uma analogia, podemos imaginar o CoinJoin como uma perseguição entre um helicóptero e um carro. Vamos imaginar um helicóptero tentando seguir um carro branco. O helicóptero representa a pessoa que deseja analisar seus pagamentos e o carro branco representa seu UTXO. O helicóptero pode facilmente seguir o carro voando sobre ele.

Imaginemos que agora existam mais quatro veículos brancos semelhantes circulando nesta estrada perto do carro que está sendo seguido. O helicóptero ainda pode seguir o carro branco que estava seguindo inicialmente.

Agora, imaginemos que esses cinco carros entrem em um túnel, impedindo o helicóptero de ver os carros por um curto período de tempo. Na saída do túnel, o helicóptero não poderá saber qual dos cinco carros brancos corresponde ao carro que estava seguindo inicialmente. Neste exemplo, o túnel age como um CoinJoin. Seu UTXO de saída da transação CoinJoin estará oculto entre um grupo de outros UTXOs. Um observador eventual saberá que seu UTXO está neste grupo, mas não poderá determinar com certeza qual é o seu.

O objetivo técnico para o usuário do CoinJoin será ter os maiores "Anonymity Sets" possíveis em seus UTXOs. Este conceito é muito importante de entender para o futuro. "Anonymity Sets", às vezes também chamados de "Anon Sets", referem-se aos parâmetros que permitem calcular o nível de anonimato de um determinado UTXO. Existem dois: o score prospectivo e o score retrospectivo.

O score prospectivo indica o tamanho do grupo de UTXOs em que o UTXO que nos pertence está escondido. Por exemplo, se eu fizer um CoinJoin com outros quatro usuários, meu score prospectivo será igual a cinco imediatamente após a transação CoinJoin.

Se voltarmos ao nosso exemplo do helicóptero, cada carro branco na saída do túnel tem um score prospectivo igual a 5. O helicóptero sabe que seu alvo está entre esse grupo de cinco carros, mas é incapaz de distinguir qual é seu carro-alvo inicial.

Explicarei mais detalhadamente o que esses dois parâmetros representam nesta parte: Anon Sets. Por enquanto, apenas lembre-se de que quanto maior forem os Anon Sets para um UTXO misturado, mais difícil será rastreá-lo por um observador.

# As diferentes implementações de CoinJoin.

Uma transação CoinJoin poderia ser realizada manualmente, diretamente com outros usuários de Bitcoin que você encontra. No entanto, essa solução, além de ser muito trabalhosa, é bastante ineficiente. Para que a transação CoinJoin seja eficiente, rápida e dimensionável na rede, é necessário poder se comunicar com qualquer outro usuário no mundo. Portanto, é preferível usar os serviços de um coordenador, cujo papel será desenvolver uma implementação com um modelo de transação, conectar os diferentes usuários e transmitir as informações necessárias para a realização adequada da transação colaborativa.

Existem principalmente 3 implementações de CoinJoin no Bitcoin:

> JoinMarket.
>
> Wasabi.
>
> Whirlpool.

Mesmo que o objetivo final destas três implementações seja o mesmo, ou seja, quebrar a história de um UTXO através da realização de transacções CoinJoin, elas funcionam de forma muito diferente. Por isso, é importante saber como cada uma funciona para poder escolher a implementação que melhor se adapta às suas necessidades.

Como já deve ter percebido por me seguir no Twitter, eu pessoalmente prefiro usar a implementação Whirlpool. Por isso, vou dar-vos uma explicação rápida de como as outras duas soluções funcionam em teoria e porque é que as considero menos adequadas. Em seguida, analisaremos mais detalhadamente o funcionamento do Whirlpool, a implementação desenvolvida pela equipa da Samourai Wallet, que, na minha opinião, é a melhor solução CoinJoin neste momento.

As características mencionadas para cada implementação são válidas atualmente. Poderão ter sido alteradas na altura em que ler este artigo.

![Legende](assets/2.jpeg)

## JoinMarket.

O JoinMarket destaca-se das outras implementações principais graças ao seu modelo de correspondência entre utilizadores. Baseia-se num mercado de troca entre utilizadores que fornecem dinheiro para misturar e utilizadores que aceitam dinheiro para misturar.

Quando se quer fazer um CoinJoin no JoinMarket, tem de se escolher entre deixar os seus bitcoins para que outros os usem para misturar, mediante o pagamento de uma taxa, ou aceitar o dinheiro de outros utilizadores para misturar diretamente, pagando a taxa exigida. Assim, há "makers" que deixam os seus bitcoins disponíveis e "takers" que utilizam o dinheiro. Os "takers" pagam aos "makers" pelo seu serviço.

Estamos, portanto, a falar de um mercado totalmente livre, sem condições de utilização.

A principal desvantagem deste serviço é o facto de a sua configuração ser bastante complexa. É necessário um conhecimento mínimo das linhas de comando do Linux para o utilizar corretamente. Esta implementação é relativamente eficiente, mas não é claramente adequada para o público em geral.

Um termos de funcionalidade relacionada com a transação CoinJoin, o JoinMarket tem algumas fraquezas em comparação com a Whirlpool. Por exemplo, a estrutura da transação CoinJoin significa que não pode haver 0% de ligações determinísticas entre entradas e saídas. De notar também que o JoinMarket não inclui uma ferramenta para impedir um novo CoinJoin entre moedas que já se encontraram no passado.

Em termos de serviços adicionais oferecidos ao utilizador, o JoinMarket não inclui uma ferramenta para calcular facilmente os UTXO Anon Sets. Quanto às ferramentas de gastos mistos de UTXO, a implementação apenas oferece PayJoin'.

Finalement, JoinMarket é uma implementação interessante de CoinJoin, mas não é destinada a qualquer pessoa. Se você está confortável com linhas de comando, se você entende bem como o CoinJoin funciona e se o modelo de "takers" / "makers" lhe agrada, então essa implementação pode ser adequada para você.

## Wasabi 2.0.

O serviço de CoinJoin do Wasabi funciona teoricamente como o do Whirlpool. Ao contrário do JoinMarket, onde a organização é feita em um mercado livre, o Wasabi age como um coordenador que automaticamente mistura os bitcoins de todos os usuários do serviço.

A estrutura da transação CoinJoin em si é, no entanto, bastante diferente da do Whirlpool. Como veremos na próxima parte, o aumento do score prospectivo (Anon Set) dos UTXO misturados no Whirlpool é feito acumulando várias CoinJoin com poucos usuários a cada vez. Por outro lado, os Anon Sets dos UTXO misturados no Wasabi são feitos em poucas transações com um grande número de usuários.

Exemplo de Coinjoin possivelmente realizado no Wasabi 1.0:
https://kycp.org/#/b994a9cbdc20e971207bde4f800b9ce99dba35478a2a997bc48e7f9f80bd2d02

Exemplo de Coinjoin realizado no Whirlpool: https://kycp.org/#/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2

As duas implementações também diferem na gestão do troco. No Whirlpool, o troco é separado e isolado dos UTXO antes do CoinJoin através do TX0 (falarei sobre isso na próxima parte). No Wasabi, o troco é uma saída da transação CoinJoin. A escolha dessa estrutura de CoinJoin no Wasabi faz com que links determinísticos permaneçam entre as entradas e algumas saídas.

Na versão 2.0, o Wasabi mudou completamente sua política de taxas de CoinJoin. As taxas do coordenador agora são de 0,3% para UTXOs acima de 0,01 bitcoin, e são gratuitas para UTXOs inferiores a esse valor. Os pequenos UTXOs também se beneficiam de remixes gratuitos. É importante notar que, mesmo que as taxas do coordenador sejam gratuitas, o usuário ainda terá que pagar as taxas de mineração para todas as transações, incluindo as transações de remixes.

Assim, ao contrário da Whirlpool, quanto mais quiser ter conjuntos Anon substanciais no seu UTXO misturados com Wasabi, mais terá de pagar. Isto aplica-se tanto à versão 1.0 como à versão 2.0 do Wasabi. Embora a última versão ofereça taxas de coordenação para pequenos UTXOs, ainda há taxas de mineração. Para além disso, fiquei com a impressão, ao utilizar a versão 2.0, que a pontuação prospetiva máxima atingível é de 300 no Wasabi. Na Whirlpool, pode facilmente atingir uma pontuação prospetiva de cinco dígitos no espaço de alguns meses, e esta pontuação não é limitada.

Para além da própria estrutura do CoinJoin, na minha opinião, o Wasabi carece de ferramentas que complementem o CoinJoin, sobretudo para gastar corretamente o UTXO misto. A versão 1.0 não tem qualquer ferramenta de despesa. Na versão 2.0, Wasabi incluiu, no entanto, uma ferramenta para gastar UTXO misto que ajusta automaticamente as entradas e saídas para maximizar a confidencialidade, eliminando a troca. Embora esta funcionalidade possa ser útil, parece ser muito menos eficaz e conveniente de utilizar do que a miríade de ferramentas oferecidas no Samurai e na Sparrow Wallet para gastar UTXO misturado de forma limpa com o Whirlpool. Falarei de todas estas ferramentas mais tarde neste artigo, nesta secção: Ferramentas de gastos.

Ao contrário da Whirlpool, a Wasabi não separa as contas de UTXO misto, UTXO não misto e UTXO de divisas. Esta estrutura de portefólio significa que a reutilização de endereços é possível entre UTXOs mistos e outros UTXOs. Se isto acontecer, pode quebrar completamente um CoinJoin.

Por último, depois de experimentar a versão 2.0, fiquei com a impressão de que não tenho o controlo da minha CoinJoin quando utilizo o Wasabi. Tudo é simplificado e automatizado, e a interface com o utilizador é magnífica, mas é isto que esperamos de uma implementação CoinJoin?

## Funcionamento teórico do Whirlpool.

Ao contrário das outras implementações mencionadas, a Whirlpool destaca-se pela construção de transacções CoinJoin "ZeroLink", ou seja, sem qualquer ligação técnica possível entre todos os inputs e todos os outputs.

Isto é possível através de uma transação CoinJoin em que cada utilizador deposita o mesmo montante de entrada, que é depois convertido em tantos outputs do mesmo montante.

Com este tipo de construção restritiva das entradas, a transação CoinJoin da Whirlpool é a única que permite aos utilizadores terem 0% de ligações determinísticas entre entradas e saídas. Isto significa que cada output tem exatamente a mesma probabilidade de pertencer a um utilizador que todos os outros outputs da transação.

O número de participantes em cada mix é limitado a 5: 2 entrantes e 3 remixadores (vamos descobrir mais tarde o que isso significa). Portanto, toda transação CoinJoin no Whirlpool sempre tem 5 entradas e 5 saídas.

![Representação esquemática de uma transação CoinJoin Whirlpool.](assets/3.jpeg)

## Design do Whirlpool.

O modelo proposto pelo Whirlpool é baseado em transações muito pequenas. Ao contrário do Wasabi e do JoinMarket, a força dos Anon Sets não é adquirida pelo número de usuários participantes do CoinJoin, mas sim pela sucessão de vários pequenos CoinJoin de 5 participantes cada vez.

O usuário será solicitado a pagar apenas uma vez, ao entrar em um pool, e depois poderá remixar gratuitamente quantas vezes quiser. São os novos entrantes que pagam as taxas de mineração para os remixadores.

Os Anon Sets aumentarão exponencialmente à medida que o usuário e seus pares se remixam. O objetivo é aproveitar ao máximo essas remixagens gratuitas que adicionam profundidade aos Anon Sets da UTXO.

O Whirlpool foi concebido com base em 2 critérios principais:

- Que a implementação seja utilizável em dispositivos móveis.

- Que os ciclos de remixagem sejam rápidos.

Por essas duas razões, as equipes da Samourai escolheram limitar o número de usuários a 5 por ciclo. Um número menor não permitiria um CoinJoin eficiente o suficiente e reduziria muito os Anon Sets por ciclo. Um número maior provavelmente não seria gerenciável em clientes móveis e reduziria o fluxo de ciclos.

No final das contas, não é necessário ter um grande número de participantes por CoinJoin no Whirlpool, pois os Anon Sets são formados pela acumulação de vários ciclos de remixagem.

## Pools e taxas.

Para garantir que esses múltiplos ciclos realmente aumentem os Anon Sets da UTXO, é necessário estabelecer um certo quadro para restringir os valores das UTXO utilizadas. O Whirlpool define diferentes pools.

Uma pool é um grupo de usuários que desejam fazer mixagem e concordaram com o valor das UTXO utilizadas para otimizar o funcionamento do CoinJoin. Cada pool define um valor fixo da UTXO ao qual o usuário deve se adaptar para poder entrar. Na prática, quando você deseja realizar CoinJoin, deve escolher uma pool na qual entrar para começar a mixar. As diferentes pools atualmente disponíveis no Whirlpool são:

- 0,5 bitcoin.
- 0,05 bitcoin.
- 0,01 bitcoin.
- 0,001 bitcoin (= 100.000 sats).

Assim, todos podem encontrar uma opção adequada.

Cada pool tem um valor máximo para entrar:

| Pool (bitcoin) | Valor máximo por entrada (bitcoin) |
| -------------- | ---------------------------------- | --- | --- | ---- | --- |
| '              | 0,5                                | 35  |     | 0,05 | 3,5 |
| 0,01           | 0,7                                |
| 0,001          | 0,025                              |

Para entrar em um pool, é necessário pagar uma taxa. Essas taxas são fixas para cada pool e são destinadas às equipes que desenvolvem e gerenciam o Whirlpool para remunerá-las por esse serviço. As taxas são cobradas apenas uma vez quando você acessa o pool. Depois de entrar em um pool, você pode remixar quantas vezes quiser gratuitamente.

Atualmente, estas são as taxas aplicadas para cada pool:

| Pool (bitcoin) | Taxa de entrada (bitcoin) |
| -------------- | ------------------------- |
| 0,5            | 0,0175                    |
| 0,05           | 0,00175                   |
| 0,01           | 0,0005 (50 000 sats)      |
| 0,001          | 0,00005 (5 000 sats)      |

Você pode facilmente calcular as taxas envolvidas em suas misturas com o Whirlpool neste site: https://www.whirlpoolfees.com/

Observe também que essas taxas são uma "taxa de entrada" para o pool. Portanto, se você entrar no pool 0,01 com 0,01 btc ou com 0,5 btc, as taxas serão exatamente as mesmas. Antes de fazer uma mistura, um usuário deve considerar se deseja pagar menos taxas com um pool pequeno, o que resultará em várias pequenas UTXO, ou se prefere usar um pool maior pagando mais taxas, mas saindo com menos UTXO.

Ao sair dos diferentes ciclos de mistura, geralmente é desaconselhável mesclar várias UTXO misturadas juntas. Isso pode comprometer a privacidade conquistada anteriormente. Portanto, às vezes é melhor usar um pool maior, mesmo que isso signifique pagar mais taxas, para sair com menos UTXO de tamanho maior.

Outras taxas a serem consideradas são as taxas de mineração inerentes a qualquer transação Bitcoin. Como usuário do Whirlpool, você precisará pagar as taxas de mineração da Tx0 e as taxas de mineração da mistura inicial. Todos os outros remixes serão gratuitos para você, pois o modelo de taxas do Whirlpool é baseado nos novos participantes.

Cada CoinJoin é composto por 5 usuários. Dentre eles, 2 são entrantes e 3 são remixes. Assim, os dois entrantes de cada mistura pagarão as taxas de mineração para os 5 usuários e, em seguida, esses dois entrantes poderão aproveitar a gratuidade dos remixes seguintes.

![legende](assets/4.jpeg)'

'Graças a esse modelo de taxas, a Whirlpool se diferencia verdadeiramente de outros serviços de CoinJoin, uma vez que os Anon Sets das UTXO não são proporcionais ao preço pago pelo usuário. Portanto, é possível obter Anon Sets muito altos, tendo apenas pago as taxas da pool e as taxas de mineração para duas transações (Tx0 e mix inicial).

Obviamente, o usuário também terá que pagar as taxas de mineração quando quiser retirar suas UTXO da pool após ter feito suas várias misturas.

Como explicado anteriormente, dizemos que uma UTXO está em uma pool quando ela está disponível para mistura. Isso não significa que o usuário perde a propriedade dela. Ao longo das diferentes CoinJoin com a Whirlpool, você permanece totalmente no controle de suas chaves e, portanto, de seus bitcoins.

## Contas na Whirlpool.

Para poder realizar esse tipo de transação CoinJoin, uma carteira que utiliza a Whirlpool precisará derivar várias contas.

Uma conta é uma subseção em uma carteira HD. Essa separação ocorre na profundidade 3 da carteira, ou seja, no nível do xpub/xprv.

Se você não está familiarizado com o conceito de contas dentro de uma carteira HD, recomendo que leia meu e-book dedicado a esse assunto, que você pode baixar gratuitamente clicando aqui. Também escrevi um artigo completo sobre o funcionamento dos caminhos de derivação: Entendendo os caminhos de derivação de uma carteira Bitcoin.

Você obviamente não precisa entender tudo isso para usar a Whirlpool, mas lembre-se de que uma conta é uma subseção de uma carteira HD, que é completamente separada das outras contas e possui seu próprio xpub/zpub.

É graças a essa separação estrita das diferentes contas que é impossível ocorrer a reutilização de endereços entre bitcoins misturados e bitcoins não misturados na Whirlpool.

Em cada carteira HD, é possível derivar até 2^(32/2) contas diferentes. A primeira conta, aquela que você usa por padrão em sua carteira sem saber, é a conta 0'.

Quando você usa uma carteira adequada para o uso da Whirlpool, ela automaticamente cria 5 contas:

> A conta de Depósito determinada pelo índice 0'.
>
> A conta Bad Bank (doxxic change) determinada pelo índice 2 147 483 644'.
>
> A conta Pre Mix determinada pelo índice 2 147 483 645'.
>
> A conta Post Mix determinada pelo índice 2 147 483 646'.
>
> A conta Ricochet determinada pelo índice 2 147 483 647': Esta última conta não é usada diretamente no protocolo Whirlpool, mas está relacionada a ele. Falarei mais sobre isso na parte dedicada às ferramentas de gasto.

Cada conta tem sua própria utilidade e será destinada a uma tarefa específica.

Todas as contas dependem da mesma semente. O usuário pode facilmente recuperar o acesso a todos os seus fundos em caso de problema com sua frase de recuperação e possível frase de acesso. No entanto, será necessário informar ao software de recuperação os diferentes índices das contas utilizadas.

Agora vamos ver as diferentes etapas de um CoinJoin Whirlpool dentro dessas contas.

## Tx0.

No início de um CoinJoin, tudo parte da conta de Depósito. Esta é a conta que você usa por padrão ao criar uma nova carteira Bitcoin. Esta conta deve ser creditada com os bitcoins que o usuário deseja misturar.

A Tx0 é a primeira transação no processo de mistura do Whirlpool. Seu objetivo é limpar o(s) UTXO a serem misturados antes de enviá-los para uma primeira mistura. Essa transação irá dividir o UTXO de entrada em vários UTXOs que correspondem ao valor do pool escolhido. Todos esses UTXOs equalizados serão enviados para a conta Prémix. A diferença restante que não pode entrar na pool escolhida será separada em uma conta dedicada a ela: Bad Bank (ou "Doxxic Change").

Essa Tx0 também será usada para pagar as taxas ao coordenador.

Você precisará pagar taxas de mineração para a Tx0.

![Esquema de uma transação Tx0 CoinJoin Bitcoin!](assets/5.jpeg)

Crédito (imagem modificada): KYCP.org: https://kycp.org/#/a126e48d4a6eb8d19682ec0e23ad45e76cd52b45f6c17be5068ae051d4b2cc24

Neste exemplo de uma transação Tx0, podemos ver uma entrada de 2,2550 bitcoins da conta de depósito do usuário que inicia a Tx0. Essa entrada é dividida em vários UTXOs de saída que representam:

- As taxas do coordenador, aqui: 0,0250 B.

- Os quatro UTXOs prontos para serem misturados que irão para a conta Premix do usuário. Esses UTXOs também são registrados junto ao coordenador.

- A diferença que não pode entrar na pool, pois é muito pequena: é a mudança tóxica que irá para sua conta dedicada e isolada.

As taxas aqui são diferentes das que eu lhe dei na tabela anterior, pois a Samourai reduziu seus preços para o Whirlpool em março de 2021.

## Conta doxxic change.

A mudança que não pode ser incluída na pool é enviada para a conta Doxxic Change (também conhecida como "Bad Bank") para separá-la completamente das demais contas.

Este UTXO é perigoso para a privacidade do usuário, pois não só está sempre ligado ao seu passado e, portanto, potencialmente à identidade de seu proprietário, mas também é registrado como pertencente a um proprietário que fez um CoinJoin.
Si este UTXO for mesclado com UTXOs misturados, estes perderão toda a confidencialidade adquirida anteriormente. Se for mesclado com outras Mudanças Doxxic, o usuário corre o risco de perder confidencialidade. Portanto, deve ser tratado com cuidado. Explicarei precisamente como lidar com este UTXO tóxico nesta parte.

## Conta Pré-Mistura.

Na conta Pré-Mistura, encontraremos os UTXOs equalizados durante a Tx0 prontos para serem misturados. Esses UTXOs são ligeiramente superiores ao valor do pool, pois devem cobrir as taxas de mineração de sua mistura inicial.

Uma vez que esses UTXOs passam por sua mistura inicial, a conta Pré-Mistura ficará vazia e novos UTXOs estarão presentes na próxima conta.

## Conta Pós-Mistura.

A conta Pós-Mistura recebe os UTXOs recém-misturados de sua mistura inicial. Também recebe todos os outros UTXOs disponíveis para remixes.

Se o cliente Whirlpool estiver em execução, os UTXOs presentes na conta Pós-Mistura estão disponíveis para remixes. Eles serão selecionados aleatoriamente para serem remixados.

Quando o usuário deseja gastar UTXOs misturados, ele pode fazê-lo diretamente desta conta Pós-Mistura. Além disso, é aconselhável deixar os UTXOs misturados nesta conta, não apenas para serem remixados gratuitamente, mas também para que não saiam do circuito Whirlpool, caso contrário, correm o risco de perder confidencialidade.

## Conjuntos Anônimos.

Como explicado anteriormente, os Conjuntos Anônimos são dois parâmetros que permitem calcular o quão confidencial é um UTXO e, portanto, quão eficiente é sua sessão de CoinJoin.

O primeiro parâmetro é a pontuação prospectiva (em inglês: "Forward-looking Anon Set"). Embora essa semântica seja incorreta, essa pontuação muitas vezes é chamada diretamente de "Anon Set" por abreviação.

A pontuação prospectiva de um UTXO representa o tamanho do grupo no qual ele está oculto em um determinado momento.

Para dar uma imagem, a pontuação prospectiva é o número de UTXOs atuais que podem corresponder a um UTXO específico no passado. Por exemplo, vamos imaginar um ator observando a cadeia do Bitcoin que rastreia um UTXO que lhe pertence antes de entrar no pool de CoinJoin. Depois que sua moeda passa por várias misturas, o observador se pergunta onde ela foi. Ele começa então a traçar os diferentes caminhos possíveis e, graças à natureza do CoinJoin, ele encontrará vários UTXOs que potencialmente podem corresponder ao seu. Esse número de UTXOs potenciais é a pontuação prospectiva do seu UTXO que está entre eles.

Assim, após a saída de um primeiro CoinJoin Whirlpool, um UTXO terá uma pontuação prospectiva igual a 5. Ou seja, estará oculto em um grupo provável de 5 UTXOs:

'![Schéma de calcul du score prospectif d'un UTXO Bitcoin](assets/6.jpeg)

Se alguém estiver monitorando minha UTXO de entrada, ele não poderá saber qual dessas 5 UTXOs de saída me pertence.

Esse score prospectivo aumenta à medida que o usuário faz remixes, mas também à medida que os pares que ele encontrou durante seus mixes anteriores fazem remixes. Vamos retomar nosso exemplo com uma UTXO que tem um score prospectivo de 5 no momento. Se essa UTXO que nos pertence for remixada, então seu score passará para 9.

O que é muito interessante no Whirlpool é que, mesmo que minha UTXO não seja remixada, já que ela faz parte de um grupo no qual não pode ser diferenciada das outras, seu score aumentará de acordo com os remixes de seus pares encontrados no passado.

Vamos imaginar que nossa UTXO tenha passado por uma primeira mixagem e, portanto, tenha um score de 5. Se uma UTXO presente nessa mesma mixagem passar por uma nova remixagem, então o score da minha UTXO aumentará para 9, mesmo que ela não tenha se movido desde a mixagem inicial:

![Schéma de calcul du score prospectif d'un UTXO Bitcoin](assets/7.jpeg)

Esse aumento do score prospectivo é exponencial, pois se uma UTXO encontrada pela UTXO que encontrei durante minha primeira mixagem for remixada, então meu Anon Set aumenta ainda mais:

![Schéma de calcul du score prospectif d'un UTXO Bitcoin](assets/8.jpeg)

Esse aumento exponencial é possível devido ao modelo único do Whirlpool estabelecido em muitas pequenas CoinJoins sucessivas.

Lembrando, todas essas remixagens são gratuitas, então é muito inteligente deixar suas UTXOs se misturarem e se remixarem, aproveitando as remixagens de seus pares encontrados, desde que você não precise gastar essas UTXOs que lhe pertencem.

![video stylé](assets/7-5.mp3)

O segundo Anon Set que pode ser determinado em uma UTXO específica para calcular seu nível de confidencialidade é o score retrospectivo (em inglês "Backward-looking Anon Set").

Esse score retrospectivo é de certa forma a herança deixada pelos pares anteriores à sua mixagem inicial. Ele indica o número de Tx0 que podem corresponder à sua UTXO mixada.

Portanto, ele permite avaliar o nível de confidencialidade de uma UTXO em relação a uma tentativa de rastreamento oposta à primeira mencionada.

Lembre-se de que, para o score prospectivo, esse parâmetro permite avaliar o quão confidencial estamos em caso de tentativa de rastreamento a partir de uma UTXO de entrada de ciclos de CoinJoin em direção à nossa UTXO de saída. Para o score retrospectivo, o parâmetro permite avaliar o quão confidencial uma UTXO de entrada é, tomando como ponto de partida de rastreamento uma UTXO de saída do ciclo. Ou seja, estamos seguindo o caminho inverso.'

Por exemplo, vamos supor que um observador da cadeia Bitcoin conheça uma UTXO e queira rastrear de onde ela veio para tentar determinar sua origem. Ele vai descobrir que essa UTXO passou por CoinJoins e vai se deparar com várias UTXOs de entrada de CoinJoin que poderiam potencialmente ser a procurada. O número de UTXOs potenciais é o score retrospectivo da UTXO rastreada.

Para calcular esse score retrospectivo, é necessário primeiro contar a partir da UTXO alvo todas as UTXOs de entrada provenientes de uma Tx0. Em seguida, será necessário analisar as UTXOs de remixagem de entrada da transação e retroceder até as 3 transações CoinJoin anteriores das quais elas são provenientes. Em cada uma dessas três transações, o mesmo cálculo será realizado. Continua-se assim sucessivamente até a transação CoinJoin Genesis, ou seja, a primeira transação CoinJoin do pool.

![Esquema de cálculo do score retrospectivo de uma UTXO Bitcoin](assets/9.jpeg)

No esquema acima, o cálculo do score retrospectivo de uma das UTXOs de saída do CoinJoin no topo é equivalente a calcular o número de Tx0 (as bolhas azuis) presentes nos CoinJoins ascendentes até o CoinJoin alvo, até o CoinJoin Genesis.

Ao contrário do score prospectivo de uma UTXO, que começa em 5 após sua mistura inicial e aumenta, o score retrospectivo de uma UTXO será imediatamente muito alto quando você fizer sua mistura inicial. Quanto mais recentemente uma UTXO foi misturada, maior será seu score retrospectivo. Você se beneficia da herança das misturas anteriores no pool escolhido.

## Ferramenta de Estatísticas Whirlpool (WST).

Para calcular facilmente os Anon Sets de uma de suas UTXOs misturadas no Whirlpool, você pode usar a Ferramenta de Estatísticas Whirlpool (WST). Uma ferramenta especialmente projetada para calcular seus Anon Sets no Whirlpool.

Se você é um usuário do RoninDojo, a ferramenta está pré-instalada em seu nó. Para acessá-la pelo RoninCLI, vá para:

```
Samourai Toolkit > Whirlpool Stat Tool
```

Se você não possui um RoninDojo, aqui está como instalar a ferramenta WST em uma máquina Linux:

Você precisará do: Navegador Tor (ou Tor), Python 3.4.4 ou superior, git e pip3.

Para verificar suas versões, digite os comandos:

```
python --version
git --version
pip --version
```

Instale as dependências:

```
pip install PySocks
pip install requests[sock5]
pip install plotly
pip install datasketch
pip install numpy
```

Instale a Ferramenta de Estatísticas Whirlpool:

```
#Clone o repositório:
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git

#Acesse o diretório /whirlpool_stats:

cd whirlpool_stats
#Instale as dependências com pip:
pip3 install -r ./requirements.txt
```

Eu pessoalmente tive alguns problemas com esta última versão do WST. Se não funcionar para você, você também pode clonar a versão anterior no github que funciona perfeitamente: https://github.com/Samourai-Wallet/whirlpool_stats. Os próximos passos serão os mesmos. Apenas observe que a pool de 100k sats não existia naquela época, então você precisa adicioná-la manualmente ao código se estiver usando a versão antiga.

Em seguida, crie um diretório de trabalho para armazenar os dados das transações e execute o WST:

#Acesse o diretório desejado, por exemplo, home:

```
cd ~

#Crie um diretório dedicado, por exemplo, chamado "wst":
mkdir wst

#Acesse o subdiretório /whirlpool_stats:
cd whirlpool_stats/whirlpool_stats/

#Execute o WST:
python3 wst.py
```

Depois de instalar e executar o WST, aqui está como calcular Anon Sets. Essas etapas são semelhantes, quer você esteja em uma máquina comum ou no RoninDojo:

Digite o seguinte comando para definir o proxy no Tor (para o RoninDojo, este comando será obrigatório):

```
        socks5 127.0.0.1:9050
```

Se você estiver usando o Tor Browser, ele deve estar em execução e o comando será:

```
        socks5 127.0.0.1:9150
```

Em seguida, acesse o diretório de trabalho criado na etapa anterior com o comando workdir. Se você estiver no RoninDojo, pule esta etapa:

```
workdir /home/psyduck/wst
#Substitua o caminho neste exemplo pelo seu próprio caminho.
```

![Lançamento do WST por linha de comando](assets/10.jpeg)

Em seguida, faça o download dos dados da pool que contém sua transação:

```
download 0001

#Substitua 0001 pelo código de denominação da pool que você está interessado.
```

Os códigos de denominação são os seguintes no WST:

- Pool 0,5 bitcoins: 05
- Pool 0,05 bitcoins: 005
- Pool 0,01 bitcoins: 001
- Pool 0,001 bitcoins: 0001

Depois de baixar os dados, carregue-os com o comando:

```
load 0001

#Substitua 0001 pelo código de denominação da pool que você está interessado.
```

![Download de dados do WST do OXT por linha de comando](assets/11.jpeg)

Após carregar os dados, digite o comando score seguido do seu TXID (identificador de transação) para obter seus Anon Sets:

```
score TXID

#Substitua TXID pelo identificador da sua transação.
```

![Resultado do cálculo dos Anon Sets de uma UTXO com o WST](assets/11.jpeg)

> Em seguida, a WST exibe a pontuação retrospetiva (métricas retrospectivas) e a pontuação prospetiva (métricas prospectivas). Para além das pontuações dos conjuntos anónimos, a WST também lhe fornece a taxa de difusão do seu resultado no conjunto com base no conjunto anónimo.
>
> Tenha em atenção que a pontuação prospetiva do seu UTXO é calculada a partir do TXID da sua mistura inicial e não da sua última mistura. Pelo contrário, a pontuação retrospetiva de um UTXO é calculada a partir do TXID do último ciclo.

## Muuuh xpubs.

Existe muita desinformação sobre o funcionamento da Whirlpool. A mais difundida é certamente a crítica de que o Samourai teria acesso aos xpubs dos utilizadores num servidor.

Na realidade, o protocolo Whirlpool funciona sem necessitar de acesso aos xpubs dos utilizadores. A necessidade de xpub está ao nível da carteira, como qualquer outro software, e está limitada a uma utilização muito específica:

- Se utilizar a Whirlpool na Samourai Wallet sem utilizar o seu próprio Dojo, então sim, o Dojo da Samourai conhece o seu xpub.

- Se utilizar a Whirlpool na Samourai Wallet com o seu próprio Dojo, não há fugas de xpub.

- Se utilizar a Whirlpool na Sparrow Wallet sem utilizar o seu próprio nó, o nó de terceiros ao qual está ligado vê as suas transacções.
- Se usar a Whirlpool na Sparrow Wallet com o seu próprio nó, não há fugas nesta frente.

Como em qualquer outra carteira Bitcoin, você deve usar seu próprio nó. Caso contrário, perde independência, confidencialidade e confiança. Mas, em última análise, isto não tem nada a ver com o protocolo Whirlpool. Nesse sentido, a Samourai Wallet age como qualquer outra carteira existente.

Agora que já vimos a teoria e o funcionamento geral, vamos tentar a prática!

# Secção prática

## Tutorial: Whirlpool na Sparrow Wallet.

Existem muitas opções para usar o Whirlpool. A primeira que vos quero apresentar é a implementação da Sparrow Wallet, um software open-source de gestão de carteiras Bitcoin no PC.

Este método tem a vantagem de ser bastante fácil de utilizar, rápido de configurar e de não necessitar de mais nenhum dispositivo para além de um computador e de uma ligação à Internet. No entanto, este método tem uma desvantagem notável que não é encontrada no segundo tutorial que encontrará na secção seguinte:

- As misturas só acontecerão quando o Sparrow for iniciado e estiver ligado. Isto significa que se quiseres misturar e remisturar os teus bitcoins 24 horas por dia, 7 dias por semana, terás de deixar o teu computador constantemente ligado.

A única solução para este problema é usar o seu próprio Dojo. Falarei sobre isso na próxima secção.

'Se você nunca usou o Whirlpool antes e deseja fazê-lo agora mais por uma questão de compreensão do que eficiência, eu recomendo que você comece devagar com o Sparrow para entender bem os mecanismos.
Vamos lá, vamos ver juntos como fazer:

Para começar, você obviamente precisará do software Sparrow. Você pode baixá-lo diretamente no site oficial do Sparrow Wallet ou no GitHub deles:

- https://sparrowwallet.com/download/

- https://github.com/sparrowwallet/sparrow/releases

Antes de instalar o software, será importante verificar a assinatura e a integridade do executável que você acabou de baixar. Se você não sabe como fazer isso, eu explico como fazer no Windows neste artigo: Como verificar a integridade de um software Bitcoin no Windows?

Depois de instalar o software, você precisará criar uma carteira Bitcoin. Note que, para misturar, é obrigatório ter uma carteira de software (chamada de "quente"). Portanto, você não poderá misturar com uma carteira segura por hardware wallet.

Isso não é obrigatório, mas se você pretende misturar quantias significativas, eu recomendo fortemente que você use uma frase secreta forte nesta carteira. Se você não sabe como criar uma carteira no Sparrow, eu explico em detalhes como fazer isso na 5ª parte do seguinte artigo: Tudo sobre a Frase Secreta Bitcoin.

Depois de criar a carteira, envie os sats para misturar. Basta clicar em "Receive" e enviá-los para um endereço que seja seu, como você faria normalmente.

Aqui, podemos ver que acabei de criar minha carteira e enviei um pouco mais de 199k sats:

![Recebendo bitcoins no Sparrow Wallet](assets/12.JPEG)

Por enquanto, você está usando uma conta comum. Esta conta indexada 0' se tornará sua conta de Depósito para misturar.

Para misturar essa UTXO que você acabou de receber, vá para a lista de UTXOs da conta clicando em "UTXOs" à esquerda da interface:

![Selecionando UTXOs para misturar no Sparrow Wallet](assets/13.JPEG)

Em seguida, selecione os diferentes UTXOs para misturar clicando neles. Se você deseja selecionar vários, mantenha pressionada a tecla Ctrl e clique em cada um deles. Uma vez selecionado o UTXO, ele será destacado em azul.

Em seguida, clique no botão "Mix Selected" na parte inferior da interface:

![Iniciando o processo de mistura de bitcoins no Sparrow Wallet](assets/14.JPEG)

Uma janela se abrirá para explicar o funcionamento do Whirlpool. Isso é uma simplificação do que expliquei na parte anterior.

Clique em "Next" depois de ler.

![Introdução ao funcionamento do Whirlpool](assets/15.JPEG)'

Também explicamos como funcionam as contas. Clique em "Seguinte" depois de ler.

Introdução ao funcionamento das contas Whirlpool](assets/16.JPEG)

Na página seguinte, pode introduzir um SCODE, se tiver um. Um SCODE é um código de desconto a aplicar à taxa de entrada na piscina. Por vezes, a Samourai Wallet oferece-os aos seus utilizadores em ocasiões especiais (por exemplo, no Natal). Não te esqueças de os seguir no Twitter para não perderes os próximos SCODES: https://twitter.com/SamouraiWallet

De seguida, escolha a taxa de mineração que pretende atribuir ao Tx0 e a mistura inicial. Isto afectará a velocidade a que a sua primeira mistura é confirmada. Lembre-se de que paga as taxas de extração para o seu Tx0 e a sua mistura inicial, mas não pagará quaisquer taxas de extração para quaisquer outras remisturas.

Quando tiveres escolhido as tuas taxas, clica em "Seguinte".

![Definições da taxa de mineração da Whirlpool](assets/17.JPEG)

Nesta nova janela, pode escolher em que grupo quer entrar, clicando na lista pendente. A janela também indica a taxa da piscina que vais pagar e o número de UTXO que vão entrar nessa piscina. Em seguida, clique em "Preview Premix" (Pré-visualizar mistura).

No meu exemplo, eu tinha um UTXO de 199k sats, por isso vou entrar com apenas um UTXO no pool de 100k sats:

![Seleção da piscina de mistura](assets/18.JPEG)

O Sparrow pedir-lhe-á então que introduza a palavra-passe da sua carteira que configurou quando a criou no software.

Confirmar palavra-passe da carteira Bitcoin](assets/19.JPEG)

Isto levá-lo-á à pré-visualização do seu Tx0.

Em primeiro lugar, pode ver que o Sparrow derivou as várias contas necessárias para utilizar o Whirlpool. Pode vê-las à esquerda do ecrã.

Também pode ver a estrutura da sua transação com as diferentes saídas:

- Taxas de Pool (coordenador).

- Premix UTXO.

- A mudança doxical.

Verificação do Tx0 final antes da difusão](assets/20.JPEG)

Se estiver satisfeito com a transação, clique no botão "Transmitir transação" para transmitir o seu Tx0. Caso contrário, pode também modificar os parâmetros deste Tx0 clicando no botão "Limpar" e reiniciando a construção desta transação.

Transmitir Tx0](assets/21.JPEG)

Uma vez transmitido o Tx0, pode encontrar o seu UTXO pronto a ser misturado na conta Premix. O seu UTXO está agora registado pelo coordenador e será enviado para a sua mistura inicial.

![Tx0 diffusée en attente de confirmation](assets/22.JPEG)

Aqui, podemos ver que minha UTXO proveniente da Tx0 foi confirmada uma vez. Também podemos ver a mistura inicial que foi construída e transmitida, mas está aguardando confirmação:

![Tx0 confirmada, mistura inicial transmitida](assets/23.JPEG)

Se acessarmos a conta Postmix, podemos ver que a UTXO proveniente da mistura inicial foi transmitida, mas ainda não foi confirmada. Assim que for confirmada, ela ficará automaticamente disponível para futuras misturas que não serão cobradas.

Na coluna "Misturas", você poderá observar o número de misturas de suas diferentes UTXOs. Lembre-se de que não é tanto o número de misturas que é importante, mas sim os Anon Sets, embora as duas informações estejam parcialmente relacionadas.

![Mistura inicial confirmada, UTXO aguardando misturas](assets/24.JPEG)

Aí está, sua UTXO foi misturada. Atualmente, está na pool aguardando misturas. Se você deseja interromper a mistura, basta clicar no botão "Parar Mistura". Você pode reiniciá-la clicando no botão "Iniciar Mistura".

Se você deseja deixar sua UTXO disponível para mistura, é obrigatório deixar o software Sparrow Wallet aberto e seu computador ligado (não em modo de espera).

Você pode eventualmente desativar o modo de espera nas opções do seu sistema operacional. Também há uma opção a ser selecionada no software Sparrow para evitar o modo de espera do seu computador:

> Ferramentas > Impedir Suspensão do Computador

![Impedir suspensão do computador](assets/25.JPEG)

O botão "Misturar para" presente em sua conta Postmix na seção UTXO permite configurar o envio automático de sua UTXO misturada para a carteira de sua escolha. Você pode escolher o número de misturas a serem feitas antes do envio para essa carteira.

Essa opção permite, por exemplo, enviar automaticamente seu Postmix para sua carteira de hardware. No entanto, é geralmente desaconselhável usar essa opção. Explicarei o motivo na seção: Boas práticas em pós-mistura.

Aqui, apresentei uma das opções para misturar com o Whirlpool, mas existem outras. Por exemplo, você pode misturar diretamente do seu smartphone com o aplicativo Samourai Wallet no Android. O funcionamento será semelhante ao descrito nesta parte.

![Samourai](assets/26.JPEG)

## Tutorial: Whirpool CLI no Dojo e Whirlpool GUI.

Se você deseja avançar para a próxima etapa, pode misturar com o Whirlpool em seu próprio Dojo.

Dojo é uma implementação de um nó Bitcoin desenvolvida pela equipe do Samourai Wallet. Se você estiver usando seu próprio Dojo para CoinJoin no Samourai, os xpubs de suas diferentes contas não serão transmitidos para servidores de terceiros. Portanto, você ganhará em privacidade ao eliminar um dos riscos inerentes ao Whirlpool.
De plus, Dojo integra Whirlpool CLI, o que permite executar remixes 24 horas por dia, 7 dias por semana, sem a necessidade de deixar sua carteira aberta constantemente em outro dispositivo.
Essa solução requer a execução de um nó Bitcoin e é um pouco mais complexa de configurar do que o exemplo anterior. No entanto, é essa solução que oferece a melhor experiência de CoinJoin no Whirlpool com o menor risco possível.

Para executar seu próprio Dojo, você pode instalar diretamente seu nó Dojo ou usar o Dojo em outra implementação de um nó Bitcoin. As implementações que permitem isso até o momento são:

- RoninDojo, que é simplesmente um Dojo com ferramentas adicionais e inclui um assistente de instalação e um assistente de administração. Explico em detalhes como configurar e usar o RoninDojo neste artigo: Instalando e usando seu nó Bitcoin RoninDojo.

- Umbrel através do aplicativo "Samourai Server".

- MyNode com o aplicativo "Dojo".

- Nodl com o aplicativo "Dojo".

Para nosso exemplo, usaremos três interfaces diferentes:

- Samourai Wallet.

- Whirlpool GUI.

- Whirlpool CLI.

Portanto, o Whirlpool CLI será executado no Dojo para aproveitar as vantagens mencionadas anteriormente. Ele será responsável por se comunicar com o coordenador e gerenciar as misturas.

A Whirlpool GUI é a interface gráfica que usaremos para ver o que está acontecendo no Whirlpool CLI e para iniciar misturas remotamente. A GUI será instalada em um PC qualquer diferente do Dojo para facilitar a administração.

A Samourai Wallet hospedará nossa carteira destinada ao CoinJoin. É um aplicativo gratuito e de código aberto que você pode baixar no Android ou em um emulador. Com este aplicativo, você sempre terá controle sobre sua carteira de mistura e poderá gastar facilmente seus pós-misturas em todos os seus deslocamentos.

### Etapa 1: Preparar seu Dojo.

Portanto, o primeiro passo é ter um Dojo. Você precisará obter o URL de conexão com o Dojo, que é apresentado como um endereço Tor. Você também pode usar o código QR. Este endereço permitirá que você conecte sua carteira Samourai Wallet ao seu nó através do Dojo.

Se você estiver usando o Umbrel, vá para a App Store no menu à esquerda e instale o "Samourai Server". Depois de iniciar o aplicativo, você encontrará o código QR de conexão com o Dojo.

Se você estiver usando o RoninDojo, vá para o RoninUI em seu navegador, faça login e clique em "Manage" em azul na parte inferior do bloco "Dojo". Você poderá acessar o código QR do Samourai Dojo clicando em "Display Values".

![Endereço de conexão Dojo](assets/27.JPEG)

### Etapa 2: Preparar sua carteira.

Para a carteira, vamos usar a Samourai Wallet. Você pode baixá-la na Google Play Store ou diretamente com o arquivo APK em seu site oficial.
Abra o aplicativo e conecte-se ao seu Dojo usando o código QR da etapa anterior. Depois de conectado, clique em "Criar uma nova carteira".

![Conectando ao Dojo pelo Samourai](assets/28.JPEG)

Em seguida, o Samourai solicitará que você crie uma Frase de Segurança. Se você não sabe o que é uma Frase de Segurança e como configurá-la corretamente, recomendo fortemente que leia meu artigo sobre o assunto: Tudo sobre a Frase de Segurança do Bitcoin.

Escolha uma Frase de Segurança forte e faça um backup físico dela. Clique em "Próximo" para continuar.

![Criando a frase de segurança da carteira](assets/29.JPEG)

Depois, você precisará escolher um PIN para acessar o aplicativo. Este PIN é muito importante, mas não tem nenhuma relação com sua carteira Bitcoin. Ele é específico para o funcionamento do aplicativo Samourai. Você precisará dele para acessar sua carteira pelo aplicativo Samourai. No entanto, se precisar recuperar sua carteira, apenas sua Frase de Segurança e sua frase de recuperação (mnemônica) serão necessárias. Escolha um PIN forte, faça um backup e clique em "Próximo".

![Escolhendo o PIN do aplicativo Samourai](assets/30.JPEG)

Será solicitado que você confirme este PIN mais uma vez. Em seguida, você poderá acessar a frase de recuperação de sua carteira Samourai. Assim como a frase de segurança, essa informação deve ser adequadamente armazenada em um suporte físico e seguro, caso contrário, você poderá perder permanentemente o acesso aos seus bitcoins em caso de problemas. Para saber mais sobre a frase de recuperação, recomendo que leia este artigo: O que é a frase de recuperação do Bitcoin?

Após confirmar, você chegará à sua nova carteira Samourai. Antes de fazer qualquer coisa, comece testando seus backups. Antes de fazer isso, obtenha um xpub de sua carteira para ter certeza de que está no caminho certo:

> Configurações > Carteira > Mostrar BIP44 XPUB

Será fornecido um código QR com o valor do XPUB. Anote apenas em um papel os últimos 8 caracteres deste xpub. Por exemplo:

> X2GGWaLt

Isso garantirá que você está na carteira correta e que não cometeu erros na frase de segurança.

Em seguida, exclua a carteira vazia ou reinstale o aplicativo Samourai e tente reconstruí-la apenas com seus backups anteriores. Para fazer isso, depois de se conectar ao seu Dojo, clique em "Restaurar uma carteira existente".
'Insira a frase de recuperação e a frase secreta anotadas em seus backups físicos, escolha o mesmo PIN que antes e restaure esta carteira. Se isso não funcionar, então o backup da sua frase de recuperação não está correto. Recomece a etapa 2 desde o início.

Se você conseguir acessar a carteira, verifique se o primeiro XPUB BIP 44 ainda é o mesmo. Vá para:

> Configurações > Carteira > Mostrar XPUB BIP44

Verifique se os últimos 8 caracteres correspondem aos que você anotou no pedaço de papel anteriormente. Se não for o caso, então o backup da sua frase secreta não está correto (ou você cometeu um erro de digitação). Recomece a etapa 2 desde o início.

Se o seu backup estiver funcionando corretamente, você pode prosseguir para a próxima etapa com tranquilidade.

> Por favor, observe que este teste de backup de uma nova carteira também deve ser realizado em qualquer outra carteira, não apenas no Samourai.

### Etapa 3: Preparar o Whirlpool GUI.

Agora vamos instalar o Whirlpool GUI, a interface gráfica que permitirá que você gerencie suas CoinJoin. Acesse seu computador pessoal.

Primeiro, você precisará instalar o kit de desenvolvimento Java Developer Kit (JDK). Você pode, por exemplo, instalar o OpenJDK gratuitamente a partir deste site: https://adoptopenjdk.net/ Isso permitirá que você compile e execute software desenvolvido em Java.

![Instalação do OpenJDK](assets/31.JPEG)

Depois de instalar o OpenJDK, você poderá instalar o Whirlpool GUI a partir do site oficial da Samourai Wallet: https://samouraiwallet.com/download/whirlpool

Inicie o Whirlpool GUI. Para que o Whirlpool GUI possa se conectar, você precisará ter o Tor Daemon ou o Tor Browser em execução em segundo plano em seu PC. Você precisará iniciá-los antes de cada uso do Whirlpool GUI neste computador. Se você não tiver o Tor, instale-o a partir do site oficial antes de começar: https://www.torproject.org/download/

![Escolha de conexão do Whirlpool GUI](assets/32.JPEG)

No Whirlpool GUI, clique em "Avançado: CLI Remoto" para conectar seu Whirlpool CLI ao seu Dojo. Você precisará do endereço Tor do seu Whirlpool CLI.

- Para encontrá-lo no Umbrel: simplesmente inicie o aplicativo Samourai Server, você o encontrará na página.

- Para encontrá-lo no RoninDojo: vá para o menu principal RoninCLI e vá para Credenciais > Whirlpool.

No Whirlpool GUI, insira o endereço Tor encontrado anteriormente no campo "Endereço CLI". Deixe o "http://", mas não coloque o ":8899". Apenas cole o endereço que foi fornecido a você.'
Sur a próxima caixa, digite 9050 se estiver usando o Tor Daemon ou 9150 se estiver usando o navegador Tor. Se esta for a primeira vez que você está conectando sua Whirlpool CLI a partir de uma Whirlpool GUI, você pode deixar a caixa de chave API vazia. Caso contrário, preencha-a.

![Conectando a Whirlpool GUI ao Dojo](assets/33.JPEG)

Clique no botão "Connect" para emparelhar sua Whirlpool GUI com sua Whirlpool CLI. Tenha paciência, pode levar alguns instantes para estabelecer a conexão.

Em seguida, você poderá emparelhar sua carteira Samourai. Clique no símbolo do código QR à direita da tela para poder escanear.

![Conectando a Whirlpool GUI à carteira Samourai](assets/34.JPEG)

A partir da sua carteira Samourai Wallet, vá para:

> ... > Configurações > Transações > Emparelhar com Whirlpool GUI

Escaneie o código QR da sua Samourai no Whirlpool GUI.

![Emparelhando a carteira Samourai com o Whirlpool GUI](assets/35.JPEG)

Verifique se a conexão foi estabelecida no Whirlpool GUI. Na próxima página, ative "Use Dojo as wallet backend". Em seguida, clique no botão "Initialize GUI".

![Configurando o Whirlpool GUI](assets/36.JPEG)

Em seguida, você será solicitado a confirmar a frase de acesso da sua carteira Samourai. Clique em "Sign in" quando terminar.

![Confirmação da frase de acesso da carteira](assets/37.JPEG)

Aguarde alguns instantes. Após a configuração ser concluída, você será direcionado para o Whirlpool GUI:

![Acesso à interface do Whirlpool GUI](assets/38.JPEG)

### Etapa 4: Misturar!

Tudo está pronto, você está pronto para misturar seus bitcoins. Para fazer isso, envie os sats para misturar para a conta Deposit da sua carteira Samourai. Você também tem a opção de fazer isso diretamente pelo Whirlpool GUI.

Clique no botão "Deposit" para gerar um endereço de recebimento.

![Gerando um endereço de recebimento de Bitcoin](assets/39.JPEG)

Nesta página, você pode ver os valores mínimos a serem depositados para entrar em um pool específico. Sempre planeje um valor ligeiramente maior do que esse montante, caso contrário, sua UTXO pode não conseguir entrar na pool desejada até que as taxas de mineração diminuam.

Portanto, envie seus bitcoins para misturar para o endereço gerado. Você pode gerar um novo endereço clicando no botão "Renew address".

Para maior segurança em seu depósito, prefira depositar seus fundos com a Samourai Wallet. Basta clicar no + azul no canto inferior direito do aplicativo e depois em "Receber".
Une vez confirmado o depósito, você poderá vê-lo aparecer na conta "Depósito" na interface gráfica do Whirlpool. Para iniciar a série de Coinjoins, selecione as UTXO para enviar para a mistura e clique no botão "Premix". Atenção, se você selecionar várias UTXO diferentes simultaneamente, elas serão mescladas durante a TX0. Isso pode levar a uma perda de privacidade, especialmente se as fontes das UTXO forem diferentes.

![Lançamento do mix Tx0](assets/40.JPEG)

A página de configuração do Whirlpool será aberta. Escolha o pool em que deseja entrar. Escolha as taxas de mineração alocadas para a TX0 e para a CoinJoin inicial. Na parte inferior da página, é indicado o valor do troco e a quantidade e o número de UTXO igualados. Se a configuração estiver correta, clique no botão "Premix" para iniciar o processo de CoinJoin.

![Configuração do mix Tx0](assets/41.JPEG)

Após a criação da TX0, você pode ver suas UTXO igualadas na conta "Premix" aguardando confirmação. Se você deseja que seu Premix seja automaticamente misturado e que seus futuros postmix sejam remixados automaticamente 24 horas por dia, 7 dias por semana, ative a opção "Misturar automaticamente premix e postmix" na guia "Configuração" à esquerda da sua janela.

Agora você pode sair da interface gráfica do Whirlpool, suas UTXO estão disponíveis para CoinJoin 24 horas por dia, graças à sua interface de linha de comando Whirlpool no seu Dojo.

Você pode acompanhar suas UTXO na conta "Postmix" na interface gráfica do Whirlpool ou na interface Whirlpool no Samourai Wallet. Para fazer isso, clique no pequeno logotipo branco do Samourai no canto superior esquerdo da tela. As contas do Whirlpool são facilmente identificadas no Samourai Wallet pela cor azul clara:

![Observando as misturas CoinJoin no Samourai](assets/42.JPEG)

Para gastar seus postmix, basta clicar no sinal de "+" no canto inferior direito da tela e escolher uma ferramenta de gastos adequada.

Para acompanhar facilmente suas misturas automáticas, também recomendo configurar uma carteira Watch-Only com o aplicativo Sentinel para Android. Informe o ZPUB da sua conta PostMix e acompanhe em tempo real a evolução dos seus CoinJoin.

# Boas práticas pós-mixagem.

Após a mistura, é importante seguir algumas boas práticas se você não quiser perder toda a privacidade que conquistou com dificuldade ao misturar.

## UTXO pós-mixagem.

A melhor opção após a mistura é deixar suas UTXOs na sua carteira PostMix aguardando para serem gastas. Você até pode deixá-las se remixarem indefinidamente até que você precise delas para comprar algo.
Certos usuários preferirão mover seus bitcoins misturados para uma carteira segura por meio de uma hardware wallet. Você pode fazer isso, mas tome muito cuidado e siga as recomendações fornecidas pela Samourai Wallet. Sem isso, você corre o risco de perder toda a privacidade conquistada anteriormente.

O erro mais comum é a fusão de UTXO. É essencial não fundir, ou seja, colocar como input de uma mesma transação UTXOs misturados e UTXOs não misturados. Isso envolve gerenciar seus UTXOs dentro de sua carteira e rotulá-los para não fazer algo errado. Além do CoinJoin, a fusão de UTXO é uma prática ruim em geral, que muitas vezes leva à perda de privacidade quando não é controlada.

Também é importante ter cuidado com as consolidações entre UTXOs misturados entre si. É possível fazer pequenas consolidações se seus UTXOs misturados tiverem conjuntos Anon significativos, mas isso reduzirá o nível de privacidade de seus bitcoins.

Tenha muito cuidado para que a consolidação não seja muito grande, ou que não ocorra após um número muito pequeno de remixes, caso contrário, será possível vincular seus UTXOs antes do CoinJoin e depois do CoinJoin por dedução simples. Se você não entender bem esses conceitos, é mais seguro não consolidar os UTXOs após a mistura e enviá-los um por um para sua hardware wallet, cada vez com um novo endereço vazio. Mais uma vez, lembre-se de rotular cada UTXO recebido corretamente.

Também desaconselho mover seus pós-mistura para uma carteira que usa scripts minoritários. Por exemplo, se você entrar no Whirlpool de uma carteira multisig que usa scripts P2WSH, é pouco provável que você seja misturado com outros usuários que tenham o mesmo tipo de carteira originalmente. Se você retirar seus pós-mistura para essa mesma carteira multisig, o nível de privacidade de seus bitcoins misturados será significativamente reduzido.

Também é importante, como em qualquer outra transação Bitcoin, não reutilizar os endereços de recebimento. Lembre-se de que os endereços de recebimento são de uso único. Qualquer nova transação de entrada implica a geração de um novo endereço vazio.

> 1 UTXO = 1 Endereço

Portanto, a maneira mais simples e segura é deixar seus UTXOs misturados em paz, em sua carteira PostMix. Eles podem continuar se misturando e só devem ser tocados quando você quiser se livrar deles, ou seja, quando quiser gastá-los.

## Os UTXOs doxxic change.

En seguida, será necessário ter cuidado com a gestão do "Doxxic Change", a mudança que não pôde entrar na pool de mistura. Esses UTXO tóxicos criados após o uso do Whirlpool são perigosos para sua privacidade, pois eles estabelecem uma ligação entre você e seu uso do CoinJoin. Portanto, é importante não usá-los para qualquer coisa e, acima de tudo, não mesclá-los com qualquer outro UTXO. Aqui está o que você pode fazer com eles:

- Misturá-los em pools menores: se o seu UTXO for grande o suficiente para entrar sozinho em uma pool menor, então misture-o. Essa é provavelmente uma das melhores soluções. No entanto, não misture vários doxxic change juntos para entrar em uma pool. Isso é uma má ideia que permitirá estabelecer uma ligação entre suas diferentes entradas no Whirlpool.

- Rotulá-los como "não gastáveis" e deixá-los na conta designada: outra boa solução é simplesmente não tocá-los e rotulá-los como "não gastáveis" para ter certeza de que não serão usados. Se o preço do bitcoin aumentar, novas pools menores provavelmente serão criadas, o que permitirá misturar seus pequenos doxxic change adequadamente.

- Doá-los: é importante fazer pequenas doações, de acordo com o que você pode, para os diferentes desenvolvedores que trabalham no Bitcoin e nos softwares relacionados, bem como para os produtores de conteúdo que nos ajudam a entender o uso desses mesmos softwares. Você também pode optar por doar para diferentes associações que aceitam pagamentos em bitcoins. Se o seu doxxic change for um fardo para você, faça uma doação.

- Usá-los para comprar cartões-presente: alguns sites permitem que você compre cartões-presente com bitcoin para poder consumir em diferentes comerciantes conhecidos. Você pode se livrar do seu doxxic change comprando esse tipo de cartão-presente.

Certamente existem outras técnicas para se livrar de um doxxic change. Alguns falam em anonimizá-los usando a Lightning Network, outros usam uma troca com Monero. Essas técnicas podem ser boas, mas não as abordo neste artigo, pois não as domino. Convido você a fazer suas próprias pesquisas sobre esses assuntos.

# Ferramentas de gasto.

Portanto, como você já deve ter entendido, a prática mais segura no Pós-Mix é deixar seus UTXOs misturados em sua conta designada e não tocá-los até que você queira se separar deles.

Justamente, será importante finalizar o trabalho com estilo e usar ferramentas especialmente projetadas para otimizar nossa privacidade até o gasto de um UTXO misturado.
A disponibilidade dessas ferramentas depende do software de carteira escolhido pelo usuário. A Samourai Wallet se destaca claramente de seus concorrentes devido à diversidade e eficácia das ferramentas oferecidas. Alguns deles também estão disponíveis na Sparrow Wallet. Vamos ver juntos quais são essas ferramentas e como usá-las.

## PayJoin - Stowaway.

O PayJoin é um CoinJoin entre duas pessoas com uma estrutura específica. É usado para gastos em bitcoins. Pode ser usado tanto para gastar bitcoins misturados quanto para gastar bitcoins não misturados.

Essa estrutura específica de transação foi implementada pela primeira vez pela Samourai Wallet com a ferramenta Stowaway. Um BIP seguiu essa implementação, pegando a ideia do PayJoin e renomeando-a para P2EP (Pay-to-End-Point).

A especificidade do PayJoin é que ele produz uma transação que parece comum, mas na realidade é um mini CoinJoin entre dois usuários. Para isso, a estrutura da transação envolve o destinatário da transação nas entradas ao lado do remetente real. O destinatário inclui um pagamento para si mesmo no meio da transação para ser pago.

Por exemplo, se você comprar uma baguete do seu padeiro por 4000 sats usando uma UTXO de 10.000 sats e quiser fazer um PayJoin, seu padeiro adicionará à sua transação original uma UTXO de 15.000 sats que pertence a ele como entrada, que ele receberá integralmente como saída, para confundir a análise heurística:

![Esquema de uma transação Bitcoin PayJoin](assets/43.JPEG)

Neste exemplo, podemos ver que o padeiro colocou 15.000 como entrada e saiu com 19.000. A diferença é de fato 4.000 sats, o preço da baguete. Você, que deseja comprar a baguete por 4.000 sats, entrou com 10.000 e saiu com 6.000. A diferença é de fato -4.000 sats, o preço da baguete. Neste exemplo, eu intencionalmente negligenciei as taxas de mineração para simplificar.

Graças a essa estrutura, o PayJoin quebra a heurística de propriedade comum das entradas de uma transação Bitcoin. Quando alguém observar esse pagamento, pensará que você simplesmente juntou 2 de suas UTXOs para comprar um bem por 19.000 sats e recebeu a mudança de 6.000 sats. Na realidade, vimos que a situação é bem diferente. A análise da cadeia é, portanto, confusa, e os parâmetros do pagamento são difíceis de entender para quem os observa.

Esse tipo de transação pode ser uma excelente solução para gastar seus bitcoins recém-misturados sem perder em confidencialidade.

O JoinMarket também inclui uma ferramenta de PayJoin para gastar, deixarei você descobrir clicando aqui.
Comme visto anteriormente, a Samourai Wallet também possui sua própria ferramenta de PayJoin: Stowaway. Você pode usá-lo tanto no software Sparrow Wallet quanto no aplicativo Samourai Wallet.

Stowaway é baseado em um tipo de transação chamado "Cahoots", ou seja, uma transação colaborativa entre vários usuários que requer uma troca de informações fora da cadeia do Bitcoin. Até o momento, existem duas ferramentas Cahoots no Samourai: Stowaway e StonewallX2, que serão discutidas mais adiante.

As transações colaborativas Cahoots exigem a troca de transações parcialmente assinadas entre os usuários. Esse processo pode ser bastante demorado e complicado de ser realizado, especialmente se você estiver distante do outro usuário. No entanto, ainda é possível fazer isso manualmente com outro usuário da Samourai Wallet, o que pode ser uma boa opção se você estiver fisicamente com a pessoa colaboradora. O processo manual envolve a troca de 5 códigos QR para serem escaneados um por um.

A distância, esse processo se torna muito complexo. Portanto, a Samourai desenvolveu uma excelente solução: seu próprio protocolo de comunicação criptografada baseado no Tor, chamado Soroban. Com o Soroban, os usuários não precisam mais realizar todas essas trocas de códigos QR. As trocas são feitas automaticamente em segundo plano, bem escondidas atrás de uma interface de usuário otimizada.

As trocas criptografadas ainda exigem algum tipo de conexão e autenticação entre os colaboradores do Cahoots. As trocas do Soroban são estabelecidas nos PayNyms dos usuários. Se você não sabe o que são PayNyms, eu explico em detalhes neste artigo: O que é PayNym e BIP47?

Simplificando, um PayNym é uma espécie de identificador vinculado à sua carteira que permite a implementação de várias funcionalidades, incluindo trocas de mensagens criptografadas. O PayNym é representado por um identificador e um desenho de um robô. Aqui está o meu, por exemplo (no Testnet):

![PayNym no Sparrow Wallet](assets/44.JPEG)

Para realizar uma transação Cahoots à distância e, portanto, um PayJoin via Samourai ou Sparrow, você precisa "seguir" outro usuário pelo seu PayNym. No caso de um Stowaway (PayJoin), é necessário seguir a pessoa para quem você deseja enviar bitcoins.

Para fazer isso no Sparrow Wallet, basta inserir o PayNym ou escanear o código QR do colaborador na caixa "Encontrar Contato", como mostrado na captura anterior.

No Samourai, clique no "+" azul no canto inferior direito da tela e, em seguida, em "PayNyms" em roxo. Se você ainda não tem um PayNym, pode gerar o seu seguindo as instruções.

![Carteira Bitcoin Samourai Wallet](assets/45.JPEG)

**Tutorial realizado na Testnet: estes não são bitcoins reais.**
Uma vez na interface PayNym, clique no botão azul "+". Em seguida, você poderá seguir o PayNym do seu colaborador colando o seu identificador ou escaneando o seu código QR.

Em seguida, clique em "Seguir":

![Seguir um PayNym](assets/46.JPEG)

Em seguida, você será perguntado se deseja "conectar-se" a ele. Essa funcionalidade permite usar o BIP47 posteriormente. Isso tem um custo. No nosso caso, não precisamos disso, então não nos conectaremos.

![Conectar-se a um PayNym](assets/47.JPEG)

No meu exemplo, fiz um PayJoin entre minha carteira Samourai e minha carteira Sparrow. Para acessar o PayNym no Sparrow Wallet, basta clicar em "Ferramentas" e depois em "Mostrar PayNym".

![Mostrar o PayNym no Sparrow Wallet](assets/48.JPEG)

Aqui, podemos ver que meu PayNym laranja recebeu com sucesso a solicitação de seguir do meu PayNym branco (no Samourai). Sou gentil, então o segui de volta:

![Seguir o PayNym no Sparrow Wallet](assets/49.JPEG)

Agora que os Nyms estão conectados, eles poderão se comunicar entre si de forma criptografada através do Soroban. Portanto, podemos iniciar uma transação Cahoots.

Para realizar um PayJoin Stowaway a partir do Samourai, será necessário construir uma transação. Se você deseja gastar UTXOs misturados, vá para a conta Pós-mix antes de iniciar a transação.

Clique no botão azul "+" e depois em "enviar". Você também pode escolher especificamente qual UTXO deseja enviar:

![Criar um PayJoin Bitcoin a partir do Samourai Wallet](assets/50.JPEG)

Em seguida, digite o valor que deseja enviar. No meu exemplo, estou enviando 45.000 sats Testnet:

![Configuração do PayJoin Stowaway](assets/51.JPEG)

Clique em "Cahoots". Esta janela será aberta, onde você poderá escolher entre fazer um StonewallX2 ou um Stowaway. Aqui, queremos fazer um Stowaway:

![Escolha do tipo de transação colaborativa Cahoots Bitcoin](assets/52.JPEG)

Como explicado anteriormente, você pode realizar o PayJoin manualmente ou remotamente. É mais rápido e fácil fazer remotamente, mas requer estar conectado via PayNym. No nosso caso, escolheremos essa opção "Online":

![Escolha do tipo de colaboração manual ou soroban](assets/53.JPEG)

Em seguida, você será solicitado a escolher seu colaborador entre seus contatos PayNym. Aqui, escolho "luckyfrost", que é meu PayNym laranja no Sparrow:

![Escolha do colaborador](assets/54.JPEG)

Confirme clicando em "Verificar Transação".

![Verificação da transação Bitcoin PayJoin Stowaway](assets/55.JPEG)

Você poderá então escolher as taxas de mineração alocadas para essa transação. É importante saber que essas taxas serão pagas pelo emissor inicial da transação. Clique em "Iniciar Stowaway".

![Escolha das taxas de mineração](assets/56.JPEG)

Em seguida, você é convidado a aguardar para que seu par confirme que concorda em realizar essa transação colaborativa.

Para confirmar uma solicitação de cahoot no Samourai, clique no "+" azul e depois em "Receber" em verde. Um endereço será exibido. No canto superior direito, clique nos três pontos e depois em "Receive Online Cahoots".

Para confirmar no Sparrow Wallet, clique na guia "Ferramentas" e depois em "Encontrar parceiro de mistura". Uma janela será aberta, clique em "Próximo" e depois em "Próximo" novamente para confirmar a transação colaborativa.

O Cahoot está em andamento. Seus dois wallets estão trocando transações parcialmente assinadas e criptografadas no Tor através do Soroban.

![Desenvolvimento do cahoots via Soroban para Stowaway](assets/57.JPEG)

Após a construção da transação Stowaway, você poderá transmitir a transação para enviar aos nós da rede Bitcoin.

![Cahoots concluído, transmissão da transação PayJoin Stowaway](assets/58.JPEG)

A transação Stowaway foi transmitida. Parabéns.

Ao observar a transação, é possível ver as entradas e saídas dos dois usuários. A diferença entre a saída e a entrada do PayNym branco é de -45.000 sats, e a diferença para o PayNym laranja é de +45.000 sats, que é o valor que enviei.

![Estrutura da transação PayJoin Stowaway](assets/59.JPEG)

### Stonewall.

Stonewall é uma estrutura de transação específica que imita um CoinJoin entre duas pessoas, sem realmente ser um.

Essa transação não é colaborativa, envolve apenas as UTXOs pertencentes ao emissor da transação. Portanto, você pode criar uma transação Stonewall para qualquer ocasião, sem precisar concordar com ninguém.

Seu funcionamento é bastante simples: várias UTXOs pertencentes ao emissor serão colocadas como entrada e serão criadas 4 saídas. 2 dessas saídas terão exatamente o mesmo valor, as outras serão troco. Entre essas 2 saídas semelhantes, apenas uma irá para o destinatário do pagamento.

Essa estrutura adiciona uma grande quantidade de entropia à transação e confunde as pistas. Ao observá-la de fora, pode-se imaginar que essa transação é um CoinJoin entre duas pessoas. Na realidade, é um pagamento. Portanto, ela cria dúvidas na análise da cadeia.

Essa ferramenta Stonewall é usada por padrão no Samourai Wallet se sua carteira atender às condições necessárias para sua implementação. Vamos ver juntos como fazer um Stonewall. Para isso, estou enviando 50.125 sats usando essa ferramenta:
![vídeo](assets/60.mp4)
Como você pode ver neste vídeo, a opção Stonewall está pré-selecionada por padrão.

Aqui está como a transação Stonewall que acabei de fazer no vídeo se parece:

![Estrutura da transação Stonewall](assets/61.JPEG)

Podemos ver que o Samourai agregou 2 UTXOs pertencentes a mim como inputs:

- 130 450 S

- 454 504 S

E, podemos reconhecer os 4 outputs da transação Stonewall:

- 50 125 S que constituem o pagamento real que acabei de fazer.

- 50 125 S que retornam para outro endereço que me pertence.

- As duas mudanças: 80 168 S e 404 222 S que também retornam para mim.

Portanto, meu destinatário recebeu apenas 50 125 sats, que é o valor do pagamento que eu queria iniciar.

Obviamente, se você quiser gastar do pós-mix, você terá que ir primeiro para sua carteira Whirlpool antes de iniciar a transação.

O Samourai não cobra nenhuma taxa pela construção de uma transação Stonewall. Você terá que pagar as taxas de mineração da sua transação. Elas serão mais altas do que uma transação "normal" porque ela tem mais inputs e outputs.

Se você quiser usar essa ferramenta no Sparrow, eu recomendo este tutorial que explica em detalhes como realizar a operação: https://sparrowwallet.com/docs/spending-privately.html#paying-to-a-paynym

## StonewallX2.

StonewallX2 funciona exatamente como Stonewall, exceto que os inputs da transação não são apenas os do remetente, mas também os de uma terceira pessoa. StonewallX2 é, portanto, uma transação colaborativa entre dois usuários do Samourai. Assim como Stowaway (PayJoin), a comunicação entre os colaboradores pode ser feita manualmente (se você estiver no mesmo local) ou remotamente através do Soroban via Tor.

A diferença entre Stowaway e StonewallX2 está no papel do colaborador. No caso de Stowaway, o colaborador é necessariamente o destinatário do pagamento. No caso de StonewallX2, o colaborador apenas disponibiliza seus bitcoins para a mistura, mas ele não é o destinatário do pagamento.

Por exemplo, se você quiser fazer uma despesa de forma confidencial, mas o comerciante para quem você deseja enviar bitcoins não suporta Stowaway, então você pode simplesmente fazer um StonewallX2 com outra pessoa que não tem nada a ver com a transação. O destinatário ainda será o comerciante, mas ele não precisa realizar todas as operações relacionadas ao Stowaway.
Assim, StonewallX2 é um mini CoinJoin entre 2 pessoas que inclui uma saída de gasto. Isso adiciona uma grande quantidade de entropia à transação. Essa estrutura específica adiciona dúvida estatística sobre as conexões entre o remetente e o destinatário.
Se olharmos uma transação StonewallX2 de fora, sua estrutura será exatamente a mesma que uma transação Stonewall. Isso adiciona ainda mais dúvidas.

Para realizar uma transação StonewallX2 remotamente, você precisará estar conectado com o PayNym do seu colaborador, da mesma forma que para o stowaway. Uma vez conectado com o colaborador, vamos ver juntos como fazer uma transação StonewallX2 remotamente. Neste exemplo, estou colaborando com meu segundo PayNym na Sparrow Wallet. Não mostro isso no vídeo, mas o colaborador do Cahoot deve confirmar em sua carteira que deseja participar da transação conjunta.

![vídeo](assets/62.mp4)

Aqui está como se parece a transação StonewallX2 que acabei de fazer no vídeo:

![Estrutura da transação colaborativa Bitcoin StonewallX2](assets/63.JPEG)

A primeira entrada de 102.588 S vem da minha carteira Samourai. A segunda entrada de 104.255 S vem da carteira do meu colaborador. Podemos observar 4 saídas, incluindo 2 com o mesmo valor para confundir os rastros:

- 50.125 sats que vão para o destinatário do meu pagamento.

- 52.306 sats que representam o meu troco e, portanto, voltam para um endereço da minha carteira.

- 50.125 sats que voltam para o meu colaborador.

- 53.973 sats que voltam para o meu colaborador.

Para as transações StonewallX2, as taxas de mineração são compartilhadas entre os dois colaboradores. Se calculamos o saldo de cada um após a transação, temos então:

- O colaborador entrou com 104.255 sats e saiu com 104.098 sats. A diferença representa a sua parte das taxas de mineração. Se negligenciarmos essas taxas, o colaborador realmente realizou uma ação em branco.

- Para o remetente, entrei com 102.588 sats e saí com 52.306 sats. A diferença de 50.282 sats representa o valor que devo ao destinatário (50.125 sats) mais a minha parte das taxas de mineração.

- O destinatário não entrou na transação e sai com 50.125 sats, que é o valor que desejo pagar a ele.

A Samourai não cobra nenhuma taxa pela construção de uma transação StonewallX2. Você obviamente terá que pagar as taxas de mineração da sua transação. Elas serão mais altas do que uma transação "clássica", pois ela tem mais entradas e saídas.
'Se você quiser usar essa ferramenta no Sparrow, eu recomendo este tutorial que explica em detalhes como realizar a operação: https://sparrowwallet.com/docs/spending-privately.html#paying-to-a-paynym

## Ricochet.

A última ferramenta que eu gostaria de apresentar é o Ricochet. Essa ferramenta é um pouco diferente das anteriores, que tinham como objetivo aumentar a privacidade prospectiva. Esta permite reduzir o rastro deixado por uma CoinJoin em uma UTXO, e assim aumentar a privacidade retrospectiva.

Se você realizar transações como a CoinJoin e enviar seus bitcoins misturados diretamente para uma exchange, é possível que o provedor bloqueie sua conta ou solicite justificativas sobre a origem dos seus fundos. Para evitar esses bloqueios hipócritas e injustos, você pode usar o Ricochet para enviar seus fundos misturados para uma exchange.

Portanto, o único caso de uso do Ricochet é quando você deseja ocultar o fato de ter realizado uma CoinJoin no passado em uma UTXO que lhe pertence.

Para reduzir esse rastro, o Ricochet realizará 4 transações em que você enviará os fundos para si mesmo em endereços diferentes, e então a ferramenta enviará os fundos para o seu destino final (a exchange). O objetivo é adicionar distância entre a transação CoinJoin e a transação de depósito. Com isso, as ferramentas de análise de blockchain pensarão que houve uma mudança de proprietário desde a CoinJoin, e portanto o provedor provavelmente não arriscará bloquear sua conta ou solicitar justificativas.

Essa ferramenta pode ser essencial se você precisar trocar bitcoins misturados, ou simplesmente se quiser reduzir o "rastro" da sua mistura passada.

Como vimos anteriormente, a conta Ricochet usada para os endereços de rebote é completamente separada da conta de depósito.

Existem duas opções para o Ricochet:

- Ricochet reforçado: também chamado de "entrega escalonada", essa opção distribuirá as taxas pagas à Samourai nas cinco transações de rebote. Ela também garantirá que cada rebote esteja presente em um bloco diferente. Essa opção é projetada para ser lenta, mas permite otimizar a privacidade e a resistência às análises de blockchain da sua operação.

- Ricochet normal: essa opção permite realizar a operação rapidamente, mas será menos confidencial e resistente às análises do que a opção anterior. É recomendada para envios urgentes.

O Ricochet é um serviço pago. Você precisará pagar uma taxa de 100.000 sats para a Samourai.

Veja como realizar um Ricochet na Samourai Wallet:

![video](assets/64.mp4)'

Vous está agora pronto para usar o Whirlpool da melhor maneira possível e gastar seus postmix adequadamente. As ferramentas de gastos da Samourai Wallet, também incluídas na Sparrow Wallet na maioria das vezes, não têm mais segredos para você. Eu recomendo que você pratique e experimente todas essas ferramentas. Para não arriscar seus fundos pessoais, não hesite em usá-los primeiro no Testnet! Esta rede não é apenas para desenvolvedores.

# É errado misturar bitcoins?

Muitas vezes, encontramos em discursos de altcoiners ou iniciantes uma descrição do CoinJoin como uma prática obscura, duvidosa ou até perigosa. Esse tipo de narrativa nebulosa geralmente é devido a um desconhecimento técnico do Bitcoin e a um fantasma do CoinJoin.

Tudo isso é obviamente falso. O CoinJoin é um uso nobre do Bitcoin que permite a qualquer indivíduo retomar o controle da privacidade de seus pagamentos, ao mesmo tempo em que melhora a fungibilidade externa da rede de pagamento, sem cair em um anonimato absoluto.

Como explicado anteriormente, o CoinJoin simplesmente permite que um usuário corte o histórico de seus bitcoins e, assim, aumente a privacidade de seus pagamentos, especialmente se sua identidade tiver sido associada a uma UTXO no passado.

É graças a essas ferramentas que permitem que cada usuário proteja sua privacidade que podemos alcançar uma rede de pagamento livre e sem restrições. Sem respeito à privacidade, não há liberdade.

Trabalhar para respeitar a privacidade dos usuários de Bitcoin é uma causa nobre. Quando você realiza um CoinJoin, não apenas garante certa privacidade pessoal, mas também ajuda muitos outros indivíduos a melhorar a deles.

Sim, o CoinJoin às vezes é usado por pessoas desonestas. Mas também é amplamente utilizado por pessoas sujeitas, para quem a necessidade de privacidade não é um conforto, mas uma obrigação. Se todos usassem o CoinJoin apenas quando se tornasse obrigatório individualmente, as pessoas realmente obrigadas a usar essa ferramenta seriam misturadas apenas com pessoas desonestas e, portanto, seriam detectáveis mais facilmente por uma autoridade tirânica.

Também retomo o argumento de Gregory Maxwell, exposto no Bitcoin Talk em 2013 durante sua introdução do CoinJoin: "Na realidade, os verdadeiros criminosos não precisam do CoinJoin, [...] eles podem se dar ao luxo de comprar privacidade de uma maneira que os usuários regulares não podem, é apenas um custo adicional para o negócio deles (geralmente muito lucrativo)."

Em qualquer caso, lembremos que o CoinJoin é uma ferramenta. Como qualquer ferramenta, pode ser usada de forma construtiva ou destrutiva.
Enfim, na minha opinião, o CoinJoin se encaixa perfeitamente na ideologia e na linha de desenvolvimento inicial do Bitcoin. Os Cypherpunks escrevem código. Eles desenvolvem ferramentas que permitem a cada indivíduo ter controle sobre sua privacidade e soberania na internet, duas características essenciais para garantir a liberdade individual.

O próprio Satoshi Nakamoto dedica uma parte inteira de seu White Paper ao respeito à privacidade do usuário do Bitcoin. Neste documento, ele destaca o risco de perda de privacidade se o proprietário de um par de chaves for revelado. Ele explica que, se isso acontecer, todas as transações do proprietário poderão ser rastreadas. O CoinJoin é atualmente a melhor solução para quebrar essa ligação entre bitcoins e proprietários, descrita por Satoshi Nakamoto no White Paper.

Para concluir, recomendo que você estude os diferentes conteúdos que apresento na seção "Recursos externos" abaixo, nos quais me baseei para produzir este artigo, e que certamente lhe fornecerão ainda mais conhecimento.

## Para saber mais:

- [Tudo sobre a Passphrase Bitcoin.](https://www.pandul.fr/post/tout-savoir-sur-la-passphrase-bitcoin)

- [Como gerar sua própria frase mnemônica Bitcoin?](https://www.pandul.fr/post/comment-g%C3%A9n%C3%A9rer-soi-m%C3%AAme-sa-phrase-mn%C3%A9monique-bitcoin)

- [O que é PayNym e BIP47?](https://www.pandul.fr/post/qu-est-ce-que-paynym-et-bip47)

## Recursos externos:

Thread Twitter Why we CoinJoin de @SamouraiWallet:

https://twitter.com/SamouraiWallet/status/1489220847336308739

Artigo HOW TO WHIRLPOOL ON DESKTOP WITH RONINDOJO de ECONOALCHEMIST em https://bitcoinmagazine.com/:

https://bitcoinmagazine.com/guides/how-to-whirlpool-with-ronindojo

Artigo THE EASIEST WAY TO WHIRLPOOL YOUR BITCOIN AND PRESERVE PRIVACY de ECONOALCHEMIST em https://bitcoinmagazine.com/:

https://bitcoinmagazine.com/guides/how-to-whirlpool-bitcoin-on-mobile

Artigo HOW TO WHIRLPOOL YOUR BITCOIN ON DESKTOP WITH SPARROW WALLET de ECONOALCHEMIST em https://bitcoinmagazine.com/:

https://bitcoinmagazine.com/technical/how-to-whirlpool-bitcoin-sparrow-wallet

Artigo Diving head first into Whirlpool Anonymity Sets. De Samourai Wallet.

https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7

Thread Twitter de @BrotherRabbit/\_ sobre o score prospectivo no Whirlpool:

https://twitter.com/BrotherRabbit_/status/1528399310227906561

Tutorial Samouraï por JohnOnChain (Privacidade), do canal Youtube Découvre Bitcoin:

https://www.youtube.com/watch?v=kS6iC_ovarQ
Recursos sobre Ricochet:
https://docs.samourai.io/en/wallet/features/ricochet

Recursos sobre ferramentas de gastos no Sparrow Wallet:
https://sparrowwallet.com/docs/spending-privately.html#paying-to-a-paynym

Recursos sobre ferramentas de gastos no Samourai Wallet:
https://docs.samourai.io/en/spend-tools#ricochet

Artigo sobre a instalação e uso do WST (em espanhol):
https://estudiobitcoin.com/como-instalar-y-utilizar-whirlpool-stats-tools-wst-para-los-calculos-de-los-sets-de-anonimato-de-las-transacciones-coinjoins/

Artigo "Dealing with Coinjoin Change Outputs" do BitcoinQ+A em https://bitcoiner.guide/:
https://bitcoiner.guide/doxxic/

Série de 4 artigos "Understanding Bitcoin Privacy with OXT" por Samourai Wallet:
https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-4-4-16cc0a8759d5

Recursos sobre Whirlpool por Samourai Wallet:
https://code.samourai.io/whirlpool/Whirlpool/-/blob/whirlpool/README.md

https://docs.samourai.io/whirlpool/basic-concepts

https://docs.samourai.io/en/wallet/features/whirlpool

> **Este artigo foi escrito por Loïc Morel, em seu site de consultoria Pandul; https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin**
