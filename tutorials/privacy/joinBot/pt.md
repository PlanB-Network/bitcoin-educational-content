---
name: JoinBot
description: Compreender e usar o JoinBot
---

![DALL·E - samurai robô em uma floresta vermelha, renderização 3D](assets/cover.webp)

***ATENÇÃO:** Após a prisão dos fundadores da Samourai Wallet e a apreensão dos seus servidores em 24 de abril, **o serviço de JoinBot não está mais disponível**. Atualmente, não é mais possível usar essa ferramenta. No entanto, ainda é possível realizar Stonewall X2, mas você precisa encontrar um colaborador e trocar os PSBT manualmente. Este serviço pode ser reiniciado nos próximos meses, dependendo do progresso do caso.*

_Estamos acompanhando de perto a evolução deste caso, bem como os desenvolvimentos relacionados aos ferramentas associadas. Fique assegurado de que atualizaremos este tutorial à medida que novas informações estiverem disponíveis._

_Este tutorial é fornecido apenas para fins educativos e informativos. Não endossamos nem encorajamos o uso dessas ferramentas para fins criminosos. É responsabilidade de cada usuário cumprir as leis em sua jurisdição._

---

O JoinBot é uma nova ferramenta que foi adicionada à suíte Samourai Wallet com a última atualização 0.99.98f do famoso software de carteira Bitcoin. Ele permite que você faça facilmente uma transação colaborativa para otimizar sua privacidade, sem precisar encontrar um parceiro.

*Agradecimentos ao excelente Fanis Michalakis pela ideia de usar o DALL-E para a miniatura!*

## O que é uma transação colaborativa no Bitcoin?

O Bitcoin é baseado em um registro de contas distribuído e transparente. Qualquer pessoa pode rastrear as transações dos usuários desse sistema de dinheiro eletrônico. Para garantir certa privacidade, o usuário do Bitcoin pode realizar transações com uma estrutura específica para adicionar plausibilidade de negação na interpretação delas.

A ideia não é esconder diretamente a informação, mas sim confundi-la entre outras. Esse objetivo é usado especialmente nas Coinjoins, transações que permitem romper o histórico de uma moeda no Bitcoin e tornar seu rastreamento complexo. Para alcançar esse resultado, é necessário criar várias entradas e saídas com o mesmo valor na transação.

As entradas são as entradas de uma transação Bitcoin, e as saídas representam as saídas. A transação consome suas entradas para criar novas saídas, alterando as condições de gastos de uma moeda. É esse mecanismo que permite mover bitcoins entre os usuários.
Falo mais sobre isso neste artigo: Mecanismo de uma transação Bitcoin: UTXO, entradas e saídas.

Uma maneira de confundir as pistas em uma transação Bitcoin é realizar uma transação colaborativa. Como o nome sugere, ela envolve um acordo entre vários usuários, cada um depositando uma quantia de bitcoins como entrada em uma mesma transação e recebendo uma quantia como saída.

Como mencionado anteriormente, a estrutura de transação colaborativa mais conhecida é a Coinjoin. Por exemplo, no protocolo Coinjoin Whirlpool, as transações envolvem 5 participantes de entrada e saída, cada um com a mesma quantidade de bitcoins.

![Diagrama de uma transação Coinjoin no Whirlpool](assets/1.webp)

Um observador externo dessa transação será incapaz de saber qual saída pertence a qual usuário de entrada. Se pegarmos o exemplo do usuário nº 4 (roxo), podemos reconhecer sua UTXO como entrada, mas não saberemos qual das 5 saídas é realmente dele. A informação inicial não está escondida, mas sim confundida em um grupo.
O utilizador tem a capacidade de negar a posse de um determinado UTXO de saída. Esse fenômeno é chamado de "plausibilidade de negação" e permite obter confidencialidade em uma transação Bitcoin, embora transparente.

Para saber mais sobre o Coinjoin, eu explico TUDO neste longo artigo: Compreendendo e usando o CoinJoin no Bitcoin.

Embora seja muito eficaz para quebrar o rastreamento de um UTXO, o Coinjoin não é adequado para gastos diretos. De fato, sua estrutura implica em ter que usar inputs de um valor pré-definido e outputs do mesmo valor (modulado pelas taxas de mineração). No entanto, a transação de gasto no Bitcoin é um momento crítico para a confidencialidade, pois muitas vezes ela cria um vínculo físico entre o usuário e sua atividade on-chain. Portanto, parece essencial usar ferramentas de confidencialidade nos gastos. Existem outras estruturas de transações colaborativas projetadas especificamente para transações de pagamento efetivo.

## A transação StonewallX2

