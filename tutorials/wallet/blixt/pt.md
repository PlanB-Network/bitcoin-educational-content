---
name: Blixt Wallet
description: Como começar a utilizar um poderoso nó LN no seu telemóvel?
---
![cover](assets/cover.webp)


Este guia é dedicado a todos os novos utilizadores que queiram começar a utilizar o Bitcoin Lightning Network (LN) de uma forma GRATUITA, DE FONTE ABERTA, COMPLETA E NÃO-CUSTODIAL.


Utilizando [Blixt Wallet](https://blixtwallet.com/), um nó LN completo no seu telemóvel, onde quer que esteja.


Se nunca utilizou o Bitcoin Lightning Network, antes de começar, [leia esta analogia explicativa simples sobre o Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## ASPECTOS IMPORTANTES:



- O Blixt é um nó privado, NÃO um nó de encaminhamento! Tenha isso em mente: Isso significa que todos os canais LN no Blixt não serão anunciados ao gráfico LN (os chamados canais privados). Isto significa que este nó não fará o encaminhamento de outros pagamentos através do nó Blixt. Este nó Blixt NÃO é para encaminhamento, repito. É principalmente para poder gerir os seus próprios canais LN e fazer os seus pagamentos LN de forma privada, sempre que precisar. Este nó Blixt, é necessário estar online e sincronizado APENAS ANTES de fazer as suas transacções. É por isso que verá um ícone no topo que indica o estado da sincronização. Demora apenas alguns momentos, dependendo de quanto tempo o mantiveste offline.



- O Blixt está a usar o LND (aezeed) como backend do Wallet, por isso não tente importar outros tipos de carteiras Bitcoin para ele. [Aqui estão explicados os tipos de sementes Wallet Mnemonic](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). E aqui está [uma lista mais extensa de todos os tipos de carteiras](https://walletsrecovery.org/). Por isso, se tinha anteriormente um nó LND, pode importar o seed e o backup.channels para o Blixt, [como é explicado neste guia](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- No final deste guia, encontrará uma secção especial com ["dicas e truques"](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Ligações importantes para o Blixt - veja-as no final deste guia, marque-as.


---

## Blixt - Primeiro contacto


Então... A mãe do Darth decidiu começar a usar LN com Blixt. Decisão Hard, mas sensata. O Blixt é apenas para pessoas inteligentes e para aqueles que realmente querem aprender mais, uma utilização profunda do LN.


![blixt](assets/en/01.webp)


Darth avisa a sua mãe:


"*Mãe, se começar a utilizar o nó Blixt LN, terá de saber primeiro o que é o Lightning Network e como funciona, pelo menos a nível básico. [Aqui reuni uma lista simples de recursos sobre o Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Por favor, leia-os primeiro.*"


A mãe de Darth leu os recursos e deu o seu primeiro passo: instalar o Blixt no seu novo dispositivo Android. O Blixt também está disponível para iOS e macOS (desktop). Mas estes não são para a mãe de Darth... No entanto, recomenda-se a utilização de uma versão mais recente do Android, pelo menos 9 ou 10, para uma melhor compatibilidade e experiência. Executar um nó LN completo num dispositivo móvel não é uma tarefa fácil e pode ocupar algum espaço (mínimo 600MB) e memória.


Depois de abrir o Blixt, o ecrã "Welcome" (Bem-vindo) dá-lhe algumas opções:


![blixt](assets/en/02.webp)


No canto superior direito, verá 3 pontos que activam um menu com:



- "enable Tor" - o utilizador pode começar com a rede Tor, em especial se quiser restaurar um antigo nó LND que estava a funcionar apenas com peers Tor.
- "Set Bitcoin node" - se o utilizador quiser ligar-se diretamente ao seu próprio nó, para sincronizar os blocos através do Neutrino, pode fazê-lo imediatamente a partir do ecrã de boas-vindas. Esta opção também é boa no caso de a tua ligação à Internet ou ao Tor não ser tão estável para te ligares ao nó Bitcoin predefinido (node.blixtwallet.com).
- Em breve será adicionada a língua, para que o utilizador possa começar diretamente com uma língua que lhe seja confortável. Se quiser contribuir para este projeto de código aberto com traduções noutras línguas, [junte-se aqui](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### OPÇÃO A - Criar um novo Wallet


Se optar por "criar um novo Wallet", será redireccionado diretamente para o ecrã principal do Blixt Wallet.


Este é o seu "cockpit" e também é o "Main LN Wallet", por isso tenha em atenção que só lhe mostrará o saldo do seu LN Wallet. O Wallet em cadeia é apresentado separadamente (ver C).


![blixt](assets/en/03.webp)


A - Ícone indicador de sincronização de blocos Blixt. Esta é a coisa mais importante para um nó LN: estar sincronizado com a rede. Se este ícone ainda estiver a funcionar, significa que o teu nó NÃO ESTÁ PRONTO! Por isso, tenha paciência, em especial para a primeira sincronização inicial. Pode demorar até 6-8 minutos, dependendo do seu dispositivo e da ligação à Internet.


Pode clicar nele e ver o estado da sincronização:


![blixt](assets/en/04.webp)


Também pode clicar no botão "Show LND Log" (A) se quiser ver e ler mais pormenores técnicos do registo do LND, em tempo real. É muito útil para depurar e aprender mais sobre o funcionamento do LN.


B - Aqui pode aceder a todas as configurações do Blixt, e são muitas! O Blixt oferece muitos recursos e opções para gerenciar seu nó LN como um profissional. Todas essas opções são explicadas em detalhes na "[Blixt Features Page](https://blixtwallet.github.io/features#blixt-options) - Options Menu".


C - Aqui tem o menu "Magic Drawer", [também explicado em pormenor aqui](https://blixtwallet.github.io/features#blixt-drawer). Aqui está o "Onchain Wallet" (B), Canais relâmpago (C), Contactos, ícone de estado dos canais (A), Keysend (D).


![blixt](assets/en/05.webp)


D - É o menu de ajuda, com ligações para a página de FAQ / Guias, contactar o programador, página Github e grupo de apoio do Telegram.


E - Indique o seu primeiro BTC Address, onde pode depositar o seu primeiro teste Sats. ISTO É OPCIONAL! Se depositar diretamente nesse Address, está a abrir um canal LN em direção ao Blixt Node. Isso significa que verá o seu Sats depositado, indo para outra transação onchain (tx), para abrir esse canal LN. Pode verificar isso no Blixt onchain Wallet (ver ponto C), clicando no menu TX no canto superior direito.


![blixt](assets/en/06.webp)


Como pode ver no registo de transacções Onchain, os passos são muito detalhados, indicando para onde vão os Sats (depósito, abrir, fechar canal).


RECOMENDAÇÃO:


Depois de testar várias situações, chegámos à conclusão de que é muito mais eficiente abrir canais entre 1 e 5 M Sats. Os canais mais pequenos tendem a esgotar-se rapidamente e a pagar uma percentagem de taxas mais elevada em comparação com os canais maiores.


F - Indica o seu saldo principal de Lightning Wallet. Este NÃO é o teu saldo total de Blixt Wallet, representa apenas o Sats que tens nos Lightning Channels, disponível para enviar. Como foi indicado anteriormente, o Wallet Onchain é separado. Tenha em mente este aspeto. O Wallet onchain é separado por uma razão importante: é usado principalmente para abrir/fechar canais LN.


Ok, então agora a mãe de Darth depositou alguns Sats no Address onchain exibido no ecrã principal. Recomenda-se que, ao fazer isso, mantenha a sua aplicação Blixt online e ativa durante algum tempo, até que o BTC tx seja levado pelos mineiros para o primeiro bloco.


Depois disso pode demorar até 20-30 minutos até que esteja totalmente confirmado e o canal esteja aberto e o verá na Gaveta Mágica - Canais Relâmpago como ativo. Também o pequeno ponto colorido no topo da gaveta, se for Green, indicará que o teu canal LN está online e pronto a ser usado para enviar Sats sobre LN.


O Address e a mensagem de boas-vindas apresentada desaparecerão. Agora já não é necessário abrir um canal automático. Também pode desativar a opção no menu Definições.


É altura de seguir em frente, testando outras funcionalidades e opções para abrir canais LN.


Agora, vamos abrir outro canal com outro par de nós. A comunidade Blixt elaborou [uma lista de bons nós para começar a utilizar com a Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Procedimento para abrir um canal LN no Blixt**


Isto é muito simples, bastam alguns passos e um pouco de paciência:



- Entrou na lista de pares da [Comunidade Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- Selecionar um nó e clicar na ligação do título do seu nome, o que abrirá a sua página Amboss
- Clicar para apresentar o código QR para o nó URI Address


![blixt](assets/en/07.webp)


Abra o Blixt e vá para a gaveta superior - Canais de relâmpagos e clique no botão "+"


![blixt](assets/en/08.webp)


Agora, clique na câmara (A) para digitalizar o código QR da página do Amboss e os detalhes do nó serão preenchidos. Adicione o montante do Sats para o canal que pretende e, em seguida, selecione a taxa de taxa para o tx. Pode deixá-lo automático (B) para uma confirmação mais rápida ou ajustá-lo manualmente deslizando o botão. Também pode premir longamente o número e editá-lo como quiser.


Não colocar menos de 1 sat/vbyte! Normalmente, é melhor consultar as [taxas Mempool](https://Mempool.space/) antes de abrir um canal e selecionar uma taxa conveniente.


Feito isso, agora é só clicar no botão "abrir canal" e aguardar 3 confirmações, o que normalmente leva 30 minutos (1 bloco aproximadamente a cada 10 minutos).


Uma vez confirmado, verá o canal ativo na sua secção "Canais Relâmpago".


---

## Blixt - Segundo contacto


Ok, então agora temos um canal LN com apenas liquidez OUTBOUND. Isso significa que só podemos ENVIAR, mas ainda não podemos RECEBER Sats através do LN.


![blixt](assets/en/09.webp)


Porquê? Leu os guias indicados no início? Não? Volte atrás e leia-os. É muito importante compreender o funcionamento dos canais LN.


![blixt](assets/en/10.webp)


Como pode ver neste exemplo, o canal aberto com o primeiro depósito não tem muita liquidez de ENTRADA ("Pode receber"), mas tem muita liquidez de SAÍDA ("Pode enviar").


Que opções tem, então, se quiser receber mais Sats do que LN?



- Gastar alguns Sats do canal existente. Sim, o LN é uma rede de pagamento do Bitcoin, usada principalmente para gastar seu Sats de forma mais rápida, barata, privada e fácil. O LN NÃO é uma forma de hodling, para isso você tem o Wallet onchain.



- Troca alguns Sats, de volta para o teu Wallet onchain, usando um serviço de troca submarino. Desta forma, não está a gastar o seu Sats, mas a devolvê-lo ao seu próprio Wallet onchain. Aqui podes ver em detalhe alguns métodos, na [Blixt Guides Page](https://blixtwallet.github.io/guides).



- Abrir um canal INBOUND a partir de qualquer fornecedor de LSP. Aqui está um vídeo de demonstração sobre como usar o LNBig LSP para abrir um canal de entrada. Isto significa que pagará uma pequena taxa por um canal VAZIO (do seu lado) e poderá receber mais Sats nesse canal. Se é um comerciante que recebe mais do que gasta, esta é uma boa opção. Também se estiver a comprar Sats em vez de LN, utilizando Robosats ou qualquer outro LN Exchange.



- Abrir um canal Dunder, com o nó Blixt ou qualquer outro fornecedor de Dunder LSP. Um canal Dunder é uma forma simples de obter alguma liquidez INBOUND, mas ao mesmo tempo deposita algum Sats nesse canal. Também é bom porque vai abrir o canal com um [UTXO](https://en.Bitcoin.it/wiki/UTXO) que não é do seu Blixt Wallet. Isso acrescenta alguma privacidade. Também é bom porque, se não tiveres Sats num Wallet onchain, para abrir um canal LN normal, mas os tiveres noutro LN Wallet, podes simplesmente pagar desse outro Wallet através do LN a abertura e o depósito (do teu lado) desse canal Dunder. [Mais detalhes sobre como funciona o Dunder e como gerir o seu próprio servidor aqui](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Eis os passos para ativar a abertura de um canal Dunder:



- Vá a Definições e, na secção "Experiências", active a caixa "Ativar Dunder LSP".
- Uma vez feito isso, volte à secção "Lightning Network" e verá que apareceu a opção "Set Dunder LSP Server" (Definir servidor Dunder LSP). Aí, por defeito, está definido "https://dunder.blixtwallet.com", mas pode alterá-lo com qualquer outro fornecedor de Dunder LSP Address. [Aqui está uma lista da comunidade Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) com nós que podem fornecer canais Dudner LSP para o seu Blixt.
- Agora pode ir para o ecrã principal e clicar no botão "Receive" (Receber). Em seguida, siga este procedimento [explicado neste guia](https://blixtwallet.github.io/guides#guide-lsp).


OK, assim, depois de o canal Dunder ser confirmado (demorará alguns minutos), acabará por ter 2 canais LN: um aberto inicialmente com o piloto automático (canal A) e outro com mais liquidez de entrada, aberto com o Dunder (canal B).


![blixt](assets/en/12.webp)


Ótimo, agora está pronto para enviar e receber Sats suficiente sobre LN!


FELIZ Bitcoin LIGHTNING!


---

## Blixt - Terceiro contacto


Lembre-se que no capítulo um "Primeiro contacto" havia duas opções no ecrã de boas-vindas:


- [Opção A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Criar um novo Wallet
- Opção B - Restaurar o Wallet


Vamos agora falar sobre como restaurar um Blixt Wallet ou qualquer outro nó LND que tenha sofrido um acidente. Isto é um pouco mais técnico, mas por favor preste atenção. Não é o Hard.


### OPÇÃO B - Restaurar a Wallet


No passado, escrevi um guia dedicado sobre [como restaurar um nó Umbrel que caiu](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), onde mencionei também o método de usar o Blixt como processo de restauração rápida, usando o ficheiro seed + channel.backup da Umbrel.


Também escrevi um guia sobre como restaurar o seu nó Blixt ou migrar o seu Blixt para outro dispositivo, [aqui](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Mas vamos explicar este processo em passos simples. Como pode ver na imagem acima, há duas coisas que deve fazer para restaurar o seu nó Blixt/LND anterior:



- a caixa superior é onde tem de preencher as 24 palavras do seu seed (nó antigo / morto)
- existem duas opções de botão para inserir / carregar o arquivo channel.backup, previamente salvo do seu antigo nó Blixt / LND. Pode ser a partir de um ficheiro local (carregaste-o no teu dispositivo anteriormente) ou pode ser a partir de uma localização remota do Google drive / iCloud. O Blixt tem esta opção para salvar o backup de seus canais diretamente em uma unidade do Google / iCloud. Veja mais detalhes em [Blixt Features Page](https://blixtwallet.github.io/features#blixt-options).


No entanto, se anteriormente não tinha nenhum canal LN aberto, não há necessidade de carregar nenhum ficheiro channels.backup. Basta inserir as 24 palavras do seed e premir o botão de restauro.


Não se esqueça de ativar o Tor, no menu dos 3 pontos superiores, como explicámos na secção Opção A. É o caso quando só tem pares Tor e não pode ser contactado através da clearnet (domínio/IP). Caso contrário, não é necessário.


Outra funcionalidade útil é definir um nó Bitcoin específico a partir desse menu superior. Por defeito, sincroniza blocos a partir de node.blixtwallet.com (modo neutrino), mas pode definir qualquer outro nó Bitcoin que forneça sincronização neutrino.


Assim que preencher estas opções e premir o botão de restauro, o Blixt começará primeiro a sincronizar os blocos através do Neutrino, como explicámos no capítulo Primeiro Contacto. Por isso, seja paciente e observe o processo de restauro no ecrã principal, clicando no ícone de sincronização.


![blixt](assets/en/14.webp)


Como pode ver neste exemplo, mostra que os blocos Bitcoin estão 100% sincronizados (A) e o processo de recuperação está em curso (B). Isso significa que os canais LN que você tinha anteriormente serão fechados e os fundos serão restaurados no seu Blixt onchain Wallet.


Este processo leva tempo! Por isso, seja paciente e tente manter o seu Blixt ativo e online. A sincronização inicial pode demorar até 6-8 minutos e o fecho dos canais pode demorar até 10-15 minutos. Por isso, é melhor ter o dispositivo bem carregado.


Uma vez iniciado este processo, pode verificar na Gaveta Mágica - Canais Relâmpago, o estado de cada um dos seus canais anteriores, mostrando que estão no estado "pendente para fechar". Uma vez fechado cada canal, pode ver o tx de fecho no Wallet onchain (ver Gaveta Mágica - Onchain), e abrir o registo do menu tx.


![blixt](assets/en/15.webp)


Também será bom verificar e adicionar, se não estiverem lá, os seus pares anteriores que tinha no seu antigo nó LN. Por isso, vá ao menu Settings (Definições), desça até "Lightning Network" e entre na opção "Show Lightning Peers" (Mostrar pares relâmpago).


![blixt](assets/en/16.webp)


Dentro da secção, verá os pares a que está ligado nesse momento e poderá adicionar mais, sendo melhor adicionar aqueles que já tinha canais anteriormente. Basta ir a [Amboss page](https://amboss.space/), procurar os pseudónimos ou o nodeID dos nós dos seus pares e procurar o URI do nó.


![blixt](assets/en/17.webp)


Como se pode ver na imagem acima, existem 3 aspectos:


A - representa o URI do nó da clearnet Address (domínio/IP)


B - representa o nó Tor onion URI Address (.onion)


C - é o código QR a digitalizar com a sua câmara Blixt ou o botão de cópia.


Este URI do nó Address tem de ser adicionado à sua lista de pares. Por isso, tenha em atenção que não é suficiente apenas o nome do alias do nó ou o nodeID.


Agora podes ir a Magic Drawer (menu superior esquerdo) - Lightning Channels, e podes ver em que altura do bloco de maturidade os fundos serão devolvidos ao teu onchain Address.


![blixt](assets/en/18.webp)


O bloco número 764272 é o momento em que os fundos poderão ser utilizados na tua Bitcoin onchain Address. E pode demorar até 144 blocos desde o primeiro bloco de confirmação até serem libertados. [Por isso, verifica isso no Mempool](https://Mempool.space/).


E é só isso. Aguarde pacientemente até que todos os canais sejam fechados e os fundos voltem para o seu Wallet onchain.


👉 **Método de restauro secreto :**


Existe outro método para restaurar o teu nó Blixt LND sem sequer fechar os canais. Mas está escondido dos utilizadores noob habituais, porque este método é APENAS para aqueles que sabem o que estão a fazer.


Se precisar de migrar o seu nó Blixt existente (em funcionamento) para outro dispositivo novo, sem fechar os canais LN existentes, terá de seguir estes passos:



- Suponhamos que já guardou o Blixt Wallet seed (24 palavras aezeed)
- No dispositivo antigo, vá a "Settings" (Definições) - secção debug (depuração) - "Compact LND database" (Compactar base de dados LND). Este passo é opcional, mas recomendado se pretender um tamanho mais pequeno do ficheiro channel.db. Normalmente é bastante grande, dependendo da atividade do seu nó. Isto reiniciará o Blixt e compactará o tamanho do ficheiro db.
- Depois de reiniciar, vá a "Definições" e altere o seu nome de utilizador normal para "Hampus". Isto activará as opções ocultas, apenas para utilizadores avançados.
- Vai até à secção "Debug" e verás uma nova opção "Export channel.db file". ATENÇÃO! Quando fizer esta exportação, o nó Blixt LN existente será desativado neste dispositivo antigo e exportará toda a base de dados do nó (channel.db), pronta para ser importada para um novo dispositivo.
- Este ficheiro db será guardado numa pasta designada no seu antigo dispositivo (Documentos ou Transferências) e, a partir daí, terá de o mover tal como está para o seu novo dispositivo. Pode utilizar, por exemplo, a [LocalSend FOSS app](https://github.com/localsend/localsend) para transferir o ficheiro diretamente entre dispositivos.
- Neste momento, o vosso Blixt antigo DEVE permanecer encerrado. NÃO O ABRA NOVAMENTE!
- Depois de transferir o ficheiro channel.db para o novo dispositivo, inicie a nova instalação do Blixt e escolha "Restore Wallet" (Restaurar Wallet) no primeiro ecrã.
- No botão onde diz "Select SCB file" (Selecionar ficheiro SCB), prima longamente (NÃO faça um simples clique!) e verá a opção de selecionar um ficheiro channel.db para o guardar localmente no novo dispositivo. Se premir simplesmente esse botão, será utilizado por predefinição um ficheiro SCB (com canais fechados), mas não funciona para cópias de segurança completas de canais em direto.
- Coloque as 24 palavras seed e clique em "Restore" (Restaurar)
- Verá que o Blixt começará a sincronizar-se com o Neutrino. Também pode ver os registos de sincronização.
- TENHAM EM MENTE! Tenta manter o Blixt sempre aberto durante esta fase! Não o deixe entrar em suspensão nem feche o ecrã da aplicação. Isso pode interromper a sincronização inicial e ter de a fazer novamente. Aguarde pacientemente, não está a demorar mais do que alguns minutos.
- Assim que a sincronização dos blocos iniciais estiver concluída, o sistema irá analisar rapidamente os endereços anteriores do Wallet e os seus canais estarão novamente online, vivos e de boa saúde.
- Infelizmente, não é possível (ainda) restaurar o histórico de pagamentos e os contactos anteriores. Mas, de qualquer forma, isso não é assim tão importante.


E pronto! Agora tens um nó Blixt LN totalmente restaurado. Também pode funcionar com outros backups do LND (Umbrel, Raspiblitz, etc.) se tiveres guardado corretamente o ficheiro channel.db. Assim, o Blixt pode literalmente salvar qualquer nó morto do LND.


---

## Blixt - Quarto contacto


Este capítulo é sobre personalização e conhecer melhor o Blixt Node. Não vou descrever todas as funcionalidades disponíveis, pois são demasiadas e já foram explicadas na [Blixt Features Page](https://blixtwallet.github.io/features).


Mas vou indicar alguns dos elementos necessários para continuar a utilizar o seu Blixt e ter uma óptima experiência.


### A - Nome (NameDesc)


![blixt](assets/en/19.webp)


[O NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) é uma norma para transmitir o "nome do destinatário" nas facturas BOLT11.


Pode ser qualquer nome e pode ser alterado em qualquer altura.


Esta opção é muito útil em vários casos, quando se pretende enviar um nome juntamente com a descrição do Invoice, para que o destinatário possa ter uma ideia de quem recebeu esses Sats. Esta opção é totalmente facultativa e, também no ecrã de pagamento, o utilizador tem de assinalar a caixa que indica o envio do nome alternativo.


Eis um exemplo de como apareceria quando utilizasse [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Este é outro exemplo de envio para outra aplicação Wallet que suporta NameDesc:


![blixt](assets/en/21.webp)


### B - Caixa de relâmpagos


A partir da nova v0.6.9-420 [recentemente anunciada](https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), o Blixt introduziu uma nova e poderosa funcionalidade para o Lightning Address no Blixt.


Esta nova funcionalidade é opcional e não está activada por defeito!


De momento, a Caixa LN por defeito é executada pelo servidor Blixt e oferece um @blixtwallet.com LN Address. Mas QUALQUER PESSOA com um nó público LND pode executar o servidor Lightning Box e oferecer LN Address para o seu próprio domínio, auto-custódia.


Neste momento, o servidor Blixt apenas reencaminha os pagamentos enviados para os endereços LN @blixtwallet.com para os utilizadores Blixt que definiram o seu LN Address. Os utilizadores devem colocar o seu nó Blixt Wallet em "modo persistente" para poderem receber estes pagamentos nos seus endereços LN @blixtwallet.com.


Veja nas notas de lançamento o vídeo de demonstração sobre como configurar o seu LN Address no Blixt.


Este LN Address implementado na aplicação Blixt Wallet, é como um chat sobre LN, instantâneo e divertido, suportando também [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (adicionar um nome de alias a um pagamento). Pode adicionar na lista de contactos todos os seus endereços LN regulares que utiliza frequentemente e tê-los à mão para conversar. Agora Blixt pode ser considerado um aplicativo de bate-papo LN completo 😂😂.


Outra caraterística útil é o suporte total ao LUD-18 (que também [Stacker.News](https://stacker.news/r/DarthCoin) e outros estão a suportar).


![blixt](assets/en/22.webp)


Como se pode ver na captura de ecrã acima, ao enviar a partir de uma conta Stacker News, o logótipo + LN Address + mensagem foram bem apresentados. A mesma forma funciona para enviar a partir do Blixt, pode anexar o seu Blixt LN Address ou simplesmente adicionar o nome do alias (previamente definido nas definições do Blixt) ou mesmo ambos.


Esta opção do LUD-18 também pode ser útil para serviços de subscrição, em que o utilizador pode enviar um pseudónimo específico (que NÃO é o pseudónimo do seu nó ou o seu nome verdadeiro!) e, com base nele, pode ser registado ou receber uma mensagem específica ou qualquer outra coisa. Anexar um nome de alias ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+ comentário ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) a um pagamento LN pode ter múltiplas utilizações!


Aqui está o código para a [Lightning Box](https://github.com/hsjoberg/lightning-box) se a executares para ti, para a tua família e amigos, no teu próprio nó.


Aqui também pode executar o [servidor LSP Dunder](https://github.com/hsjoberg/dunder-lsp) para nós móveis Blixt e oferecer liquidez aos utilizadores Blixt se tiver um bom nó público LN (funciona apenas com LND).


### C - Backup de canais LN e palavras seed


Esta é uma caraterística muito importante!


Depois de abrir ou fechar um canal LN, deves fazer uma cópia de segurança. Pode ser feito manualmente, guardando um pequeno ficheiro no dispositivo local (normalmente na pasta de transferências) ou utilizando uma conta Google Drive ou iCloud.


![blixt](assets/en/23.webp)


Vá para a secção Definições do Blixt - Wallet. Aí tem as opções para guardar todos os dados importantes do seu Blixt Wallet:



- "Show Mnemonic" - mostra as 24 palavras seed para as escrever
- "Remove Mnemonic from device" (Remover Mnemonic do dispositivo) - esta opção é opcional e só deve ser usada se você realmente quiser remover as palavras seed do seu dispositivo. Isto NÃO limpará o seu Wallet, apenas o seed. Mas atenção! Não há forma de as recuperar se não as tiver anotado primeiro.
- "Exportar cópia de segurança do canal" - esta opção guarda um pequeno ficheiro no seu dispositivo local, normalmente na pasta "transferências", de onde o pode retirar e mover para fora do seu dispositivo, para o guardar em segurança.
- "Verify channel backup" (Verificar cópia de segurança do canal) - esta é uma boa opção se utilizar o Google Drive ou o iCloud para verificar a integridade da cópia de segurança efectuada remotamente.
- " Google drive channel backup" - guardará o ficheiro de cópia de segurança no seu Google Drive pessoal. O ficheiro é encriptado e é armazenado num repositório separado dos seus ficheiros Google habituais. Assim, não há preocupações que possam ser lidas por qualquer pessoa. De qualquer forma, esse ficheiro é totalmente inútil sem as palavras seed, pelo que ninguém pode retirar os seus fundos apenas desse ficheiro.


Recomendo para esta secção o seguinte:



- utilize um gestor de senhas para armazenar com segurança o seu seed e o ficheiro de cópia de segurança. KeePass ou Bitwarden são muito bons para isso e podem ser usados em multiplataformas e auto-hospedados ou offline.
- FAÇA O BACKUP SEMPRE que abrir ou fechar um canal. Esse ficheiro é atualizado com as informações dos canais. Não há necessidade de o fazer após cada transação que fizeste no LN. O backup do canal não está a armazenar essa informação, está a armazenar apenas o estado do canal.


![blixt](assets/en/24.webp)


---

## Blixt - Dicas e truques


### CASO 1 - PROBLEMAS DE SINCRONIZAÇÃO


"_O meu Blixt não está a sincronizar... O meu Blixt não mostra o saldo... O meu Blixt não consegue abrir canais... Tentei restaurá-lo noutro dispositivo... etc_"


Todos estes problemas começam porque o seu dispositivo não está a sincronizar corretamente. Por favor, compreenda este aspeto importante: Blixt é um nó móvel LND, que usa Neutrino para sincronizar / ler os blocos.



- Eis uma explicação menos técnica da [Bitcoin Magazine](https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Eis mais recursos técnicos da [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Eis como pode ativar o Neutrino no seu próprio nó doméstico e servir filtros de blocos para o seu nó móvel, a partir de [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


LEMBRETE: Usar o Neutrino através da clearnet é totalmente seguro, o teu IP ou xpub não são divulgados. Está apenas a ler blocos de um nó remoto com o neutrino. Isso é tudo. Todo o resto é feito no seu dispositivo local.


Portanto, não há NENHUMA NECESSIDADE de usá-lo com o Tor. O Tor adicionará uma enorme latência ao seu processo de sincronização e tornará o seu Blixt muito instável. Se quiser mesmo utilizar o Tor, tenha a certeza do que está a fazer e tenha uma boa ligação e paciência. O mesmo se aplica à utilização de uma VPN. Tenha cuidado com a latência que lhe é fornecida por essa VPN.


Pode testar a latência de um servidor de neutrinos através de um simples ping, a partir de um PC ou do seu telemóvel.


![blixt](assets/en/25.webp)


Este é um ping normal para o servidor neutrino europe.blixtwallet.com, que mostra que a ligação é muito boa, com um tempo de resposta médio de 50 ms e um TTL de 51. O tempo de resposta pode variar, mas não demasiado. O TTL deve ser estável.


Se estes valores forem superiores a 100-150ms, o seu processo de sincronização ficará obsoleto ou, pior ainda, poderá causar canais fechados pelos pares! Não ignore este aspeto.


Sem uma sincronização adequada, também não é possível ver o equilíbrio correto ou os seus canais LN não ficarão online e operacionais. Não importa quantos giga ultra terra mbps tenha a velocidade de download, NÃO IMPORTA. O que importa é o tempo de resposta e o TTL (time to live).


Este é um caso geral para os utilizadores da América Latina. Não sei o que se passa aí, mas vocês têm uma ligação terrível com pings de mais de 200ms que podem perturbar qualquer sincronização.


Então, qual é a solução para estes utilizadores desesperados?



- deixar de utilizar o Blixt com o Tor. É totalmente inútil
- pode utilizar uma VPN, mas escolha-a com cuidado e monitorize sempre o ping. Utilize uma que esteja mais próxima da sua localização geográfica. A distância significa mais tempo de resposta, lembre-se.
- selecione sabiamente os seus pares de neutrinos, eis uma lista de servidores públicos de neutrinos bem conhecidos:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Outra forma é selecionar um dos nós desta lista que anuncia os "filtros compactos" (BIP157 / neutrino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Escolhe um que esteja mais próximo da tua localização geográfica.


Outra forma (a melhor forma) é ligar-se a um nó da comunidade local, gerido por um amigo ou grupo que conheça, e que esteja a oferecer uma ligação de neutrinos. (https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) O nó deles não será afetado de forma alguma, apenas precisam de uma ligação estável e pública.


Há uma necessidade de mais servidores neutrino na região LATAM, para uma melhor e mais rápida sincronização. Então, por favor, organize-se com a sua comunidade local do Bitcoin e decida quem e onde está executando um Bitcoin Core + Neutrino para seu próprio uso. Com apenas um IP público é suficiente. Se não tiveres acesso a um IP público, podes usar um IP VPS e fazer um túnel wireguard para o teu nó doméstico. Dessa forma, redirecciona todo o tráfego para o seu IP VPS local, sem revelar qualquer informação privada sobre o seu nó doméstico.


### CASO 2 - NUNCA TERMINAR A SINCRONIZAÇÃO


"_O meu Blixt tem uma boa ligação com o servidor neutrino, mas a sincronização está bloqueada


#### Servidor de tempo


Por vezes, as pessoas usam vários dispositivos antigos ou não estão corretamente ligadas a um servidor de tempo. O Neutrino está a sincronizar bem até chegar aos blocos que não correspondem à hora local real. Verá nos registos do Blixt LND um erro que diz que "o carimbo de tempo do bloco está longe do futuro" ou algo relacionado com "o cabeçalho não passa na verificação de sanidade".


Correção rápida: defina a hora e a data corretas para o seu dispositivo e reinicie o Blixt.


#### Pouco espaço no dispositivo


Por vezes, ao utilizar um dispositivo antigo, com pouco espaço, pode atingir um limite e ficar preso. De facto, quanto mais se usa este nó móvel LND, mais os ficheiros de neutrinos aumentam e também o ficheiro channel.db.


Correção rápida: Ir para Blixt Options - Debug section - Selecionar "stop LND and delete neutrino files". A aplicação será reiniciada e será iniciada uma nova sincronização. Por vezes, esta correção rápida também pode reparar dados corrompidos. Lembre-se de que levará algum tempo, entre 1 e 3 minutos, para sincronizar completamente. NÃO está a apagar os fundos ou canais existentes, mas sim, após a ressincronização, pode desencadear uma nova análise dos seus endereços Bitcoin e isso pode demorar mais tempo.


O próximo passo é verificar a quantidade de dados que ainda está ocupada. Pode ver isso em Android App info - data. Se ainda for superior a 400-500MB, pode compactar os ficheiros LND. Por isso, vá a Blixt Options - Debug section - Selecione "Compact DB LND". Reinicie a aplicação Blixt se não o fizer automaticamente. A compactação ocorre no arranque e é feita apenas uma vez. Agora verá que os dados do Blixt estão mais ou menos ocupados.


#### Modo persistente


Por vezes, as pessoas não abrem o Blixt durante muito tempo, pelo que a sincronização é demasiado antiga. Mas esperam ser sincronizadas instantaneamente quando o abrem.


Tenha paciência e observe a roda giratória superior. Opcionalmente, pode ir a Options - See Node Info e ver se a sincronização com a cadeia e a sincronização com o gráfico estão marcadas como "true". Sem essa menção "true", não pode utilizar corretamente o Blixt, não pode ver corretamente o saldo, não pode ver os canais LN online, não pode fazer pagamentos.


Solução rápida: Existe uma opção poderosa para "manter vivo" o teu nó Blixt. Vá a Options - Experiments - Selecione "Activate Persistent Mode" (Ativar modo persistente). Isso reiniciará o Blixt e colocará o serviço LND em modo persistente, ou seja, estará sempre ativo e manterá a sincronização online, mesmo que mude para outra aplicação ou simplesmente feche o Blixt (não force o fecho ou elimine a tarefa). Pode mantê-lo assim durante todo o dia se estiver numa ligação estável e precisar de utilizar o Blixt várias vezes. Não irá consumir demasiada bateria.


### CASO 3 - QUERO MIGRAR PARA OUTRO DISPOSITIVO


Relativamente a este cenário, escrevi um guia exaustivo na [página de FAQ](https://blixtwallet.github.io/faq#blixt-restore): com 2 opções, rápida (fecho cooperativo de canais antes da migração) e lenta (fecho forçado de canais porque o dispositivo antigo está morto).


Mas gostaria de reiterar aqui alguns aspectos importantes e acrescentar um novo procedimento "secreto".


LEMBRETE:



- Faça sempre uma cópia de segurança do estado dos seus canais (SCB) DEPOIS de cada vez que abrir ou fechar um canal. Demora apenas alguns segundos a fazê-lo.
- Não conservar os ficheiros SCB antigos, para não se confundir e os restaurar. São totalmente inúteis e podem desencadear um processo de penalização se os utilizar. Utilize sempre a última versão do ficheiro SCB se proceder ao seu restauro.
- Guarde o ficheiro SCB (é um texto encriptado com a extensão .bin) fora do seu dispositivo, num local seguro. Pode utilizar [LocalSend](https://github.com/localsend/localsend) para mover este ficheiro para um PC ou outro dispositivo.
- Guarde também o seed do seu Blixt Wallet num local seguro, por exemplo, um gestor de senhas offline / USB encriptado.


Método secreto: Como migrar o nó Blixt sem fechar os canais existentes. Para isso, terá de ler atentamente a secção anterior "Terceiro contacto" deste guia sobre "Restaurar o Wallet".


Este procedimento NÃO É PARA NOOBS, é apenas para utilizadores avançados! É por isso que não está amplamente aberto e recomendo que o faça apenas com a ajuda dos programadores do Blixt ou do meu apoio. Por favor, não ignore este conselho.


### CASO 4 - QUE PARES UTILIZAR PARA ABRIR CANAIS?


Como escrevi na [página de guias do Blixt](https://blixtwallet.github.io/guides) há muitas maneiras de abrir canais com este nó móvel LND. Mas gostaria de recordar aqui alguns aspectos importantes:



- aberto com nós LSP bem conhecidos e com pares validados pela comunidade. [Ver aqui uma lista](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- não abrir com nós Tor aleatórios. Estes não valem nada e só te darão problemas de impossibilidade de efetuar pagamentos. Por muito bom que seja o teu amigo "the node runner" com um nó Tor de merda numa selva, ele nunca te dará as melhores rotas para um nó privado móvel. Não se abrem canais com alguém só porque é seu amigo. Isto não é o Facebook! Abre-se um canal por: boas rotas, taxas reduzidas, disponibilidade.
- não há necessidade de abrir uma tonelada de canais pequenos, 2-3 ou no máximo 4, mas com uma boa quantidade de Sats. Não abrir canais pequenos, são totalmente inúteis. Os canais mais pequenos do que 200k para um telemóvel não têm grande utilidade.
- tenha em mente os LSPs que oferecem canais de entrada e canais JIT (just in time). Estes são muito úteis porque não precisas de usar nenhum dos teus UTXOs, podes pagar o canal de abertura com fundos que já tens noutras carteiras LN, empilhando-os e preparando-os para a abertura de um canal maior. Deves usar estes canais JIT a teu favor. [Já expliquei neste guia](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) mais opções de peers para nodes privados como Blixt. Também [aqui neste guia publicado na SN](https://stacker.news/items/679242/r/DarthCoin) expliquei como gerir a liquidez dos nós móveis privados.


---

## Conclusão


OK, existem muitas outras funcionalidades fantásticas que o Blixt oferece, vou deixá-lo descobri-las uma a uma e divertir-se.


Esta aplicação é realmente subestimada, principalmente porque não é apoiada por qualquer financiamento VCs, é orientada para a comunidade, construir com amor e paixão para Bitcoin e Lightning Network.


Este nó móvel LN, Blixt, é uma ferramenta muito poderosa nas mãos de muitos utilizadores, se souberem utilizá-la bem. Imagine-se a andar pelo mundo com um nó LN no seu bolso e ninguém o saberá.


E isto sem falar de todas as outras funcionalidades avançadas que acompanham a aplicação, que muito poucas ou nenhumas outras aplicações Wallet podem oferecer.


Entretanto, aqui estão todos os links sobre este fantástico Nó Relâmpago Bitcoin:



- [Blixt Official Webpage](https://blixtwallet.com/)
- [Blixt Github page](https://github.com/hsjoberg/blixt-Wallet/)
- [Página de caraterísticas do Blixt](https://blixtwallet.github.io/features) - explica uma a uma cada caraterística e funcionalidade.
- [Blixt FAQ page](https://blixtwallet.github.io/faq) - Lista de perguntas e respostas e resolução de problemas do Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - demonstrações, tutoriais em vídeo, guias adicionais e casos de utilização para o Blixt
- Descarregar: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK download direto](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Grupo de telegrama para apoio direto](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Geyser crowdfunding page](https://geyser.fund/project/blixt) - faça o donativo Sats que desejar para apoiar o projeto
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - chat anónimo LN
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - vídeo promocional (pode testar a sua 1ª utilização do LN)
- [Folheto A4 imprimível com os primeiros passos na utilização do Blixt, em várias línguas](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [O Blixt também oferece uma demonstração funcional completa](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) diretamente no seu sítio Web ou numa versão dedicada na Web, para testar a experiência completa antes de começar a utilizar no mundo real.


---
**AVISO LEGAL:**


*Não sou pago ou apoiado de forma alguma pelos criadores desta aplicação. Escrevi este guia porque vi que o interesse por esta aplicação Wallet está a aumentar e os novos utilizadores ainda não sabem como começar a utilizá-la. Também para ajudar o Hampus (o programador principal) com a documentação sobre a utilização deste nó Wallet.*


*Não tenho qualquer outro interesse em promover esta aplicação LN, para além de fazer avançar a adoção do Bitcoin e do LN. Esta é a única maneira!*


---