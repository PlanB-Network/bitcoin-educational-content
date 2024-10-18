---
name: Introdução teórica à Lightning Network
goal: Descobrir a Lightning Network do ponto de vista técnico
objectives:
  - Compreender o funcionamento dos canais da rede.
  - Se familiarizar com os termos HTLC, LNURL e UTXO.
  - Assimilar a gestão da liquidez e as taxas do LNN.
  - Reconhecer a Lightning Network como uma rede.
  - Compreender as utilizações teóricas da Lightning Network.
---

# Uma jornada para a segunda camada do Bitcoin

Este curso é uma formação teórica sobre o funcionamento técnico da Lightning Network.

Bem-vindo ao mundo emocionante da Lightning Network, uma segunda camada do Bitcoin, que é uma avançada tecnológica sofisticada e rica em potencialidades. Estamos prestes a mergulhar nas profundezas técnicas desta tecnologia, sem nos concentrarmos em tutoriais ou cenários de uso específicos. Para aproveitar ao máximo esta formação, é indispensável ter uma sólida compreensão do Bitcoin. É uma experiência que requer uma abordagem séria e concentrada. Você também pode considerar seguir o curso LN 202 em paralelo, que oferece um aspecto mais prático para esta exploração. Prepare-se para embarcar em uma jornada que pode mudar sua percepção do ecossistema Bitcoin.

Boa descoberta!

+++

# Os fundamentais
<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## Compreender a Lightning Network
<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

A rede Lightning é uma infraestrutura de pagamento de segunda camada, construída na rede Bitcoin, que permite transações rápidas e de baixo custo. Para entender completamente como funciona a rede Lightning, é essencial entender o que são os canais de pagamento e como eles funcionam.

Um canal de pagamento na Lightning é uma espécie de "via privada" entre dois usuários, que permite transações Bitcoin rápidas e repetitivas. Quando um canal é aberto, ele tem uma capacidade fixa, que é definida antecipadamente pelos usuários. Essa capacidade representa o valor máximo de Bitcoin que pode ser transmitido no canal em um determinado momento.

Os canais de pagamento são bidirecionais, o que significa que eles têm dois "lados". Por exemplo, se Alice e Bob abrirem um canal de pagamento, Alice pode enviar Bitcoin para Bob e Bob pode enviar Bitcoin para Alice. As transações dentro do canal não alteram a capacidade total do canal, mas alteram a distribuição dessa capacidade entre Alice e Bob.

![explication](assets/fr/1.webp)

Para que uma transação seja possível em um canal de pagamento Lightning, o usuário que envia os fundos deve ter Bitcoin suficiente do seu lado do canal. Se Alice quiser enviar 1 Bitcoin para Bob através do canal deles, ela deve ter pelo menos 1 Bitcoin do seu lado do canal.
Limites e Funcionamento dos Canais de Pagamento na Lightning.
Embora a capacidade de um canal de pagamento Lightning seja fixa, isso não limita o número total de transações ou o volume total de Bitcoin que pode ser transmitido através do canal. Por exemplo, se Alice e Bob têm um canal com capacidade de 1 Bitcoin, eles podem realizar centenas de transações de 0,01 Bitcoin ou milhares de transações de 0,001 Bitcoin, desde que a capacidade total do canal não seja excedida em um determinado momento.

Apesar dessas limitações, os canais de pagamento Lightning são uma maneira eficaz de realizar transações Bitcoin rápidas e baratas. Eles permitem que os usuários enviem e recebam Bitcoin sem ter que pagar altas taxas de transação ou esperar longos períodos de confirmação na rede Bitcoin.

Em resumo, os canais de pagamento no Lightning oferecem uma solução poderosa para aqueles que desejam realizar transações Bitcoin rápidas e baratas. No entanto, é essencial entender seu funcionamento e limitações para aproveitá-los ao máximo.

![explication](assets/fr/2.webp)

Exemplo:

- Alice tem 100.000 SAT
- Bob tem 30.000 SAT

Este é o estado atual do canal. Em uma transação, Alice decide enviar 40.000 SAT para Bob. Ela pode fazer isso porque 40.000 <100.000.

O novo estado do canal é, portanto:

- Alice 60.000 SAT
- Bob 70.000 SAT

```
Estado inicial do canal:
Alice (100.000 SAT) ============== Bob (30.000 SAT)

Após a transferência de Alice para Bob de 40.000 SAT:
Alice (60.000 SAT) ============== Bob (70.000 SAT)

```

![explication](assets/fr/3.webp)

Agora, Bob deseja enviar 80.000 SAT para Alice. Não tendo a liquidez, ele não pode. A capacidade máxima do canal é de 130.000 SAT, com um gasto possível de até 60.000 SAT para Alice e 70.000 SAT para Bob.

![explication](assets/fr/4.webp)

## Bitcoin, endereços, UTXO e transações
<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

Neste segundo capítulo, dedicamos tempo para estudar como as transações Bitcoin realmente funcionam, o que será muito útil para entender o Lightning. Também nos concentramos por um momento no conceito de endereço multiassinatura, que é fundamental para entender o próximo capítulo dedicado à abertura de canais na Lightning Network.

