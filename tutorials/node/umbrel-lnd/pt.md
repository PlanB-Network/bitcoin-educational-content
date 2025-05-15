---
name: Guarda-chuva LND
description: Tutorial avançado sobre a instalação e configuração do Lightning Network Daemon (LND) na Umbrel
---
![cover](assets/cover.webp)




## Introdução



Este tutorial avançado leva-o passo a passo através da instalação, configuração e utilização da aplicação Lightning Node (LND) no seu nó Umbrel. Aprenderá a abrir canais, a gerir a sua liquidez e a sincronizar o seu nó com uma aplicação móvel.



## 1. Pré-requisito: nó Bitcoin Umbrel funcional



Antes de implantar o Lightning, é necessário ter um nó Bitcoin totalmente operacional na Umbrel. Isso envolve a instalação do Umbrel (no Raspberry Pi, NAS ou outra máquina) e a sincronização completa do Blockchain Bitcoin.



Para instalar o Umbrel e configurar o nó Bitcoin, recomendamos que siga o nosso tutorial dedicado :



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Certifique-se de que o seu nó Bitcoin está atualizado e a funcionar corretamente, uma vez que o Lightning Network depende dele para todas as transacções off-chain.



## 2. Introdução ao Lightning Network



O Lightning Network é um segundo protocolo Layer concebido para acelerar e reduzir o custo das transacções Bitcoin, realizando-as fora do Blockchain principal.



Em termos concretos, o Lightning utiliza uma rede de canais de pagamento entre nós: dois utilizadores abrem um canal bloqueando On-Chain BTC (transação inicial), podendo depois efetuar instantaneamente pagamentos Exchange dentro deste canal. Estas transacções off-chain não são registadas no Blockchain, daí a sua rapidez e custo praticamente nulo.



Os pagamentos podem ser encaminhados através de múltiplos canais (graças aos nós intermediários) para chegar a qualquer destinatário na rede, permitindo uma escala quase ilimitada de transacções instantâneas. O Lightning oferece, assim, transacções muito rápidas e de baixo custo, ideais para pagamentos diários ou microtransacções, ao mesmo tempo que alivia a carga do Blockchain Bitcoin.



Para funcionar, um nó Lightning deve estar permanentemente ligado à rede e interagir com outros nós Lightning. Existem várias implementações de software (LND, Core Lightning, Eclair, etc.), todas compatíveis entre si. A Umbrel usa o LND (Lightning Network Daemon) como parte de seu aplicativo oficial de Lightning Node. Este tutorial concentra-se no LND.



Para uma introdução teórica completa ao Lightning Network, recomendamos-lhe que frequente o nosso curso específico :



https://planb.network/courses/introduction-theorique-au-lightning-network-34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

Este curso dar-lhe-á uma base completa nos conceitos fundamentais do Lightning Network, antes de passar à prática com o seu nó LND.



## 3. Porquê auto-hospedar o LND?



Operar o seu próprio nó Lightning (LND) na Umbrel dá-lhe total soberania sobre os seus fundos e canais, em comparação com soluções de custódia ou semi-custódia.



### Comparação das soluções Lightning :



**Soluções de custódia (ex: Wallet de Satoshi)** :




- Os seus bitcoins Lightning são geridos por um terceiro de confiança
- Fácil de utilizar, sem complexidade técnica
- O operador detém os seus fundos e pode rastrear as suas transacções
- Sacrifica-se o controlo e a confidencialidade



**Carteiras de consumo sem produtos de base (por exemplo, Phoenix, Breez)** :




- Os utilizadores conservam as suas chaves privadas e, por conseguinte, Ownership das suas BTC
- Não há gestão completa dos nós - a aplicação gere os canais em segundo plano
- Compromisso entre simplicidade e soberania
- Dependência de infra-estruturas de fornecedores para obter liquidez
- Limitações técnicas (um smartphone não pode encaminhar pagamentos para outros)



**Nó LND auto-hospedado (Umbrel)** :




