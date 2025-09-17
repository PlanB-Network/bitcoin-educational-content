---
name: Zeus Embedded - Avançado
description: Carteira Lightning auto-custodial multinó
---

![Zeus](assets/cover.webp)


## Introdução ao ZEUS Wallet


ZEUS é uma aplicação móvel de gestão de nós e Bitcoin Wallet com todas as funcionalidades de um Bitcoin Lightning Wallet que simplifica os pagamentos Bitcoin, dá aos utilizadores um controlo total das suas finanças e permite aos utilizadores mais avançados gerir os seus nós Lightning na palma da mão.


### A quem se destina o ZEUS?

Atualmente o ZEUS é para pessoas que executam os seus próprios nós domésticos / empresariais de [Lightning Network Daemon (LND)](https://lightning.engineering/) ou [Core Lightning (CLN)](https://blockstream.com/lightning/) e os gerem remotamente através do Zeus.


Os comerciantes que utilizam [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) ou [Alby](https://getalby.com/) (ou qualquer outra conta LNDhub) também podem conectar-se, usar e gerir os seus nós / contas a partir do ZEUS.


[A partir da versão v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), o ZEUS começará a atender usuários comuns que apenas querem uma maneira simples de fazer pagamentos rápidos e baratos em bitcoin a partir de seus dispositivos móveis, com um [nó Lightning móvel embutido](https://docs.zeusln.app/category/embedded-node) integrado a um [Provedor de Serviços Lightning (LSP)](https://docs.zeusln.app/lsp/intro).


### Recursos importantes de Zeus:


- Página oficial de Zeus - [https://zeusln.app/](https://zeusln.app/)
- Documentação Zeus - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Repositório Github do Zeus](https://github.com/ZeusLN/zeus)
- [Grupo de suporte do Zeus no Telegram](https://t.me/ZeusLN)
- [Zeus no NOSTR](https://iris.to/zeus@zeusln.app)
- [Anúncios do Blog do Zeus](https://blog.zeusln.com)


### Caraterísticas do Zeus

#### Caraterísticas gerais:


- Auto-tutela, apenas Bitcoin e Lightning Wallet
- Sem taxas de processamento, sem KYC
- Fonte totalmente aberta (APGLv3)
- Suporte para vários nós / contas (pode gerir o(s) seu(s) próprio(s) nó(s) doméstico(s), executar o nó LND incorporado, ligar-se a várias contas LNDhub)
- Menu de actividades fácil de utilizar
- Encriptação por PIN ou passphrase, Modo de privacidade - oculte os seus dados sensíveis
- Agenda de contactos, vários temas, vários idiomas


#### Caraterísticas técnicas


- Ligar através do Tor
- Suporte completo para LNURL (pagamento, levantamento, autenticação, canal), envio para endereços Lightning
- Gestão detalhada do canal de iluminação, suporte MPP/AMP, Keysend, gestão de taxas de encaminhamento
- Apoio Replace-by-fee (RBF) e apoio "filho por pai" (CPFP)
- Pagamentos e pedidos NFC, assinar e verificar mensagens
- Suporte para SegWit e Taproot
- Canais Taproot simples
- Endereços de autocustódia relâmpago (@zeuspay.com)
- Ponto de venda da Square (brevemente aberto)


### Guias e tutoriais em vídeo

Para poder utilizar o Zeus e gerir os canais Lightning, a liquidez, as taxas, etc., é melhor ler primeiro alguns guias importantes sobre o Lightning Network.


#### Guias:


- [LND - Documentação do Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Documentação do Core Lightning](https://lightning.readthedocs.io/index.html)
- [Guia de Lightning para iniciantes](https://bitcoiner.guide/lightning/) – por Bitcoin Q&A
- [Gerenciamento de Nó Lightning](https://www.lightningnode.info/) – por openoms
- [A Lightning Network e a analogia do aeroporto](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Gerenciamento da liquidez do nó Lightning](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Manutenção do Nó Lightning](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Tutorial em vídeo da BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Um guia passo-a-passo sobre como começar a utilizar o nó incorporado Zeus LN no seu dispositivo móvel


![Image](assets/en/01.webp)


Dedico este guia a todos os novos utilizadores do Lightning Network (LN) que queiram iniciar uma nova viagem soberana utilizando um nó de autocustódia Wallet nos seus dispositivos móveis.


Consideremos que já passou por toda essa pletora de carteiras LN de custódia, mas ainda não está pronto para começar a gerir um nó LN de roteamento PÚBLICO, apenas quer empilhar mais Sats sobre LN de uma forma mais auto-custodial e fazer os seus pagamentos regulares sobre LN.


Aqui está o Zeus, começando com a [versão v0.8.0 anunciada no blog deles](https://blog.zeusln.com/new-release-zeus-v0-8-0/), que agora oferece um nó LND incorporado no aplicativo. Até agora o Zeus era um aplicativo de gerenciamento de nós remotos + contas LNDhub. Mas agora… o nó está no telefone!


![Image](assets/en/02.webp)


### Recapitulação rápida das principais caraterísticas do Zeus Node:



- **Nó LND privado** - Isto significa que este nó NÃO fará o encaminhamento público de pagamentos de outros através do seu nó. O nó e os canais não são anunciados (privados, não visíveis no gráfico público do LN). Receber e efetuar pagamentos será feito através dos seus pares LSP ligados. **LEMBRE-SE: O Zeus Embedded Node NÃO fará roteamento público!**
- **Serviço LND persistente** - o utilizador pode ativar esta funcionalidade e manter o serviço LND ativo continuamente como qualquer nó LN normal. A aplicação não tem de estar aberta, o serviço persistente manterá toda a comunicação online.
-   **Filtros de bloco Neutrino** - a sincronização de blocos é feita usando [filtros de blocos e o protocolo Neutrino](https://bitcoinops.org/en/topics/compact-block-filters/) (sem fornecer nenhuma informação sobre os fundos on-chain dos nossos usuários). Lembrete: para conexões de internet de alta latência / lentas, essa sincronização de blocos baseada em Neutrino às vezes pode falhar. Tentar mudar para um servidor Neutrino próximo pode ajudar a restaurar a sincronização. Sem essa sincronização, seu nó LND não poderá iniciar!
- **Canais Taproot simples** - Ao fechar estes canais, os utilizadores incorrem em menos taxas e têm mais privacidade, uma vez que parecem ser como qualquer outro gasto Taproot ao examinar a sua pegada On-Chain.
- **LSP integrado** - Olympus é o novo nó LSP para Zeus. Os utilizadores podem voltar a receber Sats através de LN de imediato, sem terem previamente configurado canais LN. Simplesmente terão de criar um LN Invoice e pagar a partir de qualquer outro LN Wallet, com o serviço de canais Zeus 0-conf. Leia mais sobre o Zeus LSP aqui. O LSP também proporciona uma maior privacidade aos nossos utilizadores, fornecendo-lhes facturas embrulhadas que escondem dos pagadores as chaves públicas dos seus nós.
- **Livro de contactos** - pode guardar contactos manualmente ou importar do NOSTR, para enviar facilmente pagamentos para os seus destinos habituais.
- Suporte total para LNURL, envio e receção de **LN Address** - agora pode configurar o seu próprio LN Address autocustodial com @zeuspay.com. Lembrete: Também pode usar Zeus para LN-auth em sites onde pode fazer login com uma autenticação LN. É muito útil.
- **Ponto de venda** - Agora, os utilizadores comerciantes podem configurar os seus próprios artigos de produtos e vender diretamente a partir do Zeus, com o PoS integrado. De momento, contém as necessidades básicas mas, no futuro, incluirá funcionalidades alargadas.
- **Registos do LND** - o utilizador pode ler em tempo real os registos de serviço do LND e utilizá-los para resolver possíveis problemas (principalmente no caso de más ligações)
- **Backups automatizados** - os canais do nó LN são automaticamente copiados para o servidor Olympus. Esta cópia de segurança automática é encriptada com o seu nó Wallet seed (sem o seed é totalmente inútil). O utilizador também pode exportar manualmente um SCB (backup de canais estáticos) para uma recuperação de desastre.


### Como embarcar no Zeus LN Node (LND incorporado)


Neste guia falarei apenas sobre o nó LND incorporado, e não sobre outras formas de usar este magnífico aplicativo (gerenciamento de nós remotos e contas LNDhub). Para os outros tipos de conexões, consulte a [página de documentação do Zeus](https://docs.zeusln.app/category/getting-started), que está muito bem explicada e não precisa de um guia dedicado.


#### PASSO 1 - CONFIGURAÇÃO INICIAL


Devido ao facto de o Zeus ser um nó LND completo, terei algumas recomendações iniciais:



- Não utilize um dispositivo antigo, pois isso pode afetar a utilização desta poderosa aplicação. Especialmente durante o período de sincronização, a aplicação pode utilizar intensivamente o CPU e a RAM. A falta destes pode mesmo impossibilitar a utilização da aplicação Zeus.
- Utilize, pelo menos, o Android 11 como sistema operativo móvel e actualize-o o mais possível. Para o iOS, o mesmo, tente utilizar uma versão muito superior do sistema operativo.
- Necessitará de, pelo menos, 1 GB de espaço em disco para armazenar os dados. Com o tempo, poderá aumentar mais, mas existe uma funcionalidade para compactar a base de dados para um nível de MBs.
- Não há necessidade de utilizar o Zeus com o serviço Tor ou Orbot. Por favor, não complique as coisas mais do que o necessário. O Tor, neste caso, não lhe vai oferecer mais privacidade, só vai piorar as coisas para a sincronização inicial. Tenha também cuidado com as VPNs que está a utilizar e verifique a latência da ligação aos servidores Neutrino. Não se esqueça de que os filtros de bloqueio Neutrino não divulgam nem localizam a identidade do seu dispositivo, apenas servem blocos. O tráfego do LN está também por detrás de um LSP com canais privados, pelo que muito pouca informação é divulgada, não há razão para se preocupar com a privacidade.
-   Tenha paciência com a sincronização inicial, pode levar vários minutos. Tente estar conectado a uma conexão de internet banda larga com boa latência. Se você executa seu próprio nó Bitcoin, [pode ativar o serviço neutrino](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) e conectar seu Zeus ao seu próprio nó, mesmo usando a LAN interna, para ter velocidade máxima.


Depois de configurar o tipo de ligação "Embedded node", a aplicação começará a sincronizar durante algum tempo. Aguarde pacientemente para concluir essa parte e, em seguida, entre na página principal das Definições.


![Image](assets/en/03.webp)


Vamos analisar brevemente cada uma das secções das Definições e compreender algumas das principais caraterísticas, antes de começar a utilizar o Zeus:


**A - DEFINIÇÕES**


Esta é uma secção com definições gerais para toda a aplicação


**1 - Lightning Service Provider (LSP)**


Aqui são apresentados dois serviços LSP:



- canais just in time_ - quando não tem nenhum canal aberto ou liquidez de entrada disponível, se o serviço estiver ativado, abrirá um canal instantaneamente para si. Esta opção pode ser desactivada se não pretender abrir mais canais deste tipo.
- _Solicitar canais com antecedência_ - pode comprar canais de entrada ao LSP da Olympus diretamente na aplicação, com várias opções e montantes (para entrada e saída).


O LSP ajuda a conectar os usuários à rede Lightning, abrindo canais de pagamento para seus nós. [Leia mais sobre LSP aqui](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). O ZEUS tem um novo LSP integrado chamado [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), que está disponível para todos os usuários que utilizam o novo nó incorporado.


Nesta secção, por defeito é o Olympus LSP (https://0conf.lnolymp.us), mas em breve poderá também definir outro LSP 0conf que suporte este protocolo.


não esquecer

_quando abre um canal com o Olympus LSP utilizando as facturas LN embrulhadas, obtém também uma liquidez de entrada de 100k! Esta é uma boa opção no caso de precisar de receber imediatamente mais facturas Sats

_Exemplo: deposita 400k Sats para abrir um canal LSP, então o LSP está a abrir um canal de 500k Sats de capacidade em direção ao seu nó Zeus e empurra os 400k Sats que depositou para o seu lado

_"Liquidez de entrada" = mais "espaço" no seu canal para receber


No futuro, esperamos poder ter muitos outros LSPs que possam ser integrados no Zeus e usar alternativamente cada um deles. É apenas uma questão de tempo até que novos LSPs adoptem um padrão aberto para este tipo de canais 0conf.


Se não pretender abrir novos canais "on the fly", pode desativar esta opção.


Nesta mesma secção, tem também a opção de escolher "request Simple Taproot Channels" quando o LSP abrir um canal para o seu nó Zeus. Estes Canais Simples Taproot oferecem uma melhor privacidade On-Chain e taxas mais baixas no fecho do canal. Existem apenas duas razões para não os querer utilizar:



- São novos e ainda pode haver erros no LND quando são utilizados.
- A sua contraparte não os suporta. Até os nós LND têm de optar explicitamente por eles, por enquanto.


**2 - Definições de pagamento**


Esta funcionalidade oferece-lhe a possibilidade de definir as suas próprias taxas preferidas para pagamentos, através do LN ou onchain. Também oferece a opção de aumentar ou diminuir o tempo limite das suas facturas.


Se alguns dos seus pagamentos LN falharem, pode aumentar a taxa para encontrar uma rota melhor. Além disso, se estiveres a fazer txs onchain, podes definir uma taxa específica para que o teu tx não fique preso no Mempool durante muito tempo, no caso de um período de taxas elevadas.


**3 - Definições das facturas**


Nesta secção são apresentadas algumas opções para as facturas generate:



- Definir um memorando padrão para ser apresentado no Invoice e no generate
- Tempo de expiração em segundos, caso pretenda um tempo específico, mais longo ou mais curto, para que o seu Invoice seja pago
- Incluir sugestões de encaminhamento - fornecer informações para encontrar canais não anunciados ou privados. Isto permite o encaminhamento de pagamentos para nós que não são visíveis publicamente na rede. Uma sugestão de encaminhamento fornece uma rota parcial entre o nó privado do destinatário e um nó público. Esta sugestão de encaminhamento é então incluída no Invoice gerado pelo destinatário e fornecido ao pagador. Sugiro que seja ativado por defeito, caso contrário os pagamentos recebidos podem falhar (não foi encontrado nenhum itinerário).
- AMP Invoice - Atomic Multi-path Payments é um novo tipo de pagamentos Lightning implementado pelo LND que permite receber Sats sem um Invoice específico, usando [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). É praticamente um código de pagamento estático. [Leia mais aqui](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Mostrar campo de pré-imagem personalizado - utilize esta opção apenas em casos muito específicos, quando pretender realmente utilizar campos personalizados na pré-imagem. [Leia mais aqui](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Outra opção nesta secção é como definir o tipo de Address em cadeia que pretende utilizar: SegWit aninhado, SegWit, Taproot.


![Image](assets/en/04.webp)


Clique no botão da roda superior e aparecerá um ecrã pop-up para escolher o tipo desejado de Address. Depois de o definir, da próxima vez que premir o botão de receção para a cadeia, o generate será o tipo de Address selecionado. Pode alterá-lo em qualquer altura.


**4 - Definições dos canais**


Nesta secção, pode pré-definir algumas caraterísticas dos canais de abertura, como por exemplo



- número de confirmações
- Anunciar canal (por defeito está desligado), o que significa que serão canais não anunciados
- Canais simples do Taproot
- Mostrar botão de compra de canal


**5 - Definições de privacidade**


Aqui encontrará algumas definições básicas para aumentar a privacidade com a aplicação Zeus:



- Block explorer para abrir detalhes de tx (Mempool.space, blockstream.info ou um personalizado)
- Ler a área de transferência - ativar/desativar se pretende que o Zeus leia a área de transferência do seu dispositivo
- Modo Lurker - alternar entre ligado e desligado se pretender ocultar informações sensíveis específicas da sua aplicação Zeus. É uma boa opção quando se fazem demonstrações ou capturas de ecrã.
- Sugestão de taxa Mempool - ativar esta opção se pretender utilizar os níveis de taxa recomendados em [Mempool.space](https://Mempool.space/)


**6 - Segurança**


Esta secção tem apenas duas opções para proteger a aplicação na abertura: definir uma palavra-passe ou um PIN.


Depois de definir um PIN para abrir a aplicação, pode também definir um "PIN de coação". Este PIN secreto adicional será utilizado APENAS em caso de situação de coação, se for ameaçado. Se colocar este PIN, a configuração será toda APAGADA. Por isso, é melhor manter as suas cópias de segurança actualizadas. As cópias de segurança automáticas estão activas por defeito, mas é bom ter também as suas próprias cópias de segurança, fora do dispositivo.


**7 - Moeda**


Ativar ou desativar a opção de apresentar uma conversão de moeda fiduciária na utilização da aplicação Zeus. Atualmente, suporta mais de 30 moedas fiduciárias em todo o mundo.


**8 - Língua**


Pode alternar entre várias línguas de tradução, revistas pela comunidade Zeus com falantes nativos.


**9 - Ecrã**


Nesta secção, pode personalizar o ecrã do Zeus, selecionando vários temas de cores, o ecrã predefinido (teclado ou balanço), mostrar o seu alias de nó, ativar os botões grandes do teclado, mostrar mais casas decimais.


**10 - Ponto de venda**


Esta é uma funcionalidade especial que permite ativar/desativar um sistema PdV integrado no Zeus. Pode utilizar um PdS autónomo ou ligado a um sistema PdS Square. Atualmente suporta funcionalidades básicas como um PoS, mas é suficiente para um bom começo e pode ajudar os pequenos comerciantes (bares/restaurantes, mercearias) a começar a aceitar BTC de uma forma nativa.


Dentro destas definições, encontrará várias opções para configurar o seu PdS:



- Tipo de confirmação de pagamento: Apenas LN, 0-conf, 1-conf
- Ativar/desativar as gorjetas para os empregados que operam o ponto de venda
- Mostrar / ocultar o teclado
- Percentagem de imposto a aplicar no bilhete
- Criar produtos e categorias de produtos
- Uma listagem simples de todas as vendas


Aqui está um vídeo de demonstração ao vivo de como utilizar o Zeus PoS:


**B - Backup Wallet**


O nó embutido no ZEUS é baseado no LND e usa o formato [aezeed seed format](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Isto é diferente do típico [formato BIP39](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) que se vê na maioria das carteiras Bitcoin, embora possa parecer semelhante. O Aezeed inclui alguns dados extra, incluindo a data de nascimento do Wallet, que ajudarão a que as novas verificações durante a recuperação sejam mais eficientes.


O formato da chave aezeed deve ser compatível com as seguintes carteiras móveis: Blixt, BlueWallet e Breez. Note-se que o seed por si só será insuficiente para recuperar todos os seus saldos se tiver canais de fecho abertos ou pendentes!


Saiba mais sobre o processo de cópia de segurança e restauro na [página Zeus Docs](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


CONSELHO DE POTÊNCIA: Quando guardares o teu seed, guarda também a pubkey do nó! Por vezes é bom tê-la à mão, juntamente com o seed e o SCB (Static Channels Backup), caso seja necessário verificar a recuperação.


O SCB só é necessário se tiveres canais LN abertos. No caso de ter apenas fundos onchain, não é necessário.


Se depois de um longo período de tempo ainda não estiver a mostrar os txs do histórico antigo, vá a Embedded node - Peers e desactive a opção de usar a lista de peers selecionados (por defeito é o btcd.lnolymp.us). Isto irá despoletar um reinício e ligar-se ao primeiro nó neutrino disponível com uma melhor resposta temporal. Ou use os outros peers de neutrino bem conhecidos mencionados abaixo.


Se quiser ver mais opções de recuperação para um nó LND, [por favor leia o meu guia anterior](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), onde pode encontrar os passos para importar um seed congelado para o Sparrow Wallet ou outros métodos.


**C - Nó incorporado**


Nesta secção, encontraremos algumas ferramentas básicas para gerir o nó integrado:



- _Disaster Recovery_ - Cópias de segurança automatizadas e manuais para os canais LN. Leia mais sobre como utilizar esta funcionalidade na página Zeus Docs.
- _Express Graph Sync_ - A aplicação Zeus descarrega o gráfico de dados de mexericos LN de um servidor dedicado, para uma sincronização mais rápida e melhor, oferecendo os melhores caminhos de pagamento. Pode também optar por limpar os dados do gráfico anterior no arranque.
- _Peers_ - secção para gerir os pares neutrino e os pares 0-conf. Se tiver problemas com a sincronização inicial e os canais não ficarem online, é porque o seu dispositivo tem uma latência elevada com o par neutrino configurado. Tente mudar a lista de pares preferidos ou adicione o seu par específico que sabe que tem melhor latência para sincronização. Os servidores neutrino mais conhecidos são:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - para a região dos EUA
 - sg.lnolymp.us - para a região da Ásia
 - btcd-Mainnet.lightning.computer - para a região dos EUA
 - uswest.blixtwallet.com (Seattle) - para a região dos EUA
 - europe.blixtwallet.com (Alemanha) - para a região da UE
 - asia.blixtwallet.com - para a região da Ásia
 - node.eldamar.icu - para a região dos EUA
 - noad.sathoarder.com - para a região dos EUA
 - bb1.breez.technology | bb2.breez.technology - para a região dos EUA
 - neutrino.shock.network - região dos EUA



- _LND logs_ - ferramenta muito útil para depurar os problemas do nó LN e controlar em profundidade o que se passa a um nível mais técnico.
- _Configurações avançadas_ - mais ferramentas para controlar a utilização do nó LND:



 - modo de procura de caminhos_ - bimodal ou apriori, formas de encontrar um melhor caminho para os pagamentos do LN e também de repor a informação anterior sobre o caminho. Por favor, leia estes guias muito bons sobre pathfinding: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - por Docs Lightning Engineering e [LN Payment Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - por Voltage
 - _Persistent LND_ - active este modo se quiser que o serviço LND funcione continuamente em segundo plano e mantenha o seu nó online 24/7. Isto é muito útil se usar o Zeus como um PoS numa pequena loja ou se estiver a receber muitas dicas do LN através do LN Address.
 - _Rescan wallet_ - esta opção irá ativar no reinício uma verificação completa de todos os txs onchain do teu Wallet. Active-a apenas no caso de faltarem algumas txs no seu Wallet. A tarefa de rescan levará algum tempo, vários minutos, por isso tem paciência e verifica sempre os logs para veres mais detalhes sobre o progresso.
 - _Compact Database_ - esta opção é muito útil se a sua aplicação Zeus estiver a ocupar muito espaço no dispositivo (consulte os detalhes da aplicação nas definições do dispositivo). Se tiver muita atividade a utilizar o Zeus, recomendo que faça esta compactação com mais frequência. Quando vir que tem mais de 1-1,5 GB de dados para a aplicação Zeus, faça a compactação. O processo será reiniciado e demorará algum tempo, por isso, seja paciente.
 - _Delete Neutrino files_ - esta opção para apagar os ficheiros neutrino (com um reinício) reduzirá bastante a utilização do armazenamento de dados. Reduzir o uso de dados também tem um grande impacto no uso da bateria, reduzindo o uso da bateria, especialmente se você usar o Zeus no modo persistente.


**D - Informação do nó**


Nesta secção, encontrará mais detalhes sobre o estado do seu nó Zeus como:



- Alias - ID de nó curto
- Public Key - a chave pública completa do seu nó, necessária para que outros nós encontrem o caminho para o seu nó. Lembra-te que esta chave pública NÃO é visível nos Exploradores LN normais (Mempool, Amboss, 1ML, etc.). Esta pubkey é acessível APENAS através de seus pares e canais LN conectados.
- Versão de implementação do LN
- Versão da aplicação Zeus
- Synced to chain (Sincronizado com a cadeia) e Synced to graph status (Sincronizado com o estado do gráfico) - são muito importantes e mostram o estado correto do seu nó. Se estes dois não estiverem a mostrar "true", significa que o seu nó ainda está a sincronizar ou está a ter alguns problemas de sincronização. Por isso, sugerimos que consulte os registos do LND ou aguarde um pouco mais.
- Altura do bloco e Hash - mostra o último bloco e Hash que o seu nó viu e sincronizou.


**E - Informação de rede**


Esta secção apresenta mais detalhes sobre o estado geral do Lightning Network, extraídos dos dados de sincronização do gráfico: número de canais públicos disponíveis, número de nós, número de canais zombie (offline ou mortos), diâmetro do gráfico, grau médio e máximo do gráfico.


Estes dados de informação podem ser úteis para depurar ou apenas utilizados para estatísticas.


**F - Relâmpago Address**


Nesta secção, o utilizador pode configurar a sua própria autocustódia LN Address @zeuspay.com.


O ZEUS PAY utiliza hashes de pré-imagem gerados pelo usuário, faturas HODL e o esquema de atestado Zaplocker Nostr para permitir que os usuários que podem não estar online 24 horas por dia, 7 dias por semana, recebam pagamentos em um relâmpago estático Address. Os utilizadores só precisam de iniciar sessão nas suas carteiras ZEUS no prazo de 24 horas para reclamar os pagamentos, caso contrário, estes serão devolvidos ao remetente.


Se ativar o "modo persistente", todos os pagamentos para o seu LN Address serão recebidos instantaneamente.


Saiba como funcionam os pagamentos [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) e mais sobre as [Taxas ZeusPay aqui](https://docs.zeusln.app/lightning-Address/fees).


**G - Endereços Onchain**


Nesta secção, pode consultar os seus endereços onchain gerados para um melhor controlo da moeda


**H - Contactos**


Na versão 0.8.0 do Zeus, foi introduzida uma nova agenda de contactos que pode ser utilizada para enviar rapidamente pagamentos aos seus amigos e familiares, com a possibilidade de importar os seus contactos do Nostr.


Basta introduzir o seu Nostr npub ou NIP-05 Address legível por humanos e o ZEUS consultará o Nostr para obter todos os seus contactos. A partir daí, pode enviar um pagamento rápido a um contacto ou importar todos ou alguns contactos para a sua agenda de contactos local


Aqui está um pequeno vídeo sobre como configurar e utilizar os contactos Zeus:


**I - Ferramentas**


Aqui temos várias subsecções com mais ferramentas:



- _Accounts_ - aqui pode importar contas/carteiras externas, carteiras Cold, carteiras Hot, para controlar ou utilizar como fonte de financiamento externo para os seus canais de nós Zeus. Esta funcionalidade ainda é experimental.
- acelerar a transacção_ - Esta funcionalidade pode ser útil quando se tem um tx preso no Mempool e se pretende aumentar a taxa. Terá de fornecer a saída da tx a partir dos detalhes da tx e selecionar a nova taxa que pretende utilizar. Tem de ser mais elevada do que a anterior e requer que tenha mais fundos disponíveis no seu Wallet onchain.


![Image](assets/en/05.webp)


Tem de ir à sua tx pendente e copiar o ponto de saída txid. Depois, vá a esta secção e cole-o. Em seguida, selecione a nova taxa que pretende utilizar para o fazer subir. Aparecerá um novo ecrã com as taxas recomendadas nesse momento, ou pode definir uma taxa personalizada. Lembra-te de que DEVE ser superior à anterior.


É sempre melhor manter um UTXO com um máximo de 100k Sats no seu Zeus onchain Wallet, para poder usá-lo para aumentar as taxas quando for necessário.



- _Sign or verify_ - Com esta funcionalidade pode assinar uma mensagem específica com as suas chaves Wallet. Também pode ser utilizada para verificar uma mensagem para provar que provém de uma determinada chave Wallet.
- _Currency converter_ - uma ferramenta simples para calcular a taxa de conversão entre BTC e outras moedas fiduciárias.


**J - Mercadoria e apoio**


Aqui encontrará mais informações e ligações sobre Zeus, loja online, patrocinadores e redes sociais.


**K - Ajuda**


Nesta última secção, encontrará ligações para a página de documentação do Zeus, problemas no Github (se pretender publicar um erro ou um pedido diretamente aos programadores de aplicações) e suporte por correio eletrónico.



### PASSO 2 - COMEÇAR A UTILIZAR O NÓ ZEUS



Lembre-se, Zeus deve ser usado principalmente como um LN Wallet, para pagamentos fáceis e rápidos através do LN. Claro que também contém um Wallet onchain, mas este deve ser utilizado exclusivamente para abrir/fechar canais LN e não para pagamentos regulares de um café.


Por favor, leia o meu outro guia sobre [como ser o seu próprio banco utilizando os 3 níveis do Stash](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


Neste momento, o utilizador tem duas formas de começar a utilizar o Zeus:



- Diretamente através do LN, utilizando o canal 0-conf do Olympus LSP
- Deposita primeiro no onchain Wallet e depois abre um canal normal LN com o par que desejas.


#### Método A - Utilizar o Olympus LSP


Esta é uma forma muito fácil e direta de integrar um novo utilizador do LN no Zeus. Pode ser um utilizador Bitcoin totalmente novo que não tenha qualquer Sats, integrado por um amigo, ou um novo comerciante que esteja a iniciar o seu primeiro pagamento LN.


Por defeito, o Zeus utilizará o seu próprio LSP, o Olympus. Mas mais tarde pode mudar para outros LSPs que suportem este protocolo 0-conf para abrir canais.


Basta criar um Invoice no seu Zeus (colocar o montante e clicar no botão "solicitar") para poder receber imediatamente esses Sats.


O Invoice que generate será [embrulhado](https://docs.zeusln.app/lsp/wrapped-invoices) e ser-lhe-ão apresentadas as taxas associadas ao serviço, se forem pagas. Este Invoice embrulhado contém dicas de rota para o seu nó Zeus, para que o LSP possa encontrar o seu novo nó e abrir um canal com os novos fundos que está a depositar.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Para obter um canal LN do LSP com os fundos que pretende receber pela 1ª vez, este Invoice deve ser pago a partir de outro LN Wallet e esperar alguns momentos até que o LSP abra o canal para o seu nó Zeus, deduza a taxa e empurre o montante restante do pagamento para o seu lado do canal.


Tudo o que tem a fazer é pagar o Invoice gerado para si em ZEUS com outro Wallet relâmpago, e o seu canal será aberto instantaneamente. [Por favor, consulte as taxas do Zeus LSP](https://docs.zeusln.app/lsp/fees).


Outra vantagem de pagar por um canal é o encaminhamento com taxa zero. Isto significa que, ao encaminhar pagamentos, o primeiro salto através da OLYMPUS by ZEUS não incorre em taxas de encaminhamento. Note-se que os saltos para além da OLYMPUS by ZEUS continuarão a ser cobrados.


Quando o canal estiver pronto, clique no botão direito na parte inferior do ecrã, que apresenta os canais Zeus.


![Image](assets/en/08.webp)


E verá um canal como este, mostrando o seu lado do equilíbrio do canal:


![Image](assets/en/09.webp)


Quanto mais gastar neste canal, mais liquidez de entrada terá. Quanto mais Sats receber neste canal, menos espaço de liquidez de entrada terá.


Aqui está uma demonstração visual simples e agradável (por Rene Pickhardt) sobre o funcionamento dos canais LN:


Neste momento, considerando o ecrã de demonstração dos canais, clique no nome do canal e verá mais detalhes sobre o mesmo.


Tem um único canal com a Olympus, com uma capacidade total de 490 000 Sats, com um saldo de 378k Sats do seu lado e 88k Sats do lado da Olympus. Isto significa que pode receber um máximo de 88k Sats a mais no mesmo canal.


Se precisar de receber mais do que 88k Sats (a liquidez de entrada disponível neste caso), digamos mais 500k Sats, basta criar um novo LN Invoice com essa quantidade para acionar um novo pedido de canal ao Olympus LSP. Assim, obterá um segundo canal.


É por isso que, para evitar pagar mais taxas pela abertura de múltiplos canais, é recomendado abrir primeiro um canal maior, digamos 1-2M Sats. Uma vez aberto, pode trocar para onchain parte desses Sats, digamos 50%, utilizando qualquer serviço de troca externo descrito neste guia.


Depois de trocar esse canal, digamos 50%, e voltar a colocar o Sats no seu próprio Zeus onchain Wallet, está pronto para passar ao método seguinte de abertura de um novo canal - a partir do balanço onchain.


#### Método B - Utilizar o seu saldo onchain


Com este método, pode abrir canais para qualquer outro nó LN, incluindo o mesmo LSP Olympus. No entanto, se já tiver um canal com a Olympus, recomenda-se que o tenha também com outro nó, para maior fiabilidade, podendo também utilizar o MPP (pagamento em várias partes).


![Image](assets/en/10.webp)


Acima está um exemplo de pagamento de um LN Invoice utilizando MPP. Como pode ver, na parte inferior do ecrã, tem "definições" e abre uma página pendente com mais detalhes sobre o pagamento que está prestes a efetuar. Nesse ecrã, se tiver pelo menos 2 canais abertos, a função MPP estará activada por defeito. Também pode ativar o AMP (atomic multi-path) e definir as partes específicas que desejar. Esta é uma funcionalidade poderosa!


Para um nó privado como o Zeus, eu recomendaria ter 2-3 bons canais (máx. 4-5), com bons LSPs e boa liquidez para cobrir todas as suas necessidades de pagar ou receber Sats em LN. [Veja mais conselhos sobre a liquidez do nó LN neste guia](/nodes/managing-lightning-node-liquidity-en.html). Também aqui outro [guia geral sobre a liquidez do LN](https://Bitcoin.design/guide/how-it-works/liquidity/) da equipa de design do Bitcoin.


Escolher os pares certos, eu sei, não é uma tarefa fácil, mesmo para utilizadores experientes. [Por isso, vou dar-vos algumas opções para começar](https://github.com/ZeusLN/zeus/discussions/2265), estes são os nós de pares que eu próprio testei utilizando o Zeus (tentei ligar-me apenas a nós LND para evitar problemas de incompatibilidade)


Aqui está também uma lista de pares de nós validados para o Zeus. Se conhecer bons nós, pode adicioná-los a essa lista.


Pode abrir um canal no Zeus indo para a vista Canais, clicando no ícone do canal no canto inferior direito da vista principal e, em seguida, no ícone + no canto superior direito.


![Image](assets/en/11.webp)


Se quiser abrir um canal com um nó específico, clique no canto superior (A) para digitalizar o QR nodeID do nó (no Mempool, Amboss, 1ML pode obter esse QR) e todos os detalhes do par serão preenchidos.


LEMBRETE:


- O nó embutido Zeus não usa o serviço Tor! Portanto, por favor, não tente abrir canais com nós que estão sob Tor! Está a causar mais danos a si próprio do que a aumentar a sua privacidade. O Tor para o LN não oferece mais privacidade, mas sim mais problemas.
- escolha sabiamente os seus pares, é melhor que sejam bons LSPs, bons nós de encaminhamento, e não nós plebeus aleatórios que podem fechar os seus canais e não podem oferecer boa liquidez. [Aqui escrevi um guia dedicado](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) sobre liquidez e exemplos de nós.


Se clicar diretamente no botão "Abrir canal para a Olympus", serão preenchidos os campos necessários para abrir um canal para [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Ao contrário dos canais LSP pagos, o teu canal necessitará de confirmação On-Chain, utilizando os teus fundos onchain (podes selecionar a partir dos teus UTXOs na visualização do canal aberto); não abrirá instantaneamente. Por favor, consulte primeiro as taxas reais do Mempool e ajuste-as de acordo, dependendo da rapidez com que deseja abrir esse canal.


Antes de premir o botão para abrir o canal, deslize para baixo as opções avançadas:


![Image](assets/en/12.webp)


Também é necessário certificar-se de que o canal não é anunciado (privado). Por predefinição, a opção está desactivada para canais anunciados. Não se recomenda que esta opção seja activada para o nó incorporado Zeus, sendo útil apenas quando utiliza o Zeus com o seu nó remoto, como um nó de encaminhamento público.


Ao contrário dos canais LSP pagos, não beneficiará de um encaminhamento de taxa zero ao abrir canais com este método.


E pronto, basta clicar no botão "Abrir Canal", aguardar que o tx seja confirmado pelos mineiros. Uma vez aberto o canal, pode efetuar as transacções que desejar com o Sats a partir dos seus canais.


Não te esqueças de que estes canais terão todo o saldo do TEU lado, pelo que não terás liquidez de entrada. Como já disse, troca ou gasta algum Sats a comprar coisas no LN para "criar mais espaço" para receber.


Pense nos seus canais LN como um copo de água. Deitas um pouco de água (Sats) num copo vazio (o teu canal) até o encheres. Não podes deitar mais água até beberes alguma (gastar / trocar). Quando o copo estiver quase vazio, deita mais água (Sats) utilizando um swap in. [Lê mais sobre serviços de troca externos aqui](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Existem também outros serviços LSP que lhe vendem canais de entrada: LNBig ou Bitrefill. Penso que existem mais serviços como estes, mas não me lembro deles neste momento.


Por isso, se precisar de um canal LN praticamente vazio (o saldo é de 100% do lado do parceiro desde o início), para receber mais pagamentos do que consegue suportar nos seus canais já preenchidos, esta pode ser uma opção muito boa. Pagará uma taxa específica para abrir estes canais e obterá bastante espaço de entrada.



## DICAS E TRUQUES


### Limites de reserva de entrada


Neste momento, devido a algumas limitações do código LN, não é possível receber exatamente o valor apresentado em "Inbound". Tenha sempre em mente que deve fazer as suas facturas com um valor ligeiramente inferior, respetivamente ao valor da "Reserva Local do Canal".


![Image](assets/en/13.webp)


Como se pode ver na imagem acima, o "inbound" mostra que ainda posso receber 5101 Sats, mas de facto neste momento é impossível receber mais. E pode observar que é a mesma quantidade que a "Reserva local".


Por isso, quando fizer facturas a receber, não se esqueça de verificar também a liquidez dos seus canais e de deduzir a reserva local desse montante, se quiser levar ao limite o montante a receber.


### Conselhos rápidos para os novos utilizadores que começam a utilizar o nó Zeus:



- Aproveite corretamente os seus novos canais.


Por exemplo, se sabe que vai receber, dentro de uma semana, digamos, 1 milhão de Sats, abra um canal de 2 milhões de Sats e troque para a cadeia Wallet ou para outra conta de custódia (temporária) LN 50-60% da sua liquidez de saída. Esteja sempre preparado com mais liquidez. Quando precisar de mais liquidez nos seus canais Zeus, pode retirá-la das contas de custódia.


Se sabe que vai enviar, digamos, 500k Sats/semana, então abra um canal de 1M Sats. Desta forma, ainda terás uma reserva até a voltares a encher.



- Se é um comerciante e recebe sempre mais do que gasta regularmente, compre um canal de entrada dedicado. É a forma mais económica. Paga uma taxa mínima e obtém um canal "vazio".



- Não abram canais pequenos e insignificantes de 50-100-300-500k Sats. Irá enchê-los numa questão de dias, mesmo que os utilize apenas para zaps. Abra canais maiores e diferentes, NÃO apenas um canal.


Depois de abrir um canal maior, pode sempre usar swaps submarinos externos para mover Sats para as suas carteiras onchain (incluindo de volta para Zeus onchain). Manter um equilíbrio entre a liquidez de entrada e saída é bom e também podes "reutilizar" esses Sats para abrir mais canais, se quiseres.


### Embrulhado Invoice


Se quiser adicionar mais privacidade ao receber, pode utilizar o método "wrapped Invoice". Lembrete: para poder fazer isto, precisa de um canal com o Olympus LSP. As facturas embrulhadas "escondem" o destino final (o seu nó Zeus) e apresentam o seu nó LSP como destino para o pagador.


Para obter um Invoice embrulhado, vá para o ecrã principal do teclado, introduza o montante e prima pedir. Aparecerá um código QR normal para o seu Invoice. Agora, clica no botão "X" no canto superior direito e serás redireccionado para mais opções para o Invoice.


![Image](assets/en/14.webp)


Agora terá de ativar a opção no topo "Enable LSP" (Ativar LSP) e premir o botão "Create Invoice" (Criar Invoice). Essa opção criará o Invoice embrulhado e, lembre-se, cobrará uma pequena taxa.


### Facturas com sugestões de itinerário


Trata-se de uma funcionalidade muito útil se pretender gerir a liquidez de vários canais de entrada. Na prática, pode indicar a que canal de entrada pretende receber o Sats de um Invoice.


Esta caraterística também pode ser utilizada para o reequilíbrio circular, quando se pretende mover a liquidez de um canal cheio para outro esgotado.


Como criar um Invoice com sugestões de itinerário?



- No ecrã principal, deslize para a direita a gaveta LN e clique em "Receber"
- Na configuração do Invoice, vá até à parte inferior e active o botão "Insert route hints" (Inserir sugestões de rota) e, em seguida, selecione o separador "Custom" (Personalizar). Abrirá um ecrã com todos os seus canais disponíveis. Selecione o que pretende receber.
- Preencher todos os outros dados do Invoice, montante, nota, etc. e clicar em "create Invoice".
- Pagar esse Invoice fará com que o Sats entre no canal indicado.


Se pretender pagar a si próprio esse Invoice (reequilíbrio circular), quando o pagar a partir do mesmo nó Zeus, no ecrã de pagamento, selecione o canal de saída (um com mais liquidez) que pretende utilizar para enviar o pagamento.


### Pagar com o Keysend


O Keysend é uma funcionalidade do LN muito subestimada e os utilizadores deveriam utilizá-la com mais frequência.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) permite aos utilizadores do Lightning Network enviar pagamentos a outros, diretamente para a sua chave pública, desde que o seu nó tenha canais públicos e tenha o keysend ativado. O Keysend não requer que o beneficiário emita um Invoice.


Como é que se pode fazer isso com o Zeus?


Basta digitalizar ou copiar o nodeID de destino (ou utilizar os contactos Zeus para guardar os seus nós de destino regulares como contactos) e, em seguida, no ecrã principal do Zeus, clicar no botão "Send" (Enviar). Nesse ecrã, cole o nodeID ou selecione a partir dos seus contactos.


Introduz o montante do Sats, uma mensagem se necessário (sim, também podes utilizá-lo como conversa secreta através do LN) e clica no botão "Enviar". Já está!


![Image](assets/en/15.webp)


Se tiver um canal direto com o par de destino, NÃO haverá taxas envolvidas.


Se não tiver um canal direto com o peer de destino, o pagamento keysend pagará as taxas como um pagamento LN Invoice normal, encaminhado por um caminho regular como qualquer outro pagamento. Só que, lembre-se, não ficará qualquer rasto como um LN Invoice.


## Conlusão


Recomendo a leitura do guia de acompanhamento [Utilização avançada do Zeus](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) com mais instruções e casos de utilização.


E... é isso! A partir de agora, basta utilizar o Zeus Node como um BTC/LN Wallet normal no seu telemóvel. A interface de utilizador é bastante simples e fácil de utilizar, intuitiva para qualquer tipo de utilizador, não creio que tenha de entrar em mais detalhes sobre como fazer e receber pagamentos.


Em conclusão, eis um quadro comparativo da privacidade :


![Image](assets/en/16.webp)
