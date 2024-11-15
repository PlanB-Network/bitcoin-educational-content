---
name: Solução de Compra e Venda de Bitcoin Peer-to-Peer
goal: Explorar soluções de compra e venda de Bitcoin sem KYC
objectives:
  - Entender os diferentes tipos de KYC, seus riscos e benefícios
  - Compreender as vantagens da compra peer-to-peer
  - Implementar a solução que se adequa às suas necessidades
  - Melhorar o gerenciamento dos seus UTXOs (KYC e não-KYC)
---

# Uma Jornada pelo Mundo do Não-KYC

Pierre nos oferece este curso que mergulha nas diferentes soluções existentes para comprar e vender bitcoins de forma peer-to-peer. A compra peer-to-peer é completamente legal e permite uma maior anonimidade, de fato, essas soluções não são KYC. KYC (Conheça Seu Cliente) é uma regra reguladora do mercado (AMF) que envolve solicitar identificação dos clientes que desejam comprar ou vender bitcoin. Essas regras visam prevenir a lavagem de dinheiro, o financiamento do terrorismo e a evasão fiscal. Apesar das consequências significativas para o usuário, o KYC visa defender e proteger seu usuário, embora muitas vezes seja observado que tem o efeito oposto.

Vamos, portanto, explorar os diferentes tipos de KYC (o tipo KYC completo como na França, o tipo KYC Light como na Suíça e o tipo não-KYC como peer-to-peer). Pierre apresentará mais de 6 soluções, então você terá todas as informações necessárias para descobrir qual delas se adequa a você. Se você está procurando uma solução KYC, observe que elas estão incluídas no curso BTC 102.

+++

# Introdução
<partId>9aa6ddfd-a257-549f-bb23-f77f1ca5d330</partId>

## Explicação & Tipo de KYC
<chapterId>13d18e82-0c50-5a7f-97d8-39cf5b4ef085</chapterId>

### Introdução

