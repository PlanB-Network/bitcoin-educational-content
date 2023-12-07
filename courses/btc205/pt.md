---
name: Solução de compra e venda de Bitcoin peer-to-peer
goal: Explorar soluções de compra e venda de Bitcoin sem KYC
objectives:
  - Compreender os diferentes tipos de KYC, seus riscos e benefícios
  - Compreender as vantagens da compra peer-to-peer
  - Implementar a solução que corresponde às suas necessidades
  - Melhorar a gestão de seus UTXO (KYC e não KYC)
---

# Uma jornada para o mundo do não-KYC

Pierre nos propõe este curso que nos mergulha nas diferentes soluções existentes para comprar e vender bitcoins peer-to-peer. A compra peer-to-peer é completamente legal e permite ter mais anonimato, já que essas soluções não são KYC. O KYC (Know Your Customer) é uma regra dos reguladores de mercado (AMF) que consiste em solicitar a identidade do cliente que deseja comprar ou vender bitcoin. Essas regras têm como objetivo impedir a lavagem de dinheiro, o financiamento do terrorismo e a evasão fiscal. Com o risco de importantes consequências para o usuário, o KYC tem como objetivo defender e proteger o usuário, embora seja muito frequentemente observado o efeito oposto.

Portanto, vamos explorar os diferentes tipos de KYC (os KYC completos tipo França, os KYC Light tipo Suíça e os não-KYC tipo peer-to-peer). Pierre apresentará mais de 6 soluções, então você terá todas as cartas na mão para descobrir qual é a que mais lhe convém. Se você deseja uma solução KYC, saiba que elas estão presentes na formação BTC 102.

+++

# Introdução

## Explicação e tipo de KYC

O KYC, para "Know Your Customer" (Conheça seu cliente), é uma norma regulatória que exige a coleta de informações privadas dos clientes, como seu endereço físico, identidade ou extratos bancários. Essa prática é comum em plataformas de corretagem, que podem solicitar um KYC completo, incluindo informações detalhadas como identidade, foto, comprovante de residência, folhas de pagamento, etc.

O principal objetivo do KYC é combater a lavagem de dinheiro, o financiamento do terrorismo e a evasão fiscal. É uma lei implementada pela AMF (Autoridade dos Mercados Financeiros), o órgão regulador do mercado francês. No entanto, a aplicação do KYC leva à centralização de bases de dados muito sensíveis contendo informações pessoais dos usuários. Essas informações, tendo um certo valor, podem ser vendidas a entidades mal-intencionadas.

Além disso, as plataformas de troca frequentemente solicitam uma quantidade excessiva de informações pessoais, colocando os usuários em risco e aumentando os custos de conformidade. Esses custos regulatórios podem desencorajar empresas francesas e prejudicar sua competitividade internacionalmente.

Existem três tipos de KYC, incluindo o KYC completo, que exige a coleta completa e regulada de informações para acessar o serviço. Na Suíça, uma alternativa chamada "KYC light" permite a compra e venda de bitcoins sem fornecer identificação, desde que o valor da compra não exceda 1000 euros por dia. Soluções como o Relay permitem o uso desse método.

Nesse contexto, as autoridades suíças podem acessar informações bancárias para investigar pessoas consideradas de risco. Os endereços de entrega de bitcoins também são rastreáveis ​​por meio do sistema bancário. O KYC light é geralmente considerado mais simples e menos custoso do que o sistema francês.

Na França, a compra de bitcoins online requer o envio de dinheiro para um terceiro, por transferência SEPA ou Paypal. Para aqueles que priorizam o anonimato, a segurança e a privacidade, soluções de compra de bitcoins em dinheiro também estão disponíveis. Para volumes baixos, a compra de bitcoins em dinheiro é uma opção simples e legal.

Para vender diariamente 100 euros em bitcoins para qualquer pessoa, é necessária regulamentação pela AMF (Autoridade dos Mercados Financeiros). Na França, essa regulamentação se aplica principalmente a indivíduos que realizam grandes volumes de transações. As outras duas formas de compra de bitcoin incluem o uso de caixas eletrônicos (ATM) e trocas entre amigos. Os caixas eletrônicos são regulamentados e exigem identificação para transações acima de 500 euros. A troca entre amigos, por sua vez, oferece exposição ao bitcoin de forma mais discreta.

Essas medidas regulatórias estão em vigor para combater o financiamento do terrorismo, a evasão fiscal e a lavagem de dinheiro. O bitcoin, como um banco de dados totalmente rastreável, torna a lavagem de dinheiro particularmente difícil. O uso do Bitcoin por criminosos pode ser rastreado, o que torna o Bitcoin uma ferramenta pouco eficaz para a lavagem de dinheiro.

É importante notar que esta formação apresenta diversas alternativas, bem como ferramentas que podem ser usadas para fins maliciosos ou não. Além disso, oferece explicações sobre o funcionamento dos livros de pedidos entre os fabricantes (provedores de pedidos) e os tomadores (tomadores de pedidos).

Também é importante observar que as informações apresentadas aqui não endossam nenhuma solução em particular. É simplesmente apresentar as opções disponíveis para uma melhor compreensão do assunto. Para qualquer pergunta adicional sobre o Bitcoin, não hesite em consultar recursos online, como www.découvrebitcoin.com.

## Comparativo das soluções de compra e venda peer-to-peer

Soluções P2P para compra de Bitcoin: Bisq, RoboSat, LNP2PBot, Peach e HodlHodl

A compra de Bitcoin peer-to-peer (P2P) é uma opção preferida para investidores que desejam evitar plataformas de câmbio centralizadas. Esta parte do curso examina diferentes soluções P2P disponíveis, incluindo Bisq, RoboSat, LNP2PBot, Peach e HodlHodl.
Comparativo de vantagens e desvantagens das diferentes soluções

Cada solução P2P tem suas próprias vantagens e desvantagens. Abaixo, oferecemos uma visão geral das características-chave de cada solução.

### Bisq