Entre a miríade de ferramentas de gasto oferecidas na Samourai Wallet, existe a transação colaborativa StonewallX2. É um mini Coinjoin entre dois usuários projetado para pagamento. Do ponto de vista externo, essa transação pode levar a várias interpretações possíveis. Portanto, há plausibilidade de negação e, consequentemente, confidencialidade para o usuário.

Esse mecanismo de transação colaborativa StonewallX2 está disponível na Samourai Wallet e na Sparrow Wallet. Essa ferramenta é interoperável entre os dois softwares.

Seu mecanismo é bastante simples de entender. Aqui está seu funcionamento prático:

> - Um usuário deseja fazer um pagamento em bitcoins (por exemplo, em uma loja).
> - Ele obtém o endereço de recebimento do destinatário real do pagamento (a loja).
> - Ele constrói uma transação específica com vários inputs: pelo menos um pertencente a ele e um pertencente a um colaborador externo.
> - A transação terá 4 outputs, incluindo 2 com os mesmos valores: um para o endereço da loja para pagar, um troco que retorna para o usuário, um output com o mesmo valor do pagamento que vai para o colaborador e outro output que também retorna para o colaborador.

Por exemplo, aqui está uma transação StonewallX2 clássica na qual fiz um pagamento de 50.125 sats. A primeira input de 102.588 sats vem da minha carteira Samourai. A segunda input de 104.255 sats vem da carteira do meu colaborador:

![Esquema de uma transação StonewallX2](assets/2.webp)

Podemos observar 4 outputs, incluindo 2 com o mesmo valor para confundir as pistas:

> - 50.125 sats que vão para o destinatário efetivo do meu pagamento.
> - 52.306 sats que representam meu troco e, portanto, retornam para um endereço da minha carteira.
> - 50.125 sats que retornam para o meu colaborador.
> - 53 973 sats que retornam para o meu colaborador.
>   No final da operação, o colaborador recupera todo o seu saldo inicial (exceto as taxas de mineração), e o usuário terá pago ao comerciante. Isso permite adicionar uma grande quantidade de entropia à transação e quebrar os vínculos inegáveis entre o remetente e o destinatário do pagamento.

A força da transação do tipo StonewallX2 é que ela contraria completamente uma das regras empíricas usadas pelos analistas de blockchain: a propriedade comum das entradas em uma transação de várias entradas. Em outras palavras, na maioria dos casos, se observarmos uma transação Bitcoin que possui várias entradas, podemos admitir que todas essas entradas pertencem à mesma pessoa. Satoshi Nakamoto já havia identificado esse problema para a privacidade do usuário em seu White Paper:

> "Como uma medida de segurança adicional, um novo par de chaves poderia ser usado para cada transação, mantendo-as não vinculadas a um proprietário comum. No entanto, a vinculação é inevitável com transações de várias entradas, que necessariamente revelam que suas entradas eram detidas pelo mesmo proprietário."

Essa é uma das muitas regras empíricas usadas na análise on-chain para construir clusters de endereços. Para saber mais sobre essas heurísticas, recomendo a leitura desta série de 4 artigos da Samourai, que introduz muito bem o assunto.

A força da transação StonewallX2 reside no fato de que um observador externo pensará que as diferentes entradas da transação pertencem a um proprietário comum. Na realidade, são dois usuários diferentes que estão colaborando. A análise do pagamento é, portanto, direcionada para uma falsa pista, e a privacidade dos usuários é preservada.

Do exterior, uma transação StonewallX2 não pode ser diferenciada de uma transação Stonewall. A diferença efetiva entre elas reside apenas no fato de que o Stonewall não é colaborativo. Ele usa apenas as UTXOs de um único usuário. No entanto, em suas estruturas no registro de contas, Stonewall e StonewallX2 são perfeitamente idênticos. Isso permite adicionar ainda mais interpretações possíveis a essa estrutura de transação, pois um observador externo não poderá saber se as entradas vêm da mesma pessoa ou de dois colaboradores.

Em seguida, a vantagem do StonewallX2 em relação a um PayJoin do tipo Stowaway é que ele pode ser usado em todas as situações. O destinatário efetivo do pagamento não deposita nenhuma entrada na transação. Assim, podemos usar um StonewallX2 para pagar em qualquer comerciante que aceite Bitcoin, mesmo que este último não use Samourai ou Sparrow.

Por outro lado, a principal desvantagem desta estrutura de transação é que requer um colaborador que esteja disposto a utilizar os seus bitcoins para participar no seu pagamento. Se tiveres amigos bitcoiners que estejam dispostos a ajudar-te em qualquer circunstância, isto não é um problema. Por outro lado, se não conheceres nenhum outro utilizador da Carteira Samourai, ou se ninguém estiver disponível para colaborar, então estás preso.