- Soberania máxima: os seus BTC On-Chain e off-chain estão inteiramente sob o seu controlo
- Não há terceiros envolvidos na abertura de canais ou na gestão dos seus pagamentos
- Maior confidencialidade (os seus canais e transacções só são conhecidos por si e pelos seus pares diretos)
- Liberdade de utilização: ligue-se aos seus próprios serviços e carteiras
- Possibilidade de encaminhar transacções por conta de outrem (remuneração por microtaxa)
- Responsabilidades técnicas acrescidas (manutenção, gestão da liquidez, cópias de segurança)



Em suma, a auto-hospedagem do LND dá-lhe o máximo controlo, mas requer mais competências técnicas. É um compromisso entre conveniência e soberania.



## 4. Tutorial passo-a-passo



### 4.1 Instalando e configurando o aplicativo Lightning Node na Umbrel



Quando o nó Umbrel (Bitcoin) tiver sido sincronizado, siga estes passos:



![Installation de Lightning Node depuis l'App Store Umbrel](assets/fr/01.webp)



Instale a aplicação Lightning Node a partir da secção "App Store" do Interface Umbrel.



![Avertissement sur la nature expérimentale de Lightning](assets/fr/02.webp)



O LND (Lightning Network Daemon) será implantado no teu Umbrel como uma aplicação. Quando a abrires pela primeira vez, verás uma mensagem de aviso a informar-te de que o Lightning é uma tecnologia experimental.



![Création ou restauration d'un nœud LND](assets/fr/03.webp)



Pode escolher entre criar um novo nó ou restaurar um a partir de uma cópia de segurança/seed. Para uma primeira instalação, escolha criar um novo nó. A aplicação Lightning Node irá generate uma frase de 24 palavras Mnemonic (o seu seed Lightning): escreva-a com muito cuidado (de preferência offline, em papel), pois será utilizada para restaurar os seus fundos Lightning, se necessário.



**Nota: Nas versões recentes do Umbrel, a instalação da aplicação Lightning fornece este seed de 24 palavras (o próprio nó Bitcoin do Umbrel não o faz).



![Interface principale de Lightning Node](assets/fr/04.webp)



Após a inicialização, você acessará o Interface principal do Lightning Node.



![Paramètres de l'application](assets/fr/05.webp)



Nas definições da aplicação, encontrará uma série de opções importantes:




   - Consulte o seu ID de nó (o identificador único do seu nó)
   - Ligação de um Wallet externo (Ligar Wallet)
   - Ver palavras secretas
   - Aceder às definições avançadas
   - Recuperar canais
   - Descarregar o ficheiro de cópia de segurança do canal
   - Ativar as cópias de segurança automáticas
   - Configurar o backup via Tor (Backup over Tor)



Essas opções são essenciais para a segurança e o gerenciamento do seu Lightning node. Certifique-se de ativar backups automáticos e manter suas palavras secretas seguras.



**Recursos úteis:**




- [Comunidade Umbrel](https://community.umbrel.com) - Fórum de discussão para os utilizadores partilharem problemas e soluções relativos à Umbrel e ao seu ecossistema


> - [Umbrel App Store - Lightning Node (LND)](https://apps.umbrel.com/app/lightning) - Descrição das funcionalidades da aplicação Lightning Node na Umbrel
> - [LND Docs - Quickstart](https://docs.lightning.engineering/lightning-network-tools/LND/run-LND) - Documentação oficial do LND

### 4.2 Abrir um canal Lightning



Quando o LND estiver a funcionar, pode abrir o seu primeiro canal Lightning. Para encontrar nós de qualidade aos quais se ligar:



![Page d'accueil Amboss.space](assets/fr/06.webp)



o [Amboss.space](https://amboss.space/) é um explorador para encontrar nós fiáveis para abrir canais.



![Exemple de nœud ACINQ sur Amboss](assets/fr/07.webp)



Por exemplo, o [nó ACINQ](https://amboss.space/node/03864ef025fde8fb587d989186ce6a4a186895ee44a926bfc370e2c366597a3f8f) é um nó reconhecido com excelentes estatísticas de disponibilidade e liquidez.



![Informations de connexion Swiss Bitcoin Pay](assets/fr/08.webp)



Para este tutorial, vamos abrir um canal com [Swiss Bitcoin Pay](https://amboss.space/node/03c181e13a09a649c13f60ea3ddbeefc66123c43280da8eebc19f54445f35173ca). A informação necessária para a ligação (pubkey@ip:port) é fornecida na sua página Amboss.



Para abrir o canal :



![Bouton d'ouverture de canal](assets/fr/09.webp)



Na página inicial do Lightning Node, clique no botão "+ OPEN CHANNEL



![Configuration du canal](assets/fr/10.webp)



Na página de configuração do canal :




   - Colar o ID do nó copiado do Amboss (formato: pubkey@ip:port)
   - Definir a quantidade de capacidade do canal (alguns nós, como o ACINQ, têm mínimos, por exemplo, 400k Sats)
   - Ajustar as taxas de abertura da transação, se necessário



![Canal en cours d'ouverture](assets/fr/11.webp)



Após o envio da transação, o canal aparecerá como "aberto" na página inicial. Aguarde a confirmação da transação On-Chain.



![Détails du canal](assets/fr/12.webp)



Clique no canal para ver os respectivos detalhes:




   - Situação atual
   - Capacidade total
   - Repartição da liquidez (entradas/saídas)
   - Chave pública do nó remoto
   - E outras informações técnicas



### Utilização do Lightning Network+ para obter liquidez de entrada



![Lightning Network+ dans l'App Store](assets/fr/13.webp)



O Lightning Network+ está disponível na Umbrel App Store para facilitar a obtenção de dinheiro.



![Interface principale de LN+](assets/fr/14.webp)



O Interface principal oferece três opções importantes:




- "Swaps de liquidez: explorar as ofertas de swaps disponíveis
- "Abrir para mim": filtrar os swaps para os quais é elegível
- "To Docs": aceder à documentação



![Message d'erreur LN+](assets/fr/15.webp)



Nota: Se ainda não tiver um canal aberto, verá esta mensagem de erro quando clicar em "Abrir para mim".



![Liste des swaps disponibles](assets/fr/16.webp)



A página "Swaps de liquidez" mostra todas as ofertas de swap disponíveis na rede.



![Swaps éligibles](assets/fr/17.webp)



"Abrir para mim" filtra apenas os swaps para os quais o seu nó cumpre as condições exigidas.



![Détails d'un swap](assets/fr/18.webp)



Exemplo de pormenores de swap :




- Configuração do Pentágono (5 participantes)
- Capacidade de 300k Sats por canal
- Pré-requisito: mínimo de 10 canais abertos com uma capacidade total de 1M Sats
- Lugares disponíveis: 4/5



### 4.3 Sincronização com uma aplicação móvel (Zeus)



Para controlar o seu nó Lightning à distância (smartphone), pode utilizar o Zeus (aplicação de código aberto disponível em iOS/Android).



**Configuração de Zeus com guarda-chuva :**



![Bouton "Connect Wallet" dans l'interface LND](assets/fr/19.webp)



Certifique-se de que o seu nó Umbrel está acessível (por defeito, via Tor).


No guarda-chuva do Interface, abra a aplicação Lightning Node e, em seguida, clique no botão "Connect Wallet" (Ligar Wallet), conforme indicado pela seta.



![Page de connexion avec QR code](assets/fr/20.webp)



Aparece um código QR que contém os seus dados de acesso ao LND em formato lndconnect. Este código QR é particularmente denso em informações, por isso não hesite em ampliá-lo para facilitar a leitura.



![Configuration initiale de Zeus](assets/fr/21.webp)



No seu telemóvel :




   - Abrir Zeus
   - Na página inicial, clique em "Configuração avançada" para ligar o seu próprio nó do Lightning
   - Nos parâmetros, selecionar "Criar ou ligar um Wallet"



![Configuration de la connexion LND dans Zeus](assets/fr/22.webp)



Em Zeus:




   - Selecionar "LND (REST)" como tipo de ligação
   - Pode digitalizar o código QR (método recomendado) ou introduzir as informações manualmente. (Não hesite em fazer zoom no código QR do guarda-chuva, pois é muito denso)
   - Importante: active a opção "Utilizar Tor" se o seu Umbrel só for acessível através do Tor (a predefinição)
   - Guardar configuração



O seu Zeus está agora ligado ao seu nó Umbrel e permite-lhe fazer pagamentos Lightning, ver os seus canais, saldos, etc., mantendo-se completamente auto-gerido.



**Opções de ligação avançadas:**



Por defeito, a ligação Zeus ↔ Umbrel é feita via Tor. Para uma ligação mais rápida, existem duas alternativas:



**Ligação do Nó de Raio (LNC)** :




   - Mecanismo de ligação encriptada da Lightning Labs
   - Instalar a aplicação Lightning Terminal no Umbrel (inclui acesso LNC)
   - generate um código QR de ligação no Lightning Terminal (Ligar → Ligar Zeus via LNC)
   - Digitalize-o para o Zeus (escolha "LNC" como tipo de ligação)



**VPN Tailscale**:




   - VPN de malha fácil de configurar
   - Instale o Tailscale no Umbrel (App Store) e no seu telemóvel
   - Ligar o Zeus através do IP privado Tailscale em vez do Tor Address



Estas opções não são obrigatórias e a solução Tor + Zeus funciona bem na maioria dos casos.



> **Recursos úteis:**
> - [Documentação Zeus - Ligação Umbrel](https://community.umbrel.com/t/zeus-LN-mobile/7619) - Guia oficial para ligar Zeus à Umbrel
> - [Zeus GitHub](https://github.com/ZeusLN/zeus) - Projeto de código aberto Zeus
> - [Comunidade Umbrel - Ligar Zeus através de Tailscale](https://community.umbrel.com/t/how-to-use-tailscale-with-umbrel/6782) - Guia para ligar Zeus a Umbrel utilizando Tailscale

## 5. Segurança e boas práticas



O gerenciamento de um nó do Lightning auto-hospedado requer atenção especial à segurança.



### Cópia de segurança e segurança para o seu nó



**Tipos essenciais de cópias de segurança



Seu nó Lightning Umbrel requer dois tipos de backups:



**A frase seed (24 palavras)**




- Recupera fundos do On-Chain
- Necessário para recriar o seu Wallet Lightning
- Para armazenamento ultra-seguro (offline, em papel)



*ficheiro *Static Channel Backup (SCB)**




- Contém informações sobre o canal Lightning
- Permite o encerramento forçado do canal em caso de colisão
- Importante:** Nunca salve o arquivo `channel.db` manualmente (risco de penalidades)



**Procedimento de cópia de segurança manual



Para guardar os seus canais manualmente :


1. Aceder ao menu Nó de relâmpago (três pontos "⋮" ao lado de "+ Abrir canal")


2. Descarregar o ficheiro de cópia de segurança do canal


3. Exportar um novo SCB após cada modificação de canal


4. Armazenar o SCB de forma segura (suporte encriptado, cópia fora do local)



*sistema de backup automático *Umbrel**



A Umbrel dispõe de um sofisticado sistema de backup automático que garante :



*Proteção de dados:*




- Encriptação do lado do cliente antes da transmissão
- Enviar através da rede Tor
- Dados complementados por preenchimento aleatório
- Chave de encriptação exclusiva para o seu dispositivo



*Segurança reforçada:*




- Cópias de segurança instantâneas em caso de alterações de estado
- Cópias de segurança "enganadoras" em intervalos aleatórios
- Ocultar alterações no tamanho do backup
- Proteção contra a análise do tempo



*Processo de restauro:*




- Identificador e chave derivados do seu seed Umbrel
- Restauro completo possível apenas com a frase Mnemonic
- Recuperação automática das últimas cópias de segurança
- Restaurar definições e dados do canal



### Restauração de colisões



Se o seu nó se perder (falha de hardware, cartão SD corrompido) :




- Reinstalar o guarda-chuva
- Introduza o seu seed de 24 palavras na aplicação Lightning
- Importar o ficheiro SCB durante o restauro



O LND contactará cada parceiro dos seus canais antigos para os encerrar e recuperar a sua parte dos fundos do On-Chain. Os canais serão encerrados de forma permanente (a reabrir, se necessário).



### Disponibilidade e proteção contra a fraude



Idealmente, deixe o seu nó em linha o mais frequentemente possível. Em caso de ausência prolongada:




- Um par malicioso pode tentar transmitir um estado de canal antigo
- O Lightning prevê um "período de protesto" (cerca de 2 semanas no caso do LND)
- Se vai estar ausente durante muito tempo, crie um Watchtower



**Configuração do Watchtower:**




- Nas definições avançadas do LND, adicione o URL de um servidor Watchtower fiável
- Pode utilizar um serviço público ou instalar o seu próprio Watchtower




Para saber mais sobre a configuração e utilização de torres de vigia, recomendamos que consulte o nosso tutorial dedicado:



https://planb.network/tutorials/node/lightning-network/watch-tower-26937006-dfe5-404e-9ee4-e82e422c5cf2
### Outras boas práticas





- Actualizações de software:** Manter o Umbrel e o LND actualizados (correcções de segurança)
- Proteção do hardware:** Utilizar um sistema estável (Raspberry Pi com SSD, mini-PC) e uma UPS
- Segurança da rede:** Manter a configuração predefinida do Tor, alterar a palavra-passe de administrador do Umbrel (predefinição: "moneyprintergobrrr")
- Encriptação:** Ativar a encriptação do disco, se possível



## 6. Ferramentas adicionais



A aplicação Lightning Node da Umbrel fornece os elementos essenciais para gerir os seus canais, mas as ferramentas de terceiros oferecem funcionalidades avançadas.



### ThunderHub



Interface moderno sistema de gestão de nós Lightning baseado na Web, instalável através da Umbrel App Store.



**Caraterísticas




- Visualização em tempo real dos canais (capacidades, saldos)
- Ferramentas de reequilíbrio integradas
- Suporte para faturação multipercurso (MPP)
- Geração de código QR LNURL
- Gestão de transacções On-Chain



O ThunderHub é ideal para monitorizar um nó de encaminhamento ativo e efetuar um reequilíbrio simples.



### Ride The Lightning (RTL)



O Interface é compatível com várias implementações Lightning (LND, Core Lightning, Eclair).



**Destaques




- Gestão de vários nós
- Painéis de controlo sensíveis ao contexto
- Suporte para trocas de submarinos (Lightning Loop)
- autenticação de 2 factores
- Exportar/importar cópias de segurança de canais



O RTL é um "canivete suíço" completo para administrar um nó do Lightning com uma abordagem mais orientada para especialistas.



### Outras ferramentas úteis





- Lightning Shell** : Linha de comando (lncli) via navegador
- BTC RPC Explorer & Mempool** : Monitorização do Blockchain
- LNmetrics & Torq**: Análise de desempenho de roteamento
- Amboss & 1ML**: gestão "social" do seu nó (pseudónimos, contactos, análise de rede)



Estas ferramentas podem ser instaladas com apenas alguns cliques através da Umbrel App Store, sem qualquer configuração complexa.



**Recursos adicionais da ferramenta:**




- [ThunderHub.io - Caraterísticas](https://thunderhub.io) - Visão geral das caraterísticas do ThunderHub
- [Ride The Lightning (RTL) info](https://www.ridethelightning.info/) - Documentação RTL
- [David Kaspar - Rebalance via ThunderHub](https://blog.davidkaspar.com) - Um guia prático para o rebalanceamento
- [Guia "Gerir nós do Lightning"](https://github.com/openoms/lightning-node-management) - Documentação avançada para utilizadores avançados



## Conclusão



Executar o seu próprio nó LND na Umbrel é um passo importante para a soberania financeira. Embora exija um maior envolvimento técnico do que uma solução de custódia, os benefícios em termos de controlo, confidencialidade e participação ativa no Lightning Network são consideráveis.



Ao seguir este guia, deverá ser capaz de instalar o LND, abrir canais, gerir a sua liquidez e aceder ao seu nó remotamente. Sinta-se à vontade para explorar gradualmente os recursos avançados e as ferramentas adicionais à medida que se familiariza com o ecossistema.



Lembre-se que a segurança dos seus fundos depende das suas salvaguardas e práticas. Dedique algum tempo a compreender todos os aspectos antes de comprometer somas avultadas.