---
name: Ride The Lightning (RTL)
description: Utilize o Ride The Lightning (RTL) para gerir o seu nó Lightning
---
![cover](assets/cover.webp)


## 1. Introdução



**Ride The Lightning (RTL)** é uma aplicação Web Interface completa para gerir um nó Lightning Network. Esta aplicação Web auto-hospedada oferece um **cockpit** Lightning acessível a partir do seu browser. A RTL funciona com todas as principais implementações Lightning (LND, Core Lightning/CLN e Eclair) e dá-lhe controlo total sobre o seu nó e canais. De código aberto (licença MIT) e gratuito, o RTL está integrado por defeito em muitas soluções de nós chave na mão (RaspiBlitz, MyNode, Umbrel, etc.).



**Sem um Interface gráfico, os nós Lightning só podem ser geridos através de comandos CLI de fácil utilização. A RTL simplifica estas operações com um Interface ergonómico. Aqui estão as principais aplicações:**





- Ver os canais e o nó - O painel de controlo apresenta o saldo do On-Chain, a liquidez do Lightning (local/remoto), o estado da sincronização, o alias do nó e muito mais. Pode ver a sua lista de canais, capacidade, distribuição local/remota e estado. A RTL oferece dashboards sensíveis ao contexto para analisar a atividade de diferentes ângulos.





- **Gestão de canais relâmpago** - Abrir/fechar canais com apenas alguns cliques. A RTL permite-lhe ligar-se a um par e abrir um canal sem um comando. Pode ajustar as taxas de encaminhamento, ver a pontuação do saldo ou iniciar um reequilíbrio circular para reequilibrar os fundos entre canais.





- **Acompanhar e efetuar pagamentos** - A RTL gere as transacções Lightning: enviar pagamentos através de facturas, facturas generate para receber, acompanhar transacções (pagamentos, encaminhamento) com histórico detalhado. O Interface também analisa o encaminhamento para ver que pagamentos estão a passar pelo seu nó.





- **Gestão e cópia de segurança do Wallet On-Chain** - O separador On-Chain permite-lhe gerir endereços generate e enviar transacções. A RTL facilita a salvaguarda de canais através da exportação do ficheiro SCB para o LND, com atualização automática para cada modificação de canal.



Em suma, a RTL é um **poderoso painel de controlo para o Lightning Network**, oferecendo um Interface educacional para pilotar o seu nó diariamente. Este tutorial irá guiá-lo através da sua instalação e utilização para gerir os seus canais e pagamentos.



## 2. Funcionamento técnico da RTL



