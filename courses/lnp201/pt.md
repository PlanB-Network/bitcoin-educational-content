---
name: Introdução Teórica à Lightning Network
goal: Descobrir a Lightning Network de uma perspectiva técnica
objectives:
  - Entender o funcionamento dos canais da rede.
  - Familiarizar-se com os termos HTLC, LNURL e UTXO.
  - Assimilar a gestão de liquidez e as taxas da LNN.
  - Reconhecer a Lightning Network como uma rede.
  - Entender os usos teóricos da Lightning Network.
---

# Uma Jornada para a Segunda Camada do Bitcoin

Mergulhe no coração da Lightning Network, um sistema essencial para o futuro das transações de Bitcoin. LNP201 é um curso teórico sobre o funcionamento técnico da Lightning. Ele revela as fundações e mecanismos desta rede de segunda camada, projetada para tornar os pagamentos em Bitcoin rápidos, econômicos e escaláveis.

Graças à sua rede de canais de pagamento, a Lightning possibilita transações rápidas e seguras sem registrar cada troca na blockchain do Bitcoin. Ao longo dos capítulos, você aprenderá como a abertura, gestão e fechamento de canais funcionam, como os pagamentos são roteados através de nós intermediários de forma segura minimizando a necessidade de confiança, e como gerenciar a liquidez. Você descobrirá o que são transações de compromisso, HTLCs, chaves de revogação, mecanismos de punição, roteamento onion e faturas.

Seja você um iniciante em Bitcoin ou um usuário mais experiente, este curso fornecerá informações valiosas para entender e usar a Lightning Network. Embora vamos cobrir alguns fundamentos do funcionamento do Bitcoin nas primeiras partes, é essencial dominar os básicos da invenção de Satoshi antes de mergulhar no LNP201.

Aproveite sua descoberta!

+++

# Os Fundamentos

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Entendendo a Lightning Network

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

