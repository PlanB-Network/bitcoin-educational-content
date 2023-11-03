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

Bem-vindo ao mundo emocionante da Lightning Network, uma segunda camada do Bitcoin, que é uma avançada tecnológica sofisticada e rica em potencialidades. Estamos prestes a mergulhar nas profundezas técnicas desta tecnologia, sem nos concentrarmos em tutoriais ou cenários de uso específicos. Para aproveitar ao máximo esta formação, é indispensável ter uma sólida compreensão do Bitcoin. É uma experiência que requer uma abordagem séria e concentrada. Também podes considerar seguir o curso LN 202 em paralelo, que oferece um aspecto mais prático para esta exploração. Prepara-te para embarcar numa jornada que pode mudar a tua percepção do ecossistema Bitcoin.

Boa descoberta!

+++

# Os fundamentais
## Compreender a Lightning Network

![Compreender a Lightning Network](https://youtu.be/PszWk046x-I)

A rede Lightning é uma infraestrutura de pagamento de segunda camada, construída na rede Bitcoin, que permite transações rápidas e de baixo custo. Para entender completamente como funciona a rede Lightning, é essencial entender o que são os canais de pagamento e como eles funcionam.

Um canal de pagamento na Lightning é uma espécie de "via privada" entre dois utilizadores, que permite transações Bitcoin rápidas e repetitivas. Quando um canal é aberto, ele tem uma capacidade fixa, que é definida antecipadamente pelos utilizadores. Essa capacidade representa o valor máximo de Bitcoin que pode ser transferido no canal em um determinado momento.

Os canais de pagamento são bidirecionais, o que significa que eles têm dois "lados". Por exemplo, se Alice e Bob abrirem um canal de pagamento, Alice pode enviar Bitcoin para Bob e Bob pode enviar Bitcoin para Alice. As transações dentro do canal não alteram a capacidade total do canal, mas alteram a distribuição dessa capacidade entre Alice e Bob.

![explication](assets/chapitre1/0.JPG)

Para que uma transação seja possível num canal de pagamento Lightning, o usuário que envia os fundos deve ter Bitcoin suficiente do seu lado do canal. Se Alice quiser enviar 1 Bitcoin para Bob através do canal deles, ela deve ter pelo menos 1 Bitcoin do seu lado do canal.
Limites e Funcionamento dos Canais de Pagamento na Lightning.
Embora a capacidade de um canal de pagamento Lightning seja fixa, isso não limita o número total de transações ou o volume total de Bitcoin que pode ser transferido através do canal. Por exemplo, se Alice e Bob têm um canal com capacidade de 1 Bitcoin, eles podem realizar centenas de transações de 0,01 Bitcoin ou milhares de transações de 0,001 Bitcoin, desde que a capacidade total do canal não seja excedida em um determinado momento.

Apesar dessas limitações, os canais de pagamento Lightning são uma maneira eficaz de realizar transações Bitcoin rápidas e baratas. Eles permitem que os usuários enviem e recebam Bitcoin sem ter que pagar altas taxas de transação ou esperar longos períodos de confirmação na rede Bitcoin.

Em resumo, os canais de pagamento no Lightning oferecem uma solução poderosa para aqueles que desejam realizar transações Bitcoin rápidas e baratas. No entanto, é essencial entender o seu funcionamento e as suas limitações para aproveitá-los ao máximo.

![explication](assets/chapitre1/1.JPG)

Exemplo:

- Alice tem 100.000 SAT
- Bob tem 30.000 SAT

Este é o estado atual do canal. Numa transação, Alice decide enviar 40.000 SAT para Bob. Ela pode fazer isso porque 40.000 <100.000.

O novo estado do canal é, portanto:

- Alice 60.000 SAT
- Bob 70.000 SAT

```
Estado inicial do canal:
Alice (100.000 SAT) ============== Bob (30.000 SAT)

Após a transferência de Alice para Bob de 40.000 SAT:
Alice (60.000 SAT) ============== Bob (70.000 SAT)

```

![explication](assets/chapitre1/2.JPG)

Agora, Bob deseja enviar 80.000 SAT para Alice. Não tendo a liquidez, ele não pode. A capacidade máxima do canal é de 130.000 SAT, com um gasto possível de até 60.000 SAT para Alice e 70.000 SAT para Bob.

![explication](assets/chapitre1/3.JPG)

## Bitcoin, endereços, UTXO e transações

![bitcoin, endereços, utxo e transações](https://youtu.be/cadCJ2V7zTg)

Neste segundo capítulo, dedicamos tempo para estudar como as transações Bitcoin realmente funcionam, o que será muito útil para entender o Lightning. Também nos concentramos por um momento no conceito de endereço multiassinatura, que é fundamental para entender o próximo capítulo dedicado à abertura de canais na Lightning Network.

- Chave privada> Chave pública> Endereço: Em uma transação, Alice envia dinheiro para Bob. Este último fornece um endereço dado pela sua chave pública. Alice, que recebeu o dinheiro num endereço através da sua chave pública, agora usa a sua chave privada para assinar a transação e desbloquear os bitcoins do endereço.
- Numa transação, em Bitcoin, todos os bitcoins devem se mover. Chamado de UTXO (Unspend Transaction Output), os pedaços de bitcoin vão todos sair para depois retornar ao proprietário.

Alice tem 0,002 BTC, Bob tem 0 BTC. Alice decide enviar 0,0015 BTC para Bob. Ela assina uma transação de 0,002 BTC, onde 0,0015 vão para Bob e 0,0005 voltam para sua carteira. 

![explication](assets/chapitre2/0.JPG)

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

No Lightning Network, usamos multiassinaturas. Portanto, são necessárias 2 assinaturas para desbloquear os fundos, ou seja, duas chaves privadas para mover o dinheiro. Portanto, pode ser que Alice e Bob, juntos, devem concordar em desbloquear o dinheiro (UTXO). No LN especificamente, são transações 2/2, portanto, são necessárias as 2 assinaturas, ao contrário das multiassinaturas 2/3 ou 3/5, onde é necessária apenas uma combinação do número completo de chaves.

![explication](assets/chapitre2/1.JPG)

# Abertura e fechamento dos canais

## Abertura de canal

![abrir um canal](https://youtu.be/B2caBC0Rxko)

Agora, vamos aprofundar sobre a abertura de canal e como ela é realizada por meio de uma transação Bitcoin.

O Lightning Network tem diferentes níveis de comunicação:

- Comunicação p2p (protocolo Lightning Network)
- Canal de pagamento (protocolo Lightning Network)
- Transação Bitcoin (protocolo Bitcoin)

![explication](assets/chapitre3/0.JPG)


Para abrir um canal, os dois pares conversam por meio de um canal de comunicação:

- Alice: "Oi, quero abrir um canal!"
- Bob: "Ok, aqui está o meu endereço público."

![explication](assets/chapitre3/1.JPG)

Agora, Alice tem 2 endereços públicos para criar um endereço multiassinatura 2/2. Ela pode agora fazer uma transação bitcoin para enviar dinheiro para lá.

Suponha que Alice tenha um UTXO de 0,002 BTC e que ela queira abrir um canal com Bob de 0,0013 BTC. Ela criará uma transação com 2 UTXOs de saída:

- um UTXO de 0,0013 para o endereço multiassinatura 2/2
- um UTXO de 0,0007 para um dos seus endereços de troco (retorno dos UTXOs).

Essa transação ainda não é pública, pois, nesta altura, ela confia em Bob para desbloquear o dinheiro da multiassinatura.

Mas como fazer então?

Alice criará uma segunda transação, chamada "transação de retirada", antes de publicar o depósito dos fundos na multiassinatura.

![explication](assets/chapitre3/2.JPG)

A transação de retirada gastará os fundos do endereço multiassinatura para um endereço dela (antes que tudo seja publicado).
Une vez que as duas transações são construídas, Alice informa Bob que está feito e pede-lhe uma assinatura com a sua chave pública, explicando que assim ela poderá recuperar os seus fundos se algo der errado. Bob concorda porque não é desonesto.
Alice pode, portanto, recuperar os fundos sozinha, pois já tem a assinatura de Bob. Ela publica as transações. O canal está aberto com agora 0,0013 BTC (130.000 SAT) do lado de Alice.

![explication](assets/chapitre3/3.JPG)

## Transação Lightning e de compromisso

![transação lightning e transação de compromisso](https://youtu.be/aPqI34tpypM)

![cover](assets/chapitre4/1.JPG)


Agora, vamos analisar o que realmente acontece nos bastidores ao transferir fundos de um lado para o outro de um canal na Lightning Network, incluindo a noção de transação de compromisso. A transação de retirada/fechamento on-chain representa o estado do canal, garantindo a quem pertencem os fundos após cada transferência. Portanto, após uma transferência na Lightning Network, há uma atualização dessa transação/contrato não realizado entre os dois pares, Alice e Bob, criando assim uma mesma transação com o estado atual do canal no caso de um fechamento:

- Alice abre um canal com Bob com 130.000 SAT do seu lado. A transação de retirada aceite pelos dois em caso de fechamento diz que 130.000 SAT irão para Alice no fechamento, e Bob concorda porque é justo.

![cover](assets/chapitre4/2.JPG)

- Alice envia 30.000 SAT para Bob. Portanto, há uma nova transação de retirada que diz que, em caso de fechamento, Alice receberá 100.000 SAT e Bob 30.000 SAT. Ambos concordam porque é justo.

![cover](assets/chapitre4/3.JPG)

- Alice envia 10.000 SAT para Bob, uma nova transação de retirada é criada novamente para dizer que Alice recuperará 90.000 SAT e Bob 40.000 SAT. Ambos concordam porque é justo.

![cover](assets/chapitre4/4.JPG)


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

![transações parte 2](https://youtu.be/RRvoVTLRJ84)

Se as transações de compromisso ditam um estado do canal com a liquidez no momento X, é possível enganar publicando um estado antigo? A resposta é sim, porque já temos a pré-assinatura dos dois participantes na transação não publicada.

![instruction](assets/Chapitre5/0.JPG)

Para resolver esse problema, adicionamos complexidade:

- Timelock = fundos bloqueados até ao bloco N
- Chave de revogação = segredo de Alice e segredo de Bob'

Estes dois elementos são adicionados à transação de compromisso. Portanto, Alice deve esperar pelo fim do Timelock, e qualquer pessoa que possua a chave de revogação pode mover os fundos sem esperar pelo fim do Timelock. Se Alice tentar enganar Bob, Bob usará a chave de revogação para roubar e punir Alice.

![instruction](assets/Chapitre5/1.JPG)

A partir de agora (e na realidade), a transação de compromisso não é a mesma para Alice e Bob, eles são simétricos, mas cada um com diferentes restrições, eles dão-se mutuamente o seu segredo para criar a chave de revogação da transação de compromisso anterior. Portanto, na criação, Alice cria o canal com Bob, 130.000 SAT do seu lado, ela tem um Timelock que a impede de recuperar imediatamente o seu dinheiro, ela deve esperar um pouco. A chave de revogação pode desbloquear o dinheiro, mas apenas Alice a tem (transação de compromisso de Alice). Uma vez que há uma transferência, Alice fornecerá o seu segredo antigo a Bob e, portanto, este último poderá esvaziar o canal para o estado anterior no caso de Alice tentar enganá-lo (Alice é punida).

![instruction](assets/Chapitre5/2.JPG)

Da mesma forma, Bob fornecerá o seu segredo a Alice. Para que, se ele tentar enganá-la, Alice possa puni-lo. A operação se repete a cada nova transação de compromisso. Um novo segredo é decidido e uma nova chave de revogação. Portanto, para cada nova transação, é necessário destruir a transação de compromisso anterior, fornecendo a chave de revogação. Assim, se Alice ou Bob tentarem enganar-se, o outro pode agir antes (graças ao Timelock) e, portanto, evitar uma fraude. Na transação nº 3, portanto, o segredo da transação nº 2 é fornecido para permitir que Alice e Bob possam se defender um contra o outro.

![instruction](assets/Chapitre5/3.JPG)

A pessoa que cria a transação com o Timelock (quem envia o dinheiro) pode usar a chave de revogação somente após o Timelock. No entanto, a pessoa que recebe o dinheiro pode usá-lo antes do Timelock em caso de fraude de um lado para o outro num canal da Lightning Network. Em particular, detalhamos os mecanismos que permitem se proteger de uma possível fraude por parte do seu par no canal.

## Fechamento de canal

![fechar um canal](https://youtu.be/FVmQvNpVW8Y)

Estamos interessados no fechamento de canal por meio de uma transação Bitcoin, que pode assumir diferentes formas dependendo do caso. Existem 3 tipos de fechamento de canal:

- O bom: fechamento cooperativo
- O bruto: fechamento forçado (não cooperativo)
- O fraudulento: fechamento por um fraudador

![instruction](assets/chapitre6/1.JPG)
![instruction](assets/chapitre6/0.JPG)

### O bom

Os dois pares conversam e concordam em fechar o canal. Ambos, portanto, param todas as transações e validam um estado final do canal. Concordam com as taxas de rede (a pessoa que abre o canal paga as taxas de fechamento). E criam então a transação de fechamento. Portanto, há uma transação de fechamento, diferente das transações de compromisso, pois não há Timelock e chave de revogação. A transação é, portanto, publicada e Alice e Bob recebem os seus respectivos saldos. Esse tipo de fechamento é rápido (porque não há Timelock) e geralmente barato.

![instruction](assets/chapitre6/3.JPG)

### O bruto

Alice quer fechar o canal, e comunica isso a Bob, mas Bob não responde porque está offline (corte de internet ou eletricidade). Alice publicará então a transação de compromisso mais recente (a última). A transação é, portanto, publicada e o Timelock é ativado. Então, as taxas foram decididas quando esta transação foi criada X tempo atrás! A MemPool é a rede que mudou desde então, o protocolo usa por padrão taxas 5 vezes maiores do que as atuais na criação da transação. Criação de taxas a 10 SAT, portanto, a transação considerou 50 SAT. No momento da publicação forçada, a transação de fechamento da rede é:

- 1 SAT = pago em excesso por 50\*
- 100 SAT = pago abaixo por 2\*

Isso torna o fechamento forçado mais longo (Timelock) e especialmente mais arriscado em termos de taxas e, portanto, possível validação pelos mineradores.

![instruction](assets/chapitre6/4.JPG)

### O fraudulento

Alice faz uma tentativa de fraude publicando uma transação de compromisso antiga. Mas Bob monitora a MemPool e observa se há transações tentando publicar antigas. Se ele encontrar, usará a chave de revogação para punir Alice e pegar todos os SAT do canal.

![instruction](assets/chapitre6/5.JPG)

Para concluir, o fechamento do canal na Lightning Network é uma etapa crucial que pode assumir várias formas. Num fechamento cooperativo, ambas as partes se comunicam e concordam com um estado final do canal. Essa é a opção mais rápida e menos custosa. Por outro lado, um fechamento forçado ocorre quando uma das partes não responde. Essa é uma situação mais cara e mais longa devido às taxas de transação imprevisíveis e à ativação do Timelock. Por fim, se um participante tentar cometer fraude publicando uma transação de compromisso antiga, o fraudulento pode ser punido perdendo todos os SAT do canal. Portanto, é crucial entender estes mecanismos para uma utilização eficiente e justa da Lightning Network.

# Uma rede de liquidez
## Lightning Network

![Lightning Network](https://youtu.be/RAZAa3v41DM)

Neste sétimo capítulo, estudamos o funcionamento da Lightning como uma rede de canais e como os pagamentos são mapeados da sua fonte para o seu destino.
Lightning é uma rede de canais de pagamento. Milhares de pares com os seus próprios canais de liquidez estão ligados entre si e, portanto, são auto-utilizados para efectuar transacções entre pares não ligados.

![cover](assets/Chapitre7/0.JPG)
![cover](assets/Chapitre7/1.JPG)

A liquidez dos canais não pode ser transferida para outros canais de liquidez.

Alice -> Eden - > Bob`. Os satoshis não se deslocaram de `Alice -> Bob`, mas de `Alice -> Eden`e de`Eden -> Bob`.

Assim, cada pessoa e cada canal tem uma liquidez diferente. Para efectuar pagamentos, é necessário encontrar uma rota na rede com liquidez suficiente. Se não houver liquidez suficiente, o pagamento não será efectuado.

Considere a seguinte rede:

```
Estado inicial da rede:
Alice (130 SAT) ==== (0 SAT) Susie (90 SAT) ==== (200 SAT) Eden (150 SAT) ==== (100 SAT) Bob
```

![cover](assets/Chapitre7/2.JPG)

Se Alice tiver que fazer uma transferência de 40 SAT para Bob, então a liquidez será redistribuída ao longo da rota entre as duas partes.

```
Depois de Alice transferir 40 SAT para Bob :
Alice (90 SAT) ==== (40 SAT) Susie (50 SAT) ==== (240 SAT) Eden (110 SAT) ==== (140 SAT) Bob
```
![cover](assets/Chapitre7/4.JPG)

No entanto, no estado inicial, o Bob não pode enviar 40 SATs à Alice porque a Susie não tem liquidez com a Alice para lhe enviar 40 SATs, pelo que o pagamento não é possível através desta via. Precisamos, portanto, de outra via em que a transacção seja possível.

No primeiro exemplo, é evidente que a Susie e o Eden não ganharam nem perderam nada. Para concordar em ser usado para encaminhar a transacção, os nós da Lightning Network cobram uma taxa!

Existem diferentes taxas consoante a localização da liquidez

Alice - Bob

- Taxa da Alice = Alice -> Bob
- Taxa do Bob = Bob -> Alice

![cover](assets/Chapitre7/5.JPG)

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

![cover](assets/Chapitre7/6.JPG)

Envio :

1. Envio de 40 009,04 Alice -> Susie; Alice paga os seus próprios custos, pelo que não conta
2. A Susie faz o favor ao Eden de enviar 40 001,04, fica com esta comissão de 8 SAT
3. O Éden faz o serviço de enviar 40.000 ao Bob, fica com a sua comissão de 1,04 SAT.

A Alice pagou uma comissão de 9,04 SAT e o Bob recebeu 40.000 SAT.

![cover](assets/Chapitre7/7.JPG)

o LN, é o nó de Alice que decide a rota antes do envio. Portanto, há uma busca pela melhor rota e Alice é a única que conhece a rota e o preço. O pagamento é enviado, mas Susie não tem informações.

![cover](assets/Chapitre7/9.JPG)

Para Susie ou Eden: eles não sabem quem é o destinatário final ou quem está enviando. Isso é um roteamento em cebola. O nó deve manter um plano da rede para encontrar sua rota, mas nenhum dos intermediários tem informações.

## HTLC - Contrato de tempo bloqueado e hash

![HTLC](https://youtu.be/-JC4mkq7H48)

Num sistema de roteamento clássico, como garantir que Eden não cometa fraude e cumpra a sua parte do contrato?

O HTLC é um contrato de pagamento que só pode ser desbloqueado com um segredo. Se não for revelado, o contrato expira. É, portanto, um pagamento condicional. Como eles são usados?

![instruction](assets/chapitre8/0.JPG)

Considere a seguinte situação
`Alice (100.000 SAT) ==== (30.000 SAT) Susie (250.000 SAT) ==== (0 SAT) Bob`

- Bob gera um segredo S (a pré-imagem) e calcula o hash r = hash(s)
- Bob envia uma fatura para Alice com "r"
- Alice envia um HTLC de 40.000 SAT para Susie com a condição de revelar "s'" tal que hash(s') = r
- Susie envia um HTLC semelhante a Bob
- Bob desbloqueia o HTLC de Susie mostrando "s"
- Susie desbloqueia o HTCL de Alice mostrando "S"

Se Bob estiver offline e nunca receber o segredo que lhe dá legitimidade para receber o dinheiro, neste caso, o HTLC expirará após um certo número de blocos.

![instruction](assets/chapitre8/1.JPG)

Os HTLCs expiram na ordem inversa: portanto, expiração Susie - Bob e depois Alice - Susie.
Assim, se Bob voltar, nada mudará. Caso contrário, se Alice cancelar enquanto Bob voltar, será uma confusão e as pessoas podem ter trabalhado em vão.

E então, a pergunta é: no caso de fechamento, o que acontece? Na verdade, as nossas transações de compromisso são ainda mais complexas. É necessário representar o saldo intermediário se o canal for fechado.

Portanto, há um HTLC-out de 40.000 satoshis (com as limitações vistas anteriormente) na transação de compromisso por meio de uma saída nº 3.

![instruction](assets/chapitre8/2.JPG)

Portanto, Alice tem na transação de compromisso:

- Saída nº 1: 60.000 SAT para Alice via Timelock e chave de revogação (o que resta)
- Saída nº 2: 30.000 que já pertencem a Susie
- Saída nº 3: 40.000 em HTLC

A transação de compromisso de Alice é com um HTCL-out porque ela envia um HTLC-in para a destinatária, Susie.

![instruction](assets/chapitre8/3.JPG)

Assim, se publicarmos esta transação de compromisso, Susie pode recuperar o dinheiro do HTCL com a imagem "s". Se ela não tiver a pré-imagem, Alice recupera o dinheiro uma vez que o HTCL expira. Pensa nas saídas (UTXO) como pagamentos diferentes com diferentes condições.
Uma vez que o pagamento é feito (expiração ou execução), o estado do canal muda e a transação com HTCL não existe mais. Voltamos a algo clássico.
No caso de fechamento cooperativo: paramos os pagamentos e, portanto, aguardamos a execução das transferências / HTCL, a transação é leve, portanto, mais barata, pois há no máximo 1 ou 2 saídas.
Se forçado a fechar: publicamos com todos os HTLCs em andamento, tornando-se muito pesado e muito caro. E é uma confusão.

Resumindo, o sistema de roteamento da Lightning Network usa Contratos Hash Time-Locked (HTLC) para garantir um pagamento seguro e verificável. Os HTLCs permitem pagamentos condicionais em que o dinheiro só pode ser desbloqueado com um segredo, garantindo que os participantes cumpram os seus compromissos.
No exemplo apresentado, Alice deseja enviar SAT para Bob através de Susie. Bob gera um segredo, cria um hash dele e transmite-o para Alice. Alice e Susie estabelecem um HTLC com base nesse hash. Uma vez que Bob desbloqueia o HTLC de Susie mostrando-lhe o segredo, Susie pode então desbloquear o HTLC de Alice.
No caso em que Bob não revela o segredo num determinado período de tempo, o HTLC expira. A expiração ocorre na ordem inversa, garantindo que se Bob voltar online, não haja consequências indesejáveis.

No fechamento do canal, se for um fechamento cooperativo, os pagamentos são interrompidos e os HTLCs são resolvidos, o que geralmente é menos custoso. Se o fechamento for forçado, todas as transações HTLC em andamento são publicadas, o que pode se tornar muito caro e confuso.
Resumindo, o mecanismo HTLC adiciona uma camada adicional de segurança na Lightning Network, garantindo que os pagamentos sejam executados corretamente e que os utilizadores cumpram os seus compromissos.

## Encontrando oseu caminho

![encontrando o seu caminho](https://youtu.be/wnUGJjOxd9Q)

A única informação pública é a capacidade total do canal (Alice + Bob), mas não sabemos onde está a liquidez.
Para obter mais informações, o nosso nó ouve o canal de comunicação do LN para anúncios de novos canais e atualizações de taxas de canais. O seu nó também verifica o blockchain para o fechamento de canais.

Como não temos todas as informações, precisamos fazer uma pesquisa de gráfico / rota com as informações que temos (capacidade máxima dos canais e não onde está a liquidez).

Critérios:

- Probabilidade de sucesso - Taxas
- Prazo de expiração do HTLC
- Número de nós intermediários
- Aleatório

![graph](assets/chapitre9/1.JPG)

Portanto, se houver 3 rotas possíveis:

- Alice > 1 > 2 > 5 > Bob
- Alice > 1 > 2 > 4 > 5 > Bob
- Alice 1 > 2 > 3 > Bob

Procuramos, teoricamente, a melhor opção com as menores taxas e a maior chance de sucesso: o máximo de liquidez e o menor número de saltos possível.

Por exemplo, se 2-3 tiverem apenas 130.000 SAT de capacidade, enviar 100.000 é muito improvável, então a escolha nº 3 tem poucas chances de sucesso.

![graph](assets/chapitre9/2.JPG)

Agora que o algoritmo fez as suas 3 escolhas, ele tentará a primeira:

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

Alice não viu o fracasso da rota 1, ela apenas esperou um segundo a mais. Uma falha de pagamento ocorre quando não há rota possível. Para facilitar a busca por rotas, Bob pode fornecer informações a Alice para ajudar na sua fatura:

- O valor
- O seu endereço
- O hash da pré-imagem para que Alice possa criar o HTLC
- Indicações sobre os canais de Bob

Bob conhece a liquidez dos canais 5 e 3 porque está diretamente conectado a eles, e ele pode indicar isso a Alice. Bob avisa Alice que o nó 3 é inútil, o que evita que Alice potencialmente faça a sua rota.
Outro elemento seriam os canais privados (portanto, não publicados na rede) que Bob pode ter. Se Bob tiver um canal privado com 1, ele pode dizer a Alice para usá-lo e isso daria Alice > 1 > Bob'

![graph](assets/chapitre9/3.JPG)

Em conclusão, o roteamento de transações na Lightning Network é um processo complexo que requer a consideração de vários fatores. Embora a capacidade total dos canais seja pública, a distribuição precisa da liquidez não é diretamente acessível. Isso obriga os nós a estimar as rotas mais prováveis de sucesso, levando em consideração critérios como taxas, prazo de validade do HTLC, número de nós intermediários e um fator aleatório. Quando várias rotas são possíveis, os nós procuram minimizar as taxas e maximizar as chances de sucesso escolhendo canais com liquidez suficiente e um número mínimo de saltos. Se uma tentativa de transação falhar devido a liquidez insuficiente, outra rota é tentada até que uma transação seja bem-sucedida.

Além disso, para facilitar a busca por rotas, o destinatário pode fornecer informações adicionais, como endereço, valor, hash da pré-imagem e indicações sobre os seus canais. Isso pode ajudar a identificar canais com liquidez suficiente e evitar tentativas de transações desnecessárias. Em última análise, o sistema de roteamento da Lightning Network é projetado para otimizar a velocidade, segurança e eficiência das transações, preservando a privacidade dos usuários.

# Ferramentas da Lightning Network
## Fatura, LNURL, Keysend

![fatura, LNURL, Keysend](https://youtu.be/CHnXJuZTarU)

![cover](assets/chapitre10/0.JPG)

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

Contém 0 ou mais partes adicionais:

- Hash da pré-imagem
- Segredo de pagamento (roteamento em cebola)
- Dados arbitrários
- Chave pública LN do destinatário
- Duração de validade (padrão de 1 hora)
- Indicações de roteamento
- Assinatura do conjunto

Existem outros tipos de faturas. O meta-protocolo LNURL permite fornecer um valor em satoshis diretamente em vez de fazer uma solicitação. Isso é muito flexível e permite muitas melhorias em termos de experiência do usuário.

![cover](assets/chapitre10/2.JPG)

Um Keysend permite que Alice envie dinheiro para Bob sem ter a solicitação de Bob. Alice obtém o ID de Bob, cria uma pré-imagem sem perguntar a Bob e inclui-a no seu envio. Portanto, Bob receberá uma solicitação surpresa onde pode desbloquear o dinheiro porque Alice já fez o trabalho.

![cover](assets/chapitre10/3.JPG)

Em conclusão, uma fatura da Lightning Network, embora complexa à primeira vista, codifica efetivamente uma solicitação de pagamento. Cada seção da fatura contém informações importantes, incluindo o valor a ser pago, o destinatário, o timestamp de criação e potencialmente outras informações, como o hash da pré-imagem, o segredo de pagamento, as indicações de roteamento e a duração de validade. Protocolos como LNURL e Keysend oferecem melhorias significativas em termos de flexibilidade e experiência do usuário, permitindo, por exemplo, enviar fundos sem solicitação prévia da outra parte. Essas tecnologias tornam o processo de pagamento mais fluido e eficiente na Lightning Network.

## Gerenciando a sua liquidez

![gerenciando a sua liquidez](https://youtu.be/YuPrbhEJXbg)

![instruction](assets/chapitre11/0.JPG)


Damos algumas orientações gerais para responder à pergunta constante sobre gerenciamento de liquidez no Lightning.

No LN, existem 3 tipos de pessoas:

- Compradores: eles têm liquidez de saída, é o mais simples, pois basta abrir canais
- Comerciantes: é mais complicado, pois precisam de liquidez de entrada por meio de outros nós e outros atores. Eles devem ter pessoas conectadas a eles
- Nós de roteamento: eles querem estar equilibrados com liquidez de ambos os lados e uma boa conexão com muitos nós para serem usados o máximo possível

Portanto, se precisares de liquidez de entrada, podes comprá-la com serviços.

![instruction](assets/chapitre11/1.JPG)

Alice compra um canal com Susie por 1 milhão de satoshis, então ela abre um canal com 1.000.000 SAT diretamente do lado de entrada. Ela pode então aceitar até 1 milhão de SAT de pagamento pelos clientes que estariam conectados com Susie (que está muito conectada).

Outra solução seria fazer pagamentos; pagas 100.000 por X motivo, agora podes receber 100.000.

![instruction](assets/chapitre11/2.JPG)

### Solução Loop Out: Atomic swap LN - BTC

Alice 2 milhões - Susie 0

![instruction](assets/chapitre11/3.JPG)

Alice quer enviar a liquidez para Susie, então ela faz um Loop out (um nó especial que oferece um serviço profissional de reequilíbrio LN/BTC).
Alice envia 1 milhão para o loop através do nó de Susie, então Susie tem a liquidez e o Loop retorna o saldo on-chain para o nó de Alice.

![instruction](assets/chapitre11/4.JPG)

Portanto, 1 milhão vão para Susie, esta envia 1 milhão para o Loop, o Loop envia 1 milhão para Alice. Alice moveu a liquidez para Susie ao preço de algumas taxas pagas ao Loop pelo serviço.

O mais complicado no LN é manter a liquidez.

![instruction](assets/chapitre11/5.JPG)

Em conclusão, a gestão de liquidez na rede Lightning Network é um desafio chave, que depende do tipo de usuário: comprador, comerciante ou nó de roteamento. Compradores, que precisam de liquidez de saída, têm a tarefa mais simples: eles simplesmente abrem canais. Comerciantes, que precisam de liquidez de entrada, devem estar conectados a outros nós e atores. Os nós de roteamento, por sua vez, buscam manter um equilíbrio de liquidez em ambos os lados. Existem várias soluções para gerenciar a liquidez, como a compra de canais ou o pagamento para aumentar a capacidade de recebimento. A opção "Loop Out", permitindo uma troca atômica entre LN e BTC, oferece uma solução interessante para reequilibrar a liquidez. Apesar destas estratégias, manter a liquidez na rede Lightning Network continua sendo um desafio complexo.

# Vai mais além

## Resumo da formação

![conclusão](https://youtu.be/MaWpD0rbkVo)

O nosso objetivo era explicar como a rede Lightning funciona e como ela se baseia no Bitcoin para funcionar.

A rede Lightning é uma rede de canais de pagamento. Vimos como um canal de pagamento funciona entre duas partes interessadas, mas também ampliamos a nossa visão para toda a rede, para a noção de rede de canais de pagamento.

![instruction](assets/chapitre12/0.JPG)

Os canais são abertos por meio de uma transação Bitcoin e podem acomodar o máximo de transações possível. O estado do canal é representado por uma transação de compromisso que envia para cada uma das partes interessadas o que ela possui do seu lado do canal. Quando uma transação ocorre dentro do canal, as partes interessadas comprometem-se com o novo estado, revogando o antigo estado e construindo uma nova transação de compromisso.

![instruction](assets/chapitre12/1.JPG)

Os pares protegem-se contra fraudes com chaves de revogação e um bloqueio de tempo. O fechamento mútuo consentido é preferido para fechar o canal. Em caso de fechamento forçado, a última transação de compromisso é publicada.

![instruction](assets/chapitre12/3.JPG)

Os pagamentos podem usar os canais de outros nós intermediários. Pagamentos condicionais à pré-imagem (HTLC) permitem bloquear fundos enquanto o pagamento é completamente resolvido. O roteamento em cebola é usado na Lightning Network. Os nós intermediários não conhecem o destino final dos pagamentos. Alice deve calcular a rota do pagamento, mas não tem todas as informações sobre a liquidez nos canais intermediários.

![instruction](assets/chapitre12/4.JPG)

Há uma componente de probabilidade ao enviar um pagamento via Lightning Network. 

![instruction](assets/chapitre12/5.JPG)

Para receber pagamentos, é necessário gerenciar a liquidez nos canais, o que pode ser feito pedindo a outras pessoas para abrir canais conosco, abrindo canais nós mesmos e usando ferramentas como Loop ou comprando/alugando canais em marketplaces.

## Entrevista com Fanis

![interview de Fanis](https://youtu.be/VeJ4oJIXo9k)

Aqui está um resumo da entrevista:

A Lightning Network é uma solução de pagamento ultra-rápida no Bitcoin que permite contornar as limitações relacionadas à escalabilidade da rede. No entanto, os bitcoins na Lightning não são tão seguros quanto os da cadeia Bitcoin, pois a descentralização e a segurança são privilegiadas em detrimento da escalabilidade.

O aumento excessivo do tamanho dos blocos não é uma boa solução, pois isso compromete os nós e a capacidade de dados. Em vez disso, a Lightning Network permite criar canais de pagamento entre dois utilizadores do Bitcoin sem que as transações apareçam na blockchain, economizando espaço nos blocos e permitindo que o Bitcoin escale hoje.

No entanto, há críticas em relação à escalabilidade e centralização da Lightning Network, com potenciais problemas relacionados ao fechamento de canais e altas taxas de transação. Para resolver esses problemas, é recomendável evitar a abertura de pequenos canais para evitar problemas futuros e aumentar as taxas de transação com Child Pay for Parent.

Soluções consideradas para o futuro da Lightning Network são o batching e a criação de canais em grupos para reduzir as taxas de transação, bem como o aumento do tamanho dos blocos a longo prazo. No entanto, é importante notar que os bitcoins na Lightning não são tão seguros quanto os bitcoins na cadeia Bitcoin.

A privacidade no Bitcoin e na Lightning estão relacionadas, com o roteamento em cebola garantindo um certo nível de privacidade para as transações. No entanto, no Bitcoin, tudo é transparente por padrão, com heurísticas usadas para rastrear os Bitcoins de endereço em endereço na cadeia Bitcoin.

Compras de Bitcoins com KYC permitem que a exchange conheça as transações de retirada, enquanto os montantes redondos e os endereços de troca permitem saber qual parte de uma transação é destinada a outra pessoa e qual parte é destinada a si mesmo.

Para melhorar a privacidade, ações conjuntas e coinjoins permitem quebrar os cálculos de probabilidade fazendo transações em que várias pessoas fazem uma transação juntas. As empresas de análise de cadeias têm mais dificuldade em determinar o que você está fazendo com seus bitcoins seguindo.

Na Lightning, apenas duas pessoas estão cientes da transação e é mais confidencial do que o Bitcoin. O roteamento em cebola significa que um nó intermediário não conhece o remetente e o destinatário do pagamento.

Para usar a Lightning Network, é recomendável seguir um treinamento no seu canal do YouTube ou diretamente no site descubra Bitcoin, ou usar o treinamento em Umbrell. Também é possível enviar texto arbitrário durante um pagamento na Lightning usando um campo dedicado para isso, o que pode ser útil para doações ou mensagens.
Contudo, é importante notar que os nós de roteamento no Lightning podem ser regulados no futuro, com alguns estados tentando regular os nós de roteamento.
Para os comerciantes, é necessário gerenciar a liquidez para aceitar pagamentos na Lightning Network, com restrições atuais que podem ser superadas com soluções apropriadas.

Por fim, o futuro do Bitcoin é promissor, com uma possível projeção de um milhão em cinco anos. Para garantir a profissionalização da indústria e a criação de um sistema alternativo ao sistema bancário existente, é importante contribuir para a rede e não parar de confiar.

## Agradecimentos e continua a cavar a toca do coelho

Parabéns! 🎉
Concluiste a formação LN 201 - Introdução à Lightning Network!
Podes estar orgulhoso(a), pois não é fácil. Poucas pessoas descem tão fundo na toca do Bitcoin.

Em primeiro lugar, um grande obrigado a Fanis Makalakis por nos oferecer este ótimo curso gratuito sobre um aspecto mais étnico do Lightning. Não hesites em segui-lo no Twitter, no seu blog ou através do seu trabalho na LN market.

De seguida, se desejas ajudar o projeto, não hesites em patrocinar-nos no Patreon. As tuas doações serão usadas para produzir conteúdo para novas formações e, é claro, serás o(a) primeiro(a) a ser informado(a) (incluindo o próximo de Fanis que está em construção).

A aventura da Lightning Network continua com a formação em Umbrel e a configuração de um nó da Lightning Network. Chega de teoria e vamos para a prática com a formação LN 202 agora!

Abraços e até breve!

Rogzy'