![Schéma de l'architecture RTL : interface responsive compatible avec tous les appareils, frontend Angular, serveur Node (port 3000), connecté aux API REST de LND](assets/fr/01.webp)



Antes de entrar no âmago da questão, é útil entender brevemente **como o RTL interage com seu nó do Lightning** em um nível técnico.



**Arquitetura geral:** A RTL é uma aplicação Web construída com Node.js (backend) e Angular (frontend). Em termos concretos, a RTL é executada como um pequeno servidor Web local (na porta 3000 por defeito) que dialoga com a sua implementação Lightning através das suas API. Dependendo do tipo de :





- Com o **LND**, a RTL usa a API REST do LND (porta 8080) para executar comandos do Lightning. A conexão é protegida por TLS e requer o arquivo **admin macaroon** do LND para autenticação.





- Com o **Core Lightning (CLN)**, a RTL usa a API REST fornecida pelo *c-lightning-REST*, ou uma **access rune** através do plugin `commando`. Soluções como a Umbrel configuram automaticamente estes Elements.





- Com **Eclair**, a RTL liga-se à API REST Eclair utilizando a palavra-passe de autenticação configurada.



**Configuração e segurança:** A RTL é configurada através de um ficheiro JSON (`RTL-Config.json`) onde se define a porta web, a password de acesso e a informação de ligação ao seu nó. A web do Interface é protegida por um login/senha (senha padrão que pode ser alterada) e suporta 2FA. Por padrão, a RTL é executada como HTTP local (`http://localhost:3000`), mas para acesso remoto, use sempre uma conexão segura (HTTPS via proxy reverso, Tor ou VPN).



Em resumo, a RTL é um componente adicional que se conecta ao seu nó por meio de APIs seguras, requer tokens de acesso apropriados e oferece sua própria segurança Layer. Esta arquitetura modular permite-lhe mesmo gerir **vários nós Lightning com uma única instância RTL**.



## 3. Instalação RTL



Como a RTL é distribuída como software de código aberto, há várias maneiras de instalá-la em seu sistema. Nesta secção, cobriremos duas abordagens principais: instalação manual e instalação via Umbrel.



### Método manual



A instalação manual é adequada se pretender manter um controlo mais fino, ou se estiver a integrar RTL numa configuração personalizada. As etapas abaixo são para um nó LND executando Linux (por exemplo, Raspberry Pi ou VPS executando Ubuntu/Debian), mas são semelhantes para CLN/Eclair.



**Pré-requisito:** certificar-se de ter um nó **sincronizado** Bitcoin e um nó Lightning em funcionamento (LND, CLN ou Eclair) na máquina. O RTL não contém um nó Lightning em si, ele se conecta a um nó existente. Você também precisa do **Node.js** instalado (versão 14+ recomendada). Você pode verificar com `node -v` ou instalar o Node a partir do site oficial (https://nodejs.org/en/download/) ou do seu gerenciador de pacotes.



As principais fases de instalação são :



**Faça o download do código RTL**: Clone o repositório oficial do RTL no GitHub no diretório de sua escolha. Por exemplo:



```bash
git clone https://github.com/Ride-The-Lightning/RTL.git
cd RTL
```



**Instalar dependências**: A RTL é uma aplicação Node.js, por isso é necessário instalar os módulos necessários. Na pasta RTL, execute :



```bash
npm install --omit=dev --legacy-peer-deps
```



Este comando instala os pacotes NPM necessários (ignorando as dependências de desenvolvimento). A opção `--legacy-peer-deps` é recomendada para evitar possíveis conflitos de dependências do Node.



**RTL-Config**: Uma vez que as dependências estejam no lugar, prepare o arquivo de configuração. Copie/renomeie o arquivo `Sample-RTL-Config.json` na raiz do projeto para `RTL-Config.json`. Abra-o no seu arquivo :





- **Palavra-passe da interface do utilizador**: escolha uma palavra-passe segura e introduza-a em `multiPass` (em vez da predefinição `"password"`).
- **Porta**: padrão `3000`. Pode alterá-la se esta porta já estiver ocupada na sua máquina.
- **Nó**: na secção `nós[0]`, ajuste os parâmetros do seu nó:
     - `lnNode`: um nome descritivo para o seu nó (por exemplo, `"LND Node Maison"`).
     - lnImplementation`: `"LND"` (ou `"CLN"`/`"ECL"` consoante o caso).
     - Em `authentication`:
       - macaroonPath`: especificar o caminho completo para a pasta que contém o macaroon admin do LND.
       - `configPath`: caminho para o ficheiro de configuração do nó (`LND.conf` para o LND).
     - Em `configurações`:
       - `fiatConversion`: definido como `true` se pretender a conversão da moeda fiduciária.
       - `unannouncedChannels`: definido como `true` para ver os canais não anunciados.
       - themeColor` e `themeMode`: Personalização do Interface.
       - channelBackupPath`: caminho para as cópias de segurança do canal LND.
       - `lnServerUrl`: URL do seu nó Lightning (por exemplo, `https://127.0.0.1:8080`).



**Iniciar o servidor RTL**: Na pasta RTL, execute :



```bash
node rtl
```



A aplicação é iniciada e pode ser acedida em `http://localhost:3000`.



**(Opcional) Executar a RTL como um serviço**: Para inicialização automática, crie um arquivo systemd :



Para tal:




- Abra um terminal no seu computador.
- Crie um novo ficheiro de serviço com o seguinte comando (substitua `nano` pelo seu editor favorito):


```bash
sudo nano /etc/systemd/system/RTL.service
```




- Copie e cole o conteúdo abaixo neste ficheiro:



```ini
[Unit]
Description=Ride The Lightning web UI
Wants=lnd.service
After=lnd.service

[Service]
ExecStart=/usr/bin/node /chemin/vers/RTL/rtl
User=<votre_user>
Restart=always
TimeoutSec=120
RestartSec=30

[Install]
WantedBy=multi-user.target
```





- Substitua `/path/to/RTL/rtl` pelo caminho real para o arquivo `rtl` em sua máquina, e `<seu_usuário>` pelo seu nome de usuário Linux.
- Guardar e fechar o ficheiro.
- Recarregar a configuração do systemd:


```bash
sudo systemctl daemon-reload
```




- Ativar e iniciar o serviço RTL:


```bash
sudo systemctl enable RTL
sudo systemctl start RTL
```



A RTL arrancará automaticamente sempre que a máquina for reiniciada. Pode verificar o seu estado com :


```bash
sudo systemctl status RTL
```



### Instalação via Umbrel



Se utilizar [Umbrel] (https://getumbrel.com), a instalação RTL é muito mais simples:





- Aceder ao guarda-chuva Interface (normalmente através de `http://umbrel.local`)
- Aceder à **App Store**
- Procurar por "Ride The Lightning"



**Nota importante: existem duas aplicações RTL separadas na Umbrel App Store:**




- **Ride The Lightning** (para LND): para usar com o nó Lightning predefinido da Umbrel (LND).
- **Ride The Lightning (Core Lightning)**: utilizar apenas se tiver instalado a aplicação *Core Lightning* no Umbrel e pretender gerir este nó com RTL.



*Cada versão RTL é pré-configurada para dialogar com a implementação correspondente (LND ou Core Lightning). Se não tiver alterado o seu nó Lightning, basta escolher a versão clássica LND*



![Fiche de l'application Ride The Lightning dans Umbrel : présentation de l'app avec captures d'écran et bouton violet "Install" en haut à droite](assets/fr/02.webp)





- Clique em **Instalar**



![Fenêtre d'affichage du mot de passe par défaut après installation de RTL dans Umbrel, avec bouton "Open Ride The Lightning"](assets/fr/03.webp)



**Importante:** Após a instalação, a RTL apresenta um ecrã com a palavra-passe predefinida. **Copie e guarde esta palavra-passe** - vai precisar dela para iniciar a sessão no Interface RTL. Esta palavra-passe será apresentada sempre que a RTL for iniciada até que selecione a opção "Não voltar a mostrar".



A Umbrel trata automaticamente de :




- Descarregar e configurar RTL
- Configuração do acesso ao Lightning node
- Gerir actualizações
- Proteger o acesso ao Interface



Uma vez instalada, a aplicação aparece no menu *Apps* da Umbrel. Clica em **Ride The Lightning** para a iniciares.



![Écran de connexion RTL via Umbrel : champ de mot de passe avec logo du cheval en haut à gauche, bouton "Login"](assets/fr/04.webp)



No ecrã de início de sessão, introduza a palavra-passe que copiou anteriormente. Uma vez iniciada a sessão, a RTL Web Interface estará acessível diretamente a partir do painel de controlo da Umbrel, sem necessidade de qualquer configuração adicional!



## 4. Introdução e utilização do Interface RTL



Agora que a RTL está a funcionar, vamos explorar o Interface web e as suas principais caraterísticas. Iremos percorrer as diferentes secções da aplicação para lhe dar uma visão geral completa.



### O painel de controlo principal



![Tableau de bord RTL : solde Lightning, solde on-chain, capacité de liquidité entrante/sortante et création de facture](assets/fr/05.webp)



Assim que iniciar sessão, acede ao **painel de controlo principal**, que lhe dá uma visão geral do seu Lightning node. Esta página centraliza as informações essenciais:




- O seu saldo total do Lightning
- On-Chain saldo disponível
- A repartição da sua liquidez (entradas/saídas)
- Acesso rápido para enviar e receber Satss através do seu nó Lightning



### Gestão de fundos On-Chain



![Onglet "On-chain" actif dans RTL : solde Bitcoin (en sats, BTC, USD), et liste des transactions avec type d'adresse Taproot](assets/fr/06.webp)



O separador **On-Chain** permite-lhe gerir os seus bitcoins diretamente na cadeia principal:




- Visualização do saldo em diferentes unidades (Sats, BTC, USD)
- Lista completa de transacções
- Geração Address Taproot (P2TR), P2SH (NP2WKH) ou Bech32 (P2WKH)
- Gestão do UTXO, receção e envio de bitcoins



### Relâmpago: apresentação pormenorizada dos submenus



O Interface RTL apresenta um menu lateral dedicado ao Lightning Network, reunindo todas as funções essenciais para gerir o seu nó. Eis os pormenores de cada submenu, pela ordem da imagem de ecrã:



#### 1. Pares/Canais



![Vue de gestion des canaux Lightning (onglet "Peers/Channels" ouvert)](assets/fr/07.webp)



Este submenu permite-lhe :




- Veja a lista dos seus pares ligados e dos canais Lightning abertos ou em espera.
- Adicionar um novo par (conectar-se a outro nó do Lightning).
- Abrir, fechar ou gerir canais existentes.
- Ver detalhes de cada canal: capacidade, saldos locais/remotos, estado, histórico de transacções, pontuação do saldo, etc.



#### 2. Transacções



![Historique des transactions Lightning (onglet "Transactions" > "Payments")](assets/fr/08.webp)



Neste submenu, é possível :




- Enviar pagamentos relâmpago (via Invoice).
- generate e gerir facturas para receber pagamentos.
- Ver o historial completo dos pagamentos enviados e recebidos, com detalhes (montante, data, estado, encargos, número de saltos, etc.).



#### 3. Encaminhamento



Este submenu apresenta :




- Pagamentos encaminhados pelo seu nó para outros utilizadores do Lightning Network.
- Estatísticas de encaminhamento: número de transacções encaminhadas, taxas cobradas, erros encontrados.
- Histórico exportável para análise avançada.



#### 4. Diferimentos



Este submenu oferece :




- Relatórios detalhados sobre a atividade do seu Lightning node.
- Gráficos e quadros sobre canais, pagamentos, taxas, capacidade, etc.
- Ferramentas para compreender melhor o desempenho do seu nó.



#### 5. Pesquisa de gráficos



Este submenu permite-lhe :




- Explorar a topologia do Lightning Network.
- Procurar nós ou canais específicos.
- Obter informações sobre a conetividade e a capacidade global da rede.



#### 6. Assinar/Verificar



Este submenu oferece :




- A capacidade de assinar uma mensagem com a chave do seu nó (prova de Ownership).
- Verificação de assinaturas para autenticar mensagens de outros nós.



#### 7. Cópia de segurança



Este submenu é dedicado à cópia de segurança:




- Exportar ficheiro de cópia de segurança do canal (SCB para LND).
- Repor a configuração ou os canais, se necessário.
- Sugestões para proteger as suas cópias de segurança.



#### 8. Nó/Rede



![Vue d'ensemble du nœud Lightning (onglet "Node/Network")](assets/fr/09.webp)



Neste submenu, encontrará :




- Um resumo completo do status do seu nó do Lightning: alias, versão, cor, status de sincronização.
- Estatísticas sobre canais (activos, em espera, fechados), capacidade total, conetividade.
- Informações sobre o Lightning Network global e a posição do seu nó no mesmo.



### Serviços: Boltz Swaps



![Interface de gestion des swaps avec Boltz (onglet "Services" > "Boltz")](assets/fr/10.webp)



Boltz é um serviço Exchange sem custódia e que respeita a privacidade, que converte bitcoins entre o Lightning Network e o Blockchain Bitcoin (On-Chain). Oferece dois tipos de operação: Reverse Submarine Swap (**Swap Out**) e Submarine Swap (**Swap In**).



#### Swap Out (Troca Submarina Inversa)



Swap Out converte Satss disponíveis no Lightning Network em bitcoins On-Chain. Este mecanismo é útil quando um nó fica sem capacidade de entrada, ou quando se pretende recuperar fundos de um On-Chain Address. O processo funciona da seguinte forma:




- O utilizador seleciona um montante a ser trocado
- O nó envia um pagamento Lightning para Boltz
- Em Exchange, Boltz bloqueia um montante equivalente em bitcoins em On-Chain
- Assim que a transação for confirmada, o utilizador pode reclamar os fundos revelando um segredo utilizado na troca



Este processo não tem custódia, sendo que a Boltz nunca detém os fundos do utilizador.


![Double capture des étapes de configuration d'un swap-out](assets/fr/11.webp)



#### Swap In (Troca de Submarinos)



O Swap In, por outro lado, permite que os fundos do On-Chain sejam reinjectados no Lightning Network. Isto é particularmente útil para restaurar a capacidade de saída nos seus canais. O procedimento é o seguinte:




- O utilizador envia bitcoins para um Address específico gerado por Boltz
- Estes fundos só podem ser libertados por Boltz se este pagar um Lightning Invoice gerado pelo nó do utilizador
- Após o pagamento do Invoice, os fundos ficam disponíveis no canal Lightning, aumentando a capacidade de produção do nó



![Configuration d'un swap-in](assets/fr/12.webp)



Estes dois mecanismos permitem gerir eficazmente a liquidez do canal Lightning, mantendo a soberania do utilizador sobre os seus fundos.



### Configuração e personalização



![Écran de configuration du nœud (onglet "Node Config")](assets/fr/13.webp)



O separador **Node Config** permite-lhe personalizar a sua experiência:




- Ativação de canais não anunciados
- Personalizar o ecrã de venda
- Configuração do Block explorer
- Ajuste do Interface



### Documentação e ajuda



![Section d'aide de RTL (onglet "Help")](assets/fr/14.webp)



Por fim, a secção **Help** oferece documentação abrangente sobre o :




- Configuração inicial
- Gestão de pares e canais
- Pagamentos e transacções
- Cópias de segurança e restauros
- Relatórios e estatísticas
- Assinaturas e verificações
- Parâmetros do nó e da aplicação



Este Interface abrangente permite-lhe gerir o seu Lightning node de forma eficiente, desde operações básicas a funcionalidades avançadas, tudo num Interface intuitivo e bem organizado.



## 5. Casos de utilização avançados e segurança



Nesta seção, veja o que você precisa saber para ir além com RTL e proteger seu nó do Lightning:



### Monitorização e resolução de problemas



Para monitorizar o seu nó, pode exportar os dados RTL (logs, CSV) e visualizá-los em ferramentas como o Grafana. Em caso de problema (pagamento bloqueado, canal inativo), consulte os logs do LND/CLN e utilize os comandos de diagnóstico (`lncli listchannels`, `lncli pendingchannels`, etc.). A RTL também disponibiliza os logs do Interface para monitorizar os eventos de encaminhamento.



### Acesso remoto seguro



Nunca exponha a RTL diretamente na Internet. Dê preferência a :




- **VPN** (por exemplo, Tailscale) para acesso privado e encriptado
- **Tor** para um acesso seguro e anónimo
- Proxy inverso **HTTPS** (Nginx/Caddy) apenas se souber como o configurar



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Boas práticas de segurança





- **Proteja o seu acesso**: nunca partilhe admin.macaroon ou a sua palavra-passe RTL. Limite as permissões em ficheiros sensíveis.
- **Cópias de segurança regulares**: exportar o ficheiro de cópia de segurança do canal (SCB) após cada modificação e armazená-lo fora do nó.
- **Actualizações**: mantenha a RTL, o seu nó e a Umbrel actualizados com as últimas correcções de segurança.
- **Confidencialidade**: torne anónimos os registos e as capturas de ecrã antes de os partilhar. Nunca partilhe publicamente os seus saldos ou listas de pares.
- **Acesso único**: A RTL não é multi-utilizador. Não partilhe o acesso de administrador. Para acesso só de leitura, utilize um macaroon dedicado, se necessário.



Ao aplicar estes princípios, o utilizador limita consideravelmente os riscos e mantém o controlo sobre o seu Lightning node.



## 7. Conclusão



**Ride The Lightning** é uma ferramenta essencial para gerir eficazmente um nó Bitcoin/Lightning, quer seja um principiante ou um utilizador avançado. Fornece um Interface claro para controlar os seus canais, pagamentos e saúde do nó, enquanto aprofunda a sua compreensão do Lightning Network.



A RTL destaca-se pela sua compatibilidade com múltiplas implementações, pelas suas funções avançadas (reequilíbrio, trocas, relatórios) e pela sua abordagem pedagógica. Para necessidades simples, o Interface Umbrel ou um Wallet móvel serão suficientes, mas a RTL faz todo o sentido para uma gestão ativa e optimizada dos nós.



Para saber mais :




- Sítio Web oficial da RTL: https://www.ridethelightning.info/
- GitHub RTL: https://github.com/Ride-The-Lightning/RTL
- **Reddit r/lightningnetwork**: [r/lightningnetwork](https://www.reddit.com/r/lightningnetwork) - Discussões técnicas, anúncios de projectos, feedback e recursos educativos
- **Fórum da Comunidade Umbrel**: [community.getumbrel.com](https://community.getumbrel.com) - Fórum oficial com secção dedicada a Bitcoin/Lightning, guias e soluções para problemas comuns
- **Desenvolvedores do Lightning Network**: [github.com/lightning](https://github.com/lightning) - Repositório oficial do GitHub para acompanhar o desenvolvimento e contribuir com código-fonte
- **Pilha Exchange Bitcoin**: [Bitcoin.stackexchange.com](https://Bitcoin.stackexchange.com) - Perguntas e respostas técnicas com programadores e utilizadores avançados



Em suma, o RTL dá-lhe controlo total sobre o seu nó Lightning, num Interface moderno e com todas as funcionalidades.



**Fontes :** Sítio Web oficial da RTL; RTL GitHub; Umbrel App Store; Umbrel Community; Recursos da rede do Plano B.



Para aprofundar os seus conhecimentos sobre o funcionamento do Lightning Network, recomendo também que faça este curso gratuito:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb