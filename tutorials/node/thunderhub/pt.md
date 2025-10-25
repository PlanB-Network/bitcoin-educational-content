---
name: ThunderHub
description: Interface Web de gestão do nó do relâmpago LND
---
![cover](assets/cover.webp)



## Introdução



O ThunderHub é um **gerenciador de código aberto para nós Lightning (LND)**, oferecendo um Interface intuitivo e acessível a partir de qualquer dispositivo ou navegador.



**Principais caraterísticas**




- **Monitorização**: Visão global de saldos, canais, transacções, estatísticas de encaminhamento
- **Gestão**: Abrir/fechar canais, entrada/saída de pagamentos, equilíbrio de canais
- **Integrações**: Suporte LNURL, trocas via Boltz, backup Amboss
- **Interface responsivo**: Compatível com dispositivos móveis, tablets e computadores de secretária com temas escuros/claros



O ThunderHub integra-se facilmente com **Umbrel**, **Voltage**, **RaspiBlitz** e **MyNode**, simplificando a gestão diária do seu nó.



**O ThunderHub está particularmente adaptado aos operadores que procuram um Interface ergonómico para gerir os seus canais, controlar a liquidez (reequilíbrio), acompanhar as transacções e integrar serviços de terceiros, como o Amboss. A segurança é assegurada através de uma ligação local ou Tor.**



Se ainda não tens um nó Relâmpago, recomendamos que sigas o nosso tutorial LND Umbrel:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalação



O ThunderHub pode ser instalado de várias maneiras diferentes, dependendo do seu ambiente de hospedagem do Lightning node. Quer utilize uma solução chave-na-mão (Umbrel, Voltage, RaspiBlitz, MyNode, Start9, etc.) ou uma instalação manual, o ThunderHub está frequentemente disponível sem grande esforço. Abaixo, descrevemos duas abordagens comuns: através da Umbrel App Store e através da instalação manual (aplicável a um servidor ou a uma distribuição auto-hospedada).



### Instalação via Umbrel



O Umbrel integra o ThunderHub na sua **App Store**, tornando a instalação extremamente simples. Não há necessidade de uma linha de comando ou configuração manual: tudo é feito através do Interface Umbrel. Basta seguir estes passos:





- Abra o painel de controlo da Umbrel: Ligue-se ao Interface web do seu nó Umbrel (por exemplo, `http://umbrel.local` na sua rede local, ou através do seu `.onion` Address se estiver a utilizar o Tor).
- Aceder à **App Store**: No menu principal do Umbrel, clique em "App Store" (ou "App"). Procure **ThunderHub** na lista de aplicações disponíveis.



![Écran d'installation de ThunderHub via Umbrel](assets/fr/01.webp)





- **Instalar o ThunderHub**: Clique na aplicação ThunderHub e, em seguida, no botão de instalação. Confirme se necessário. O Umbrel descarregará e implementará automaticamente o ThunderHub no seu nó.





- **Iniciar a aplicação**: Quando a instalação estiver concluída (algumas dezenas de segundos), o ThunderHub aparece na sua página inicial. Clique no ícone para o abrir. O ThunderHub é iniciado no seu browser.



![Identifiants par défaut pour ThunderHub](assets/fr/02.webp)



**Importante:** Quando o ThunderHub é aberto pela primeira vez, apresenta automaticamente a **palavra-passe predefinida** necessária para iniciar sessão. A opção "Não voltar a mostrar isto" permite-lhe ocultar este ecrã para futuras ligações. **Aconselhamo-lo vivamente a:**




- Guarde esta palavra-passe imediatamente **no seu gestor de palavras-passe**
- **Copiar** para utilizar no passo seguinte
- Marque "Não voltar a mostrar isto" quando a palavra-passe tiver sido guardada



![Page de connexion de ThunderHub](assets/fr/03.webp)



Será então encaminhado para a página de início de sessão, onde deverá introduzir a palavra-passe que copiou no passo anterior para desbloquear o Interface.



![Interface de connexion complète à ThunderHub](assets/fr/04.webp)



A Umbrel encarrega-se de fornecer ao ThunderHub as informações de ligação LND (certificado TLS, macaroon de administração, etc.) em segundo plano, pelo que não precisa de efetuar qualquer configuração adicional. Com apenas alguns cliques, terá o ThunderHub instalado e a funcionar no seu nó Umbrel.



### Instalação manual (auto-hospedada, excluindo a Umbrel)



Para os utilizadores fora da Umbrel (por exemplo, num servidor pessoal, num Raspberry Pi com RaspiBlitz ou numa instalação *sózinha*), a instalação do ThunderHub requer alguns passos extra. Abaixo descrevemos a instalação a partir da fonte e a configuração, de acordo com a [documentação oficial do ThunderHub] (https://docs.thunderhub.io).



#### Instalação



**Pré-requisitos:** Certifique-se de que o seu sistema cumpre os requisitos mínimos de acordo com [documentation setup](https://docs.thunderhub.io/setup):




- **Node.js** versão 18 ou superior
- **npm** instalado
- Acesso aos ficheiros de autenticação do LND :
  - Certificado TLS LND (`tls.cert`)
  - Macaroon de administração LND (`admin.macaroon`)
  - LND serviço gRPC Address (nome do anfitrião:porta) (predefinição `127.0.0.1:10009` localmente)



**1. Recuperar o código ThunderHub:** Clonar o repositório GitHub do projeto, conforme descrito na [documentação de instalação] (https://docs.thunderhub.io/installation):



```bash
git clone https://github.com/apotdevin/thunderhub.git
cd thunderhub
```



**2. instalar as dependências e construir a aplicação**



```bash
npm install
npm run build
```



Estes comandos instalam todos os módulos necessários e depois compilam a aplicação (o ThunderHub é escrito em TypeScript/React).



**3. Atualizar mais tarde:** O ThunderHub oferece vários métodos para futuras actualizações:



```bash
# Méthode rapide
npm run update

# Ou méthode manuelle
git pull
npm install
npm run build
```



#### Configuração (Setup)



**1. Ficheiro de configuração principal:** Criar um ficheiro `.env.local` na raiz da pasta ThunderHub para personalizar a configuração (isto evitará que as suas definições sejam substituídas durante as actualizações). Variáveis principais de acordo com a [documentação de configuração](https://docs.thunderhub.io/setup):



```bash
# -----------
# Server Configs
# -----------
LOG_LEVEL='info' # 'error' | 'warn' | 'info' | 'http' | 'verbose' | 'debug' | 'silly'
PORT=3000
NODE_ENV=production

# -----------
# Interface Configs
# -----------
THEME='dark' # 'dark' | 'light' | 'night'
CURRENCY='sat' # 'sat' | 'btc' | 'fiat'

# -----------
# Privacy Configs
# -----------
FETCH_PRICES=true # Récupération des prix BTC/fiat depuis Blockchain.com
FETCH_FEES=true # Récupération des frais on-chain depuis Earn.com
DISABLE_LINKS=false # Liens vers 1ml.com et Blockchain.com
NO_VERSION_CHECK=false # Vérification de version depuis GitHub

# -----------
# TOR (optionnel)
# -----------
TOR_PROXY_SERVER='socks://127.0.0.1:9050' # Pour proxifier via TOR

# -----------
# Account Configs
# -----------
ACCOUNT_CONFIG_PATH='/chemin/vers/thubConfig.yaml' # Fichier de comptes
```



**2. Configuração das contas do servidor:** Criar o ficheiro YAML especificado em `ACCOUNT_CONFIG_PATH` :



```yaml
masterPassword: 'votre_mot_de_passe_principal'
accounts:
- name: 'Mon Nœud LND'
serverUrl: '127.0.0.1:10009'
macaroonPath: '/home/user/.lnd/data/chain/bitcoin/mainnet/admin.macaroon'
certificatePath: '/home/user/.lnd/tls.cert'
password: 'mot_de_passe_compte_specifique'
# Optionnel : compte avec macaroon en hexadécimal
- name: 'Nœud Distant'
serverUrl: 'ip.distante:10009'
macaroon: '0201056c6e6402f8...' # Macaroon en HEX ou Base64
certificate: '0202045c7365...' # Certificat en HEX ou Base64
```



**3. Acesso remoto:** Para se conectar a um nó remoto do LND, adicione ao `LND.conf` :



```bash
# Option 1 : accès par IP
tlsextraip=<ip-externe-accessible>
rpclisten=0.0.0.0:10009

# Option 2 : accès par domaine
tlsextradomain=<domaine-externe-accessible>
rpclisten=0.0.0.0:10009
```



**4. Segurança:** Na primeira inicialização, o ThunderHub **automaticamente** esconde a `masterPassword` e todas as senhas de contas no arquivo YAML, para evitar ter senhas em texto claro no servidor.



**5. Iniciar o ThunderHub:**



```bash
npm start
```



Por defeito, o servidor escuta na porta 3000. Aceder a `http://localhost:3000` (ou `http://ip-serveur:3000` a partir da rede local).



**6. Alternativa ao Docker:** O ThunderHub fornece imagens oficiais do Docker:



```bash
# Image standard
docker pull apotdevin/thunderhub:latest
docker run --rm -it -p 3000:3000/tcp apotdevin/thunderhub:latest

# Image avec base path /thub
docker pull apotdevin/thunderhub:base-v0.11.1
```



É apresentada a página de início de sessão do ThunderHub. Selecione a conta configurada e introduza a palavra-passe para aceder ao painel de controlo.



**Instalação noutras distribuições:** As distribuições de nós pré-embalados (RaspiBlitz, MyNode, Start9, etc.) geralmente oferecem suporte nativo ao ThunderHub através das suas respectivas interfaces de administração.



**Para mais informações:** Consultar a documentação oficial completa :




- **Instalação:** [docs.thunderhub.io/installation](https://docs.thunderhub.io/installation)
- **Configuração:** [docs.thunderhub.io/setup](https://docs.thunderhub.io/setup)



Estes recursos detalham opções avançadas, como contas SSO, macarons encriptados, configuração TOR e muito mais.



Quando o ThunderHub estiver instalado e acessível, está pronto para explorar todas as suas funcionalidades. Na secção seguinte, vamos analisar o ThunderHub Interface e os seus vários separadores, para o guiar na sua utilização.



## Apresentação da Interface



O Interface ThunderHub está estruturado em torno de um menu principal (normalmente apresentado na coluna do lado esquerdo) que inclui várias secções principais. Cada uma corresponde a um aspeto da gestão do seu nó Lightning. Vamos examiná-las uma a uma:





- **Página inicial** - Separador Página inicial com painel geral (visão geral do seu nó e acções rápidas).
- **Dashboard** - Dashboard personalizável com widgets e métricas avançadas.
- **Peers** - Gestão de pares de relâmpagos (ligações a outros nós).
- **Canais** - Gestão pormenorizada dos canais Lightning.
- **Reequilíbrio** - Ferramenta de equilíbrio de canais (pagamentos circulares).
- **Transacções** - Histórico de pagamentos relâmpago (transacções LN).
- **Forwards** - Estatísticas de encaminhamento (pagamentos retransmitidos pelo seu nó).
- **Cadeia** - Carteira On-Chain do Node (On-Chain BTC: UTXOs, transacções).
- **Amboss** - Integração com o Amboss (monitorização de nós, cópias de segurança, etc.).
- **Ferramentas** - Ferramentas diversas (cópias de segurança, mensagens assinadas, macarons, relatórios, etc.).
- **Troca** - Funções de troca On-Chain/Lightning através de Boltz.
- **Estatísticas** - Estatísticas avançadas e métricas de desempenho de nós.



*(Nota: Dependendo da versão do ThunderHub, algumas secções podem ter títulos ligeiramente diferentes ou funcionalidades adicionais, mas os princípios gerais permanecem os mesmos)*



### Página inicial (Painel de controlo geral)



O separador **Home** do ThunderHub é a página inicial que aparece depois de iniciar sessão. Ela contém o **Dashboard geral**, que oferece uma **visão geral** do status do seu nó do Lightning e sugere **ações rápidas** para operações de rotina. Aqui está o que você normalmente encontrará:



![Tableau de bord principal de ThunderHub](assets/fr/05.webp)





- **Saldos e capacidades:** Na parte superior da página, o ThunderHub apresenta os seus saldos disponíveis. Aqui, normalmente, verá o saldo On-Chain (Bitcoin On-Chain no Wallet do nó, simbolizado por um Anchor ⚓) e o saldo Lightning (as capacidades dos seus canais, simbolizadas por um relâmpago Bolt ⚡). Isto dá-lhe uma ideia imediata dos fundos que tem em On-Chain e Lightning. Se tiveres várias contas ou canais, certifica-te de que estás no canal certo (por exemplo, Mainnet vs. Testnet).





- **Estatísticas principais:** O painel de controlo pode mostrar algumas métricas globais do seu nó - por exemplo, o número de canais abertos, o número de pares ligados, as taxas de encaminhamento obtidas (se aplicável), etc. Trata-se de um resumo da atividade recente e da saúde do nó.





- **Acções rápidas:** O painel de controlo inclui botões para executar rapidamente as tarefas mais comuns, sem ter de navegar pelos menus. Estas acções rápidas incluem :





- **Fantasma**: Configurar um Lightning Address personalizado via Amboss.
- **Doar**: Fazer um donativo através do Lightning.
- Iniciar sessão/ir para: Ligue-se à sua conta Amboss (Quick Connect) e vá diretamente para **Amboss.space** para ver as informações do seu nó.
- **Address**: Introduzir um Lightning Address para efetuar um pagamento.
- **Abrir**: Abrir um novo canal Lightning. Clicar em abrir abre um formulário para inserir o URI do nó remoto para o qual abrir o canal, o valor e, se aplicável, a taxa máxima de On-Chain a ser usada.
- **Descodificar**: Descodificar um Lightning Invoice ou LNURL para ver os detalhes antes do pagamento.
- **LNURL**: Processar LNURLs para pagamentos ou levantamentos Lightning.
- **LnMarkets Login**: Entrar no LnMarkets para negociar.



Estas acções rápidas permitem-lhe realizar as operações mais frequentes diretamente a partir da página inicial, sem ter de navegar pelos vários separadores do Interface.



Em suma, o painel de controlo do ThunderHub dá-lhe uma **visão rápida** do seu nó e permite-lhe efetuar as operações mais frequentes (enviar/receber, abrir um canal) com um simples clique. É o ponto de partida ideal para a administração quotidiana.



### Painel de controlo



A secção **Dashboard** é separada do separador Página inicial e oferece um painel de instrumentos mais avançado e personalizável. Esta secção permite-lhe criar uma vista personalizada com widgets específicos de acordo com as suas necessidades enquanto operador de nós.





- **Widgets personalizáveis:** Ao contrário da página inicial, que tem um esquema fixo, o Dashboard permite-lhe escolher exatamente quais os Elements a apresentar e como os organizar.



![Dashboard sans widgets activés](assets/fr/06.webp)



Se nenhum widget estiver ativado, verá uma mensagem "Nenhum widget ativado!" com um botão "Definições" para aceder aos parâmetros de personalização.



![Paramètres des widgets du Dashboard](assets/fr/07.webp)



Nas definições, pode escolher entre uma vasta gama de widgets organizados em categorias: "Relâmpago - Informações", "Relâmpago - Tabela", "Relâmpago - Gráfico" e assim por diante. Cada widget pode ser ativado ou desativado individualmente com os botões "Mostrar/Ocultar".



![Bas de la page des paramètres](assets/fr/08.webp)



Na parte inferior das definições, encontrará o botão "To Dashboard" (Para o painel de controlo) para regressar ao painel de controlo e o botão "Reset Widgets" (Repor widgets) para repor a apresentação predefinida.



![Dashboard personnalisé avec widgets](assets/fr/09.webp)



Uma vez configurado, o seu painel de controlo pode apresentar vários gráficos e métricas: Gráficos de pagamentos relâmpago, número de facturas emitidas, estatísticas de adiantamentos, saldos detalhados, etc.





- **Métricas avançadas:** Aceda a estatísticas mais detalhadas sobre o desempenho do seu nó, com gráficos e dados em tempo real.





- **Visão geral configurável:** Adapte o visor para se adequar a um utilizador ocasional ou a um operador profissional que gere vários canais de encaminhamento.





- **Interface modular:** Adicione ou remova widgets conforme necessário: gráficos de avanço, métricas de liquidez, alertas de integridade do nó, etc.



Esta seção é particularmente útil para usuários avançados que desejam monitorar métricas específicas ou obter uma visão geral mais técnica de seu nó do Lightning. Ela complementa a seção Início, oferecendo maior flexibilidade e controle sobre como as informações são exibidas.



### Pares



A seção **Peers** lista todos os nós do Lightning atualmente conectados ao seu como peers. Um **peer** é uma conexão direta nó-a-nó no Lightning Network. Seu nó pode estar conectado a pares mesmo sem um canal aberto (por exemplo, apenas para informações de fofoca do Exchange na rede), ou é claro que todo canal aberto implica automaticamente em um par conectado.



![Vue de l'onglet Peers avec les pairs connectés](assets/fr/10.webp)



No separador Pares, verá :





- **Colunas de informação:** O Interface apresenta pormenores úteis, como o estado de sincronização, o tipo de ligação (clearnet ou Tor), o ping, os satoshis recebidos/enviados e o volume de dados trocados.
- Adicionar um peer: O ThunderHub permite-lhe ligar-se manualmente a um novo peer através do botão **"Add"** no canto superior direito. Terá de introduzir o URI do nó (formato `<public_key>@<socket>`). Uma vez validado, o ThunderHub envia o comando `lncli connect` correspondente. Se o nó estiver online e acessível, será adicionado à sua lista de pares.



### Canais



A guia **Canais** é o coração do gerenciamento de canais do Lightning. É provavelmente a seção que você consultará com mais frequência. Ela apresenta **todos os seus canais do Lightning** com seus detalhes e permite que você execute ações de gerenciamento nesses canais.



![Vue d'ensemble des channels ouverts](assets/fr/11.webp)



Eis o que encontra na página Canais:





- **Vista da lista de canais:** Cada canal aberto (ou a abrir/fechar) é listado, normalmente com o alias do nó remoto, a capacidade total do canal e uma barra colorida que ilustra a distribuição da liquidez local vs. remota. O ThunderHub utiliza um código de cor (frequentemente azul/Green) ou uma percentagem para indicar o equilíbrio do canal: por exemplo, azul para a sua quota local, Green para a quota remota. Se um canal estiver perfeitamente equilibrado (50/50), a barra terá metade de cada cor. Isto permite-lhe identificar rapidamente quais os canais que não estão equilibrados (tudo azul = quase tudo local, tudo Green = quase tudo remoto).





- **Colunas de informação:** O Interface apresenta colunas pormenorizadas, incluindo Estado, Acções disponíveis, Informações do par, ID do canal, Capacidade, Atividade, Taxas e Saldo com visualização gráfica da liquidez.





- **Configuração do ecrã:** Uma roda dentada no canto superior direito permite-lhe personalizar o ecrã do canal de acordo com as suas preferências.





- **Estado:** Também verá indicadores de estado - por exemplo, `Active` (o canal está aberto e operacional), `Offline` (o par está desligado, pelo que o canal está momentaneamente inutilizável), `Pending` (para aberturas ou encerramentos que aguardam confirmação do On-Chain).





- **Acções num canal:** Para cada canal, o ThunderHub fornece botões de ação (frequentemente sob a forma de ícones):



![Actions de gestion des canaux - Modifier et Fermer](assets/fr/12.webp)





- Editar taxas: O Interface "Atualizar política de canal" permite-lhe ajustar todos os parâmetros do canal: Taxa Base, Taxa de Taxa (em ppm), Delta CLTV, Max HTLC e Min HTLC. Isto permite-lhe ajustar as suas políticas de taxas individualmente por canal, com o objetivo de atrair (ou desencorajar) o tráfego de encaminhamento. *(Nota: o ThunderHub não substitui uma ferramenta de gestão automática de taxas, mas é muito eficaz para o ajuste manual)*
- Canal de fecho (*Close*): O "Canal de fecho" do Interface permite-lhe escolher entre um **fecho cooperativo** (predefinição) ou um **fecho forçado** (*Force Close*), definindo os encargos (em Sats/vByte). **Importante:** preferir sempre o fecho cooperativo quando possível, para evitar atrasos na liquidação do On-Chain e taxas mais elevadas. O ThunderHub dir-lhe-á se o par está online (cooperativo possível) ou não. Em caso de fecho forçado, não se esqueça de confirmar, pois é irreversível e desencadeará uma transação de varrimento com um bloqueio de tempo (geralmente 144 blocos ou ~1 dia em Bitcoin Mainnet).
- **Abrir um novo canal:** Para abrir um novo canal, clique na roda dentada no canto superior direito da página Canais e selecione "Abrir". Pode então iniciar um canal para um par novo ou existente. A vantagem de utilizar esta página é que tem uma lista dos canais existentes à sua frente, o que pode ajudá-lo a decidir onde abrir um novo canal.



Em suma, a secção Canais dá-lhe **controlo preciso sobre cada canal**. É aqui que conduz a alocação de liquidez, decide quais os canais a manter ou fechar, e define os seus parâmetros de encaminhamento por canal. O ThunderHub oferece um Interface claro para estas operações cruciais de gestão de nós.



### Reequilíbrio



O separador **Rebalance** é dedicado ao **balanceamento de canais**. O balanceamento (ou *rebalanceamento*) envolve reajustar a distribuição de fundos entre os seus canais de saída e de entrada, fazendo um **pagamento circular** de um dos seus canais para outro dos seus canais, através do Lightning Network. Isto permite-te, sem trazeres novos fundos, transferir liquidez de um canal que está demasiado cheio para um que está demasiado vazio, tornando os teus canais mais úteis (um canal equilibrado pode tanto enviar como receber pagamentos).



![Interface de rebalance des canaux](assets/fr/13.webp)



O ThunderHub facilita muito esta operação, que de outra forma seria tediosa na linha de comando. Eis como utilizar a secção Rebalance:





- **Vista inicial do canal:** Ao aceder ao Rebalance, o ThunderHub apresenta uma lista dos seus canais, com um indicador de equilíbrio para cada um (semelhante ao da página Canais). Pode ver imediatamente quais os canais que estão desequilibrados. O ThunderHub pode ordenar os canais por ordem crescente de equilíbrio, de modo a que os canais mais desequilibrados se destaquem no topo da lista (0,0 significa totalmente local ou remoto).





- **Seleção de pares:** O Interface facilita a seleção de pares de saída e de entrada para reequilíbrio.





- **Definições dos parâmetros:** Pode definir :
  - A taxa **máxima** (em Sats e ppm) que está disposto a pagar
  - O **montante a reequilibrar** com a opção "Fixo" ou "Objetivo
- Nós a **evitar** durante o encaminhamento
- **Tempo máximo de ensaio** para encontrar o itinerário





- Selecionar o canal **source**: Primeiro, selecione o canal de **saída (fonte)**, ou seja, o canal a partir do qual tem demasiada liquidez local para se deslocar. Na prática, este é um canal em que a sua quota local é elevada (> 50%). Imaginemos um canal A com 1.000.000 Satss, 900.000 dos quais são locais - um bom candidato para enviar Satss para outro local. Ao clicar neste canal A como "de saída", o ThunderHub marca-o como uma fonte.





- Selecionar **canal de destino**: De seguida, escolha o **canal de entrada (alvo)** que precisa de receber liquidez. Normalmente, este será um canal onde é o contrário - a maioria dos fundos está no lado mais distante (por exemplo, apenas 100.000 Satss locais em 1.000.000). O ThunderHub, depois de selecionado o canal de origem, ordenará os outros canais por ordem inversa (saldo decrescente) para ajudar a identificar os canais mais complementares. Selecione um canal B que tenha espaço no lado local. O ThunderHub apresentará então claramente quais os dois canais que foram selecionados (fonte A e alvo B).





- **Definir o montante da taxa e a tolerância:** Um formulário permite-lhe introduzir :





  - A **quantidade** a ser reequilibrada (em Sats). Muitas vezes, escolhemos uma quantidade igual ao que equilibraria ambos os canais em \~50/50. O ThunderHub pode preencher previamente metade do excesso de capacidade do canal de origem, por exemplo.
  - A **taxa máxima** que está disposto a pagar por esta operação (facultativo). Esta taxa é expressa em Sats (custo total do encaminhamento circular). Se deixar em branco, o ThunderHub irá procurar um caminho independentemente do custo, o que geralmente não é aconselhável (é melhor definir um limite, por exemplo, 10 Sats para um pequeno rebalanceamento, ou um máximo de ppm).





- **Find Route:** Clique no botão para encontrar uma rota. O ThunderHub consulta o LND para calcular uma rota do seu canal de origem através da rede para o seu próprio canal de destino. Se encontrar uma rota possível que satisfaça os seus critérios de taxa, apresenta-a com os detalhes dos saltos e o custo da taxa. Por exemplo, pode indicar que encontrou um caminho de 3 saltos com um total de 2 Sats em taxas.





- **Iniciar o rebalanceamento:** Se estiver satisfeito com a rota proposta, clique em **Balance Channel**. O ThunderHub irá então iniciar o pagamento circular via LND. Se o pagamento for bem sucedido, verá uma notificação de sucesso e os canais A e B terão os seus saldos modificados em tempo real. O ThunderHub actualizará o indicador de saldo para estes canais (idealmente, ficarão mais verdes do que antes, indicando um melhor saldo).





- **Ajustes e iterações:** Se não for encontrado um itinerário à primeira tentativa (ou se for demasiado caro), pode ajustar os parâmetros:





  - Experimente um montante mais pequeno (por vezes, um reequilíbrio parcial é bem sucedido, enquanto um montante elevado falha).
  - Aumente gradualmente a taxa máxima, mas tenha cuidado para não pagar mais em taxas do que vale a pena.
  - Utilize o botão **Obter outro itinerário**, se disponível, para tentar uma alternativa.
  - Tente outro par de canais se as coisas ficarem realmente complicadas.



O ThunderHub torna o processo muito **intuitivo e visual**. Em apenas 4 passos (selecionar canal de saída, selecionar canal de entrada, montante, validar), pode fazer o que antes exigia comandos manuais complexos. A ferramenta é inestimável para manter um nó bem equilibrado, melhorando o desempenho e a experiência do seu encaminhamento (mais fácil de enviar e receber pagamentos em todos os seus canais).



Por fim, note que um rebalanceamento consome custos de roteamento (pagos aos nós intermediários), portanto é um **investimento** para tornar seu nó mais fluido. Utilize-o de forma sensata, por exemplo, para suportar um canal para um serviço que utiliza frequentemente (liquidez de entrada) ou para equilibrar um grande canal de encaminhamento. O ThunderHub permite-lhe fazer isto de forma **simples e eficiente**.



### Transacções



A secção **Transactions** no ThunderHub corresponde ao histórico de transacções **Lightning** do seu nó, ou seja, pagamentos e facturas pagos ou recebidos através dos canais. É uma espécie de extrato de conta para as suas operações LN.



![Historique des transactions Lightning](assets/fr/14.webp)



Neste separador, encontrará :





- **Gráfico Invoice:** No canto superior direito, um gráfico mostra a evolução das facturas recebidas ao longo do tempo, permitindo-lhe visualizar a atividade do seu nó.





- Uma lista cronológica de todas as transacções Lightning feitas *de* ou *para* o seu nó. Cada entrada pode mostrar :





  - Tipo de operação: **pagamento enviado** (pagamento de saída) ou **pagamento recebido** (entrada, através de um Invoice pago).
  - O montante em Sats.
  - Data/hora.
  - Identificação do pagamento (Hash ou pré-imagem RHash) ou comentário (se tiver adicionado uma nota ao Invoice).
  - Estado: **concluído**, ou possivelmente **em curso**/*fracassado* (por exemplo, um pagamento a aguardar resolução, mas geralmente o LND processa-o rapidamente, pelo que há pouco "pendente" aqui em comparação com as transacções do On-Chain).



Em suma, a secção Transacções serve como o seu **registo de actividades LN**. É muito útil para verificar se um pagamento foi efectuado, quantas taxas custou, ou traçar o histórico das suas trocas Lightning. Em conjunto com a secção Forwards (descrita a seguir), terá uma visão completa do dinheiro que passou pelo seu nó.



### Avançados



O separador **Forwards** é dedicado à atividade de **encaminhamento** do seu nó, ou seja, aos pagamentos que **transitam** através dos seus canais (quando actua como nó intermediário no Lightning Network). Se operar o seu nó como um nó de encaminhamento, esta é uma secção importante para acompanhar o seu desempenho.



![Statistiques de routage Lightning](assets/fr/15.webp)



Em Forwards, o ThunderHub apresenta :





- **Filtros e opções de visualização:** No canto superior direito, os filtros permitem-lhe ordenar os dados por dia/semana/mês/ano e escolher entre visualização gráfica ou tabular.





- **Mensagem de atividade:** Se não tiver sido efectuado qualquer encaminhamento durante o período selecionado, o Interface apresenta "No forwards for this period" (Sem encaminhamentos para este período), conforme ilustrado neste exemplo.





- Uma **tabela de reencaminhamentos recentes**: cada entrada corresponde a um pagamento que foi **reencaminhado** através do seu nó. Para cada envio, geralmente vemos :





  - Timestamp,
  - a quantidade encaminhada (em Sats),
  - a **taxa ganha** neste reencaminhamento (no Sats, é a diferença entre o que recebeu no canal de entrada e o que enviou no canal de saída),
  - os canais de entrada e de saída utilizados (frequentemente identificados pelo pseudónimo do par ou pelo ID do canal).
  - estado (normalmente *concluído*, ou falha se um reencaminhamento falhou no percurso).





- **Estatísticas agregadas**: O ThunderHub calcula e apresenta no topo da página os totais e as estatísticas durante um determinado período (por exemplo, últimas 24 horas, ou 7 dias, etc., por vezes configurável).



Em resumo, a seção Encaminhamentos oferece uma **visão geral em tempo real da atividade de roteamento do seu nó do Lightning**. Juntamente com as secções Canais e Reequilíbrio, isto forma um pacote completo para otimizar o seu nó: Canais/Rebalanceamento para liquidez, Encaminhamentos para observar os resultados (fluxos e lucros).



### Cadeia



A secção **Chain** corresponde à gestão da carteira Bitcoin On-Chain do seu nó LND. Este Interface permite-lhe visualizar e gerir os fundos do Bitcoin, que são utilizados para abrir canais ou receber fundos de canais fechados.



![Gestion du portefeuille on-chain](assets/fr/16.webp)



Em Chain, encontrará :





- Saldo On-Chain: **Apresenta o saldo total de BTC disponível em Wallet LND.**





- **Lista de UTXOs:** Ver todas as saídas não gastas (UTXO) com montante, confirmações, Address e formato para cada saída.





- **Histórico de transacções:** Quadro pormenorizado de todas as transacções Bitcoin com tipo (entrada/saída), data, montante, encargos, confirmações, bloco de inclusão, endereços e txid.



### Amboss



O ThunderHub integra-se na plataforma **Amboss** (amboss.space), que oferece informações detalhadas sobre os nós Lightning, um mercado de liquidez e funcionalidades úteis, como a cópia de segurança encriptada do canal e a monitorização da disponibilidade.



![Intégration Amboss avec ses options](assets/fr/17.webp)



No ThunderHub, a secção Amboss permite-lhe **ligar** o seu nó à sua conta Amboss:





- **Ghost Address:** Configura um **Lightning Address** personalizado para o teu nó, facilitando a entrada de pagamentos.





- Cópias de segurança automáticas de canais:** Funcionalidade principal para cópias de segurança encriptadas de canais** (ficheiros SCB) no Amboss. Active **Amboss Auto Backup = Sim** nas definições para enviar automaticamente actualizações de cópias de segurança encriptadas sempre que mudar de canal. Em caso de falha, poderá recuperar os seus fundos graças a esta cópia de segurança externa.





- Verificações de saúde: **Active Amboss Healthcheck = Yes** para que o seu nó envie pings regulares para o Amboss. Receberá alertas se o seu nó parecer estar offline.





- Outras caraterísticas: envio automático de saldos, integração **Magma/Hydro** (mercado de liquidez) e acesso a estatísticas de desempenho detalhadas.



A integração do Amboss acrescenta uma **segurança Layer** essencial com cópia de segurança externa automática e monitorização da disponibilidade, acessível diretamente a partir do ThunderHub.



### Ferramentas



A secção **Tools** agrupa várias ferramentas avançadas para gerir o seu nó. Aqui estão as principais Elements:



![Interface des outils disponibles](assets/fr/18.webp)





- **Cópias de segurança:** Gerir manualmente as cópias de segurança dos seus canais (SCB). O ThunderHub permite-lhe **descarregar o ficheiro de backup completo** dos seus canais (opção "Backup de todos os canais -> Download"). Guarde este ficheiro `channel-all.bak` num local seguro - é essencial para recuperar os seus fundos no caso de uma falha. Pode também **importar** um ficheiro de backup quando redistribuir um nó.





- **Contabilidade:** Ferramenta de exportação para relatórios financeiros, incluindo honorários ganhos/pagos e volumes encaminhados durante um determinado período.
- **Mensagens assinadas:** Assinar ou verificar mensagens com o seu nó para provar o Ownership do seu nó Lightning através de assinatura criptográfica.
- Macarons (secção Padaria):** Gerir os macarons LND** para criar acessos personalizados. O Interface "Bakery" permite-lhe selecionar com precisão cada permissão: "Adicionar ou remover pares", "Criar endereços em cadeia", "Criar facturas", "Criar macarrões", "Derivar chaves", "Obter chaves de acesso", "Obter transacções em cadeia", "Obter facturas", "Obter informações Wallet", "Obter pagamentos", "Obter pares", "Pagar facturas", "Revogar IDs de acesso", "Enviar para endereços em cadeia", "Assinar bytes", "Assinar mensagens", "Parar daemon", "Verificar assinatura de bytes", "Verificar mensagens", etc. Cada permissão pode ser activada individualmente com os botões "Sim/Não" para criar um macaroon personalizado.
- **Informações sobre o sistema:** Visualização da versão do Wallet e dos RPCs activados.



Em suma, a secção Ferramentas reúne funções de administração avançadas - cópias de segurança, contabilidade, segurança e gestão de acesso - num Interface unificado.



### Troca



O separador **Swap** do ThunderHub permite-lhe trocar satoshis Lightning para Bitcoin On-Chain através do serviço Boltz. Este recurso é útil para "despejar" o excesso de liquidez do Lightning no canal sem fechar um canal.



![Interface de swap via Boltz](assets/fr/19.webp)



O processo é simples:





- **Montante**: Definir o montante a ser trocado
- **Address**: Introduzir a receção Bitcoin Address
- **Execução**: O ThunderHub comunica com o Boltz para processar automaticamente o Exchange



**Benefícios**




- Serviço sem custódia (sem custódia de dinheiro)
- Preservar os canais existentes
- Interface integrado fácil de utilizar



A Boltz cobra uma pequena comissão e você paga a taxa de transação normal do Bitcoin. O ThunderHub apresenta todos os custos antes da confirmação.



### Estatísticas



A seção **Estatísticas** do ThunderHub oferece **estatísticas avançadas** no nó do Lightning para analisar o desempenho e otimizar o roteamento.



![Statistiques du nœud via Amboss](assets/fr/20.webp)



Esta secção é essencial para otimizar os seus custos, identificar canais de sucesso e planear a expansão do seu nó.



## Conclusão



**O ThunderHub** estabeleceu-se como a ferramenta essencial para uma fácil administração de um nó Lightning **LND**. Este moderno Interface oferece todas as funções essenciais: gestão de canais, pagamentos, monitorização, com funcionalidades avançadas como o reequilíbrio automático e a integração Amboss.



**Principais benefícios**




- Interface elegante e intuitivo
- Ferramentas poderosas (reequilíbrio, swaps Boltz, cópias de segurança automáticas)
- Compatível com Umbrel, Voltage, RaspiBlitz e outras distribuições



O ThunderHub democratiza o gerenciamento avançado de nós do Lightning, tornando acessível o que antes exigia comandos técnicos complexos. Quer seja um principiante ou um operador experiente, o ThunderHub permite-lhe gerir eficientemente o seu Lightning node através de um Interface moderno e abrangente.



## Recursos



**Ligações oficiais:**




- **Sítio Web oficial:** [thunderhub.io](https://thunderhub.io)
- **Documentação:** [docs.thunderhub.io](https://docs.thunderhub.io)
- **Código-fonte do GitHub:** [github.com/apotdevin/thunderhub](https://github.com/apotdevin/thunderhub)