- Chave privada> Chave pública> Endereço: Em uma transação, Alice envia dinheiro para Bob. Este último fornece um endereço dado por sua chave pública. Alice, que recebeu o dinheiro em um endereço por meio de sua chave pública, agora usa sua chave privada para assinar a transação e desbloquear os bitcoins do endereço.
- Em uma transação, no Bitcoin, todos os bitcoins devem se mover. Chamado de UTXO (Unspend Transaction Output), os pedaços de bitcoin vão todos sair para depois retornar ao proprietário.

Alice tem 0,002 BTC, Bob tem 0 BTC. Alice decide enviar 0,0015 BTC para Bob. Ela assina uma transação de 0,002 BTC, onde 0,0015 vão para Bob e 0,0005 voltam para sua carteira. 

![explication](assets/fr/5.webp)

A partir de uma UTXO (Alice tem 0,0002 BTC em um endereço), criamos 2 UTXOs (Bob tem 0,0015 e Alice recuperou um novo UTXO (independente do anterior) de 0,0005 BTC).

```
Alice (0,002 BTC)
  |
  V
Transação Bitcoin (0,002 BTC)
  |
  |----> Bob (0,0015 BTC)
  |
  V
Alice (novo UTXO: 0,0005 BTC)
```

No Lightning Network, usamos multiassinaturas. Portanto, são necessárias 2 assinaturas para desbloquear os fundos, ou seja, duas chaves privadas para mover o dinheiro. Portanto, pode ser Alice e Bob que, juntos, devem concordar em desbloquear o dinheiro (UTXO). No LN especificamente, são transações 2/2, portanto, são necessárias as 2 assinaturas, ao contrário das multiassinaturas 2/3 ou 3/5, onde é necessária apenas uma combinação do número completo de chaves.

![explication](assets/fr/6.webp)

# Abertura e fechamento dos canais
<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## Abertura de canal
<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

Agora, vamos nos aprofundar na abertura de canal e como ela é realizada por meio de uma transação Bitcoin.

O Lightning Network tem diferentes níveis de comunicação:

- Comunicação p2p (protocolo Lightning Network)
- Canal de pagamento (protocolo Lightning Network)
- Transação Bitcoin (protocolo Bitcoin)

![explication](assets/fr/7.webp)


Para abrir um canal, os dois pares conversam por meio de um canal de comunicação:

- Alice: "Oi, quero abrir um canal!"
- Bob: "Ok, aqui está meu endereço público."

![explication](assets/fr/8.webp)

Agora, Alice tem 2 endereços públicos para criar um endereço multiassinatura 2/2. Ela pode agora fazer uma transação bitcoin para enviar dinheiro para lá.

Suponha que Alice tenha um UTXO de 0,002 BTC e que ela queira abrir um canal com Bob de 0,0013 BTC. Ela criará uma transação com 2 UTXOs de saída:

- um UTXO de 0,0013 para o endereço multiassinatura 2/2
- um UTXO de 0,0007 para um de seus endereços de troco (retorno dos UTXOs).

Essa transação ainda não é pública, pois, neste estágio, ela confia em Bob para desbloquear o dinheiro da multiassinatura.

Mas como fazer então?

Alice criará uma segunda transação, chamada "transação de retirada", antes de publicar o depósito dos fundos na multiassinatura.

![explication](assets/fr/9.webp)

A transação de retirada gastará os fundos do endereço multiassinatura para um endereço dela (antes que tudo seja publicado).
Une vez que as duas transações são construídas, Alice informa Bob que está feito e pede a ele uma assinatura com sua chave pública, explicando que assim ela poderá recuperar seus fundos se algo der errado. Bob concorda porque não é desonesto.
Alice pode, portanto, recuperar os fundos sozinha, pois já tem a assinatura de Bob. Ela publica as transações. O canal está aberto com agora 0,0013 BTC (130.000 SAT) do lado de Alice.

![explication](assets/fr/10.webp)

## Transação Lightning e de compromisso
<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

![cover](assets/fr/11.webp)


Agora, vamos analisar o que realmente acontece nos bastidores ao transferir fundos de um lado para o outro de um canal na Lightning Network, incluindo a noção de transação de compromisso. A transação de retirada/fechamento on-chain representa o estado do canal, garantindo a quem pertencem os fundos após cada transferência. Portanto, após uma transferência na Lightning Network, há uma atualização dessa transação/contrato não realizado entre os dois pares, Alice e Bob, criando assim uma mesma transação com o estado atual do canal no caso de um fechamento:

- Alice abre um canal com Bob com 130.000 SAT do seu lado. A transação de retirada aceita pelos dois em caso de fechamento diz que 130.000 SAT irão para Alice no fechamento, e Bob concorda porque é justo.

![cover](assets/fr/12.webp)

- Alice envia 30.000 SAT para Bob. Portanto, há uma nova transação de retirada que diz que, em caso de fechamento, Alice receberá 100.000 SAT e Bob 30.000 SAT. Ambos concordam porque é justo.

![cover](assets/fr/13.webp)

- Alice envia 10.000 SAT para Bob, uma nova transação de retirada é criada novamente para dizer que Alice recuperará 90.000 SAT e Bob 40.000 SAT. Ambos concordam porque é justo.

![cover](assets/fr/14.webp)