![Entendendo a Lightning Network](https://youtu.be/PszWk046x-I)

Bem-vindo ao curso LNP201, que visa explicar o funcionamento técnico da Lightning Network.

A Lightning Network é uma rede de canais de pagamento construída sobre o protocolo do Bitcoin, com o objetivo de possibilitar transações rápidas e de baixo custo. Ela permite a criação de canais de pagamento entre participantes, dentro dos quais transações podem ser realizadas quase instantaneamente e com taxas mínimas, sem a necessidade de registrar cada transação individualmente na blockchain. Assim, a Lightning Network busca melhorar a escalabilidade do Bitcoin e torná-lo utilizável para pagamentos de baixo valor.

Antes de explorar o aspecto "rede", é importante entender o conceito de um **canal de pagamento** na Lightning, como ele funciona e suas especificidades. Este é o assunto deste primeiro capítulo.

### O Conceito de Canal de Pagamento

Um canal de pagamento permite que duas partes, aqui **Alice** e **Bob**, troquem fundos pela Lightning Network. Cada protagonista tem um nó, simbolizado por um círculo, e o canal entre eles é representado por um segmento de linha.

![LNP201](assets/en/01.webp)

No nosso exemplo, Alice tem 100.000 satoshis do lado dela do canal, e Bob tem 30.000, totalizando 130.000 satoshis, o que constitui a **capacidade do canal**.

**Mas o que é um satoshi?**

O **satoshi** (ou "sat") é uma unidade de conta no Bitcoin. Semelhante a um centavo para o euro, um satoshi é simplesmente uma fração de Bitcoin. Um satoshi é igual a **0.00000001 Bitcoin**, ou um centésimo milionésimo de um Bitcoin. Usar o satoshi torna-se cada vez mais prático à medida que o valor do Bitcoin aumenta.

### A Alocação de Fundos no Canal

Vamos retornar ao canal de pagamento. O conceito chave aqui é o "**lado do canal**". Cada participante tem fundos no seu lado do canal: Alice 100.000 satoshis e Bob 30.000. Como vimos, a soma desses fundos representa a capacidade total do canal, um valor estabelecido quando ele é aberto.

![LNP201](assets/en/02.webp)

Vamos pegar um exemplo de uma transação Lightning. Se Alice quer enviar 40.000 satoshis para Bob, isso é possível porque ela tem fundos suficientes (100.000 satoshis). Após essa transação, Alice terá 60.000 satoshis do seu lado e Bob 70.000.

![LNP201](assets/en/03.webp)

A **capacidade do canal**, em 130.000 satoshis, permanece constante. O que muda é a alocação dos fundos. Esse sistema não permite enviar mais fundos do que se possui. Por exemplo, se Bob quisesse enviar de volta 80.000 satoshis para Alice, ele não poderia, porque ele só tem 70.000.

Outra maneira de imaginar a alocação de fundos é pensar em um **deslizante** que indica onde os fundos estão no canal. Inicialmente, com 100.000 satoshis para Alice e 30.000 para Bob, o deslizante está logicamente do lado de Alice. Após a transação de 40.000 satoshis, o deslizante moverá ligeiramente para o lado de Bob, que agora tem 70.000 satoshis.

![LNP201](assets/en/04.webp)

Essa representação pode ser útil para imaginar o equilíbrio dos fundos em um canal.

### As Regras Fundamentais de um Canal de Pagamento

O primeiro ponto a lembrar é que a **capacidade do canal** é fixa. É um pouco como o diâmetro de um cano: determina a quantidade máxima de fundos que podem ser enviados através do canal de uma só vez.
Vamos pegar um exemplo: se Alice tem 130.000 satoshis do seu lado, ela só pode enviar no máximo 130.000 satoshis para Bob em uma única transação. No entanto, Bob pode então enviar esses fundos de volta para Alice, parcial ou totalmente.

O que é importante entender é que a capacidade fixa do canal limita a quantidade máxima de uma única transação, mas não o número total de transações possíveis, nem o volume geral de fundos trocados dentro do canal.

**O que você deve reter deste capítulo?**

- A capacidade de um canal é fixa e determina a quantidade máxima que pode ser enviada em uma única transação.
- Os fundos em um canal são distribuídos entre os dois participantes, e cada um só pode enviar para o outro os fundos que possuem do seu lado.
- A Lightning Network permite, assim, a troca rápida e eficiente de fundos, respeitando as limitações impostas pela capacidade dos canais.

Este é o fim deste primeiro capítulo, onde estabelecemos as bases para a Lightning Network. Nos próximos capítulos, veremos como abrir um canal e aprofundar nos conceitos discutidos aqui.

## Bitcoin, Endereços, UTXO e Transações

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

![bitcoin, endereços, utxo e transações](https://youtu.be/cadCJ2V7zTg)
Este capítulo é um pouco especial, pois não será dedicado diretamente ao Lightning, mas ao Bitcoin. De fato, a Lightning Network é uma camada sobre o Bitcoin. Portanto, é essencial entender certos conceitos fundamentais do Bitcoin para compreender adequadamente o funcionamento do Lightning nos capítulos subsequentes. Neste capítulo, revisaremos os conceitos básicos de endereços de recebimento do Bitcoin, UTXOs, bem como o funcionamento das transações Bitcoin.

### Endereços Bitcoin, Chaves Privadas e Chaves Públicas

Um endereço Bitcoin é uma série de caracteres derivados de uma **chave pública**, que por sua vez é calculada a partir de uma **chave privada**. Como você certamente sabe, ele é usado para bloquear bitcoins, o que equivale a recebê-los em nossa carteira.

A chave privada é um elemento secreto que **nunca deve ser compartilhado**, enquanto a chave pública e o endereço podem ser compartilhados sem risco de segurança (a divulgação deles representa apenas um risco para sua privacidade). Aqui está uma representação comum que adotaremos ao longo deste treinamento:

- As **chaves privadas** serão representadas **verticalmente**.
- As **chaves públicas** serão representadas **horizontalmente**.
- Sua cor indica quem as possui (Alice em laranja e Bob em preto...).

### Transações Bitcoin: Enviando Fundos e Scripts

No Bitcoin, uma transação envolve enviar fundos de um endereço para outro. Vamos tomar o exemplo de Alice enviando 0,002 Bitcoin para Bob. Alice usa a chave privada associada ao seu endereço para **assinar** a transação, provando assim que ela realmente pode gastar esses fundos. Mas o que exatamente acontece por trás dessa transação? Os fundos em um endereço Bitcoin são bloqueados por um **script**, uma espécie de mini-programa que impõe certas condições para gastar os fundos.

O script mais comum exige uma assinatura com a chave privada associada ao endereço. Quando Alice assina uma transação com sua chave privada, ela **desbloqueia o script** que bloqueia os fundos, e eles podem então ser transferidos. A transferência de fundos envolve adicionar um novo script a esses fundos, estipulando que, para gastá-los desta vez, será necessária a assinatura da chave privada de **Bob**.

![LNP201](assets/en/05.webp)

### UTXOs: Saídas de Transação Não Gastas

No Bitcoin, o que realmente trocamos não são diretamente bitcoins, mas **UTXOs** (_Unspent Transaction Outputs_), significando "saídas de transação não gastas".

Um UTXO é um pedaço de bitcoin que pode ser de qualquer valor, por exemplo, **2.000 bitcoins**, **8 bitcoins**, ou até mesmo **8.000 sats**. Cada UTXO é bloqueado por um script, e para gastá-lo, deve-se satisfazer as condições do script, muitas vezes uma assinatura com a chave privada correspondente a um determinado endereço de recebimento.

Os UTXOs não podem ser divididos. Cada vez que são usados para gastar a quantidade em bitcoins que representam, deve ser feito em sua totalidade. É um pouco como uma nota de banco: se você tem uma nota de €10 e deve ao padeiro €5, você não pode simplesmente cortar a nota ao meio. Você tem que dar a ele a nota de €10, e ele lhe dará €5 de troco. Este é exatamente o mesmo princípio para UTXOs no Bitcoin! Por exemplo, quando Alice desbloqueia um script com sua chave privada, ela desbloqueia o UTXO inteiro. Se ela deseja enviar apenas uma parte dos fundos representados por este UTXO para Bob, ela pode "fragmentá-lo" em vários menores. Ela então enviará 0,0015 BTC para Bob e enviará o restante, 0,0005 BTC, para um **endereço de troco**.

Aqui está um exemplo de uma transação com 2 saídas:

- Um UTXO de 0.0015 BTC para Bob, bloqueado por um script que requer a assinatura da chave privada de Bob.
- Um UTXO de 0.0005 BTC para Alice, bloqueado por um script que requer sua própria assinatura.

![LNP201](assets/en/06.webp)

### Endereços Multi-assinatura

Além de endereços simples gerados a partir de uma única chave pública, é possível criar **endereços multi-assinatura** a partir de múltiplas chaves públicas. Um caso particularmente interessante para a Lightning Network é o **endereço multi-assinatura 2/2**, gerado a partir de duas chaves públicas:

![LNP201](assets/en/07.webp)

Para gastar os fundos bloqueados com este endereço multi-assinatura 2/2, é necessário assinar com as duas chaves privadas associadas às chaves públicas.

![LNP201](assets/en/08.webp)

Este tipo de endereço é precisamente a representação na blockchain do Bitcoin dos canais de pagamento na Lightning Network.

**O que você deve reter deste capítulo?**

- Um **endereço Bitcoin** é derivado de uma chave pública, que por sua vez é derivada de uma chave privada.
- Os fundos no Bitcoin são bloqueados por **scripts**, e para gastar esses fundos, deve-se satisfazer o script, o que geralmente envolve fornecer uma assinatura com a chave privada correspondente.
- **UTXOs** são pedaços de bitcoins bloqueados por scripts, e cada transação no Bitcoin consiste em desbloquear um UTXO e, em seguida, criar um ou mais novos em troca.
- **Endereços multi-assinatura 2/2** requerem a assinatura de duas chaves privadas para gastar os fundos. Esses endereços específicos são usados no contexto da Lightning para criar canais de pagamento.

Este capítulo sobre o Bitcoin nos permitiu revisar algumas noções essenciais para o que segue. No próximo capítulo, descobriremos especificamente como funciona a abertura de canais na Lightning Network.

# Abertura e Fechamento de Canais

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Abertura de Canal

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

![open a channel](https://youtu.be/B2caBC0Rxko)

Neste capítulo, veremos mais precisamente como abrir um canal de pagamento na Lightning Network e entender a ligação entre esta operação e o sistema Bitcoin subjacente.

### Canais Lightning

Como vimos no primeiro capítulo, um **canal de pagamento** na Lightning pode ser comparado a um "tubo" para troca de fundos entre dois participantes (**Alice** e **Bob** em nossos exemplos). A capacidade deste canal corresponde à soma dos fundos disponíveis de cada lado. Em nosso exemplo, Alice tem **100.000 satoshis** e Bob tem **30.000 satoshis**, resultando em uma **capacidade total** de **130.000 satoshis**.

![LNP201](assets/en/09.webp)

### Níveis de Troca de Informações

É crucial distinguir claramente os diferentes níveis de troca na Lightning Network:

- **Comunicações peer-to-peer (protocolo Lightning)**: São as mensagens que os nós da Lightning enviam uns aos outros para se comunicar. Representaremos essas mensagens com linhas tracejadas pretas em nossos diagramas.
- **Canais de pagamento (protocolo Lightning)**: São os caminhos para troca de fundos na Lightning, que representaremos com linhas pretas sólidas.
- **Transações Bitcoin (protocolo Bitcoin)**: São as transações feitas onchain, que representaremos com linhas laranjas.

![LNP201](assets/en/10.webp)
Vale ressaltar que um nó Lightning pode se comunicar via protocolo P2P sem abrir um canal, mas para trocar fundos, um canal é necessário.

### Passos para Abrir um Canal Lightning

1. **Troca de mensagens**: Alice quer abrir um canal com Bob. Ela lhe envia uma mensagem contendo a quantidade que deseja depositar no canal (130.000 sats) e sua chave pública. Bob responde compartilhando sua própria chave pública.

![LNP201](assets/en/11.webp)

2. **Criação do endereço de multisignatura**: Com essas duas chaves públicas, Alice cria um **endereço de multisignatura 2/2**, significando que os fundos que serão posteriormente depositados neste endereço exigirão ambas as assinaturas (Alice e Bob) para serem gastos.

![LNP201](assets/en/12.webp)

3. **Transação de depósito**: Alice prepara uma transação Bitcoin para depositar fundos neste endereço de multisignatura. Por exemplo, ela pode decidir enviar **130.000 satoshis** para este endereço de multisignatura. Esta transação é **construída mas ainda não publicada** na blockchain.

![LNP201](assets/en/13.webp)

4. **Transação de retirada**: Antes de publicar a transação de depósito, Alice constrói uma transação de retirada para que ela possa recuperar seus fundos em caso de problema com Bob. De fato, uma vez que Alice publica a transação de depósito, seus sats ficarão bloqueados em um endereço de multisignatura 2/2 que requer ambas as suas assinaturas e a de Bob para ser desbloqueado. Alice se protege contra esse risco de perda construindo a transação de retirada que lhe permite recuperar seus fundos.

![LNP201](assets/en/14.webp)

5. **Assinatura de Bob**: Alice envia a transação de depósito para Bob como prova e pede que ele assine a transação de retirada. Uma vez obtida a assinatura de Bob na transação de retirada, Alice tem a certeza de poder recuperar seus fundos a qualquer momento, pois agora apenas sua própria assinatura é necessária para desbloquear a multisignatura.

![LNP201](assets/en/15.webp)

6. **Publicação da transação de depósito**: Uma vez obtida a assinatura de Bob, Alice pode publicar a transação de depósito na blockchain do Bitcoin, abrindo oficialmente o canal Lightning entre os dois usuários.

![LNP201](assets/en/16.webp)

### Quando o canal está aberto?

O canal é considerado aberto uma vez que a transação de depósito é incluída em um bloco Bitcoin e alcança uma certa profundidade de confirmações (número de blocos subsequentes).

**O que você deve lembrar deste capítulo?**

- A abertura de um canal começa com a troca de **mensagens** entre as duas partes (troca de quantias e chaves públicas).
- Um canal é formado pela criação de um **endereço de multisignatura 2/2** e depositando fundos nele via uma transação Bitcoin.
- A pessoa que abre o canal garante que pode **recuperar seus fundos** através de uma transação de retirada assinada pela outra parte antes de publicar a transação de depósito.

No próximo capítulo, exploraremos o funcionamento técnico de uma transação Lightning dentro de um canal.

## Transação de Compromisso

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![Transação Lightning & transação de compromisso](https://youtu.be/aPqI34tpypM)

Neste capítulo, descobriremos o funcionamento técnico de uma transação dentro de um canal na Rede Lightning, ou seja, quando fundos são movidos de um lado do canal para o outro.

### Lembrete do ciclo de vida do canal

Como visto anteriormente, um canal Lightning começa com uma **abertura** por meio de uma transação Bitcoin. O canal pode ser **fechado** a qualquer momento, também via uma transação Bitcoin. Entre esses dois momentos, um número quase infinito de transações pode ser realizado dentro do canal, sem passar pelo blockchain do Bitcoin. Vamos ver o que acontece durante uma transação no canal.
![LNP201](assets/en/17.webp)

### O estado inicial do canal

No momento da abertura do canal, Alice depositou **130.000 satoshis** no endereço de multisignatura do canal. Assim, no estado inicial, todos os fundos estão do lado de Alice. Antes de abrir o canal, Alice também fez Bob assinar uma **transação de retirada**, que permitiria a ela recuperar seus fundos caso desejasse fechar o canal.

![LNP201](assets/en/18.webp)

### Transações Não Publicadas: As Transações de Compromisso

Quando Alice faz uma transação no canal para enviar fundos para Bob, uma nova transação Bitcoin é criada para refletir essa mudança na distribuição de fundos. Esta transação, chamada de **transação de compromisso**, não é publicada no blockchain, mas representa o novo estado do canal após a transação Lightning.

Vamos tomar um exemplo com Alice enviando 30.000 satoshis para Bob:

- **Inicialmente**: Alice tem 130.000 satoshis.
- **Após a transação**: Alice tem 100.000 satoshis, e Bob 30.000 satoshis.
  Para validar essa transferência, Alice e Bob criam uma nova **transação Bitcoin não publicada** que enviaria **100.000 satoshis para Alice** e **30.000 satoshis para Bob** a partir do endereço de multisignatura. Ambas as partes constroem essa transação independentemente, mas com os mesmos dados (quantias e endereços). Uma vez construída, cada uma assina a transação e troca sua assinatura com a outra. Isso permite que qualquer uma das partes publique a transação a qualquer momento, se necessário, para recuperar sua parte do canal no blockchain principal do Bitcoin.
  ![LNP201](assets/en/19.webp)

### Processo de Transferência: A Fatura

Quando Bob quer receber fundos, ele envia a Alice uma **_fatura_** de 30.000 satoshis. Alice então procede ao pagamento desta fatura, iniciando a transferência dentro do canal. Como vimos, esse processo depende da criação e assinatura de uma nova **transação de compromisso**.

Cada transação de compromisso representa a nova distribuição de fundos no canal após a transferência. Neste exemplo, após a transação, Bob tem 30.000 satoshis e Alice tem 100.000 satoshis. Se qualquer um dos dois participantes decidisse publicar essa transação de compromisso no blockchain, isso resultaria no fechamento do canal e os fundos seriam distribuídos de acordo com essa última distribuição.

![LNP201](assets/en/20.webp)

### Novo Estado Após uma Segunda Transação

Vamos tomar outro exemplo: após a primeira transação onde Alice enviou 30.000 satoshis para Bob, Bob decide enviar **10.000 satoshis de volta para Alice**. Isso cria um novo estado do canal. A nova **transação de compromisso** representará essa distribuição atualizada:

- **Alice** agora tem **110.000 satoshis**.
- **Bob** tem **20.000 satoshis**.

![LNP201](assets/en/21.webp)

Novamente, essa transação não é publicada no blockchain, mas pode ser a qualquer momento, caso o canal seja fechado.

Em resumo, quando fundos são transferidos dentro de um canal Lightning:

- Alice e Bob criam uma nova **transação de compromisso**, que reflete a nova distribuição de fundos. - Esta transação Bitcoin é **assinada** por ambas as partes, mas **não publicada** na blockchain do Bitcoin enquanto o canal permanecer aberto.
- As transações de compromisso garantem que cada participante possa recuperar seus fundos a qualquer momento na blockchain do Bitcoin, publicando a última transação assinada.

No entanto, este sistema tem uma falha potencial, que abordaremos no próximo capítulo. Veremos como cada participante pode se proteger contra uma tentativa de trapaça por parte da outra parte.

## Chave de Revogação

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>
![transações parte 2](https://youtu.be/RRvoVTLRJ84)
Neste capítulo, vamos aprofundar em como as transações funcionam na Lightning Network, discutindo os mecanismos em vigor para proteger contra trapaças, garantindo que cada parte adira às regras dentro de um canal.

### Lembrete: Transações de Compromisso

Como visto anteriormente, as transações na Lightning dependem de **transações de compromisso** não publicadas. Essas transações refletem a distribuição atual de fundos no canal. Quando uma nova transação Lightning é feita, uma nova transação de compromisso é criada e assinada por ambas as partes para refletir o novo estado do canal.

Vamos tomar um exemplo simples:

- **Estado inicial**: Alice tem **100.000 satoshis**, Bob **30.000 satoshis**.
- Após uma transação onde Alice envia **40.000 satoshis** para Bob, a nova transação de compromisso distribui os fundos da seguinte forma:
  - Alice: **60.000 satoshis**
  - Bob: **70.000 satoshis**

![LNP201](assets/en/22.webp)

A qualquer momento, ambas as partes podem publicar a **última transação de compromisso** assinada para fechar o canal e recuperar seus fundos.

### O Problema: Trapacear Publicando uma Transação Antiga

Um problema potencial surge se uma das partes decidir **trapacear** publicando uma transação de compromisso antiga. Por exemplo, Alice poderia publicar uma transação de compromisso mais antiga onde ela tinha **100.000 satoshis**, mesmo que agora ela tenha apenas **60.000** na realidade. Isso permitiria que ela roubasse **40.000 satoshis** de Bob.

![LNP201](assets/en/23.webp)

Pior ainda, Alice poderia publicar a primeira transação de retirada, aquela antes de o canal ser aberto, onde ela tinha **130.000 satoshis**, e assim roubar todos os fundos do canal.

![LNP201](assets/en/24.webp)

### Solução: Chave de Revogação e Timelock

Para prevenir esse tipo de trapaça por Alice, na Lightning Network, **mecanismos de segurança** são adicionados às transações de compromisso:

1. **O timelock**: Cada transação de compromisso inclui um timelock para os fundos de Alice. O timelock é um primitivo de contrato inteligente que estabelece uma condição de tempo que deve ser cumprida para que uma transação seja adicionada a um bloco. Isso significa que Alice não pode recuperar seus fundos até que um certo número de blocos tenha passado, caso ela publique uma das transações de compromisso. Este timelock começa a aplicar-se a partir da confirmação da transação de compromisso. Sua duração é geralmente proporcional ao tamanho do canal, mas também pode ser configurada manualmente.
2. **Chave de Revogação**: Os fundos de Alice também podem ser imediatamente gastos por Bob se ele possuir a **chave de revogação**. Esta chave consiste em um segredo mantido por Alice e um segredo mantido por Bob. Note que este segredo é diferente para cada transação de compromisso.
   Graças a esses 2 mecanismos combinados, Bob tem tempo para detectar a tentativa de Alice de enganá-lo e puni-la recuperando seu output com a chave de revogação, o que para Bob significa recuperar todos os fundos do canal. Nossa nova transação de compromisso agora terá esta aparência:
   ![LNP201](assets/en/25.webp)

Vamos detalhar o funcionamento desse mecanismo juntos.

### Processo de Atualização da Transação

Quando Alice e Bob atualizam o estado do canal com uma nova transação Lightning, eles trocam antecipadamente seus respectivos **segredos** para a transação de compromisso anterior (aquela que se tornará obsoleta e poderia permitir que um deles enganasse o outro). Isso significa que, no novo estado do canal:

- Alice e Bob têm uma nova transação de compromisso representando a distribuição atual de fundos após a transação Lightning.
- Cada um tem o segredo do outro para a transação anterior, o que lhes permite usar a chave de revogação apenas se um deles tentar enganar publicando uma transação com um estado antigo nos mempools dos nós Bitcoin. De fato, para punir a outra parte, é necessário ter ambos os segredos e a transação de compromisso do outro, que inclui a entrada assinada. Sem esta transação, a chave de revogação por si só é inútil. A única maneira de obter esta transação é recuperá-la dos mempools (nas transações aguardando confirmação) ou nas transações confirmadas na blockchain durante o timelock, o que prova que a outra parte está tentando enganar, intencionalmente ou não.

Vamos tomar um exemplo para entender bem esse processo:

1. **Estado Inicial**: Alice tem **100.000 satoshis**, Bob **30.000 satoshis**.

![LNP201](assets/en/26.webp)

2. Bob quer receber 40.000 satoshis de Alice através do canal Lightning deles. Para fazer isso:
   - Ele envia a ela uma fatura junto com seu segredo para a chave de revogação de sua transação de compromisso anterior.
   - Em resposta, Alice fornece sua assinatura para a nova transação de compromisso de Bob, bem como seu segredo para a chave de revogação de sua transação anterior.
   - Finalmente, Bob envia sua assinatura para a nova transação de compromisso de Alice.
   - Essas trocas permitem que Alice envie **40.000 satoshis** para Bob no Lightning através do canal deles, e as novas transações de compromisso agora refletem essa nova distribuição de fundos.

![LNP201](assets/en/27.webp)

3. Se Alice tentar publicar a antiga transação de compromisso onde ela ainda possuía **100.000 satoshis**, Bob, tendo obtido a chave de revogação, pode imediatamente recuperar os fundos usando esta chave, enquanto Alice é bloqueada pelo timelock.

![LNP201](assets/en/28.webp)

Mesmo que, neste caso, Bob não tenha interesse econômico em tentar enganar, se ele o fizer mesmo assim, Alice também se beneficia de proteção simétrica oferecendo a ela as mesmas garantias.

**O que você deve levar deste capítulo?**

As **transações de compromisso** na Lightning Network incluem mecanismos de segurança que reduzem tanto o risco de trapaça quanto os incentivos para fazê-lo. Antes de assinar uma nova transação de compromisso, Alice e Bob trocam seus respectivos **segredos** para as transações de compromisso anteriores. Se Alice tentar publicar uma transação de compromisso antiga, Bob pode usar a **chave de revogação** para recuperar todos os fundos antes que Alice possa (porque ela está bloqueada pelo timelock), o que a pune por tentar enganar.

Este sistema de segurança garante que os participantes adiram às regras da Lightning Network, e eles não podem se beneficiar publicando transações de compromisso antigas.
Neste ponto do treinamento, você já sabe como os canais Lightning são abertos e como as transações dentro desses canais funcionam. No próximo capítulo, descobriremos as diferentes maneiras de fechar um canal e recuperar seus bitcoins na blockchain principal.

## Encerramento de Canal

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

![fechar um canal](https://youtu.be/FVmQvNpVW8Y)

Neste capítulo, discutiremos sobre **fechar um canal** na Rede Lightning, o que é feito através de uma transação Bitcoin, assim como a abertura de um canal. Após ver como as transações dentro de um canal funcionam, agora é hora de ver como fechar um canal e recuperar os fundos na blockchain do Bitcoin.

### Lembrete do ciclo de vida do canal

O **ciclo de vida de um canal** começa com sua **abertura**, via uma transação Bitcoin, depois são feitas transações Lightning dentro dele, e finalmente, quando as partes desejam recuperar seus fundos, o canal é **fechado** através de uma segunda transação Bitcoin. As transações intermediárias feitas na Lightning são representadas por **transações de compromisso** não publicadas.

![LNP201](assets/en/29.webp)

### Os três tipos de encerramento de canal

Existem três maneiras principais de fechar este canal, que podem ser chamadas de **o bom, o bruto e o traidor** (inspirado por Andreas Antonopoulos em _Dominando a Rede Lightning_):

1. **O Bom**: o **fechamento cooperativo**, onde Alice e Bob concordam em fechar o canal.
2. **O Bruto**: o **fechamento forçado**, onde uma das partes decide fechar o canal honestamente, mas sem o acordo da outra.
3. **O Traidor**: o **fechamento com trapaça**, onde uma das partes tenta roubar fundos publicando uma transação de compromisso antiga (qualquer uma, exceto a última, que reflete a distribuição justa e atual dos fundos).

Vamos tomar um exemplo:

- Alice possui **100.000 satoshis** e Bob **30.000 satoshis**.
- Esta distribuição é refletida em **2 transações de compromisso** (uma por usuário) que não são publicadas, mas poderiam ser no evento de fechamento do canal.

![LNP201](assets/en/30.webp)

### O Bom: o fechamento cooperativo

Em um **fechamento cooperativo**, Alice e Bob concordam em fechar o canal. Veja como isso acontece:

1. Alice envia uma mensagem para Bob através do protocolo de comunicação Lightning para propor o fechamento do canal.
2. Bob concorda, e as duas partes não fazem mais transações no canal.

![LNP201](assets/en/31.webp)

3. Alice e Bob negociam juntos as taxas da **transação de fechamento**. Essas taxas são geralmente calculadas com base no mercado de taxas Bitcoin no momento do fechamento. É importante notar que **é sempre a pessoa que abriu o canal** (Alice em nosso exemplo) que paga as taxas de fechamento.
4. Eles constroem uma nova **transação de fechamento**. Esta transação se assemelha a uma transação de compromisso, mas sem timelocks ou mecanismos de revogação, já que ambas as partes estão cooperando e não há risco de trapaça. Esta transação de fechamento cooperativo, portanto, difere das transações de compromisso.
   Por exemplo, se Alice possui **100.000 satoshis** e Bob **30.000 satoshis**, a transação de encerramento enviará **100.000 satoshis** para o endereço de Alice e **30.000 satoshis** para o endereço de Bob, sem restrições de timelock. Uma vez que esta transação seja assinada por ambas as partes, é publicada por Alice. Uma vez que a transação seja confirmada na blockchain do Bitcoin, o canal Lightning será oficialmente fechado.
   ![LNP201](assets/en/32.webp)

O **encerramento cooperativo** é o método preferido de fechamento porque é rápido (sem timelock) e as taxas de transação são ajustadas de acordo com as condições atuais do mercado Bitcoin. Isso evita pagar pouco, o que poderia arriscar bloquear a transação nos mempools, ou pagar demais desnecessariamente, o que leva a perdas financeiras desnecessárias para os participantes.

### O Ruim: o fechamento forçado

Quando o nó de Alice envia uma mensagem para o de Bob pedindo um encerramento cooperativo, se ele não responder (por exemplo, devido a uma queda de internet ou um problema técnico), Alice pode prosseguir com um **fechamento forçado** publicando a **última transação de compromisso assinada**.
Neste caso, Alice simplesmente publicará a última transação de compromisso, que reflete o estado do canal no momento em que a última transação Lightning ocorreu com a distribuição correta de fundos.

![LNP201](assets/en/33.webp)

Esta transação inclui um **timelock** para os fundos de Alice, tornando o fechamento mais lento.

![LNP201](assets/en/34.webp)

Além disso, as taxas da transação de compromisso podem ser inadequadas no momento do fechamento, pois foram definidas quando a transação foi criada, às vezes vários meses antes. Geralmente, os clientes Lightning superestimam as taxas para evitar problemas futuros, mas isso pode levar a taxas excessivas, ou inversamente muito baixas.

Em resumo, o **fechamento forçado** é uma opção de último recurso quando o par não responde mais. É mais lento e menos econômico do que um fechamento cooperativo. Portanto, deve ser evitado tanto quanto possível.

### A trapaça: trapacear

Finalmente, um fechamento com **trapaça** ocorre quando uma das partes tenta publicar uma transação de compromisso antiga, muitas vezes onde possuíam mais fundos do que deveriam. Por exemplo, Alice pode publicar uma transação antiga onde ela possuía **120.000 satoshis**, enquanto na realidade possui apenas **100.000** agora.

![LNP201](assets/en/35.webp)

Bob, para prevenir essa trapaça, monitora a blockchain do Bitcoin e seu mempool para garantir que Alice não publique uma transação antiga. Se Bob detectar uma tentativa de trapaça, ele pode usar a **chave de revogação** para recuperar os fundos de Alice e puni-la tomando todo o fundo do canal. Como Alice está bloqueada pelo timelock em sua saída, Bob tem tempo para gastá-lo sem um timelock do lado dele para recuperar a soma inteira em um endereço que ele possui.

![LNP201](assets/en/36.webp)

Obviamente, a trapaça pode potencialmente ter sucesso se Bob não agir dentro do tempo imposto pelo timelock na saída de Alice. Neste caso, a saída de Alice é desbloqueada, permitindo que ela a consuma para criar uma nova saída para um endereço que ela controla.

**O que você deve levar deste capítulo?**

Existem três maneiras de fechar um canal:

1. **Encerramento Cooperativo**: Rápido e menos caro, onde ambas as partes concordam em fechar o canal e publicar uma transação de encerramento sob medida.
2. **Fechamento Forçado**: Menos desejável, pois depende da publicação de uma transação de compromisso, com taxas potencialmente inadequadas e um timelock, o que retarda o fechamento.
3. **Trapaça**: Se uma das partes tentar roubar fundos publicando uma transação antiga, a outra pode usar a chave de revogação para punir essa trapaça.
   Nos próximos capítulos, exploraremos a Lightning Network de uma perspectiva mais ampla, focando em como sua rede opera.

# Uma Rede de Liquidez

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

![lightning network](https://youtu.be/RAZAa3v41DM)

Neste capítulo, exploraremos como os pagamentos na Lightning Network podem chegar a um destinatário mesmo que eles não estejam diretamente conectados por um canal de pagamento. A Lightning é, de fato, uma **rede de canais de pagamento**, que permite que fundos sejam enviados a um nó distante através dos canais de outros participantes. Descobriremos como os pagamentos são roteados pela rede, como a liquidez se move entre os canais e como as taxas de transação são calculadas.

### A Rede de Canais de Pagamento

Na Lightning Network, uma transação corresponde a uma transferência de fundos entre dois nós. Como visto em capítulos anteriores, é necessário abrir um canal com alguém para realizar transações Lightning. Este canal permite um número quase infinito de transações fora da cadeia antes de fechá-lo para reivindicar o saldo na cadeia. No entanto, este método tem a desvantagem de exigir um canal direto com a outra pessoa para receber ou enviar fundos, o que implica uma transação de abertura e uma transação de fechamento para cada canal. Se eu planejo fazer um grande número de pagamentos com essa pessoa, abrir e fechar um canal se torna custo-efetivo. Por outro lado, se eu só preciso realizar algumas transações Lightning, abrir um canal direto não é vantajoso, pois me custaria 2 transações na cadeia para um número limitado de transações fora da cadeia. Esse caso pode ocorrer, por exemplo, ao querer pagar com Lightning em um comerciante sem planejar retornar.

Para resolver esse problema, a Lightning Network permite rotear um pagamento através de vários canais e nós intermediários, possibilitando assim uma transação sem um canal direto com a outra pessoa.

Por exemplo, imagine que:

- **Alice** (em laranja) tem um canal com **Suzie** (em cinza) com **100.000 satoshis** do lado dela e **30.000 satoshis** do lado de Suzie.
- **Suzie** tem um canal com **Bob** no qual ela possui **250.000 satoshis** e onde Bob não tem satoshis.

![LNP201](assets/en/37.webp)

Se Alice quer enviar fundos para Bob sem abrir um canal direto com ele, ela terá que passar por Suzie, e cada canal precisará ajustar a liquidez de cada lado. **Os satoshis enviados permanecem dentro de seus respectivos canais**; eles não "cruzam" os canais de fato, mas a transferência é feita via um ajuste da liquidez interna em cada canal.

Suponha que Alice queira enviar **50.000 satoshis** para Bob:

1. **Alice** envia 50.000 satoshis para **Suzie** em seu canal comum.
2. **Suzie** replica essa transferência enviando 50.000 satoshis para **Bob** em seu canal.

![LNP201](assets/en/38.webp)
Assim, o pagamento é encaminhado para Bob através de um movimento de liquidez em cada canal. Ao final da operação, Alice fica com 50.000 sats. Ela realmente transferiu 50.000 sats, já que inicialmente tinha 100.000. Bob, por sua vez, acaba com 50.000 sats adicionais. Para Suzie (o nó intermediário), esta operação é neutra: inicialmente, ela tinha 30.000 sats em seu canal com Alice e 250.000 sats em seu canal com Bob, um total de 280.000 sats. Após a operação, ela possui 80.000 sats em seu canal com Alice e 200.000 sats em seu canal com Bob, que é a mesma soma que no início.
Esta transferência é, portanto, limitada pela **liquidez disponível** na direção da transferência.

### Cálculo da Rota e Limites de Liquidez

Vamos pegar um exemplo teórico de outra rede com:

- **130.000 satoshis** do lado de Alice (em laranja) em seu canal com **Suzie** (em cinza).
- **90.000 satoshis** do lado de **Suzie** e **200.000 satoshis** do lado de **Carol** (em rosa).
- **150.000 satoshis** do lado de **Carol** e **100.000 satoshis** do lado de **Bob**.

![LNP201](assets/en/39.webp)

O máximo que Alice pode enviar para Bob nesta configuração é **90.000 satoshis**, pois ela é limitada pela menor liquidez disponível no canal de **Suzie para Carol**. Na direção oposta (de Bob para Alice), nenhum pagamento é possível porque o lado de **Suzie** no canal com **Alice** não contém satoshis. Portanto, não há **nenhuma rota** utilizável para uma transferência nesta direção.
Alice envia **40.000 satoshis** para Bob através dos canais:

1. Alice transfere 40.000 satoshis para seu canal com Suzie.
2. Suzie transfere 40.000 satoshis para Carol em seu canal compartilhado.
3. Carol finalmente transfere 40.000 satoshis para Bob.

![LNP201](assets/en/40.webp)

Os **satoshis enviados** em cada canal **permanecem no canal**, então os satoshis enviados por Carol para Bob não são os mesmos que foram enviados por Alice para Suzie. A transferência é feita apenas ajustando a liquidez dentro de cada canal. Além disso, a capacidade total dos canais permanece inalterada.

![LNP201](assets/en/41.webp)

Como no exemplo anterior, após a transação, o nó de origem (Alice) tem 40.000 satoshis a menos. Os nós intermediários (Suzie e Carol) retêm o mesmo valor total, tornando a operação neutra para eles. Finalmente, o nó de destino (Bob) recebe 40.000 satoshis adicionais.

O papel dos nós intermediários é, portanto, muito importante no funcionamento da Lightning Network. Eles facilitam as transferências, oferecendo múltiplos caminhos para os pagamentos. Para incentivar esses nós a fornecerem sua liquidez e participarem do roteamento de pagamentos, **taxas de roteamento** são pagas a eles.

### Taxas de Roteamento

Os nós intermediários aplicam taxas para permitir que os pagamentos passem por seus canais. Essas taxas são definidas por **cada nó para cada canal**. As taxas consistem em 2 elementos:

1. "**Taxa base**": um valor fixo por canal, frequentemente **1 sat** por padrão, mas personalizável.
2. "**Taxa variável**": uma porcentagem do valor transferido, calculada em **partes por milhão (ppm)**. Por padrão, é **1 ppm** (1 sat por milhão de satoshis transferidos), mas também pode ser ajustada.
   As taxas também variam dependendo da direção da transferência. Por exemplo, para uma transferência de Alice para Suzie, aplicam-se as taxas de Alice. Inversamente, de Suzie para Alice, são utilizadas as taxas de Suzie.

Por exemplo, para um canal entre Alice e Suzie, poderíamos ter:

- **Alice**: taxa base de 1 sat e 1 ppm para taxas variáveis.
- **Suzie**: taxa base de 0,5 sat e 10 ppm para taxas variáveis.

![LNP201](assets/en/42.webp)

Para entender melhor como funcionam as taxas, vamos estudar a mesma Rede Lightning de antes, mas agora com as seguintes taxas de roteamento:

- Canal **Alice - Suzie**: taxa base de 1 satoshi e 1 ppm para Alice.
- Canal **Suzie - Carol**: taxa base de 0 satoshi e 200 ppm para Suzie.
- Canal **Carol - Bob**: taxa base de 1 satoshi e 1 ppm para Suzie 2.
  ![LNP201](assets/en/43.webp)

Para o mesmo pagamento de **40.000 satoshis** para Bob, Alice terá que enviar um pouco mais, já que cada nó intermediário deduzirá suas taxas:

- **Carol** deduz 1,04 satoshis no canal com Bob:
  $$ f*{\text{Carol-Bob}} = \text{taxa base} + \left(\frac{\text{ppm} \times \text{quantidade}}{10^6}\right) $$
  $$ f*{\text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0,04 = 1,04 \text{ sats} $$

- **Suzie** deduz 8 satoshis em taxas no canal com Carol:
  $$ f*{\text{Suzie-Carol}} = \text{taxa base} + \left(\frac{\text{ppm} \times \text{quantidade}}{10^6}\right) $$
  $$ f*{\text{Suzie-Carol}} = 0 + \frac{200 \times 40001,04}{10^6} = 0 + 8,0002 \approx 8 \text{ sats} $$

As taxas totais para este pagamento neste caminho são, portanto, **9,04 satoshis**. Assim, Alice deve enviar **40.009,04 satoshis** para que Bob receba exatamente **40.000 satoshis**.

![LNP201](assets/en/44.webp)

A liquidez é, portanto, atualizada:

![LNP201](assets/en/45.webp)

### Roteamento Onion

Para rotear um pagamento do remetente ao destinatário, a Rede Lightning utiliza um método chamado "**roteamento onion**". Diferentemente do roteamento de dados clássicos, onde cada roteador decide a direção dos dados com base em seu destino, o roteamento onion funciona de maneira diferente:

- **O nó remetente calcula toda a rota**: Alice, por exemplo, determina que seu pagamento deve passar por Suzie e Carol antes de chegar a Bob.
- **Cada nó intermediário conhece apenas seu vizinho imediato**: Suzie só sabe que recebeu fundos de Alice e que deve transferi-los para Carol. No entanto, Suzie não sabe se Alice é o nó de origem ou um nó intermediário, e ela também não sabe se Carol é o nó destinatário ou apenas outro nó intermediário. Este princípio também se aplica a Carol e todos os outros nós no caminho. O roteamento Onion, assim, preserva a confidencialidade das transações ao mascarar a identidade do remetente e do destinatário final. Para garantir que o nó transmissor possa calcular uma rota completa até o destinatário no roteamento Onion, ele deve manter um **gráfico da rede** para conhecer sua topologia e determinar rotas possíveis.
  **O que você deve levar deste capítulo?**

1. No Lightning, pagamentos podem ser roteados entre nós indiretamente conectados através de canais intermediários. Cada um desses nós intermediários facilita o retransmissão de liquidez.
2. Nós intermediários recebem uma comissão por seu serviço, consistindo de taxas fixas e variáveis.
3. O roteamento Onion permite que o nó transmissor calcule a rota completa sem que os nós intermediários saibam a origem ou o destino final.

Neste capítulo, exploramos o roteamento de pagamentos na Rede Lightning. Mas surge uma questão: o que impede os nós intermediários de aceitar um pagamento de entrada sem encaminhá-lo para o próximo destino, com o objetivo de interceptar a transação? Este é precisamente o papel dos HTLCs que estudaremos no capítulo seguinte.

## HTLC – Hashed Time Locked Contract

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

![HTLC](https://youtu.be/-JC4mkq7H48)

Neste capítulo, descobriremos como o Lightning permite que pagamentos transitem através de nós intermediários sem a necessidade de confiar neles, graças aos **HTLC** (_Hashed Time-Locked Contracts_). Esses contratos inteligentes garantem que cada nó intermediário só receberá os fundos de seu canal se encaminhar o pagamento para o destinatário final, caso contrário, o pagamento não será validado.

O problema que surge para o roteamento de pagamentos é, portanto, a confiança necessária nos nós intermediários, e entre os próprios nós intermediários. Para ilustrar isso, vamos revisitar nosso exemplo simplificado de rede Lightning com 3 nós e 2 canais:

- Alice tem um canal com Suzie.
- Suzie tem um canal com Bob.

Alice quer enviar 40.000 sats para Bob, mas ela não tem um canal direto com ele e não deseja abrir um. Ela procura uma rota e decide passar pelo nó de Suzie.

![LNP201](assets/en/46.webp)

Se Alice ingenuamente enviar 40.000 satoshis para Suzie esperando que Suzie transfira essa soma para Bob, Suzie poderia manter os fundos para si e não transmitir nada para Bob.

![LNP201](assets/en/47.webp)
Para evitar essa situação, no Lightning, usamos HTLCs (Hashed Time-Locked Contracts), que tornam o pagamento ao nó intermediário condicional, significando que Suzie deve cumprir certas condições para acessar os fundos de Alice e transferi-los para Bob.

### Como Funcionam os HTLCs

Um HTLC é um contrato especial baseado em dois princípios:

- **Condição de acesso**: O destinatário deve revelar um segredo para desbloquear o pagamento devido a eles.
- **Expiração**: Se o pagamento não for totalmente concluído dentro de um período definido, ele é cancelado e os fundos retornam ao remetente.

Aqui está como esse processo funciona em nosso exemplo com Alice, Suzie e Bob:

![LNP201](assets/en/48.webp)
**Criando o segredo**: Bob gera um segredo aleatório notado como _s_ (a pré-imagem) e calcula seu hash notado como _r_ com a função hash notada como _h_. Temos:

$$
r = h(s)
$$

Usar uma função hash torna impossível encontrar _s_ apenas com _h(s)_, mas se _s_ for fornecido, é fácil verificar que corresponde a _h(s)_.

![LNP201](assets/en/49.webp)

**Enviando a solicitação de pagamento**: Bob envia uma **fatura** para Alice pedindo um pagamento. Esta fatura inclui notavelmente o hash _r_.

![LNP201](assets/en/50.webp)

**Enviando o pagamento condicional**: Alice envia um HTLC de 40.000 satoshis para Suzie. A condição para Suzie receber esses fundos é que ela forneça a Alice um segredo _s'_ que satisfaça a seguinte equação:

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

**Transferindo o HTLC para o destinatário final**: Suzie, para obter os 40.000 satoshis de Alice, deve transferir um HTLC similar de 40.000 satoshis para Bob, que tem a mesma condição, ou seja, ele deve fornecer a Suzie um segredo _s'_ que satisfaça a equação:

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

**Validação pelo segredo _s_**: Bob fornece _s_ a Suzie para receber os 40.000 satoshis prometidos no HTLC. Com esse segredo, Suzie pode então desbloquear o HTLC de Alice e obter os 40.000 satoshis de Alice. O pagamento é então corretamente encaminhado para Bob.

![LNP201](assets/en/53.webp)
Este processo impede que Suzie fique com os fundos de Alice sem completar a transferência para Bob, pois ela deve enviar o pagamento a Bob para obter o segredo _s_ e assim desbloquear o HTLC de Alice. A operação permanece a mesma mesmo se a rota incluir vários nós intermediários: é simplesmente uma questão de repetir os passos de Suzie para cada nó intermediário. Cada nó é protegido pelas condições dos HTLCs, porque desbloquear o último HTLC pelo destinatário automaticamente desencadeia o desbloqueio de todos os outros HTLCs em cascata.

### Expiração e gestão dos HTLCs em caso de problemas

Se durante o processo de pagamento, um dos nós intermediários, ou o nó destinatário, parar de responder, especialmente em caso de uma interrupção da internet ou de energia, então o pagamento não pode ser completado, porque o segredo necessário para desbloquear os HTLCs não é transmitido. Tomando nosso exemplo com Alice, Suzie e Bob, este problema ocorre, por exemplo, se Bob não transmitir o segredo _s_ para Suzie. Neste caso, todos os HTLCs a montante do caminho são bloqueados, e os fundos que eles asseguram também.

![LNP201](assets/en/54.webp)

Para evitar isso, os HTLCs no Lightning têm uma expiração que permite a remoção do HTLC se ele não for completado após um determinado tempo. A expiração segue uma ordem específica, pois começa primeiro com o HTLC mais próximo do destinatário, e então progride até o emissor da transação. No nosso exemplo, se Bob nunca der o segredo _s_ para Suzie, isso causaria primeiro a expiração do HTLC de Suzie para Bob.

![LNP201](assets/en/55.webp)

Depois o HTLC de Alice para Suzie.
![LNP201](assets/en/56.webp)
Se a ordem de expiração fosse invertida, Alice poderia recuperar seu pagamento antes que Suzie pudesse se proteger de uma possível trapaça. De fato, se Bob voltasse para reivindicar seu HTLC enquanto Alice já tivesse removido o dela, Suzie estaria em desvantagem. Esta ordem cascata de expiração de HTLCs, portanto, garante que nenhum nó intermediário sofra de perdas injustas.

### Representação de HTLCs em transações de compromisso

Transações de compromisso representam HTLCs de tal forma que as condições que impõem ao Lightning podem ser transferidas para o Bitcoin em caso de fechamento forçado do canal durante a vida útil de um HTLC. Como lembrete, transações de compromisso representam o estado atual do canal entre os dois usuários e permitem um fechamento forçado unilateral em caso de problemas. Com cada novo estado do canal, 2 transações de compromisso são criadas: uma para cada parte. Vamos revisitar nosso exemplo com Alice, Suzie e Bob, mas olhar mais de perto o que acontece no nível do canal entre Alice e Suzie quando o HTLC é criado.
![LNP201](assets/en/57.webp)

Antes do início do pagamento de 40.000 sats entre Alice e Bob, Alice tem 100.000 sats em seu canal com Suzie, enquanto Suzie possui 30.000. Suas transações de compromisso são as seguintes:

![LNP201](assets/en/58.webp)

Alice acabou de receber a fatura de Bob, que contém notavelmente _r_, o hash do segredo. Ela pode, assim, construir um HTLC de 40.000 satoshis com Suzie. Este HTLC é representado nas últimas transações de compromisso como uma saída chamada "**_HTLC Out_**" do lado de Alice, já que os fundos estão saindo, e "**_HTLC In_**" do lado de Suzie, já que os fundos estão entrando.

![LNP201](assets/en/59.webp)

Estas saídas associadas ao HTLC compartilham exatamente as mesmas condições, a saber:

- Se Suzie for capaz de fornecer o segredo _s_, ela pode desbloquear esta saída imediatamente e transferi-la para um endereço que ela controla.
- Se Suzie não possuir o segredo _s_, ela não pode desbloquear esta saída, e Alice será capaz de desbloqueá-la após um timelock para enviá-la a um endereço que ela controla. O timelock, assim, concede a Suzie um período para reagir se ela obtiver _s_.

Estas condições aplicam-se apenas se o canal for fechado (ou seja, uma transação de compromisso for publicada na blockchain) enquanto o HTLC ainda estiver ativo no Lightning, significando que o pagamento entre Alice e Bob ainda não foi finalizado, e os HTLCs ainda não expiraram. Graças a estas condições, Suzie pode recuperar os 40.000 satoshis do HTLC devido a ela fornecendo _s_. Caso contrário, Alice recupera os fundos após a expiração do timelock, porque se Suzie não conhece _s_, significa que ela não transferiu os 40.000 satoshis para Bob, e, portanto, os fundos de Alice não lhe são devidos.

Além disso, se o canal for fechado enquanto vários HTLCs estiverem pendentes, haverá tantas saídas adicionais quantos forem os HTLCs em andamento.
Se o canal não for fechado, então após a expiração ou sucesso do pagamento Lightning, novas transações de compromisso são criadas para refletir o novo estado agora estável do canal, ou seja, sem quaisquer HTLCs pendentes. As saídas relacionadas aos HTLCs podem, portanto, ser removidas das transações de compromisso.
![LNP201](assets/en/60.webp)
Finalmente, no caso de um fechamento cooperativo de canal enquanto um HTLC está ativo, Alice e Suzie param de aceitar novos pagamentos e esperam pela resolução ou expiração dos HTLCs em andamento. Isso permite que elas publiquem uma transação de fechamento mais leve, sem as saídas relacionadas aos HTLCs, reduzindo assim as taxas e evitando a espera por um possível timelock.
**O que você deve absorver deste capítulo?**

HTLCs possibilitam o roteamento de pagamentos Lightning através de múltiplos nós sem a necessidade de confiar neles. Aqui estão os pontos chave para lembrar:

1. HTLCs garantem a segurança dos pagamentos através de um segredo (preimage) e um tempo de expiração.
2. A resolução ou expiração de HTLCs segue uma ordem específica: então, do destino em direção à fonte, a fim de proteger cada nó.
3. Enquanto um HTLC não é resolvido nem expirado, ele é mantido como uma saída nas transações de compromisso mais recentes.

No próximo capítulo, descobriremos como um nó emitindo uma transação Lightning encontra e seleciona rotas para que seu pagamento alcance o nó destinatário.

## Encontrando Seu Caminho

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

![encontrando seu caminho](https://youtu.be/wnUGJjOxd9Q)

Nos capítulos anteriores, vimos como usar os canais de outros nós para rotear pagamentos e alcançar um nó sem estar diretamente conectado a ele através de um canal. Também discutimos como garantir a segurança da transferência sem confiar nos nós intermediários. Neste capítulo, focaremos em encontrar a melhor rota possível para alcançar um nó alvo.

### O Problema de Roteamento no Lightning

Como vimos, no Lightning, é o nó que envia o pagamento que deve calcular a rota completa até o destinatário, porque usamos um sistema de roteamento em cebola. Os nós intermediários não sabem nem o ponto de origem nem o destino final. Eles apenas sabem de onde o pagamento vem e para qual nó eles devem transferi-lo a seguir. Isso significa que o nó remetente deve manter uma topologia local dinâmica da rede, com os nós Lightning existentes e os canais entre cada um, levando em conta aberturas, fechamentos e atualizações de estado.

![LNP201](assets/en/61.webp)
Mesmo com essa topologia da Rede Lightning, há informações essenciais para o roteamento que permanecem inacessíveis ao nó remetente, que é a distribuição exata de liquidez nos canais em qualquer momento dado. De fato, cada canal apenas exibe sua **capacidade total**, mas a distribuição interna de fundos é conhecida apenas pelos dois nós participantes. Isso representa desafios para o roteamento eficiente, pois o sucesso do pagamento depende notavelmente de se o seu montante é menor que a liquidez mais baixa na rota escolhida. No entanto, as liquidezes não são todas visíveis ao nó remetente.
![LNP201](assets/en/62.webp)

### Atualização do Mapa da Rede

Para manter seu mapa da rede atualizado, os nós trocam regularmente mensagens através de um algoritmo chamado "**_gossip_**". Este é um algoritmo distribuído usado para espalhar informações de maneira epidêmica para todos os nós na rede, o que permite a troca e sincronização do estado global dos canais em poucos ciclos de comunicação. Cada nó propaga informações para um ou mais vizinhos escolhidos ao acaso ou não, estes, por sua vez, propagam a informação para outros vizinhos e assim por diante até que um estado globalmente sincronizado seja alcançado.

As 2 principais mensagens trocadas entre nós Lightning são as seguintes:

- "**Anúncios de Canal**": mensagens sinalizando a abertura de um novo canal.
- "**Atualizações de Canal**": mensagens de atualização sobre o estado de um canal, particularmente sobre a evolução das taxas (mas não sobre a distribuição de liquidez).
  Os nós do Lightning também monitoram o blockchain do Bitcoin para detectar transações de fechamento de canal. O canal fechado é então removido do mapa, pois não pode mais ser usado para rotear nossos pagamentos.

### Roteando um Pagamento

Vamos tomar um exemplo de uma pequena Rede Lightning com 7 nós: Alice, Bob, 1, 2, 3, 4 e 5. Imagine que Alice quer enviar um pagamento para Bob, mas deve passar por nós intermediários.

![LNP201](assets/en/63.webp)

Aqui está a distribuição atual de fundos nesses canais:

- **Canal entre Alice e 1**: 250.000 sats do lado de Alice, 80.000 do lado de 1 (capacidade total de 330.000 sats).
- **Canal entre 1 e 2**: 300.000 sats do lado de 1, 200.000 do lado de 2 (capacidade total de 500.000 sats).
- **Canal entre 2 e 3**: 50.000 sats do lado de 2, 60.000 do lado de 3 (capacidade total de 110.000 sats).
- **Canal entre 2 e 5**: 90.000 sats do lado de 2, 160.000 do lado de 5 (capacidade total de 250.000 sats).
- **Canal entre 2 e 4**: 180.000 sats do lado de 2, 110.000 do lado de 4 (capacidade total de 290.000 sats).
- **Canal entre 4 e 5**: 200.000 sats do lado de 4, 10.000 do lado de 5 (capacidade total de 210.000 sats).
- **Canal entre 3 e Bob**: 50.000 sats do lado de 3, 250.000 do lado de Bob (capacidade total de 300.000 sats).
- **Canal entre 5 e Bob**: 260.000 sats do lado de 5, 100.000 do lado de Bob (capacidade total de 360.000 sats).

![LNP201](assets/en/64.webp)

Para fazer um pagamento de 100.000 sats de Alice para Bob, as opções de roteamento são limitadas pela liquidez disponível em cada canal. A rota ótima para Alice, com base nas distribuições de liquidez conhecidas, poderia ser a sequência `Alice → 1 → 2 → 4 → 5 → Bob`:

![LNP201](assets/en/65.webp)

Mas, como Alice não conhece a distribuição exata de fundos em cada canal, ela deve estimar a rota ótima de forma probabilística, levando em conta os seguintes critérios:

- **Probabilidade de sucesso**: um canal com uma capacidade total maior tem mais chances de conter liquidez suficiente. Por exemplo, o canal entre o nó 2 e o nó 3 tem uma capacidade total de 110.000 sats, então é improvável encontrar 100.000 sats ou mais do lado do nó 2, embora permaneça possível.
- **Taxas de transação**: ao escolher a melhor rota, o nó remetente também considera as taxas aplicadas por cada nó intermediário e busca minimizar o custo total de roteamento.
- **Expiração dos HTLCs**: para evitar pagamentos bloqueados, o tempo de expiração dos HTLCs também é um parâmetro a considerar.
- **Número de nós intermediários**: finalmente, de forma mais ampla, o nó de envio procurará encontrar uma rota com o menor número possível de nós para reduzir o risco de falha e limitar as taxas de transação do Lightning.
  Analisando esses critérios, o nó de envio pode testar as rotas mais prováveis e tentar otimizá-las. No nosso exemplo, Alice poderia classificar as melhores rotas da seguinte forma:

1. `Alice → 1 → 2 → 5 → Bob`, porque é a rota mais curta com a maior capacidade.
2. `Alice → 1 → 2 → 4 → 5 → Bob`, porque esta rota oferece boas capacidades, embora seja mais longa que a primeira.
3. `Alice → 1 → 2 → 3 → Bob`, porque esta rota inclui o canal `2 → 3`, que tem capacidade muito limitada, mas permanece potencialmente utilizável.

### Execução do Pagamento

Alice decide testar sua primeira rota (`Alice → 1 → 2 → 5 → Bob`). Ela, portanto, envia um HTLC de 100.000 sats para o nó 1. Este nó verifica se tem liquidez suficiente com o nó 2 e continua a transmissão. O nó 2 então recebe o HTLC do nó 1, mas percebe que não tem liquidez suficiente em seu canal com o nó 5 para rotear um pagamento de 100.000 sats. Ele então envia uma mensagem de erro de volta para o nó 1, que a transmite para Alice. Esta rota falhou.

![LNP201](assets/en/66.webp)

Alice então tenta rotear seu pagamento usando sua segunda rota (`Alice → 1 → 2 → 4 → 5 → Bob`). Ela envia um HTLC de 100.000 sats para o nó 1, que o transmite para o nó 2, depois para o nó 4, para o nó 5 e, finalmente, para Bob. Desta vez, a liquidez é suficiente, e a rota é funcional. Cada nó desbloqueia seu HTLC em cascata usando o preimage fornecido por Bob (o segredo _s_), o que permite que o pagamento de Alice para Bob seja finalizado com sucesso.

![LNP201](assets/en/67.webp)

A busca por uma rota é conduzida da seguinte forma: o nó de envio começa identificando as melhores rotas possíveis, depois tenta pagamentos sucessivamente até encontrar uma rota funcional.

Vale ressaltar que Bob pode fornecer a Alice informações na **fatura** para facilitar o roteamento. Por exemplo, ele pode indicar canais próximos com liquidez suficiente ou revelar a existência de canais privados. Essas indicações permitem que Alice evite rotas com pouca chance de sucesso e tente primeiro os caminhos recomendados por Bob.

**O que você deve levar deste capítulo?**

1. Os nós mantêm um mapa da topologia da rede através de anúncios e monitorando o fechamento de canais na blockchain do Bitcoin.
2. A busca por uma rota ótima para um pagamento permanece probabilística e depende de muitos critérios.
3. Bob pode fornecer indicações na **fatura** para guiar o roteamento de Alice e salvá-la de testar rotas improváveis.

No próximo capítulo, estudaremos especificamente o funcionamento das faturas, além de algumas outras ferramentas usadas na Rede Lightning.

# As Ferramentas da Rede Lightning

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Fatura, LNURL e Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>
![fatura, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)
Neste capítulo, vamos examinar mais de perto a operação de **faturas** Lightning, ou seja, solicitações de pagamento enviadas pelo nó receptor para o nó remetente. O objetivo é entender como pagar e receber pagamentos no Lightning. Também discutiremos 2 alternativas às faturas clássicas: LNURL e Keysend.
![LNP201](assets/en/68.webp)

### A Estrutura das Faturas Lightning

Como explicado no capítulo sobre HTLCs, cada pagamento começa com a geração de uma **fatura** pelo destinatário. Esta fatura é então transmitida ao pagador (via um código QR ou por copiar e colar) para iniciar o pagamento. Uma fatura consiste em duas partes principais:

1. **A Parte Legível por Humanos**: esta seção contém metadados claramente visíveis para melhorar a experiência do usuário.
2. **O Payload**: esta seção inclui informações destinadas às máquinas para processar o pagamento.

A estrutura típica de uma fatura começa com um identificador `ln` para "Lightning", seguido por `bc` para Bitcoin, e então o valor da fatura. Um separador `1` distingue a parte legível por humanos da parte de dados (payload).

Vamos tomar a seguinte fatura como exemplo:

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

Já podemos dividi-la em 2 partes. Primeiro, há a Parte Legível por Humanos:

```invoice
lnbc100u
```

Então a parte destinada ao payload:

```invoice

p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

As duas partes são separadas por um `1`. Esse separador foi escolhido em vez de um caractere especial para permitir a cópia e colagem fácil de toda a fatura com um duplo clique.
Na primeira parte, podemos ver que:

- `ln` indica que é uma transação Lightning.
- `bc` indica que a rede Lightning está na blockchain do Bitcoin (e não no testnet ou no Litecoin).
- `100u` indica a quantidade da fatura, expressa em **microsatoshis** (`u` significando "micro"), que aqui equivale a 10.000 sats.

Para designar a quantidade de pagamento, ela é expressa em subunidades do bitcoin. Aqui estão as unidades usadas:

- **Millibitcoin (denotado `m`):** Representa um milésimo de um bitcoin.

  $$
  1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
  $$

- **Microbitcoin (denotado `u`):** Também às vezes chamado de "bit", representa um milionésimo de um bitcoin.

  $$
  1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
  $$

- **Nanobitcoin (denotado `n`):** Representa um bilionésimo de um bitcoin.

  $$
  1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
  $$

- **Picobitcoin (denotado `p`):** Representa um trilionésimo de um bitcoin.
  $$
  1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
  $$

### O Conteúdo de uma Fatura

O conteúdo de uma fatura inclui várias peças de informação necessárias para processar o pagamento:

- **O timestamp:** O momento da criação da fatura, expresso em Timestamp Unix (o número de segundos que se passaram desde 1 de janeiro de 1970).
- **Hashing o Segredo**: Como vimos na seção sobre HTLCs, o nó receptor deve fornecer ao nó de envio o hash da pré-imagem. Isso é usado em HTLCs para garantir a transação. Nós nos referimos a isso como "_r_".
- **O Segredo de Pagamento**: Outro segredo é gerado pelo destinatário, mas desta vez é transmitido ao nó de envio. É usado no roteamento de cebola para impedir que os nós intermediários adivinhem se o próximo nó é o destinatário final ou não. Isso, portanto, mantém uma forma de confidencialidade para o destinatário em relação ao último nó intermediário na rota.
- **A Chave Pública do Destinatário**: Indica ao pagador o identificador da pessoa a ser paga.
- **A Duração da Expiração**: O tempo máximo para a fatura ser paga (1 hora por padrão).
- **Dicas de Roteamento**: Informações adicionais fornecidas pelo destinatário para ajudar o remetente a otimizar a rota de pagamento.
- **A Assinatura**: Garante a integridade da fatura autenticando todas as informações.

As faturas são então codificadas em **bech32**, o mesmo formato que para endereços Bitcoin SegWit (formato começando com `bc1`).

### LNURL Saque

Em uma transação tradicional, como uma compra em loja, a fatura é gerada pelo valor total a ser pago. Uma vez que a fatura é apresentada (na forma de um código QR ou sequência de caracteres), o cliente pode escaneá-la e finalizar a transação. O pagamento então segue o processo tradicional que estudamos na seção anterior. No entanto, esse processo pode às vezes ser muito complicado para a experiência do usuário, pois requer que o receptor envie informações ao remetente via fatura.
Para certas situações, como retirar bitcoins de um serviço online, o processo tradicional é muito complicado. Nestes casos, a solução de retirada **LNURL** simplifica esse processo exibindo um código QR que a carteira do destinatário escaneia para criar automaticamente a fatura. O serviço então paga a fatura, e o usuário simplesmente vê uma retirada instantânea.

![LNP201](assets/en/69.webp)

LNURL é um protocolo de comunicação que especifica um conjunto de funcionalidades projetadas para simplificar interações entre nós Lightning e clientes, bem como aplicações de terceiros. A retirada LNURL, como acabamos de ver, é apenas um exemplo entre outras funcionalidades.
Este protocolo é baseado em HTTP e permite a criação de links para várias operações, como um pedido de pagamento, um pedido de retirada, ou outras funcionalidades que aprimoram a experiência do usuário. Cada LNURL é uma URL codificada em bech32 com o prefixo lnurl, que, uma vez escaneada, desencadeia uma série de ações automáticas na carteira Lightning.
Por exemplo, a funcionalidade LNURL-withdraw (LUD-03) permite retirar fundos de um serviço escaneando um código QR, sem a necessidade de gerar manualmente uma fatura. Da mesma forma, LNURL-auth (LUD-04) possibilita o login em serviços online usando uma chave privada na carteira Lightning em vez de uma senha.

### Enviando um Pagamento Lightning sem uma Fatura: Keysend

Outro caso interessante é a transferência de fundos sem ter recebido uma fatura previamente, conhecido como "**Keysend**". Este protocolo permite enviar fundos adicionando uma pré-imagem nos dados de pagamento criptografados, acessíveis apenas pelo destinatário. Esta pré-imagem permite que o destinatário desbloqueie o HTLC, assim recuperando os fundos sem ter gerado uma fatura previamente.

Para simplificar, neste protocolo, é o remetente quem gera o segredo usado nos HTLCs, em vez do destinatário. Na prática, isso permite que o remetente faça um pagamento sem ter tido que interagir com o destinatário previamente.

![LNP201](assets/en/70.webp)

**O que você deve levar deste capítulo?**

1. Uma **Fatura Lightning** é um pedido de pagamento consistindo de uma parte legível por humanos e uma parte de dados de máquina.
2. A fatura é codificada em **bech32**, com um separador `1` para facilitar a cópia e uma parte de dados contendo todas as informações necessárias para processar o pagamento.
3. Existem outros processos de pagamento no Lightning, notavelmente **LNURL-Withdraw** para facilitar retiradas, e **Keysend** para transferências diretas sem uma fatura.

No próximo capítulo, veremos como um operador de nó pode gerenciar a liquidez em seus canais, para nunca ser bloqueado e sempre ser capaz de enviar e receber pagamentos na Rede Lightning.

## Gerenciando Sua Liquidez

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![gerenciando sua liquidez](https://youtu.be/YuPrbhEJXbg)

Neste capítulo, exploraremos estratégias para gerenciar efetivamente a liquidez na Rede Lightning. A gestão da liquidez varia dependendo do tipo de usuário e contexto. Vamos olhar para os principais princípios e técnicas existentes para entender melhor como otimizar essa gestão.

### Necessidades de Liquidez

Existem três principais perfis de usuários no Lightning, cada um com necessidades específicas de liquidez:

1. **O Pagador**: Este é quem faz pagamentos. Eles precisam de liquidez de saída para poder transferir fundos para outros usuários. Por exemplo, isso poderia ser um consumidor.
2. **O Vendedor (ou Beneficiário)**: Este é quem recebe pagamentos. Eles precisam de liquidez de entrada para poder aceitar pagamentos em seu nó. Por exemplo, isso poderia ser um negócio ou uma loja online.
3. **O Roteador**: Um nó intermediário, muitas vezes especializado em rotear pagamentos, que deve otimizar sua liquidez em cada canal para rotear o máximo de pagamentos possível e ganhar taxas.

Esses perfis obviamente não são fixos; um usuário pode alternar entre pagador e beneficiário dependendo das transações. Por exemplo, Bob poderia receber seu salário no Lightning de seu empregador, colocando-o na posição de um "vendedor" que requer liquidez de entrada. Posteriormente, se ele quiser usar seu salário para comprar comida, ele se torna um "pagador" e deve então ter liquidez de saída.

Para entender melhor, vamos tomar o exemplo de uma rede simples composta por três nós: o comprador (Alice), o roteador (Suzie) e o vendedor (Bob).

![LNP201](assets/en/71.webp)

Imagine que o comprador queira enviar 30.000 sats para o vendedor e que o pagamento passe pelo nó do roteador. Cada parte deve então ter uma quantidade mínima de liquidez na direção do pagamento:

- O pagador deve ter pelo menos 30.000 satoshis do seu lado do canal com o roteador.
- O vendedor deve ter um canal onde 30.000 satoshis estejam do lado oposto para poder recebê-los.
- O roteador deve ter 30.000 satoshis do lado do pagador em seu canal, e também 30.000 satoshis do seu lado no canal com o vendedor, para poder rotear o pagamento.

![LNP201](assets/en/72.webp)

### Estratégias de Gestão de Liquidez

Os pagadores devem garantir a manutenção de liquidez suficiente do seu lado dos canais para garantir a liquidez de saída. Isso prova ser relativamente simples, pois basta abrir novos canais Lightning para ter essa liquidez. De fato, os fundos iniciais bloqueados no multisig on-chain estão inteiramente do lado do pagador no canal Lightning no início. A capacidade de pagamento é assim assegurada enquanto canais forem abertos com fundos suficientes. Quando a liquidez de saída se esgota, basta abrir novos canais.
Por outro lado, para o vendedor, a tarefa é mais complexa. Para poder receber pagamentos, eles devem ter liquidez do lado oposto dos seus canais. Portanto, abrir um canal não é suficiente: eles também devem fazer um pagamento neste canal para mover a liquidez para o outro lado antes que possam receber pagamentos eles mesmos. Para certos perfis de usuários do Lightning, como comerciantes, existe uma clara desproporção entre o que seu nó envia e o que recebe, já que o objetivo de um negócio é principalmente coletar mais do que gasta, a fim de gerar lucro. Felizmente, para esses usuários com necessidades específicas de liquidez de entrada, várias soluções existem:

- **Atrair canais**: O comerciante se beneficia de uma vantagem devido ao volume de pagamentos de entrada esperados em seu nó. Levando isso em conta, eles podem tentar atrair nós de roteamento que estão procurando renda de taxas de transação e que possam abrir canais em direção a eles, esperando rotear seus pagamentos e coletar as taxas associadas.
- **Movimento de Liquidez**: O vendedor também pode abrir um canal e transferir parte dos fundos para o lado oposto, fazendo pagamentos fictícios para outro nó, que retornará o dinheiro de outra forma. Veremos na próxima parte como realizar essa operação.
- **Abertura Triangular**: Existem plataformas para nós que desejam abrir canais colaborativamente, permitindo que cada um se beneficie de liquidez imediata de entrada e saída. Por exemplo, [LightningNetwork+](https://lightningnetwork.plus/) oferece este serviço. Se Alice, Bob e Suzie querem abrir um canal com 100.000 sats, eles podem combinar nesta plataforma para Alice abrir um canal em direção a Bob, Bob em direção a Suzie, e Suzie em direção a Alice. Dessa forma, cada um tem 100.000 sats de liquidez de saída e 100.000 sats de liquidez de entrada, enquanto apenas bloquearam 100.000 sats.

![LNP201](assets/en/73.webp)

- **Comprando canais**: Serviços para alugar canais Lightning também existem para obter liquidez de entrada, como [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) ou [Lightning Labs Pool](https://lightning.engineering/pool/). Por exemplo, Alice pode comprar um canal de um milhão de satoshis em direção ao seu nó para poder receber pagamentos.

![LNP201](assets/en/74.webp)

Finalmente, para os roteadores, cujo objetivo é maximizar o número de pagamentos processados e as taxas coletadas, eles devem:

- Abrir canais bem financiados com nós estratégicos.
- Ajustar regularmente a distribuição de fundos nos canais de acordo com as necessidades da rede.

### O Serviço Loop Out

O serviço [Loop Out](https://lightning.engineering/loop/), oferecido pela Lightning Labs, permite mover a liquidez para o lado oposto do canal enquanto recupera os fundos na blockchain do Bitcoin. Por exemplo, Alice envia 1 milhão de satoshis via Lightning para um nó de loop, que então retorna esses fundos para ela em bitcoins on-chain. Isso equilibra o canal dela com 1 milhão de satoshis de cada lado, otimizando sua capacidade de receber pagamentos.

![LNP201](assets/en/75.webp)

Portanto, este serviço possibilita a liquidez de entrada enquanto recupera os bitcoins on-chain, o que ajuda a limitar a imobilização de dinheiro necessário para aceitar pagamentos com Lightning.

**O que você deve levar deste capítulo?**

- Para enviar pagamentos no Lightning, você deve ter liquidez suficiente do seu lado nos seus canais. Para aumentar essa capacidade de envio, basta abrir novos canais.
- Para receber pagamentos, você precisa ter liquidez do lado oposto nos seus canais. Aumentar essa capacidade de recebimento é mais complexo, pois requer que outros abram canais em sua direção, ou que façam pagamentos (fictícios ou reais) para mover a liquidez para o outro lado.
- Manter a liquidez onde desejado pode ser ainda mais desafiador dependendo do uso dos canais. É por isso que existem ferramentas e serviços para ajudar a equilibrar os canais conforme desejado.

No próximo capítulo, proponho revisar os conceitos mais importantes deste treinamento.

# Ir Além

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Conclusão do Treinamento

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

![conclusão](https://youtu.be/MaWpD0rbkVo)
Neste capítulo final, marcando o término do treinamento LNP201, proponho revisitar os conceitos importantes que cobrimos juntos.
O objetivo deste treinamento era fornecer a você um entendimento abrangente e técnico sobre a Lightning Network. Descobrimos como a Lightning Network depende da blockchain do Bitcoin para realizar transações fora da cadeia, mantendo as características fundamentais do Bitcoin, notavelmente a ausência da necessidade de confiar em outros nós.

### Canais de Pagamento

Nos capítulos iniciais, exploramos como duas partes, ao abrir um canal de pagamento, podem conduzir transações fora da blockchain do Bitcoin. Aqui estão os passos abordados:

1. **Abertura do Canal**: A criação do canal é feita através de uma transação Bitcoin que bloqueia os fundos em um endereço multisignature 2/2. Este depósito representa o canal Lightning na blockchain.

![LNP201](assets/en/76.webp) 2. **Transações no Canal**: Neste canal, é então possível realizar inúmeras transações sem ter que publicá-las na blockchain. Cada transação Lightning cria um novo estado do canal refletido em uma transação de compromisso.
![LNP201](assets/en/77.webp)

3. **Segurança e Fechamento**: Os participantes se comprometem com o novo estado do canal trocando chaves de revogação para assegurar os fundos e prevenir qualquer trapaça. Ambas as partes podem fechar o canal cooperativamente fazendo uma nova transação na blockchain do Bitcoin, ou, como último recurso, através de um fechamento forçado. Esta última opção, embora menos eficiente porque é mais longa e às vezes mal avaliada em termos de taxas, ainda permite a recuperação dos fundos. Em caso de trapaça, a vítima pode punir o trapaceiro recuperando todos os fundos do canal na blockchain.

![LNP201](assets/en/78.webp)

### A Rede de Canais

Após estudar canais isolados, estendemos nossa análise para a rede de canais:

- **Roteamento**: Quando duas partes não estão diretamente conectadas por um canal, a rede permite o roteamento através de nós intermediários. Os pagamentos então transitam de um nó para outro.

![LNP201](assets/en/79.webp)

- **HTLCs**: Pagamentos transitando através de nós intermediários são assegurados por "_Hash Time-Locked Contracts_" (HTLC), que permitem que os fundos sejam bloqueados até que o pagamento seja completado de ponta a ponta.

![LNP201](assets/en/80.webp)

- **Roteamento Onion**: Para garantir a confidencialidade do pagamento, o roteamento onion mascara o destino final para nós intermediários. O nó de envio deve, portanto, calcular toda a rota, mas na ausência de informações completas sobre a liquidez dos canais, procede através de tentativas sucessivas para rotear o pagamento.

![LNP201](assets/en/81.webp)

### Gestão de Liquidez

Vimos que a gestão de liquidez é um desafio na Lightning para garantir o fluxo suave de pagamentos. Enviar pagamentos é relativamente simples: basta abrir um canal. No entanto, receber pagamentos requer ter liquidez no lado oposto dos seus canais. Aqui estão algumas estratégias discutidas:

- **Atraindo Canais**: Ao incentivar outros nós a abrir canais em direção a si mesmo, um usuário obtém liquidez de entrada.

- **Movendo Liquidez**: Ao enviar pagamentos para outros canais, a liquidez se move para o lado oposto.

![LNP201](assets/en/82.webp)

- **Usando Serviços como Loop e Pool**: Esses serviços permitem o reequilíbrio ou a compra de canais com liquidez no lado oposto.
  ![LNP201](assets/en/83.webp)
- **Aberturas Colaborativas**: Também existem plataformas disponíveis para se conectar e realizar aberturas triangulares e ter liquidez de entrada.

![LNP201](assets/en/84.webp)

# Conclusão

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## Avalie este curso

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Exame final

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Conclusão

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>
Parabéns! 🎉

Você concluiu o treinamento LNP 201 - Introdução à Lightning Network!

Você pode se orgulhar, pois este não é um assunto fácil.

Poucas pessoas se aventuram tão profundamente na toca do coelho do Bitcoin.

Um grande agradecimento ao **Fanis Michalakis** por nos oferecer este excelente curso gratuito sobre o funcionamento técnico da Lightning Network.

Fique à vontade para segui-lo no [Twitter](https://x.com/FanisMichalakis), no [seu blog](https://fanismichalakis.fr/) ou através do seu trabalho na [LN Markets](https://lnmarkets.com/).

Agora que você domina a Lightning Network, convido você a explorar nossos outros cursos gratuitos na Plan ₿ Network para aprofundar seu conhecimento sobre outros aspectos da invenção de Satoshi Nakamoto:

#### Entenda como funciona uma carteira Bitcoin com

https://planb.network/courses/cyp201

#### Descubra a história das origens do Bitcoin com

https://planb.network/courses/his201

#### Configure um servidor de pagamento BTC com

https://planb.network/courses/btc305

#### Domine os princípios de privacidade no Bitcoin

https://planb.network/courses/btc204

#### Descubra os fundamentos da mineração com

https://planb.network/courses/min201

#### Aprenda a criar sua comunidade Bitcoin com

https://planb.network/courses/btc302