![introdução por Rogzy](https://youtu.be/3AHeKLTK7Sg)

### Explicação

![explicação dos tipos de KYC](https://youtu.be/kDhXoPU1KtM)

KYC, para "Conheça Seu Cliente", é um padrão regulatório que exige a coleta de informações privadas dos clientes, como seu endereço físico, identificação ou extratos bancários. Essa prática é comum em plataformas de corretagem, que podem solicitar um KYC completo, incluindo informações detalhadas como um ID, uma foto, comprovante de residência, contracheques, etc.
O principal objetivo do KYC (Conheça Seu Cliente) é combater a lavagem de dinheiro, o financiamento do terrorismo e a evasão fiscal. É uma lei implementada pela AMF (Autorité des marchés financiers), o órgão regulador do mercado francês. No entanto, a aplicação do KYC leva à centralização de bancos de dados altamente sensíveis contendo informações pessoais dos usuários. Essas informações, tendo um certo valor, podem ser vendidas a entidades maliciosas.
Além disso, as plataformas de troca muitas vezes solicitam uma quantidade excessiva de informações pessoais, colocando assim os usuários em risco e aumentando os custos de conformidade. Esses custos regulatórios podem desencorajar empresas francesas e prejudicar sua competitividade internacional.

Existem três tipos de KYC, incluindo o KYC completo, que requer uma coleta completa e regulada de informações para acessar o serviço. Na Suíça, uma alternativa chamada "KYC light" permite a compra e venda de bitcoins sem fornecer um ID, desde que o valor da compra não exceda 1000 euros por dia. Soluções como o Relay permitem o uso deste método.
Neste contexto, as autoridades suíças podem acessar informações bancárias para investigar indivíduos considerados em risco. Os endereços de entrega dos bitcoins também são rastreáveis através do sistema bancário. O KYC light é geralmente considerado mais simples e menos custoso do que o sistema francês.
Na França, comprar bitcoins online requer o envio de dinheiro a um terceiro, via transferência SEPA ou Paypal. Para aqueles que priorizam o anonimato, segurança e privacidade, soluções para comprar bitcoins em dinheiro também estão disponíveis. Para pequenos volumes, comprar bitcoins em dinheiro é uma opção simples e legal.
Para poder vender diariamente PLT de 100 euros de bitcoin para todos, é necessária a regulamentação pela AMF (Autorité des Marchés Financiers). Na França, essa regulamentação aplica-se principalmente a indivíduos que realizam volumes significativos de transações. Os dois outros métodos de compra de bitcoin incluem o uso de caixas eletrônicos e trocas entre amigos. Os caixas eletrônicos são regulados e exigem uma identificação para transações acima de 500 euros. A troca entre amigos, por outro lado, oferece uma exposição mais discreta ao bitcoin.

Essas medidas regulatórias estão em vigor para combater o financiamento do terrorismo, evasão fiscal e lavagem de dinheiro. O Bitcoin, como um banco de dados totalmente rastreável, torna a lavagem de dinheiro particularmente difícil. O uso do Bitcoin por criminosos pode ser rastreado, tornando o Bitcoin uma ferramenta ineficaz para lavagem de dinheiro.
É importante notar que este treinamento apresenta várias alternativas, bem como ferramentas que podem ser usadas para fins maliciosos ou não maliciosos. Além disso, oferece explicações sobre como funcionam os livros de ordens entre os criadores (fornecedores de ordens) e os tomadores (receptores de ordens).

Também é importante notar que as informações apresentadas aqui não endossam nenhuma solução específica. É simplesmente para apresentar as opções disponíveis para um melhor entendimento do assunto. Para quaisquer outras dúvidas sobre o Bitcoin, sinta-se à vontade para consultar recursos online como www.discoverbitcoin.com.

## Comparação de Soluções de Compra e Venda Peer-to-Peer
<chapterId>aad2dccb-0d2c-5533-859b-372b0f10d1ca</chapterId>

![comparação de soluções de compra e venda p2p](https://youtu.be/HiwSjN04Mz0)

Soluções P2P para Comprar Bitcoin: Bisq, RoboSat, LNP2PBot, Peach e HodlHodl

Comprar Bitcoin em uma base peer-to-peer (P2P) é uma opção preferida para investidores que desejam evitar plataformas de troca centralizadas. Esta parte do curso examina diferentes soluções P2P disponíveis, incluindo Bisq, RoboSat, LNP2PBot, Peach e HodlHodl.
Comparação das Vantagens e Desvantagens de Diferentes Soluções

Cada solução P2P tem suas próprias vantagens e desvantagens. Abaixo está uma visão geral das principais características de cada solução.

### Bisq

[Bisq](https://bisq.network/) é uma solução P2P não custodial que apresenta um sistema DAO (Organização Autônoma Descentralizada) e usa multisig para resolução de disputas. Seu código é de fonte aberta, o que contribui para sua robustez e proteção da privacidade do usuário.

| Vantagens                                     | Desvantagens                                                                                                       |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| - P2P, não custodial, multisig, solução DAO | - O aplicativo é bastante pesado e não muito amigável, disponível apenas em computadores                           |
| - Robusto e seguro                        | - As limitações na compra e venda, bem como a gestão de contas com assinaturas, têm um aspecto de dois gumes. |
| - Código aberto                                 |                                                                                                                     |

### RoboSat

[RoboSat](https://learn.robosats.com/) é uma solução fácil de usar, rápida, que opera sob TOR e não requer uma conta. É de código aberto e usa a Lightning Network para transações rápidas.

| Vantagens                                                    | Desvantagens                                                                  |
| - Fácil de usar                                        | - O protocolo é frágil com apenas um coordenador                              || - Taxas de transação baixas                         | - Requer conhecimento técnico e compreensão sobre privacidade |
| - Utiliza a Lightning Network para transações rápidas | - O aplicativo Umbrell permite gerenciar sua própria instância de cliente    |
### LNP2PBot

[LNP2PBot](https://lnp2pbot.com/) é acessível via Telegram para compras de Bitcoin sem KYC. Oferece transações rápidas através da Lightning Network e taxas baixas.

| Vantagens                                                          | Desvantagens                                                         |
| ------------------------------------------------------------------ | --------------------------------------------------------------------- |
| - Acessível via Telegram                                           | - Menos robusto e seguro do que outras soluções                      |
| - Velocidade através da Lightning Network                          | - Mais lento e menos amigável ao usuário do que Robosat              |
| - Taxas de transação baixas                                        | - Pode ser vinculado à identidade do Telegram do usuário             |
| - Resolução interna de disputas                                    | - Falta de liquidez e fragilidade do aplicativo                      |
| - Oferece comunidades para mitigar questões de confiança           | - A confiança deve ser depositada no LNP2Pbot para resolução de disputas |

### Peach

[Peach](https://peachbitcoin.com/) é um aplicativo móvel dedicado à negociação de Bitcoin. Destaca-se pela sua simplicidade, não exigindo uma conta para operar. As trocas são rápidas, mesmo sem a Lightning Network. Além disso, notificações por telefone aceleram o processo de transação.

| Vantagens                                                          | Desvantagens                                                                                                                  |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| - Uso simplificado: não é necessário criar uma conta.              | - Segurança e robustez: estando vinculado a uma empresa, o Peach tem potenciais fraquezas em termos de segurança.             |
| - Velocidade de transação: as trocas são rápidas.                  | - Ausência da Lightning Network: esta tecnologia, que permite transações Bitcoin mais rápidas, não é utilizada pelo Peach.    |
| - Notificações: elas aceleram o processo de transação.             |                                                                                                                               |

### HodlHodl

[HodlHodl](https://hodlhodl.com/) é uma solução não custodial para troca de Bitcoin. Oferece várias vantagens, como alta liquidez, a possibilidade de trocas privadas, um sistema de referência, bem como contas com histórico de trocas e um sistema de avaliação. No entanto, as trocas são vinculadas ao endereço de e-mail e identidade digital do usuário, armazenadas no HodlHodl. Além disso, o código-fonte do HodlHodl não é aberto ao público, e o aplicativo não pode ser usado com o Tor.

| Vantagens                                                                                                                     | Desvantagens                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| - Não custodial: o usuário permanece na posse de suas chaves privadas.                                                       | - Armazenamento de informações pessoais: o endereço de e-mail e a identidade digital do usuário são armazenados pelo HodlHodl. |
| - Liquidez: HodlHodl oferece uma ampla gama de possibilidades de troca.                                                      | - Código-fonte fechado: o código do HodlHodl não é aberto ao público.                                                          |
| - Opções de troca privada: o usuário pode escolher com quem negociar.                                                        | - Incompatibilidade com o Tor: HodlHodl não pode ser usado com esta rede focada em privacidade.                               |
| - Sistema de referência: HodlHodl recompensa o boca a boca.                                                                  | - Possibilidade de KYC forçado: em certas situações, HodlHodl pode exigir informações de identificação para recuperar fundos. |
| - Histórico de trocas e sistema de avaliação: essas funcionalidades permitem avaliar a confiabilidade de outros usuários.     | |

## Conclusão sobre Soluções P2P
<chapterId>c904985a-78dd-593e-a9c4-bfd1208d10c3</chapterId>
Em resumo, cada solução P2P tem suas vantagens e desvantagens. Bisq é considerado o mais robusto e seguro, mas menos acessível. RoboSat é de código aberto, mas menos robusto que o Bisq. LNP2PBot é menos robusto e seguro que as outras soluções, mais lento e menos amigável que o RoboSat, mas mais do que o Bisq. Peach é o aplicativo mais fácil e rápido para comprar Bitcoin sem KYC, mas é respaldado por uma empresa, portanto, apresenta fraquezas em termos de segurança e robustez. HodlHodl é um protocolo gerenciado por uma empresa e é de código fechado, portanto, tem fraquezas em termos de segurança e robustez, e é um pouco mais complicado que o Peach.
O bom e velho dinheiro em espécie cara a cara permanece sempre uma solução, para pequenas quantias.
Além das soluções P2P, existem outras opções de troca de criptomoedas. kycnot.me oferece serviços como VPN, VPS, SMS, etc. Bitrefil permite comprar cartões-presente. Cada solução em [kycnotme](https://kycnot.me/) é apresentada com seus prós e contras.

# Tutoriais sobre soluções de compra/venda P2P
<partId>582cee39-f6d0-5fb8-906f-b3e4c9f36fa5</partId>

## Robosats
<chapterId>1f1bd705-fcb3-5e32-8aa7-9ba184488326</chapterId>

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/) é um projeto de código aberto desenvolvido por Reckless Satoshi para trocar Bitcoins por moedas nacionais de forma privada. Simplifica a experiência peer-to-peer e usa faturas Lightning para minimizar a necessidade de custódia e confiança. Para usá-lo, precisaremos do Tor, uma rede de comunicação anônima.

A primeira coisa que você precisa fazer é baixar o Tor. Você pode encontrá-lo no GitHub ou diretamente no site oficial no seguinte endereço: tor.org/download.
Uma vez que o Tor esteja baixado e instalado:
- Pressione "Conectar" para estabelecer a conexão.
- Vá para o [endereço onion do Robosats](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/).
- Copie o token para salvar sua identidade.

Aqui estão os passos para comprar bitcoins com Robosats:

- Verifique o livro de ofertas, você pode filtrar por moeda e método de pagamento - por exemplo, comprar bitcoin em euros com Revolut.
- Antes de comprar, verifique a expiração da oferta, o preço em euros e o prêmio (você também pode filtrar ofertas por prêmio).
- Preferencialmente, escolha uma oferta com um usuário ativo e um prêmio menor que a média.
- Verifique o resumo do pedido com o valor, método de pagamento, prêmio, ID do pedido e expiração.
- Você pode receber seus satoshis em um endereço bitcoin com taxas de swap-out (de LN para BTC-onchain) de cerca de 1% (você pode modificar as taxas de mineração on-chain).
- Alternativamente, crie uma fatura com uma carteira LN desta [lista](https://learn.robosats.com/docs/wallets/) e copie a fatura no Robosats.
- Contate o vendedor via chat criptografado para discutir o pagamento em fiat.

Agora vamos olhar para os passos para vender bitcoins no Robosats:

- Personalize sua oferta escolhendo o método de pagamento, prêmio, duração da expiração, etc.
- O tamanho da Fiança de Fidelidade é equivalente ao depósito de segurança no BISQ. Coloque depósitos de segurança de 15% ou 10% para incentivar o jogo limpo pela outra parte.
- Bloqueie os satoshis para confirmar a criação do pedido e evitar spam.
- Se alguém aceitar sua oferta de venda, discuta com o par para prosseguir com o pagamento em fiat. Uma vez feito o pagamento, a negociação é concluída, e os satoshis vendidos são seus!

## BISQ: Uma solução de compra peer-to-peer
<chapterId>28b010ce-0e9b-5f20-a622-fa64629b2d88</chapterId>

[Bisq](https://bisq.network/) é uma plataforma de troca descentralizada para ativos digitais, principalmente Bitcoin. Permite transações diretas, seguras e privadas entre usuários em todo o mundo sem a necessidade de um intermediário.

🚨 Por favor, tenha cautela ao usar o Bisq, pois é uma solução avançada. Pode não ser adequado para usuários iniciantes. Certifique-se de ter alguma experiência e entendimento antes de começar. 🚨

Vamos olhar em detalhes esta solução, aqui estão os vídeos tutoriais:
Para aqueles mais adeptos, aqui está um guia conciso delineando rapidamente os passos essenciais:

1. Baixar e Instalar: Visite o site do Bisq e baixe o aplicativo. Instale-o em seu sistema.
2. Configurar Método de Pagamento: Abra o aplicativo e vá para "Conta". Adicione os detalhes do seu método de pagamento.
3. Financiar Sua Carteira Bisq: Clique em "Fundos" e depois em "Receber Fundos" para obter seu endereço Bisq. Envie Bitcoins para este endereço.
4. Fazer uma Transação: Clique em "Comprar/Vender" e escolha a transação desejada. Siga as instruções para completar a transação.
5. Confirmar Recebimento: Uma vez que você tenha recebido o pagamento, confirme-o no aplicativo Bisq. Isso libera o Bitcoin do escrow.

Lembre-se de sempre verificar todos os detalhes de suas transações e lidar apenas com partes confiáveis.

Aqui está agora um guia completo que o guiará por todos os passos para usar o Bisq.

BISQ é uma rede descentralizada e segura que respeita sua privacidade. De fato, é não custodial, significando que você sempre possui seus fundos. Além disso, o BISQ usa um token, o BSQ, que permite pagar taxas de transação mais baixas e incentiva sua participação na DAO (Organização Autônoma Descentralizada). Para proteger vendedores em transações Bitcoin-fiat, o BISQ implementou um sistema de assinaturas e limites de conta. Como comprador, você precisará obter uma conta assinada para aumentar seu limite de compra. A assinatura é também uma maneira de verificar o histórico de negociações dos traders, assegurando assim a segurança das transações.

Para instalar o Bisq e fazer backup dos seus dados, siga estes passos simples:

- Vá ao site bisc.network para baixar o software (Captura de tela da página de download)
- Verifique a integridade do software usando ferramentas como as oferecidas por Loïc Morel para usuários do Windows.
- Uma vez verificado o instalador, lance o BISQ, conceda as permissões necessárias e aceite os termos de uso. (Captura de tela dos termos de uso)
- O BISQ se conectará à rede Bitcoin e a si mesmo via Tor, o que pode levar algum tempo.
- Configure sua conta de pagamento e faça backups do seu SID (Identificador Seguro) da sua carteira para prevenir qualquer perda ou roubo. (Captura de tela da página de configuração da conta)
- Além disso, configure uma senha para criptografar suas informações.
Dependendo do seu sistema operacional, os dados do BISQ serão armazenados em locais diferentes. Você pode encontrá-los na pasta "Diretório de Dados". Tenha cuidado, se você deletar esta pasta, todos os seus dados do BISQ serão perdidos. Para recuperar seus dados através de um backup:
- Copie a pasta de backup para o local 'usuário/suporte de aplicação/BISQ'.
- Renomeie a pasta de backup para 'BISQ'.
- Reinicie o BISQ, e todos os seus dados devem ser restaurados.

Antes de começar a comprar ou vender Bitcoin no BISQ, é crucial configurar sua conta de pagamento. Por exemplo, você pode configurar uma conta na sua moeda nacional, como uma conta SEPA, uma conta REVOLUT ou uma conta PAYPAL. Para configurar sua conta REVOLUT:

- Adicione uma conta e selecione REVOLUT da lista de opções. (Captura de tela da lista de opções de conta)
- Você pode escolher diferentes moedas: euro, libra esterlina, dólar americano ou franco suíço.
- A duração máxima da transação é de um dia, e o limite de compra é de 0.25 Bitcoin.
- Use o nome da sua conta pessoal REVOLUT para evitar qualquer confusão.
- Certifique-se de assinar suas contas e estabelecer limites de compra para mais segurança.

Para comprar Bitcoin no BISQ:

- Vá para a seção "Comprar" onde você pode escolher entre diferentes mercados. (Captura de tela da seção "Comprar")
- Para se beneficiar de taxas reduzidas, recomendamos comprar BSQ, que você pode adquirir com Bitcoin.
- Você pode escolher entre diferentes ofertas baseadas em preço, quantidade, método de pagamento, etc.
- Para comprar BSQ, primeiro deposite Bitcoin na sua carteira.
- Escolha uma oferta com um prêmio baixo e uma pequena quantidade para comprar BSQ.
- O BISQ verifica a validade da oferta e a conexão com o par.
- Se o vendedor não estiver conectado, escolha outro.
- Verifique a oferta e aceite um prêmio de 5%.
- Confirme as taxas e a troca de BSQ, então aguarde a confirmação da transação para comprar Bitcoins com BSQ.

Para vender Bitcoin no BISQ:

- Crie uma nova oferta na aba "Vender". (Captura de tela da aba "Vender")
- Você pode escolher definir o número de Bitcoins para vender ou o montante em euros que deseja receber.
- Você pode definir um prêmio como uma porcentagem acima do preço de mercado.
- Você pode criar uma faixa de venda ou deixar a escolha para o comprador.
- Você também pode definir um preço para interromper a oferta.
- Escolha o valor mínimo do depósito e as taxas de transação.
- Financie o pedido depositando os Bitcoins a vender, o valor do depósito de segurança e as taxas.
- Uma vez que você tenha criado a oferta, espere por um comprador aparecer.
Uma vez que o comprador tenha feito o depósito da transação no BISQ, os Bitcoins são automaticamente enviados ao comprador, e você recebe o dinheiro. A conta é verificada e assinada após uma transação com uma conta assinada.
## LNP2PBOT
<chapterId>e3b61150-90e3-5ab4-bc12-4a05879321f5</chapterId>

![Tutorial do LNp2pbot](https://tube.nuagelibre.fr/videos/watch/57ed232d-6149-4267-be38-92b0f32800f7)

[Telegram](https://telegram.org/) é uma plataforma de mensagens que, com a ajuda do bot [Lnp2pbot](https://lnp2pbot.com/), permite que você compre e venda bitcoins de maneira rápida e fácil. Veja como fazer isso:

Para comprar Bitcoins via LNP2PBOT no Telegram, siga estes passos:
- Comece indo até a conta do Twitter do Lnp2pbot e clique no link na bio. (Captura de tela da conta do Twitter do bot e do link na bio)
- No Telegram, use os comandos "/buy" ou "/sell" para postar ordens de compra ou venda. (Captura de tela do uso dos comandos "/buy" ou "/sell")
- Vá até o canal P2P Lightning para encontrar ofertas de compra e venda de acordo com seus critérios. (Captura de tela do canal P2P Lightning)
- Crie uma oferta de compra usando o Lnp2pbot e o comando "/buy".
- Selecione a moeda de sua escolha, indique a quantidade, o preço (com um prêmio, se desejar) e escolha seu método de pagamento.
- Aguarde até que um vendedor em potencial entre em contato com você.

Para vender Bitcoins via Revolut, aqui está o que você precisa fazer:

- Clique em 'vender Satoshi' para abrir uma notificação no LNP2PBot. (Captura de tela da opção 'vender Satoshi')
- Receba uma fatura Lightning para pagar a fim de vender os Satoshis. (Captura de tela da fatura Lightning)
- Aguarde o comprador enviar uma fatura com os satoshis para receber os pagamentos.
- Estabeleça contato direto com o comprador via Telegram para concordar sobre o método de pagamento e trocar as informações necessárias.
- Valide a transação com uma nota.

Se você quiser comprar Bitcoins enviando uma Fatura LN, siga estes passos:

- Copie a fatura e envie-a para o bot para comprar Satoshi.
- Faça contato com o vendedor para finalizar a compra de bitcoins.
- Em caso de problema, sugira esperar ou tentar cancelar.
- Cancele a oferta e procure uma nova, se necessário.
- Escolha uma oferta que aceite CPAs instantâneos para a compra de Satoshi.
- Envie a fatura e aguarde a confirmação de pagamento do vendedor.
- Uma vez feito o pagamento, envie a confirmação para o bot.
- Aguarde a validação do recebimento de euros e o envio de satoshis pelo vendedor.
Usando esses métodos, você pode comprar e vender bitcoins no Telegram de forma segura.

## Peach Bitcoin
<chapterId>05e328c4-1003-586e-85c3-65109e3486e1</chapterId>

site: https://peachbitcoin.com/

Damos uma olhada detalhada nesta solução em BTC 205 oferecido por @pivi\_, aqui estão os vídeos tutoriais:

![peach](https://youtu.be/ziwhv9KqVkM)

[Peach](https://peachbitcoin.com/) é um aplicativo móvel suíço que permite comprar e vender bitcoins peer-to-peer. Esta solução fácil de usar oferece uma interface intuitiva, ideal para transações de criptomoedas.

A interface do aplicativo Peach consiste em quatro abas: comprar, vender, histórico e configurações. (Captura de tela da interface do aplicativo)
Comprar bitcoins no Peach é simplificado. Para começar, você precisa criar uma oferta. Isso é possível acessando a aba "comprar". (Captura de tela da aba "comprar")
Em seguida, navegue pelas ofertas disponíveis deslizando até encontrar aquela que lhe convém. Os métodos de pagamento aceitos são variados, incluindo transferência bancária, carteira online, cartão presente e opção local. (Captura de tela dos métodos de pagamento disponíveis)
Uma vez que você tenha escolhido uma oferta, você pode discutir com o vendedor através do chat integrado ao aplicativo. (Captura de tela do chat do aplicativo)
Após o pagamento, confirmado pelo vendedor, a transação está completa. Os bitcoins são então enviados ao comprador, que recebe uma notificação confirmando o recebimento dos fundos. (Captura de tela da notificação de recebimento de bitcoin)
Peach é uma aplicação não custodial, o que significa que os bitcoins permanecem em sua posse durante todo o processo. No entanto, quaisquer disputas potenciais são gerenciadas centralmente. Portanto, é crucial fazer backup das informações relacionadas à transação e das suas informações pessoais usando o recurso de Backup. (Captura de tela do recurso de Backup) Como o Peach ainda está em versão beta, alguns bugs podem ocorrer. É recomendado verificar todas as informações antes de concluir uma transação.
Em resumo, o aplicativo móvel Peach oferece uma solução acessível para comprar e vender bitcoins peer-to-peer. O uso seguro e otimizado do Peach é chave para transações bem-sucedidas.

## Hold Hodl
<chapterId>2c285751-ae9f-54af-8b28-c7c0beac7b43</chapterId>
[HodlHodl](https://hodlhodl.com/) é um mercado descentralizado de Bitcoin que prioriza o controle e a segurança do usuário. Ao contrário das bolsas tradicionais, opera em um modelo peer-to-peer, permitindo trocas diretas entre usuários. Graças ao seu sistema de escrow multi-assinatura, o Hodl Hodl garante a segurança dos fundos durante as transações. A plataforma também suporta vários métodos de pagamento e oferece opções de negociação, como Contratos por Diferença (CFD).
![tutorial hodlhodl](https://youtu.be/BDH9jE7kpD8)

Neste tutorial, explicamos como comprar e vender bitcoins peer-to-peer na plataforma HodlHodl.

Antes de começar a usar a plataforma HodlHodl, alguns passos preparatórios são necessários:

- Abra o site do HodlHodl.
- Crie uma conta usando um endereço de email para manter um histórico das suas transações.
- Leia o guia de segurança cuidadosamente antes de começar a negociar.
- Note que a plataforma não é open source e retém algumas das suas informações pessoais.

Aqui está o processo a seguir para fazer uma compra na plataforma HodlHodl:

- Use a função de filtro para encontrar ofertas que lhe convêm.
- Clique na oferta que lhe interessa.
- Preencha os campos necessários para aceitar o contrato.
- Em nosso exemplo, usamos Revolut como método de pagamento.

A configuração do contrato multisig para a transação é feita da seguinte forma no HodlHodl:

- Uma vez que a oferta é aceita, faça o pagamento pelo método escolhido (Revolut no nosso caso).
- Crie um contrato multisig gerando uma senha.
- Aguarde até que os bitcoins sejam depositados no endereço multisig.
- Escolha o número de confirmações para o contrato.
- Faça o pagamento do valor acordado ao vendedor e confirme no HodlHodl.
- Tenha paciência, pois a duração do depósito pode ser longa, dependendo do banco utilizado.
- Aguarde a confirmação do vendedor antes de liberar os bitcoins após a compra.

Criar uma oferta de venda ou compra de bitcoins no HodlHodl é feito da seguinte forma:

- No site do HodlHodl, indique o endereço de liberação para ofertas de compra.
- Insira o valor, preço e método de pagamento.
- Você também pode adicionar recursos opcionais como limites de transação ou um título para a oferta.
- Uma vez que a oferta é criada, você pode visualizar, editar, duplicar ou deletar conforme desejar.

## Bônus: Side Shift.AI
<chapterId>bd1f0844-af1e-53da-9518-b3b22f802276</chapterId>

![SideShift AI](https://youtu.be/xG8Wc1Ti5b8)
Aqui está um breve tutorial sobre como usar o [SideShift AI](https://sideshift.ai/), uma ferramenta muito útil para converter shitcoins em bitcoin. É a ferramenta ideal para aqueles que fecharam todas as suas trocas pessoais. Não é necessário um sistema de ordens, e a liquidez está disponível. No entanto, observe que há uma taxa de 2,5% por transação. Se você comprou criptos de maneira KYC, é recomendado usar Monero para converter essas criptos em bitcoin. Monero oferece privacidade superior em comparação ao Bitcoin. Para segurança aprimorada, também é recomendada a operação CoinJoin. CoinJoin mistura suas transações com as de outros usuários para complicar a rastreabilidade de suas transações.

Gostaria também de apresentar a você uma ferramenta de código aberto para comprar e vender bitcoins. Esta ferramenta permite que você escolha entre muitas blockchains. Você só precisa inserir seu endereço Bitcoin e selecionar a quantidade que deseja enviar. Não é necessário criar uma conta ou conectar sua carteira à ferramenta. Você pode usar uma taxa fixa para enviar ou receber uma quantidade específica. Além disso, esta ferramenta também permite a venda de bitcoins em troca de USDC.

### Apoie-nos

Este curso, assim como todo o conteúdo presente nesta universidade, foi oferecido gratuitamente pela nossa comunidade. Para nos apoiar, você pode compartilhá-lo com outros, tornar-se um membro da universidade e até contribuir para o seu desenvolvimento via GitHub. Em nome de toda a equipe, obrigado!

### Avalie o Treinamento

Um sistema de avaliação para o treinamento será em breve integrado a esta nova plataforma de E-learning! Enquanto isso, muito obrigado por seguir o curso, e se você gostou, pense em compartilhá-lo com aqueles ao seu redor.

# Para Ir Além
<partId>28194543-78b5-5f98-852a-2fc76439ddde</partId>

## Entrevista com Steph da Peach Bitcoin
<chapterId>76ed1f17-1d0b-5c0f-8726-91ab4e2e2955</chapterId>

![entrevista com Steph](https://youtu.be/LRGKD8qNSXw)

Aqui está um resumo da entrevista:

Peach Bitcoin é um aplicativo móvel não custodial, que permite a compra e venda peer-to-peer de Bitcoin. Atualmente, a equipe da Peach Bitcoin, baseada na Suíça, inclui oito membros e está se esforçando para evoluir o aplicativo para também servir como uma carteira. O modelo único da Peach Bitcoin é baseado em uma estrutura de empresa centralizada, mantendo um livro-razão de compra e venda descentralizado. Além disso, o aplicativo oferece uma opção para transações em dinheiro durante encontros pessoais.
Uma das principais vantagens da Peach Bitcoin é o nível de segurança que oferece aos usuários. O sistema de escrow com multisignatura e bloqueio por tempo é projetado para gerenciar conflitos e garantir a segurança das transações. Além disso, a Peach Bitcoin tem acesso prioritário aos fundos de multisignatura, permitindo transferir bitcoins para o comprador em caso de comportamento malicioso por parte do vendedor. A empresa planeja integrar todas as moedas europeias, bem como outros métodos de pagamento quando for lançada em beta aberto em janeiro.

A ideia para a Peach Bitcoin nasceu da experiência pessoal de sua fundadora na indústria do Bitcoin. Após descobrir o Bitcoin em 2017 e participar de vários meetups e conferências, ela se tornou uma maximalista do Bitcoin e viu a oportunidade de criar uma plataforma para Bitcoiners se encontrarem e realizarem transações em dinheiro. Além disso, o aplicativo inclui chat criptografado para comunicação com outros usuários, preservando assim o anonimato do usuário.
Atualmente, a Pitch Bitcoin está desenvolvendo várias funcionalidades para facilitar o trabalho dos vendedores, incluindo a criação de uma API para vendedores, uma plataforma para grandes vendedores e a integração do BTC Pay Server para automatizar transferências. O aplicativo será lançado em beta aberto em janeiro de 2023.
Para concluir, a fundadora da Pitch Bitcoin enfatiza a importância da competição no ecossistema Bitcoin, pois o que é bom para o Bitcoin é benéfico para todos. Ela também incentiva a diversidade e inclusão na indústria do Bitcoin e além.

## Entrevista com Pierre
<chapterId>4e4ba218-01ec-5f3a-bc49-c148bb22ee61</chapterId>

![entrevista com Pierre](https://youtu.be/COoezuJncm8)

Aqui está um resumo da entrevista:
Esta entrevista conclui o curso Bitcoin 205, que aborda o tema de soluções de compra de Bitcoin peer-to-peer. Organizado por Pierre, este curso visa educar o público francófono sobre as soluções técnicas para compras peer-to-peer de Bitcoin, uma área que foi negligenciada até agora. Graças ao progresso feito, agora é possível comprar e usar Bitcoin preservando a privacidade, mesmo com apenas um telefone e o aplicativo Telegram.

Um dos métodos destacados é o uso de CoinJoin com Samourai para aumentar a segurança. Esta solução minimiza os riscos associados a entidades centralizadas que detêm informações pessoais sobre os usuários do Bitcoin. É recomendado comprar Bitcoins não-KYC, um método que fortalece o anonimato. Além disso, algumas plataformas de câmbio como a Kraken oferecem taxas de saque menores do que outras, alinhando-se aos princípios do Bitcoin.
Bisq, Robosat e Peach são apresentados como soluções democráticas para a negociação de Bitcoin. Peach, em particular, é destacado pela sua facilidade de acesso como aplicativo móvel. No entanto, há desafios a serem abordados, incluindo a regulação das criptomoedas e a necessidade de respeitar certos limites para evitar regulamentações excessivas.

O uso de caixas eletrônicos de Bitcoin também é discutido; estes representam um método econômico para obter bitcoins não-KYC. Dependendo das regulamentações locais, esses caixas eletrônicos podem ser instalados em casa ou em locais públicos e podem ser usados para oferecer bitcoins a entes queridos ou para pagamentos em bares.

O treinamento enfatiza a importância do papel da educação no entendimento do Bitcoin. Sugere-se que o Bitcoin pode oferecer uma solução em caso de recessão ou hiperinflação e que é importante conscientizar sobre seu potencial antes que seja tarde demais. Além disso, destaca-se que a separação do estado e do dinheiro é tão essencial quanto a separação do estado e da religião.

Em conclusão, o Bitcoin é apresentado como uma moeda descentralizada que requer educação pública e uma mente aberta para ser plenamente compreendida e utilizada. O treinamento visa ajudar os participantes a entender as várias soluções de compra peer-to-peer e a usar essas ferramentas para aumentar seu anonimato e segurança ao usar o Bitcoin.

## Avalie este curso
<chapterId>a6410a99-adfc-50fd-a004-8048be620c8a</chapterId>
<isCourseReview>true</isCourseReview>

## Exame Final
<chapterId>38d03a01-ae5f-5c21-acd4-42f18b20c2b4</chapterId>
<isCourseExam>true</isCourseExam>

## Artigo Bônus sobre Privacidade
<chapterId>9f1aa75a-3031-58b2-9d4a-11a5c4197302</chapterId>

Um ótimo [artigo](https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/) de Loïc Morel sobre KYC e a identificação
Este artigo detalhado explora os desafios e soluções para preservar a privacidade ao adquirir e usar bitcoins. Loïc desconstrói alguns equívocos comuns sobre a identificação KYC (Know Your Customer - Conheça Seu Cliente), detalha os riscos associados a este processo e oferece técnicas para manter o anonimato das transações. É uma leitura obrigatória para aqueles que procuram entender as nuances da privacidade no mundo do Bitcoin e aprender a usar ferramentas como CoinJoin, Stonewall e PayJoin para obscurecer o rastreamento de transações e, assim, proteger sua privacidade.