```
Estado inicial do canal:
Alice (130.000 SAT) =============== Bob (0 SAT)

Após a primeira transferência:
Alice (100.000 SAT) =============== Bob (30.000 SAT)

Após a segunda transferência:
Alice (90.000 SAT) =============== Bob (40.000 SAT)

```

O dinheiro nunca se move, mas o saldo final é atualizado por meio de uma transação assinada, mas não publicada on-chain. A transação de retirada é, portanto, uma transação de compromisso. As transferências de satoshis são outra transação de compromisso mais recente que atualiza o saldo.

## Transações de compromisso
<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>


Se as transações de compromisso ditam um estado do canal com a liquidez no momento X, é possível trapacear publicando um estado antigo? A resposta é sim, porque já temos a pré-assinatura dos dois participantes na transação não publicada.

![instruction](assets/fr/15.webp)

Para resolver esse problema, adicionamos complexidade:

- Timelock = fundos bloqueados até o bloco N
- Chave de revogação = segredo de Alice e segredo de Bob'

Ces dois elementos são adicionados à transação de compromisso. Portanto, Alice deve esperar pelo fim do Timelock, e qualquer pessoa que possua a chave de revogação pode mover os fundos sem esperar pelo fim do Timelock. Se Alice tentar trapacear, Bob usará a chave de revogação para roubar e punir Alice.

![instruction](assets/fr/16.webp)

A partir de agora (e na realidade), a transação de compromisso não é a mesma para Alice e Bob, eles são simétricos, mas cada um com diferentes restrições, eles se dão mutuamente seu segredo para criar a chave de revogação da transação de compromisso anterior. Portanto, na criação, Alice cria o canal com Bob, 130.000 SAT do seu lado, ela tem um Timelock que a impede de recuperar imediatamente seu dinheiro, ela deve esperar um pouco. A chave de revogação pode desbloquear o dinheiro, mas apenas Alice a tem (transação de compromisso de Alice). Uma vez que há uma transferência, Alice fornecerá seu segredo antigo a Bob e, portanto, este último poderá esvaziar o canal para o estado anterior no caso de Alice tentar trapacear (Alice é punida).

![instruction](assets/fr/17.webp)

Da mesma forma, Bob fornecerá seu segredo a Alice. Para que, se ele tentar trapacear, Alice possa puni-lo. A operação se repete a cada nova transação de compromisso. Um novo segredo é decidido e uma nova chave de revogação. Portanto, para cada nova transação, é necessário destruir a transação de compromisso anterior, fornecendo a chave de revogação. Assim, se Alice ou Bob tentar trapacear, o outro pode agir antes (graças ao Timelock) e, portanto, evitar uma trapaça. Na transação nº 3, portanto, o segredo da transação nº 2 é fornecido para permitir que Alice e Bob possam se defender contra Alice ou Bob.

![instruction](assets/fr/18.webp)

A pessoa que cria a transação com o Timelock (quem envia o dinheiro) pode usar a chave de revogação somente após o Timelock. No entanto, a pessoa que recebe o dinheiro pode usá-lo antes do Timelock em caso de trapaça de um lado para o outro de um canal na Lightning Network. Em particular, detalhamos os mecanismos que permitem se proteger de uma possível trapaça por parte do seu par no canal.

## Fechamento de canal
<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

Estamos interessados no fechamento de canal por meio de uma transação Bitcoin, que pode assumir diferentes formas dependendo do caso. Existem 3 tipos de fechamento de canal:

- O bom: fechamento cooperativo
- O bruto: fechamento forçado (não cooperativo)
- O trapaceiro: fechamento por um trapaceiro

![instruction](assets/fr/19.webp)
![instruction](assets/fr/20.webp)

### O bom

Os dois pares conversam e concordam em fechar o canal. Eles, portanto, param todas as transações e validam um estado final do canal. Eles concordam com as taxas de rede (a pessoa que abre o canal paga as taxas de fechamento). Eles agora criam a transação de fechamento. Portanto, há uma transação de fechamento, diferente das transações de compromisso, pois não há Timelock e chave de revogação. A transação é, portanto, publicada e Alice e Bob recebem seus respectivos saldos. Esse tipo de fechamento é rápido (porque não há Timelock) e geralmente barato.

![instruction](assets/fr/21.webp)

### O brutamontes

Alice quer fechar o canal, ela se comunica, mas Bob não responde porque está offline (corte de internet ou eletricidade). Alice, portanto, publicará a transação de compromisso mais recente (a última). A transação é, portanto, publicada e o Timelock é ativado. Então, as taxas foram decididas quando esta transação foi criada X tempo atrás! A MemPool é a rede que mudou desde então, o protocolo usa por padrão taxas 5 vezes maiores do que as atuais na criação da transação. Criação de taxas a 10 SAT, portanto, a transação considerou 50 SAT. No momento da publicação forçada, a transação de fechamento da rede é:

- 1 SAT = pago em excesso por 50\*
- 100 SAT = pago abaixo por 2\*

Isso torna o fechamento forçado mais longo (Timelock) e especialmente mais arriscado em termos de taxas e, portanto, possível validação pelos mineradores.

![instruction](assets/fr/22.webp)

### O trapaceiro

Alice tenta trapacear publicando uma transação de compromisso antiga. Mas Bob monitora a MemPool e observa se há transações tentando publicar antigas. Se ele encontrar, usará a chave de revogação para punir Alice e pegar todos os SAT do canal.

![instruction](assets/fr/23.webp)

Para concluir, o fechamento do canal na Lightning Network é uma etapa crucial que pode assumir várias formas. Em um fechamento cooperativo, ambas as partes se comunicam e concordam com um estado final do canal. Essa é a opção mais rápida e menos custosa. Por outro lado, um fechamento forçado ocorre quando uma das partes não responde. Essa é uma situação mais cara e mais longa devido às taxas de transação imprevisíveis e à ativação do Timelock. Finalmente, se um participante tentar trapacear publicando uma transação de compromisso antiga, o trapaceiro, ele pode ser punido perdendo todos os SAT do canal. Portanto, é crucial entender esses mecanismos para uma utilização eficiente e justa da Lightning Network.

# Uma rede de liquidez
<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network
<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

Neste sétimo capítulo, estudamos o funcionamento da Lightning como uma rede de canais e como os pagamentos são roteados de sua fonte para seu destino.
Lightning é uma rede de canais de pagamento. Milhares de pares com os seus próprios canais de liquidez estão ligados entre si e, portanto, auto-utilizados para efectuar transacções entre pares não ligados.

![cover](assets/fr/24.webp)
![cover](assets/fr/25.webp)

A liquidez dos canais não pode ser transferida para outros canais de liquidez.

Alice -> Eden - > Bob`. Os satoshis não se deslocaram de `Alice -> Bob`, mas de `Alice -> Eden`e de`Eden -> Bob`.

Assim, cada pessoa e cada canal têm uma liquidez diferente. Para efectuar pagamentos, é necessário encontrar uma rota na rede com liquidez suficiente. Se não houver liquidez suficiente, o pagamento não será efectuado.

Considere a seguinte rede:

```
Estado inicial da rede:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```

![cover](assets/fr/26.webp)

Se Alice tiver que fazer uma transferência de 40 SAT para Bob, então a liquidez será redistribuída ao longo da rota entre as duas partes.

```
Depois de Alice transferir 40 SAT para Bob :
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```
![cover](assets/fr/27.webp)

No entanto, no estado inicial, o Bob não pode enviar 40 SATs à Alice porque a Susie não tem liquidez com a Alice para lhe enviar 40 SATs, pelo que o pagamento não é possível através desta via. Precisamos, portanto, de outra via em que a transacção seja impossível.

No primeiro exemplo, é evidente que a Susie e o Eden não ganharam nem perderam nada. Para concordar em ser usado para encaminhar a transacção, os nós da Lightning Network cobram uma taxa!

Existem diferentes taxas consoante a localização da liquidez

Alice - Bob

- Taxa da Alice = Alice -> Bob
- Taxa do Bob = Bob -> Alice

![cover](assets/fr/28.webp)

Existem dois tipos de comissões:

- uma comissão fixa, independentemente do montante: 1 SAT (por defeito, mas pode ser alterada)
- uma taxa variável (0,01% por defeito)

Exemplo de taxa:

- Alice - Susie; 1/1 (1 taxa fixa e 1 taxa variável)
- Susie - Eden; 0/200
- Eden - Bob; 1/1

Por conseguinte :

- Taxa 1: (paga pela Alice a si própria) 1 + (40 000\*0,000001)
- Taxa 2: 0 + 40 000 \* 0,0002 = 8 SAT
- Custo 3: 1 + 40.000\* 0,000001 = 0,4 SAT

![cover](assets/fr/29.webp)

Envio :

1. Envio de 40 009,04 Alice -> Susie; Alice paga os seus próprios custos, pelo que não conta
2. A Susie faz o favor ao Eden de enviar 40 001,04, fica com esta comissão de 8 SAT
3. O Éden faz o serviço de enviar 40.000 ao Bob, fica com a sua comissão de 1,04 SAT.

A Alice pagou uma comissão de 9,04 SAT e o Bob recebeu 40.000 SAT.

![cover](assets/fr/30.webp)

Traduzido com a versão gratuita do tradutor - www.DeepL.com/TranslatorDans o LN, é o nó de Alice que decide a rota antes do envio. Portanto, há uma busca pela melhor rota e Alice é a única que conhece a rota e o preço. O pagamento é enviado, mas Susie não tem informações.

![cover](assets/fr/31.webp)

Para Susie ou Eden: eles não sabem quem é o destinatário final ou quem está enviando. Isso é um roteamento em cebola. O nó deve manter um plano da rede para encontrar sua rota, mas nenhum dos intermediários tem informações.

## HTLC - Contrato de tempo bloqueado e hash
<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

Em um sistema de roteamento clássico, como garantir que Eden não trapaceie e cumpra sua parte do contrato?

O HTLC é um contrato de pagamento que só pode ser desbloqueado com um segredo. Se não for revelado, o contrato expira. É, portanto, um pagamento condicional. Como eles são usados?

![instruction](assets/fr/32.webp)

Considere a seguinte situação
`Alice (100.000 SAT) ==== (30.000 SAT) Susie (250.000 SAT) ==== (0 SAT) Bob`

- Bob gera um segredo S (a pré-imagem) e calcula o hash r = hash(s)
- Bob envia uma fatura para Alice com "r"
- Alice envia um HTLC de 40.000 SAT para Susie com a condição de revelar "s'" tal que hash(s') = r
- Susie envia um HTLC semelhante a Bob
- Bob desbloqueia o HTLC de Susie mostrando "s"
- Susie desbloqueia o HTCL de Alice mostrando "S"

Se Bob estiver offline e nunca receber o segredo que lhe dá legitimidade para receber o dinheiro, neste caso, o HTLC expirará após um certo número de blocos.

![instruction](assets/fr/33.webp)

Os HTLCs expiram na ordem inversa: portanto, expiração Susie - Bob e depois Alice - Susie.
Assim, se Bob voltar, nada mudará. Caso contrário, se Alice cancelar enquanto Bob voltar, será uma bagunça e as pessoas podem ter trabalhado em vão.

E então, a pergunta é: no caso de fechamento, o que acontece? Na verdade, nossas transações de compromisso são ainda mais complexas. É necessário representar o saldo intermediário se o canal for fechado.

Portanto, há um HTLC-out de 40.000 satoshis (com as limitações vistas anteriormente) na transação de compromisso por meio de uma saída nº 3.

![instruction](assets/fr/34.webp)

Portanto, Alice tem na transação de compromisso:

- Saída nº 1: 60.000 SAT para Alice via Timelock e chave de revogação (o que resta)
- Saída nº 2: 30.000 que já pertencem a Susie
- Saída nº 3: 40.000 em HTLC

A transação de compromisso de Alice é com um HTCL-out porque ela envia um HTLC-in para a destinatária, Susie.

![instruction](assets/fr/35.webp)

Donc, si publicarmos esta transação de compromisso, Susie pode recuperar o dinheiro do HTCL com a imagem "s". Se ela não tiver a pré-imagem, Alice recupera o dinheiro uma vez que o HTCL expira. Pense nas saídas (UTXO) como pagamentos diferentes com diferentes condições.
Uma vez que o pagamento é feito (expiração ou execução), o estado do canal muda e a transação com HTCL não existe mais. Voltamos a algo clássico.
No caso de fechamento cooperativo: paramos os pagamentos e, portanto, aguardamos a execução das transferências / HTCL, a transação é leve, portanto, mais barata, pois há no máximo 1 ou 2 saídas.
Se forçado a fechar: publicamos com todos os HTLCs em andamento, tornando-se muito pesado e muito caro. E é uma bagunça.

Resumindo, o sistema de roteamento da Lightning Network usa Contratos Hash Time-Locked (HTLC) para garantir um pagamento seguro e verificável. Os HTLCs permitem pagamentos condicionais em que o dinheiro só pode ser desbloqueado com um segredo, garantindo que os participantes cumpram seus compromissos.
No exemplo apresentado, Alice deseja enviar SAT para Bob por meio de Susie. Bob gera um segredo, cria um hash dele e o transmite para Alice. Alice e Susie estabelecem um HTLC com base nesse hash. Uma vez que Bob desbloqueia o HTLC de Susie mostrando-lhe o segredo, Susie pode então desbloquear o HTLC de Alice.
No caso em que Bob não revela o segredo em um determinado período de tempo, o HTLC expira. A expiração ocorre na ordem inversa, garantindo que se Bob voltar online, não haja consequências indesejáveis.

No fechamento do canal, se for um fechamento cooperativo, os pagamentos são interrompidos e os HTLCs são resolvidos, o que geralmente é menos custoso. Se o fechamento for forçado, todas as transações HTLC em andamento são publicadas, o que pode se tornar muito caro e confuso.
Em resumo, o mecanismo HTLC adiciona uma camada adicional de segurança na Lightning Network, garantindo que os pagamentos sejam executados corretamente e que os usuários cumpram seus compromissos.

## Encontrando seu caminho
<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

A única informação pública é a capacidade total do canal (Alice + Bob), mas não sabemos onde está a liquidez.
Para obter mais informações, nosso nó ouve o canal de comunicação do LN para anúncios de novos canais e atualizações de taxas de canais. Seu nó também verifica o blockchain para o fechamento de canais.

Como não temos todas as informações, precisamos fazer uma pesquisa de gráfico / rota com as informações que temos (capacidade máxima dos canais e não onde está a liquidez).

Critérios:

- Probabilidade de sucesso - Taxas
- Prazo de expiração do HTLC
- Número de nós intermediários
- Aleatório

![graph](assets/fr/36.webp)

Portanto, se houver 3 rotas possíveis:

- Alice > 1 > 2 > 5 > Bob
- Alice > 1 > 2 > 4 > 5 > Bob
- Alice 1 > 2 > 3 > Bob

Procuramos, teoricamente, a melhor opção com as menores taxas e a maior chance de sucesso: o máximo de liquidez e o menor número de saltos possível.

Por exemplo, se 2-3 tiverem apenas 130.000 SAT de capacidade, enviar 100.000 é muito improvável, então a escolha nº 3 tem poucas chances de sucesso.

![graph](assets/fr/37.webp)

Agora que o algoritmo fez suas 3 escolhas, ele tentará a primeira:

Escolha 1:

- Alice envia um HTCL de 100.000 SAT para 1;
- 1 faz um HTLC de 100.000 SAT para 2;
- 2 faz um HTLC de 100.000 SAT para 5, exceto que o 5 não pode, então anuncia.

A informação é enviada de volta, então Alice decide tentar a segunda rota:

- Alice envia um HTLC de 100.000 para 1;
- 1 faz um HTLC de 100.000 para 2;
- 2 faz um HTLC de 100.000 para 4;
- 4 faz um HTLC de 100.000 para Bob. Bob tem a liquidez, então está tudo bem.
- Bob usa a pré-imagem (hash) do HTLC e, portanto, usa o segredo para recuperar os 100.000 SAT
- 5 agora tem o segredo do HTLC para recuperar o HTLC bloqueado de 4
- 4 agora tem o segredo do HTLC para recuperar o HTLC bloqueado de 2
- 2 agora tem o segredo do HTLC para recuperar o HTLC bloqueado de 1
- 1 agora tem o segredo do HTLC para recuperar o HTLC bloqueado de Alice

Alice não viu o fracasso da rota 1, ela apenas esperou um segundo a mais. Uma falha de pagamento ocorre quando não há rota possível. Para facilitar a busca por rotas, Bob pode fornecer informações a Alice para ajudar em sua fatura:

- O valor
- Seu endereço
- O hash da pré-imagem para que Alice possa criar o HTLC
- Indicações sobre os canais de Bob

Bob conhece a liquidez dos canais 5 e 3 porque está diretamente conectado a eles, ele pode indicar isso a Alice. Ele avisa Alice que o nó 3 é inútil, o que evita que Alice potencialmente faça sua rota.
Outro elemento seriam os canais privados (portanto, não publicados na rede) que Bob pode ter. Se Bob tiver um canal privado com 1, ele pode dizer a Alice para usá-lo e isso daria Alice > 1 > Bob'

![graph](assets/fr/38.webp)

Em conclusão, o roteamento de transações na Lightning Network é um processo complexo que requer a consideração de vários fatores. Embora a capacidade total dos canais seja pública, a distribuição precisa da liquidez não é diretamente acessível. Isso obriga os nós a estimar as rotas mais prováveis de sucesso, levando em consideração critérios como taxas, prazo de validade do HTLC, número de nós intermediários e um fator aleatório. Quando várias rotas são possíveis, os nós procuram minimizar as taxas e maximizar as chances de sucesso escolhendo canais com liquidez suficiente e um número mínimo de saltos. Se uma tentativa de transação falhar devido a liquidez insuficiente, outra rota é tentada até que uma transação seja bem-sucedida.

Além disso, para facilitar a busca por rotas, o destinatário pode fornecer informações adicionais, como endereço, valor, hash da pré-imagem e indicações sobre seus canais. Isso pode ajudar a identificar canais com liquidez suficiente e evitar tentativas de transações desnecessárias. Em última análise, o sistema de roteamento da Lightning Network é projetado para otimizar a velocidade, segurança e eficiência das transações, preservando a privacidade dos usuários.

# Ferramentas da Lightning Network
<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Fatura, LNURL, Keysend
<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

![cover](assets/fr/39.webp)

Uma fatura LN (ou invoice) é longa e não é agradável de ler, mas permite representar de forma densa uma solicitação de pagamento.

Exemplo:
lnbc1m1pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3

- lnbc1m = parte legível
- 1 = separação com o restante
- Em seguida, o restante
- Bc1 = Codificação Bech32 (base 32), portanto, são usados 32 caracteres.
- 10 = 1.2.3.4.5.6.7.8.9.0
- 26 = abcdefghijklmnopqrstuvwxyz
- 32 = não o "b-i-o" e não o "1"

### lnbc1m

- ln = Lightning
- Bc = bitcoin (mainnet)
- 1 = valor
- M = milli (10*-3 / u = micro 10*-6 / n = nano 10*-9 / p = pico 10*-12'
  Ici 1m = 1 \* 0.0001btc = 100 000 BTC
  "Por favor, pague 100.000 SAT na rede Lightning da mainnet do Bitcoin para pskuawzpp5qeuuva2txazy5g483tuv9pznn9ft8l5e49s5dndj2pqq0ptyn8msdqqcqzpgxqrrsssp5v4s00u579atm0em6eqm9nr7d0vr64z5j2sm5s33x3r9m4lgfdueq9qyyssqxkjzzgx5ef7ez3dks0laxayx4grrw7j22ppgzyhpydtv6hmc39skf9hjxn5yd3kvv7zpjdxd2s7crcnemh2fz26mnr6zu83w0a2fwxcqnvujl3"

### Timestamp (quando foi criado)

Ele contém 0 ou mais partes adicionais:

- Hash da pré-imagem
- Segredo de pagamento (roteamento em cebola)
- Dados arbitrários
- Chave pública LN do destinatário
- Duração de validade (padrão de 1 hora)
- Indicações de roteamento
- Assinatura do conjunto

Existem outros tipos de faturas. O meta-protocolo LNURL permite fornecer um valor em satoshis diretamente em vez de fazer uma solicitação. Isso é muito flexível e permite muitas melhorias em termos de experiência do usuário.

![cover](assets/fr/40.webp)

Um Keysend permite que Alice envie dinheiro para Bob sem ter a solicitação de Bob. Alice obtém o ID de Bob, cria uma pré-imagem sem perguntar a Bob e a inclui em seu envio. Portanto, Bob receberá uma solicitação surpresa onde ele pode desbloquear o dinheiro porque Alice já fez o trabalho.

![cover](assets/fr/41.webp)

Em conclusão, uma fatura da Lightning Network, embora complexa à primeira vista, codifica efetivamente uma solicitação de pagamento. Cada seção da fatura contém informações importantes, incluindo o valor a ser pago, o destinatário, o timestamp de criação e potencialmente outras informações, como o hash da pré-imagem, o segredo de pagamento, as indicações de roteamento e a duração de validade. Protocolos como LNURL e Keysend oferecem melhorias significativas em termos de flexibilidade e experiência do usuário, permitindo, por exemplo, enviar fundos sem solicitação prévia da outra parte. Essas tecnologias tornam o processo de pagamento mais fluido e eficiente na Lightning Network.

## Gerenciando sua liquidez
<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

![instruction](assets/fr/42.webp)


Damos algumas orientações gerais para responder à pergunta constante sobre gerenciamento de liquidez no Lightning.

No LN, existem 3 tipos de pessoas:

- Compradores: eles têm liquidez de saída, é o mais simples, pois basta abrir canais
- Comerciantes: é mais complicado, pois precisam de liquidez de entrada por meio de outros nós e outros atores. Eles devem ter pessoas conectadas a eles
- Nós de roteamento: eles querem estar equilibrados com liquidez em ambos os lados e uma boa conexão com muitos nós para serem usados o máximo possível

Portanto, se você precisar de liquidez de entrada, pode comprá-la de serviços.

![instruction](assets/fr/43.webp)

Alice compra um canal com Susie por 1 milhão de satoshis, então ela abre um canal com 1.000.000 SAT diretamente do lado de entrada. Ela pode então aceitar até 1 milhão de SAT de pagamento pelos clientes que estariam conectados com Susie (que está muito conectada).

Outra solução seria fazer pagamentos; você paga 100.000 por X motivo, agora pode receber 100.000.

![instruction](assets/fr/44.webp)

### Solução Loop Out: Atomic swap LN - BTC

Alice 2 milhões - Susie 0

![instruction](assets/fr/45.webp)

Alice quer enviar a liquidez para Susie, então ela faz um Loop out (um nó especial que oferece um serviço profissional de reequilíbrio LN/BTC).
Alice envia 1 milhão para o loop através do nó de Susie, então Susie tem a liquidez e o Loop retorna o saldo on-chain para o nó de Alice.

![instruction](assets/fr/46.webp)

Portanto, os 1 milhão vão para Susie, esta envia 1 milhão para o Loop, o Loop envia 1 milhão para Alice. Alice moveu a liquidez para Susie ao preço de algumas taxas pagas ao Loop pelo serviço.

O mais complicado no LN é manter a liquidez.

![instruction](assets/fr/47.webp)

Em conclusão, a gestão de liquidez na rede Lightning Network é um desafio chave, que depende do tipo de usuário: comprador, comerciante ou nó de roteamento. Compradores, que precisam de liquidez de saída, têm a tarefa mais simples: eles simplesmente abrem canais. Comerciantes, que precisam de liquidez de entrada, devem estar conectados a outros nós e atores. Os nós de roteamento, por sua vez, buscam manter um equilíbrio de liquidez em ambos os lados. Existem várias soluções para gerenciar a liquidez, como a compra de canais ou o pagamento para aumentar a capacidade de recebimento. A opção "Loop Out", permitindo uma troca atômica entre LN e BTC, oferece uma solução interessante para reequilibrar a liquidez. Apesar dessas estratégias, manter a liquidez na rede Lightning Network continua sendo um desafio complexo.

# Vá além
<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## Resumo da formação
<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

Nosso objetivo era explicar como a rede Lightning funciona e como ela se baseia no Bitcoin para funcionar.

A rede Lightning é uma rede de canais de pagamento. Vimos como um canal de pagamento funciona entre duas partes interessadas, mas também ampliamos nossa visão para toda a rede, para a noção de rede de canais de pagamento.

![instruction](assets/fr/48.webp)

Os canais são abertos por meio de uma transação Bitcoin e podem acomodar o máximo de transações possível. O estado do canal é representado por uma transação de compromisso que envia para cada uma das partes interessadas o que ela possui do seu lado do canal. Quando uma transação ocorre dentro do canal, as partes interessadas se comprometem com o novo estado, revogando o antigo estado e construindo uma nova transação de compromisso.

![instruction](assets/fr/49.webp)

Os pares se protegem contra trapaças com chaves de revogação e um bloqueio de tempo. O fechamento mútuo consentido é preferido para fechar o canal. Em caso de fechamento forçado, a última transação de compromisso é publicada.

![instruction](assets/fr/50.webp)

Os pagamentos podem usar os canais de outros nós intermediários. Pagamentos condicionais à pré-imagem (HTLC) permitem bloquear fundos enquanto o pagamento é completamente resolvido. O roteamento em cebola é usado na Lightning Network. Os nós intermediários não conhecem o destino final dos pagamentos. Alice deve calcular a rota do pagamento, mas não tem todas as informações sobre a liquidez nos canais intermediários.

![instruction](assets/fr/51.webp)

Há uma componente de probabilidade ao enviar um pagamento via Lightning Network. 

![instruction](assets/fr/52.webp)

Para receber pagamentos, é necessário gerenciar a liquidez nos canais, o que pode ser feito pedindo a outras pessoas para abrir canais conosco, abrindo canais nós mesmos e usando ferramentas como Loop ou comprando/alugando canais em marketplaces.

## Entrevista com Fanis
<chapterId>077cb5f5-1626-5da5-9964-e67b1de503bf</chapterId>

Aqui está um resumo da entrevista:

A Lightning Network é uma solução de pagamento ultra-rápida no Bitcoin que permite contornar as limitações relacionadas à escalabilidade da rede. No entanto, os bitcoins na Lightning não são tão seguros quanto os da cadeia Bitcoin, pois a descentralização e a segurança são privilegiadas em detrimento da escalabilidade.

O aumento excessivo do tamanho dos blocos não é uma boa solução, pois isso compromete os nós e a capacidade de dados. Em vez disso, a Lightning Network permite criar canais de pagamento entre dois usuários do Bitcoin sem que as transações apareçam na blockchain, economizando espaço nos blocos e permitindo que o Bitcoin escale hoje.

No entanto, há críticas em relação à escalabilidade e centralização da Lightning Network, com potenciais problemas relacionados ao fechamento de canais e altas taxas de transação. Para resolver esses problemas, é recomendável evitar a abertura de pequenos canais para evitar problemas futuros e aumentar as taxas de transação com Child Pay for Parent.

Soluções consideradas para o futuro da Lightning Network são o batching e a criação de canais em grupos para reduzir as taxas de transação, bem como o aumento do tamanho dos blocos a longo prazo. No entanto, é importante notar que os bitcoins na Lightning não são tão seguros quanto os bitcoins na cadeia Bitcoin.

A privacidade no Bitcoin e na Lightning estão relacionadas, com o roteamento em cebola garantindo um certo nível de privacidade para as transações. No entanto, no Bitcoin, tudo é transparente por padrão, com heurísticas usadas para rastrear os Bitcoins de endereço em endereço na cadeia Bitcoin.

Compras de Bitcoins com KYC permitem que a exchange conheça as transações de retirada, enquanto os montantes redondos e os endereços de troca permitem saber qual parte de uma transação é destinada a outra pessoa e qual parte é destinada a si mesmo.

Para melhorar a privacidade, ações conjuntas e coinjoins permitem quebrar os cálculos de probabilidade fazendo transações em que várias pessoas fazem uma transação juntas. As empresas de análise de cadeias têm mais dificuldade em determinar o que você está fazendo com seus bitcoins seguindo.

Na Lightning, apenas duas pessoas estão cientes da transação e é mais confidencial do que o Bitcoin. O roteamento em cebola significa que um nó intermediário não conhece o remetente e o destinatário do pagamento.

Para usar a Lightning Network, é recomendável seguir um treinamento em seu canal do YouTube ou diretamente no site descubra Bitcoin, ou usar o treinamento em Umbrell. Também é possível enviar texto arbitrário durante um pagamento na Lightning usando um campo dedicado para isso, o que pode ser útil para doações ou mensagens.
Cependant, é importante notar que os nós de roteamento no Lightning podem ser regulados no futuro, com alguns estados tentando regular os nós de roteamento.
Para os comerciantes, é necessário gerenciar a liquidez para aceitar pagamentos na Lightning Network, com restrições atuais que podem ser superadas com soluções apropriadas.

Por fim, o futuro do Bitcoin é promissor, com uma possível projeção de um milhão em cinco anos. Para garantir a profissionalização da indústria e a criação de um sistema alternativo ao sistema bancário existente, é importante contribuir para a rede e parar de confiar.



## Dê-nos seu feedback sobre este curso
<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>
<isCourseReview>true</isCourseReview>

## Exame Final
<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>
<isCourseExam>true</isCourseExam>

## Agradecimentos e continue a cavar a toca do coelho
<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

Parabéns! 🎉
Você concluiu o treinamento LN 201 - Introdução à Lightning Network!
Você pode se orgulhar, pois não é fácil. Saiba que poucas pessoas descem tão fundo na toca do Bitcoin.

Em primeiro lugar, um grande obrigado a Fanis Makalakis por nos oferecer este ótimo curso gratuito sobre um aspecto mais étnico do Lightning. Não hesite em segui-lo no Twitter, em seu blog ou por meio de seu trabalho na LN market.

Em seguida, se você deseja ajudar o projeto, não hesite em nos patrocinar no Patreon. Suas doações serão usadas para produzir conteúdo para novos treinamentos e, é claro, você será o primeiro a ser informado (incluindo o próximo de Fanis que está em andamento!).

A aventura da Lightning Network continua com o treinamento em Umbrel e a configuração de um nó da Lightning Network. Chega de teoria e vamos para a prática com o treinamento LN 202 agora!

Beijos e até breve!

Rogzy'