[Bisq](https://bisq.network/) é uma solução P2P não custodial que possui um sistema DAO (Organização Autônoma Descentralizada) e usa multisign para gerenciamento de disputas. Seu código é open source, o que contribui para sua robustez e proteção da privacidade dos usuários.

| Vantagens                                    | Desvantagens                                                                                       |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| - Solução P2P, não custodial, multisign, DAO | - O aplicativo é bastante pesado e não muito amigável, disponível apenas em computadores           |
| - Robusta e segura                           | - As limitações de compra e venda, bem como a gestão de contas com assinaturas, são de dois gumes. |
| - Open source                                |                                                                                                    |

### RoboSat

[RoboSat](https://learn.robosats.com/) é uma solução fácil de usar, rápida, que funciona sob TOR e não requer uma conta. É open source e usa a Lightning Network para permitir transações rápidas.

| Vantagens                                         | Desvantagens                                                              |
| ------------------------------------------------- | ------------------------------------------------------------------------- |
| - Fácil de usar                                   | - O protocolo é frágil com apenas um coordenador                          |
| - Baixas taxas de transação                       | - Requer conhecimentos técnicos e compreensão da privacidade              |
| - Usa a Lightning Network para transações rápidas | - O aplicativo Umbrell permite gerenciar sua própria instância de cliente |
| - Open source                                     |                                                                           |

### LNP2PBot

[LNP2PBot](https://lnp2pbot.com/) é acessível via Telegram para compra de Bitcoin sem KYC. Oferece transações rápidas através da Lightning Network e baixas taxas.

| Vantagens                                                    | Desvantagens                                          |
| ------------------------------------------------------------ | ----------------------------------------------------- |
| - Acessível via Telegram                                     | - Menos robusto e seguro do que outras soluções       |
| - Rapidez graças à Lightning Network                         | - Menos rápido e menos amigável do que Robosat        |
| - Baixas taxas de transação                                  | - Pode estar ligado à identidade Telegram do usuário  |
| - Gerenciamento de disputas internamente                     | - Falta de liquidez e fragilidade do aplicativo       |
| Propostas da comunidade para limitar o problema da confiança | O LNP2Pbot deve ser confiável para gerenciar disputas |

### Peach

[Peach](https://peachbitcoin.com/) é um aplicativo móvel dedicado à negociação de Bitcoin. Ele se destaca por sua simplicidade, não exigindo a criação de uma conta para operar. As negociações são rápidas, mesmo na ausência da Lightning Network. Além disso, as notificações nos telefones aceleram o processo de transação.

| Vantagens                                              | Desvantagens                                                                                                           |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| - Uso simplificado: não é necessário criar uma conta.  | - Segurança e robustez: por estar ligado a uma empresa, a peach apresenta possíveis fraquezas em segurança.            |
| - Velocidade de transação: as trocas são rápidas.      | - Ausência da Lightning Network: essa tecnologia, que permite transações Bitcoin mais rápidas, não é usada pela peach. |
| - Notificações: elas aceleram o processo de transação. |                                                                                                                        |

### HodlHodl

[HodlHodl](https://hodlhodl.com/) é uma solução não custodial para a troca de Bitcoin. Ele oferece muitas vantagens, como alta liquidez, a possibilidade de negociações privadas, um sistema de indicação, bem como contas com histórico de negociação e um sistema de classificação. No entanto, as negociações estão ligadas ao endereço de e-mail e à identidade digital do usuário, armazenados na HodlHodl. Além disso, o código-fonte da HodlHodl não é aberto ao público e o aplicativo não pode ser usado com o Tor.

| Vantagens                                                                                                                  | Desvantagens                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| - Não custodial: o usuário mantém a posse de suas chaves privadas.                                                         | - Armazenamento de informações pessoais: o endereço de e-mail e a identidade digital do usuário são armazenados pela HodlHodl. |
| - Liquidez: HodlHodl oferece uma ampla gama de possibilidades de troca.                                                    | - Código-fonte fechado: o código da HodlHodl não é aberto ao público.                                                          |
| - Possibilidade de negociações privadas: o usuário pode escolher com quem negociar.                                        | - Incompatibilidade com Tor: HodlHodl não pode ser usado com esta rede focada em privacidade.                                  |
| - Sistema de indicação: HodlHodl recompensa o boca a boca.                                                                 | - Possibilidade de KYC forçado: em algumas situações, HodlHodl pode exigir informações de identificação para recuperar fundos. |
| - Histórico de negociação e sistema de classificação: esses recursos permitem avaliar a confiabilidade de outros usuários. |                                                                                                                                |

## Conclusão sobre as soluções P2P

Em resumo, cada solução P2P tem suas vantagens e desvantagens. Bisq é considerada a mais robusta e segura, mas menos acessível. RoboSat é de código aberto, mas menos robusta que Bisq. LNP2PBot é menos robusta e segura que as outras soluções, menos rápida e menos amigável que RoboSat, mas mais do que Bisq. Peach é o aplicativo mais fácil e rápido para comprar Bitcoin sem KYC, mas uma empresa está por trás, então há fraquezas em termos de segurança e robustez. HodlHodl é um protocolo gerenciado por uma empresa e fechado, portanto, há fraquezas em termos de segurança e robustez, e um pouco mais complicado que Peach.

O bom e velho dinheiro em mãos ainda é uma solução para pequenas quantias.

Além das soluções P2P, existem outras opções de troca de criptomoedas. kycnot.me oferece serviços como VPN, VPS, SMS, etc. Bitrefil permite comprar cartões-presente. Cada solução em [kycnotme](https://kycnot.me/) é apresentada com seus pontos positivos e negativos.

# Tutoriais sobre soluções de compra/venda P2P

## Robosats

![robosats](https://tube.nuagelibre.fr/videos/watch/1978a2e0-64a0-4437-9229-7614cdf5bf61?start=0s)

[RoboSat](https://learn.robosats.com/) é um projeto de código aberto desenvolvido por Reckless Satoshi para trocar Bitcoins por moedas nacionais de forma privada. Ele simplifica a experiência peer-to-peer e usa faturas Lightning para minimizar as necessidades de custódia e confiança. Para usá-lo, precisaremos do Tor, uma rede de comunicação anônima.

A primeira coisa que você precisa fazer é baixar o Tor. Você pode encontrá-lo no GitHub ou diretamente no site oficial no seguinte endereço: tor.org/download.
Depois que o Tor for baixado e instalado:

- Pressione "Conectar" para estabelecer a conexão.
- Vá para o [endereço onion do robosats](http://robosats6tkf3eva7x2voqso3a5wcorsnw34jveyxfqi2fu7oyheasid.onion/).
- Copie o token para salvar sua identidade.

Aqui estão os passos para comprar bitcoins com Robosats:

- Consulte o livro de pedidos, você pode filtrar por moeda e forma de pagamento - por exemplo, comprar bitcoin em euros com Revolut.
- Antes de comprar, verifique a expiração da oferta, o preço em euros e o prêmio (você também pode filtrar as ofertas por prêmio)
- De preferência, escolha uma oferta com um usuário ativo e com um prêmio inferior à média.
- Verifique o resumo do pedido com o valor, a forma de pagamento, o prêmio, o ID do pedido e a expiração.
- Você pode receber seus satoshis em um endereço bitcoin com taxas de swap-out (de LN para BTC-onchain) da ordem de 1% (você pode alterar as taxas de mineração on-chain).
- Caso contrário, crie uma fatura com uma carteira LN da [lista](https://learn.robosats.com/docs/wallets/) e copie a fatura para Robosats.
- Entre em contato com o vendedor via chat criptografado para discutir o pagamento em fiat.

Agora vamos ver os passos para vender bitcoins na Robosats:

- Personalize sua oferta escolhendo o método de pagamento, o prêmio, o prazo de validade, etc.
- O tamanho do Fidelity Bond é equivalente ao depósito de garantia na BISC. Coloque 15% ou 10% de depósito de garantia para incentivar a outra parte a jogar limpo.
- Bloqueie os satoshis para confirmar a criação do pedido e evitar spam.
- Se alguém aceitar sua oferta de venda, converse com a outra parte para fazer o pagamento em fiat. Uma vez que o pagamento for feito, a negociação é concluída e os satoshis são vendidos!

## BISQ: solução de compra peer-to-peer

[Bisq](https://bisq.network/) é uma plataforma de troca descentralizada para ativos digitais, principalmente Bitcoin. Ele permite transações diretas, seguras e privadas entre usuários em todo o mundo sem a necessidade de um intermediário.

🚨 Por favor, tenha cuidado ao usar o Bisq, pois é uma solução avançada. Pode não ser adequado para usuários iniciantes. Certifique-se de ter alguma experiência e compreensão antes de começar. 🚨

Estamos olhando mais de perto esta solução, aqui estão os vídeos tutoriais:

![parte 1](https://tube.nuagelibre.fr/videos/watch/b3885ea9-23e9-4b58-aa3f-401348da85a1)

![parte 2](https://tube.nuagelibre.fr/videos/watch/53276305-70d6-4c7f-9df9-e100a82eee16)

Para os mais experientes, aqui está um guia sintético que relata rapidamente as etapas essenciais:

1. Baixar e Instalar: Visite o site do Bisq e baixe o aplicativo. Instale-o em seu sistema.
2. Configurar o Modo de Pagamento: Abra o aplicativo e vá para "Conta". Adicione os detalhes do seu modo de pagamento.
3. Alimente sua carteira Bisq: Clique em "Fundos" e "Receber Fundos" para obter seu endereço Bisq. Envie Bitcoins para este endereço.
4. Fazer uma Transação: Clique em "Comprar/Vender" e escolha a transação desejada. Siga as instruções para concluir a transação.
5. Confirmar Recebimento: Depois de receber o pagamento, confirme-o no aplicativo Bisq. Isso libera o Bitcoin do depósito em garantia. Não se esqueça de sempre verificar todos os detalhes de suas transações e negociar apenas com partes confiáveis.

Aqui está um guia completo que o guiará por todas as etapas para usar o Bisq.

O Bisq é uma rede descentralizada e segura que respeita sua propriedade privada. Na verdade, é não custodial, o que significa que você sempre possui seus fundos. Além disso, o Bisq usa um token, o BSQ, que permite que você pague taxas de transação mais baixas e estimula sua participação na DAO (Organização Autônoma Descentralizada). Para proteger os vendedores em transações Bitcoin-fiat, o Bisq estabeleceu um sistema de assinaturas e limites de conta. Como comprador, você precisará obter uma conta assinada para aumentar seu limite de compra. A assinatura também é uma maneira de verificar o histórico dos traders, garantindo assim a segurança das transações.

Para instalar o Bisq e fazer backup de seus dados, siga estas etapas simples:

- Acesse o site bisc.network para baixar o software (Captura de tela da página de download)
- Verifique a integridade do software usando ferramentas como as oferecidas por Loïc Morel para usuários do Windows.
- Depois que o instalador for verificado, inicie o Bisq, conceda as permissões necessárias e aceite os termos de uso. (Captura de tela dos termos de uso)
- O Bisq se conectará à rede Bitcoin e a si mesmo via Tor, o que pode levar algum tempo.
- Configure sua conta de pagamento e faça backup do seu SID (Identificador Seguro) da sua carteira para evitar perda ou roubo. (Captura de tela da página de configuração da conta)
- Também configure uma senha para criptografar suas informações.

Dependendo do seu sistema operacional, os dados do Bisq serão armazenados em locais diferentes. Você pode encontrá-los na pasta "Diretório de Dados". Atenção, se você excluir esta pasta, todos os seus dados do Bisq serão perdidos.
Para recuperar seus dados por meio de um backup:

- Copie a pasta de backup para a localização 'usuário / suporte de aplicativo / BISQ'.
- Renomeie a pasta de backup para 'BISQ'.
- Reinicie o Bisq e todos os seus dados devem ser restaurados.

Antes de começar a comprar ou vender Bitcoin no Bisq, é crucial configurar sua conta de pagamento. Você pode, por exemplo, configurar uma conta em sua moeda nacional, como uma conta SEPA, uma conta REVOLUT ou uma conta PAYPAL.
Para configurar sua conta REVOLUT:

- Adicione uma conta e selecione REVOLUT na lista de opções. (Captura de tela da lista de opções de conta)
- Você pode escolher diferentes moedas: euro, libra esterlina, dólar americano ou franco suíço.
- A duração máxima da transação é de um dia e o limite de compra é de 0,25 Bitcoin.
- Use seu nome de conta pessoal REVOLUT para evitar confusão.
- Certifique-se de assinar suas contas e estabelecer limites de compra para mais segurança.

Para comprar Bitcoin na BISQ:

- Acesse a seção "Comprar" onde você pode escolher diferentes mercados. (Captura de tela da seção "Comprar")
- Para obter taxas reduzidas, recomendamos que você compre BSQ, que pode ser comprado com Bitcoin.
- Você pode escolher entre diferentes ofertas com base no preço, quantidade, método de pagamento, etc.
- Para comprar BSQ, primeiro deposite Bitcoin em sua carteira.
- Escolha uma oferta com um prêmio baixo e uma quantidade baixa para a compra de BSQ.
- A BISQ verifica a validade da oferta e a conexão do par.
- Se o vendedor não estiver conectado, escolha outro.
- Verifique a oferta e aceite um prêmio de 5%.
- Confirme as taxas e a troca de BSQ, e aguarde a confirmação da transação para comprar Bitcoins com BSQ.

Para vender Bitcoin na BISQ:

- Crie uma nova oferta na guia "Vender". (Captura de tela da guia "Vender")
- Você pode escolher fixar o número de Bitcoins a serem vendidos ou o valor em euros que deseja receber.
- Você pode definir um prêmio em porcentagem acima do preço de mercado.
- Você pode criar uma faixa de venda ou deixar a escolha para o comprador.
- Você também pode definir um preço para interromper a oferta.
- Escolha o valor mínimo do depósito e as taxas de transação.
- Financie o pedido depositando os Bitcoins a serem vendidos, o valor do depósito de garantia e as taxas.
- Depois de criar a oferta, aguarde que um comprador apareça.

Depois que o comprador fizer o depósito da transação na BISQ, os Bitcoins são automaticamente enviados ao comprador e você recebe o dinheiro. A conta é verificada e assinada após uma transação com uma conta assinada.

## LNP2PBOT

![Tutorial do LNp2pbot](https://tube.nuagelibre.fr/videos/watch/57ed232d-6149-4267-be38-92b0f32800f7)

[Telegram](https://telegram.org/) é uma plataforma de mensagens que, com a ajuda do bot [Lnp2pbot](https://lnp2pbot.com/), permite que você compre e venda bitcoins de maneira rápida e fácil. Veja como fazer:

Para comprar Bitcoins via Bot LNP2PBOT no Telegram, siga estas etapas: '

- Comece acessando a conta do Lnp2pbot no Twitter e clicando no link na biografia (captura de tela da conta do bot no Twitter e o link na biografia).
- No Telegram, utilize os comandos "/buy" ou "/sell" para publicar ordens de compra ou venda. (Captura de tela do uso dos comandos "/buy" ou "/sell")
- Acesse o canal P2P Lightning para encontrar ofertas de compra e venda de acordo com seus critérios. (Captura de tela do canal P2P Lightning)
- Crie uma oferta de compra usando o bot Lnp2pbot e o comando "/buy".
- Selecione a moeda de sua escolha, indique o valor, o preço (com um prêmio, se desejar) e escolha seu método de pagamento.
- Aguarde até que um potencial vendedor entre em contato com você.

Para vender Bitcoins via Revolut, siga estas etapas:

- Clique em 'vender Satoshi' para abrir uma notificação no LNP2PBot. (Captura de tela da opção 'vender Satoshi')
- Receba uma fatura Lightning para pagar pela venda dos Satoshis. (Captura de tela da fatura Lightning)
- Aguarde o comprador enviar uma fatura com os satoshis para receber os pagamentos.
- Estabeleça contato direto com o comprador via Telegram para concordar com o método de pagamento e trocar as informações necessárias.
- Valide a transação com uma nota.

Se você deseja comprar Bitcoins enviando uma fatura LN, siga estas etapas:

- Copie a fatura e envie-a para o bot para comprar Satoshis.
- Entre em contato com o vendedor para finalizar a compra dos bitcoins.
- Em caso de problemas, proponha esperar ou tentar cancelar.
- Cancele a oferta e procure uma nova, se necessário.
- Escolha uma oferta que aceite CPA instantâneos para a compra de Satoshis.
- Envie a fatura e aguarde a confirmação de pagamento do vendedor.
- Depois que o pagamento for efetuado, envie a confirmação para o bot.
- Aguarde a validação do recebimento dos euros e o envio dos satoshis pelo vendedor.

Usando esses métodos, você pode comprar e vender bitcoins no Telegram de forma segura.

## Peach Bitcoin

site: https://peachbitcoin.com/

Estamos analisando esta solução em detalhes no BTC 205 oferecido por @pivi\_, aqui estão os vídeos tutoriais:

[Peach](https://peachbitcoin.com/) é um aplicativo móvel suíço que permite comprar e vender bitcoins peer-to-peer. Esta solução fácil de usar oferece uma interface intuitiva, ideal para transações em criptomoedas.

A interface do aplicativo Peach é composta por quatro guias: comprar, vender, histórico e configurações. (Captura de tela da interface do aplicativo)
A compra de bitcoins na Peach é simplificada. Para começar, é necessário criar uma oferta. Isso é possível acessando a guia "comprar". (Captura de tela da guia "comprar") Em seguida, navegue pelas ofertas disponíveis, deslizando até encontrar a que lhe convém. Os meios de pagamento aceitos são variados, incluindo transferência bancária, carteira online, cartão presente e opção local. (Captura de tela dos meios de pagamento disponíveis)

Depois de escolher uma oferta, é possível conversar com o vendedor por meio do chat integrado ao aplicativo. (Captura de tela do chat do aplicativo) Após o pagamento, confirmado pelo vendedor, a transação é concluída. Os bitcoins são então enviados ao comprador, que recebe uma notificação confirmando o recebimento dos fundos. (Captura de tela da notificação de recebimento dos bitcoins)

A Peach é um aplicativo não custodial, o que significa que os bitcoins permanecem em sua posse durante todo o processo. No entanto, eventuais disputas são gerenciadas de forma centralizada. Portanto, é crucial salvar as informações relacionadas à transação e suas informações pessoais usando a função Backup. (Captura de tela da função Backup) Como a Peach ainda está em versão beta, alguns bugs podem ocorrer. É recomendável verificar todas as informações antes de concluir uma transação.

Em resumo, o aplicativo móvel Peach oferece uma solução acessível para comprar e vender bitcoins peer-to-peer. O uso seguro e ideal da Peach é a chave para o sucesso de suas transações.

## Hold Hodl

[HodlHodl](https://hodlhodl.com/) é um mercado descentralizado de Bitcoin que prioriza o controle e a segurança dos usuários. Ao contrário das bolsas tradicionais, funciona com um modelo peer-to-peer, permitindo trocas diretas entre usuários. Com seu sistema de custódia multiassinatura, Hodl Hodl garante a segurança dos fundos durante as transações. A plataforma também suporta vários modos de pagamento e oferece opções de negociação, como contratos por diferença (CFD).

Neste tutorial, explicamos como comprar e vender bitcoins peer-to-peer na plataforma HodlHodl.

Antes de começar a usar a plataforma HodlHodl, algumas etapas de preparação são necessárias:

- Abra o site HodlHodl.
- Crie uma conta usando um endereço de e-mail para manter um histórico de suas transações.
- Leia atentamente o guia de segurança antes de começar a negociar.
- Observe que a plataforma não é de código aberto e mantém algumas de suas informações pessoais.

Aqui está o processo a seguir para fazer uma compra na plataforma HodlHodl:

- Use a função de filtro para encontrar as ofertas que lhe interessam.
- Clique na oferta que lhe interessa.
- Preencha os campos necessários para aceitar o contrato.
- Em nosso exemplo, usamos o Revolut como método de pagamento.

A configuração do contrato multisig para a transação é feita da seguinte maneira na HodlHodl:

- Uma vez que a oferta é aceita, faça o pagamento através do método escolhido (Revolut no nosso caso).
- Crie um contrato multisig gerando uma senha.
- Aguarde o depósito dos bitcoins no endereço multisig.
- Escolha o número de confirmações para o contrato.
- Faça o pagamento do valor acordado ao vendedor e confirme na HodlHodl.
- Seja paciente, pois o tempo de depósito pode ser longo, dependendo do banco utilizado.
- Aguarde a confirmação do vendedor antes de liberar os bitcoins após a compra.

A criação de uma oferta de venda ou compra de bitcoins na HodlHodl é feita da seguinte maneira:

- No site da HodlHodl, indique o endereço de liberação para as ofertas de compra.
- Informe o valor, o preço e o método de pagamento.
- Você também pode adicionar opções opcionais, como limites de transação ou um título para a oferta.
- Uma vez criada a oferta, você pode vê-la, editá-la, duplicá-la ou excluí-la como desejar.

## Bônus: Side Shift.AI

Aqui está um breve tutorial sobre como usar o [SideShift AI](https://sideshift.ai/), uma ferramenta muito útil para converter shitcoins em bitcoin. É a ferramenta ideal para aqueles que fecharam todas as suas exchanges pessoais. Nenhum sistema de ordem é necessário e há liquidez disponível. No entanto, observe que há uma taxa de 2,5% por transação.

Se você comprou criptomoedas de forma KYC, é recomendável usar o Monero para converter essas criptomoedas em bitcoin. O Monero oferece maior privacidade do que o Bitcoin. Para maior segurança, a operação CoinJoin também é recomendada. O CoinJoin mistura suas transações com as de outros usuários para complicar a rastreabilidade de suas transações.

Também gostaria de apresentar uma ferramenta de código aberto para compra e venda de bitcoins. Esta ferramenta permite que você escolha entre muitas blockchains. Basta inserir seu endereço Bitcoin e selecionar a quantidade que deseja enviar. Não é necessário criar uma conta ou conectar sua carteira à ferramenta. Você pode usar uma taxa fixa para enviar ou receber uma quantia específica. Além disso, esta ferramenta também permite a venda de bitcoins em troca de USDC.

### Apoie-nos

Este curso, assim como todo o conteúdo presente nesta universidade, foi oferecido gratuitamente pela nossa comunidade. Para nos apoiar, você pode compartilhá-lo com seus amigos, tornar-se um membro da universidade e até mesmo contribuir para o seu desenvolvimento via GitHub. Em nome de toda a equipe, obrigado!

### Nota sobre a formação

Um sistema de avaliação para a formação será em breve integrado a esta nova plataforma de E-learning! Enquanto isso, muito obrigado por ter seguido o curso e se você gostou, pense em compartilhá-lo com seus amigos.

# Para ir mais longe

## Entrevista com Steph de Peach Bitcoin

Aqui está um resumo da entrevista:

Pitch Bitcoin é um aplicativo móvel não custodial, permitindo a compra e venda de Bitcoin peer-to-peer. Atualmente, a equipe do Pitch Bitcoin, com sede na Suíça, é composta por oito membros e está trabalhando para evoluir o aplicativo para que ele também sirva como uma carteira. O modelo único do Pitch Bitcoin é baseado em uma estrutura de empresa centralizada, enquanto mantém um livro de pedidos descentralizado. Além disso, o aplicativo oferece uma opção para transações em dinheiro durante encontros pessoais.

Uma das principais vantagens do Pitch Bitcoin é o nível de segurança que oferece aos usuários. O sistema deskrow com multisignature e time lock é projetado para lidar com conflitos e garantir a segurança das transações. Além disso, o Pitch Bitcoin tem acesso prioritário ao dinheiro do multisignature, permitindo que ele transfira os bitcoins para o comprador em caso de comportamento malicioso do vendedor. A empresa planeja integrar todas as moedas europeias, bem como outros métodos de pagamento, quando lançar em open beta em janeiro.

A ideia do Pitch Bitcoin nasceu da experiência pessoal de sua fundadora na indústria do Bitcoin. Depois de descobrir o Bitcoin em 2017 e participar de vários meetups e conferências, ela se tornou uma maximalista do Bitcoin e viu a oportunidade de criar uma plataforma que permitisse aos Bitcoiners se encontrarem e fazerem transações em dinheiro. Além disso, o aplicativo inclui um chat criptografado para se comunicar com outros usuários, preservando o anonimato dos usuários.

Atualmente, o Pitch Bitcoin está desenvolvendo várias funcionalidades para facilitar o trabalho dos vendedores, incluindo a criação de uma API para vendedores, uma plataforma para grandes vendedores e a integração do BTC Pay Server para automatizar transferências. O aplicativo será lançado em open beta em janeiro de 2023.

Para concluir, a fundadora do Pitch Bitcoin destaca a importância da competição no ecossistema Bitcoin, pois o que é bom para o Bitcoin é benéfico para todos. Ela também incentiva a diversidade e a inclusão na indústria do Bitcoin e além.

## Entrevista com Pierre

Aqui está um resumo da entrevista:

Esta entrevista encerra o curso de treinamento Bitcoin 205 sobre o tema das soluções de compra peer-to-peer de Bitcoin. Organizado por Pierre, o objetivo do curso é educar o público de língua francesa sobre soluções técnicas para a compra de Bitcoin peer-to-peer, uma área que tem sido negligenciada até agora. Graças ao progresso alcançado, agora é possível comprar e usar Bitcoin preservando sua privacidade, mesmo com um simples telefone e o aplicativo Telegram.

Um dos métodos destacados é o uso do CoinJoin com o Samurai para reforçar a segurança. Essa solução minimiza os riscos associados a entidades centralizadas que detêm informações pessoais sobre os usuários de Bitcoin. Recomenda-se a compra de Bitcoins em moedas que não sejam KawaiiShii, um método que aumenta o anonimato. Além disso, algumas plataformas de câmbio, como a Kraken, oferecem taxas de saque mais baixas do que outras, o que está de acordo com os princípios do Bitcoin.

Bisq, Robosat e Peach são apresentadas como soluções democráticas para a negociação de bitcoin. A Peach, em particular, é destacada por sua facilidade de acesso como um aplicativo móvel. Por outro lado, há desafios, incluindo a regulamentação das criptomoedas e a necessidade de respeitar certos limites para evitar o excesso de regulamentação.

O uso de caixas eletrônicos de Bitcoin também é discutido, pois eles representam um método econômico de obter bitcoins sem KYC. Dependendo das regulamentações locais, essas máquinas podem ser instaladas em casa ou em locais públicos e podem ser usadas para oferecer bitcoins a amigos e familiares ou para pagamentos em bares.

O treinamento destaca a importância da educação para a compreensão do Bitcoin. Sugere-se que o Bitcoin pode oferecer uma solução no caso de uma recessão ou hiperinflação e que é importante conscientizar as pessoas sobre seu potencial antes que seja tarde demais. Além disso, enfatiza-se que a separação entre Estado e moeda é tão essencial quanto a separação entre Estado e religião.

Em conclusão, o Bitcoin é apresentado como uma moeda descentralizada que requer educação pública e mente aberta para ser totalmente compreendida e utilizada. O objetivo do treinamento é ajudar os participantes a entender as várias soluções de compra ponto a ponto e como usar essas ferramentas para aumentar o anonimato e a segurança ao usar o Bitcoin.

## Artigo bônus sobre privacidade

Um excelente [artigo] (https://decouvrebitcoin.fr/tribune-sur-le-kyc-et-lidentification-des-bitcoins-onchain/) de Loïc Morel sobre KYC e identificação.
Esse artigo detalhado explora os desafios e as soluções para preservar a privacidade ao adquirir e usar Bitcoins. Loïc desconstrói certas ideias preconcebidas sobre a identificação KYC (Know Your Customer), detalha os riscos e as soluções para preservar a privacidade ao adquirir e usar Bitcoins.