Para resolver este problema, as equipas do Samourai adicionaram recentemente uma nova funcionalidade à sua aplicação: JoinBot.

# O que é o JoinBot?

O princípio por detrás do JoinBot é simples. Se você não consegue encontrar ninguém para colaborar em uma transação StonewallX2, você pode colaborar com eles. Em termos práticos, você pode realmente realizar uma transação colaborativa diretamente com a Samourai Wallet.

Este serviço é muito conveniente, especialmente para utilizadores novatos, uma vez que está disponível 24 horas por dia, 7 dias por semana. Se precisar de fazer um pagamento urgente e desejar fazer um StonewallX2, já não precisará de contactar um amigo ou procurar um colaborador online. O JoinBot ajuda-o.

Outra vantagem do JoinBot é o facto de os UTXO que fornece como entrada serem exclusivamente provenientes de postmixes da Whirlpool, o que melhora a confidencialidade do seu pagamento. Além disso, como o JoinBot está sempre online, deve trabalhar com UTXOs que tenham grandes Anonsets potenciais.

Obviamente, o JoinBot tem alguns compromissos que vale a pena salientar:

Tal como num StonewallX2 clássico, o seu colaborador está necessariamente ciente dos UTXOs usados e para onde vão. No caso do JoinBot, Samourai conhece os detalhes da transação. Isto não é necessariamente uma coisa má, mas é algo a ter em conta.

Para evitar spam, Samourai cobra uma taxa de serviço de 3,5% sobre o valor real da transação, com um limite máximo de 0,01 BTC. Por exemplo, se eu enviar um pagamento efetivo de 100 kilosats utilizando o JoinBot, a taxa de serviço será de 3.500 sats.

Para usar o JoinBot, tens de ter pelo menos dois UTXO desvinculados disponíveis na tua carteira.

Numa StonewallX2 clássica, os custos de mineração são partilhados igualmente entre os dois colaboradores. Com o JoinBot, terá obviamente de pagar a totalidade da taxa de extração.

A fim de que uma transação JoinBot seja exatamente igual a uma transação clássica StonewallX2 ou Stonewall, o pagamento das taxas de serviço é feito em uma transação totalmente separada. O reembolso da metade das taxas de mineração inicialmente pagas pela Samourai será feito nesta segunda transação. Para otimizar sua privacidade até o fim, o pagamento das taxas é feito usando uma transação com a estrutura Stowaway (PayJoin).

## Como usar o JoinBot?

Para realizar uma transação JoinBot, você precisa ter uma carteira Samourai Wallet. Você pode baixá-la aqui ou no Google Playstore.

Ao contrário da maioria das ferramentas desenvolvidas pela Samourai, até o momento, a Sparrow Wallet ainda não anunciou a implementação do JoinBot. Portanto, essa ferramenta está disponível apenas no Samourai.

Descubra passo a passo como realizar uma transação StonewallX2 com o JoinBot neste vídeo:

![Como usar o Joinbot](https://youtu.be/80MoMz2Ne5g)

Aqui está o esquema da transação que acabamos de realizar no vídeo:

![Esquema da minha transação StonewallX2 com o JoinBot.](assets/3.webp)

Podemos ver 5 inputs:

> - 3 inputs de 100 kilosats provenientes do Samourai (JoinBot).
> - 2 inputs provenientes da minha carteira pessoal, de 3.524 sats e 1,8 megasat.

Os 4 outputs da transação são os seguintes:

> - 1 de 212.452 sats para o destinatário efetivo do meu pagamento.
> - 1 outro do mesmo valor que retorna para um endereço do Samourai.
> - 1 troco que também retorna para o Samourai, no valor de 87.302 sats. Isso representa a diferença entre o total de seus inputs (300.000 sats) e o output de ofuscação (212.452 sats) menos as taxas de mineração.
> - 1 troco que retorna para outro endereço da minha carteira. Isso representa a diferença entre o total dos meus inputs e o pagamento efetivo, menos as taxas de mineração.

Lembrando que as taxas de mineração não representam um output das transações. Elas simplesmente representam a diferença entre o total dos inputs e o total dos outputs.

## Conclusão

O JoinBot é uma ferramenta adicional que permite adicionar mais escolhas e liberdade para o usuário do Samourai. Ele permite realizar uma transação colaborativa StonewallX2 diretamente com o Samourai como colaborador. Esse tipo de transação ajuda a melhorar a privacidade dos usuários.

Se você puder realizar um StonewallX2 clássico com um amigo, eu ainda recomendo usar essa opção. No entanto, se você estiver bloqueado e não encontrar nenhum colaborador para fazer um pagamento, saiba que o JoinBot estará disponível 24 horas por dia, 7 dias por semana para colaborar com você.

**Recursos externos:**
- https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin
