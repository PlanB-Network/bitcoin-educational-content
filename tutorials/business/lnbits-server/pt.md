---
name: Servidor LNbits
description: Instalação e configuração de um servidor LNbits auto-hospedado no Ubuntu VPS com PHOENIXD ou no Umbrel
---

![cover](assets/cover.webp)



O LNbits é uma aplicação web Interface de código aberto que transforma qualquer backend Lightning (LND, Core Lightning, PHOENIXD) numa plataforma de serviços completa. Esta solução auto-hospedada permite-lhe gerir várias carteiras Lightning isoladamente, implementar pontos de venda, criar sistemas de donativos ou serviços de faturação, mantendo um controlo total sobre os seus fundos.



Este tutorial abrange duas abordagens de instalação: **VPS Ubuntu com PHOENIXD** (solução leve sem um nó Bitcoin completo) e **Umbrel** (integração com seu nó LND existente). Ao contrário do tutorial geral do LNbits da Plan B Network, que cobre conceitos e extensões, este guia concentra-se em procedimentos técnicos de instalação passo a passo.



## O que é o LNbits?



LNbits é um sistema de contabilidade Lightning desenvolvido em Python (FastAPI) que se conecta a um backend existente (LND, Core Lightning, PHOENIXD). Ao contrário dos nós Lightning tradicionais, o LNbits oferece um Interface acessível, permitindo-lhe gerir várias carteiras isoladas com as suas próprias chaves API. Pode criar subcontas para a sua família, empregados ou projectos, sem lhes dar acesso a todos os seus fundos.



A arquitetura dissociada armazena as informações em SQLite (predefinição) ou PostgreSQL (produção), enquanto os fundos continuam a ser geridos pelo seu backend Lightning. Esta separação garante a portabilidade: pode migrar do PHOENIXD para o LND sem perder os dados dos seus utilizadores.



## Caraterísticas principais



O LNbits oferece um sistema versátil de **extensões**: TPoS (ponto de venda), Paywall (monetização de conteúdos), Eventos (emissão de bilhetes), LndHub (servidor para BlueWallet), Bolt Cards (pagamentos NFC), Split Payments (distribuição automática) e User Manager (gestão de utilizadores com autenticação).



O **dashboard** apresenta os saldos em tempo real, o histórico das transacções e as ferramentas de faturação. Cada Wallet tem um URL único que contém as suas chaves API, permitindo o acesso sem um login tradicional. O sistema de chaves API de três níveis** (admin, Invoice, só leitura) oferece um controlo granular das permissões para integrações seguras.



O LNbits implementa nativamente **LNURL** (LNURL-pay, LNURL-Withdraw, LNURL-auth) e suporta **Lightning Address**, garantindo compatibilidade com carteiras Lightning modernas e facilitando a implantação de serviços profissionais.



## Plataformas suportadas



**Ubuntu VPS**: Solução leve sem nó Bitcoin completo. Pré-requisitos: 1 vCPU, 1-2 GB de RAM, Ubuntu 22.04 LTS, Python 3.10+, Git, UV. HTTPS + nome de domínio necessário para exposição pública (serviços LNURL).



**Umbrel**: Instalação fácil a partir da App Store. Pré-requisito: nó Umbrel funcional com LND sincronizado e canais abertos. Configuração automática.



Abaixo estão as ligações para os nossos tutoriais Umbrel e Umbrel LND:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

https://planb.academy/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Instalando no Ubuntu VPS com PHOENIXD



### Passo 1: Proteger o servidor VPS



**Antes de qualquer instalação**, é necessário proteger o seu servidor VPS Ubuntu de acordo com as regras da arte. Este passo é **crítico** para proteger a sua infraestrutura e os seus fundos Lightning.



Aqui está um guia detalhado para o ajudar a começar: **[Initial Ubuntu server configuration - Step-by-step guide](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/)** por Daniel P. Costas.



Este guia abrange a configuração do utilizador, SSH seguro, firewall (UFW), fail2ban, actualizações automáticas e boas práticas de segurança do sistema.



### Passo 2: Instalação do PHOENIXD



Quando o seu servidor estiver seguro, precisa de instalar e configurar o PHOENIXD. A Plan B Network oferece um tutorial dedicado completo que cobre a instalação, a geração do seed e a configuração do serviço systemd:



https://planb.academy/tutorials/node/lightning-network/phoenixd-beb86edd-f9c0-4bec-ad36-db234c88e7b1

Quando o PHOENIXD estiver funcionando (verifique com `./Phoenix-CLI getinfo`), anote a **senha HTTP** em `~/.Phoenix/Phoenix.conf` - você precisará dela para conectar o LNbits ao PHOENIXD.



### Implantação de LNbits



Instalar o UV e clonar o LNbits :


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
git clone https://github.com/lnbits/lnbits.git && cd lnbits
uv sync --all-extras
```



Configurar o backend do PHOENIXD:


```bash
cp .env.example .env && nano .env
```



Adicionar a `.env` :


```
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://127.0.0.1:9740
PHOENIXD_API_PASSWORD=<mot-de-passe-phoenix.conf>
```



Teste com `uv run lnbits --host 0.0.0.0 --port 5000` e crie um serviço systemd com `Wants=PHOENIXD.service`.



## Configuração inicial e primeira utilização



### Ativação do SuperUtilizador



Ativar o administrador do Interface em `.env` :


```
LNBITS_ADMIN_UI=true
```



Reinicie o LNbits (`sudo systemctl restart lnbits`) e recupere o ID do SuperUsuário:


```bash
cat ~/lnbits/data/.super_user
```



Aceda a `http://<IP-VPS>:5000/Wallet?usr=<SuperUserID>` para aceder ao painel de administração. O menu "Servidor" permite-lhe configurar fontes de financiamento, extensões e contas de utilizador.



### Criação de conta segura



**Importante para exposição pública**: Se estiver a expor a sua instância LNbits num nome de domínio público acessível a partir da Internet, é **crítico** desativar a criação livre de contas de utilizador.



A partir do Interface de administração do SuperUser, vá para "Definições" e depois para a secção "Gestão de utilizadores". Encontrará a opção "Permitir a criação de novos utilizadores".



![Gestion des utilisateurs - Sécurité](assets/fr/17.webp)



**Para uma exposição pública com nome de domínio** :




- Deve desativar** a opção "Permitir a criação de novos utilizadores
- Sem esta proteção, qualquer pessoa na Internet pode criar uma conta na sua instância
- Um atacante pode criar contas e utilizar a liquidez do seu LIGHTNING NODE sem o seu conhecimento
- Terá de criar contas de utilizador manualmente a partir do Interface SuperUser



**Apenas para uso local** :




- Esta opção é menos crítica se a sua instância só for acessível localmente (http://localhost:5000)
- No entanto, desativar esta opção é uma boa prática de segurança geral



Uma vez configurado, apenas o administrador SuperUser pode criar novas contas de utilizador através do Interface "Utilizadores". Esta abordagem garante um controlo total sobre quem pode aceder à sua infraestrutura Lightning e utilizar os seus fundos.



### Abrir o primeiro canal



O PHOENIXD gere automaticamente os canais através da auto-liquidez. generate um Lightning Invoice de ~30,000 Sats da LNbits e paga-o a partir de outro Wallet. O PHOENIXD abre automaticamente um canal para a ACINQ. A taxa de abertura (~20-23k Sats) é deduzida, o saldo restante (~7-10k Sats) aparece após a confirmação do On-Chain.



Verifique o status com `./Phoenix-CLI getinfo`. Em seguida, considere a possibilidade de desativar a auto-liquidez (`auto-liquidity=off` em `Phoenix.conf`) para controlar a abertura de canais.



### Apresentação pública e HTTPS



**Importante**: HTTPS obrigatório para exibição pública (segurança da chave API + compatibilidade LNURL). Ignorar este passo apenas para utilização local.



**Caddy (recomendado)**: SSL automático. `sudo apt install -y caddy`, editar `/etc/caddy/Caddyfile` :


```
votre-domaine.com {
reverse_proxy 127.0.0.1:5000
}
```


Reiniciar: `sudo systemctl restart caddy`.



**Nginx** : Mais controlo. Instalar `nginx certbot python3-certbot-nginx`, criar `/etc/nginx/sites-available/lnbits` :


```nginx
server {
listen 80;
server_name votre-domaine.com;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Forwarded-Proto $scheme;
}
}
```


Ativar: `sudo LN -s /etc/nginx/sites-available/lnbits /etc/nginx/sites-enabled/ && sudo nginx -t && sudo systemctl reload nginx && sudo certbot --nginx -d your-domain.com`



Adicionar ao `.env`: `FORWARDED_ALLOW_IPS=*`



## Instalação do guarda-chuva



### Implementação a partir da App Store



Aceda à Umbrel App Store, procure "LNbits" e clique em "Instalar".



![Installation LNbits Umbrel](assets/fr/01.webp)



O Umbrel verifica automaticamente as dependências necessárias. O LNbits requer o LIGHTNING NODE (LND) para funcionar. Se o seu LIGHTNING NODE já estiver operacional, clique em "Install LNbits" para confirmar.



![Dépendances LNbits](assets/fr/02.webp)



O Umbrel descarrega a imagem Docker, configura automaticamente as ligações com o LND e inicia o contentor (2-5 minutos). A instalação ocorre inteiramente em segundo plano.



### Configuração inicial do SuperUsuário



No primeiro lançamento, o LNbits solicita que você crie a conta de administrador SuperUser. Digite um nome de usuário e defina uma senha segura para proteger o acesso ao sistema de administração do Interface.



![Configuration SuperUser](assets/fr/03.webp)



**Importante**: Esta conta de SuperUsuário tem privilégios totais na sua instância do LNbits. Escolha uma senha forte e mantenha-a segura.



Depois de criar uma conta, é automaticamente encaminhado para a área de administração principal do Interface. A Umbrel já definiu o LND como a sua fonte de financiamento - todos os pagamentos Lightning passarão pelos seus canais existentes.



### Acesso ao administrador do Interface



No menu do lado esquerdo, clique em "Definições" para aceder a todo o painel de administração.



![Interface Settings](assets/fr/04.webp)



A secção "Gestão de carteiras" apresenta informações importantes sobre a sua configuração:




- Fonte de Financiamento** : LndBtcRestWallet (ligação direta ao seu nó LND Umbrel)
- Saldo do nó** : Liquidez total disponível nos seus canais Lightning
- Saldo LNbits**: Fundos afectados ao sistema LNbits (inicialmente 0 Sats)



Agora você pode explorar diretamente a liquidez do seu nó Umbrel para todas as carteiras LNbits que você criar. Nenhuma configuração adicional é necessária - o LNbits está pronto e funcionando.



### Gestão de utilizadores



Uma das caraterísticas mais poderosas do LNbits é a sua capacidade de criar vários utilizadores independentes, cada um com autenticação por palavra-passe e carteiras isoladas. Esta arquitetura permite tirar partido da liquidez do seu nó Umbrel, oferecendo ao mesmo tempo sub-contas totalmente isoladas para diferentes utilizações: empresa, família, empregados, projectos, etc.



No menu lateral, clique em "Utilizadores" para aceder à gestão dos utilizadores. Clique em "CRIAR CONTA" para adicionar um novo utilizador.



![Gestion des utilisateurs](assets/fr/05.webp)



Preencher o formulário de criação de utilizador:




- Nome de utilizador**: Nome de utilizador de início de sessão (exemplo: "Satoshi")
- Definir palavra-passe**: Ativar esta opção para definir uma palavra-passe de autenticação
- Password** e **Password repeat**: Definir a palavra-passe para este utilizador



![Création utilisateur satoshi](assets/fr/06.webp)



Os campos opcionais (chave pública Nostr, e-mail, nome e apelido) podem ser deixados em branco para uma configuração mínima. Clique em "CREATE ACCOUNT" (Criar conta) para confirmar.



![Confirmation utilisateur créé](assets/fr/07.webp)



O novo utilizador aparece agora na lista de utilizadores com o seu identificador único e nome de utilizador.



![Liste des utilisateurs](assets/fr/08.webp)



**Ponto importante**: Cada utilizador pode iniciar sessão de forma completamente independente com a sua própria palavra-passe. O administrador do SuperUser mantém o controlo total através da ferramenta de administração do Interface.



### Gestão do utilizador Wallet



Agora que o utilizador "Satoshi" foi criado, é necessário atribuir-lhe um Raio Wallet. Clique no ícone Wallet (segundo ícone) do utilizador em questão e depois em "CREATE NEW Wallet".



![Gestion des wallets](assets/fr/09.webp)



Uma caixa de diálogo pede-lhe para dar um nome ao Wallet. Introduza um nome descritivo (por exemplo, "Wallet Of Satoshi") e selecione a moeda de apresentação (CUC, USD, EUR, etc.).



![Création wallet](assets/fr/10.webp)



Clique em "CREATE". O LNbits gera instantaneamente um Wallet Lightning funcional para este usuário.



![Confirmation wallet créé](assets/fr/11.webp)



Agora vê as duas carteiras existentes: a Wallet padrão "LNbits Wallet" criada automaticamente, e a nova "Wallet Of Satoshi". Para simplificar a experiência do utilizador, pode eliminar o Wallet predefinido clicando no ícone de eliminação (caixote do lixo vermelho).



![Wallet final unique](assets/fr/12.webp)



O utilizador "Satoshi" tem agora um único Wallet claramente identificado. Cada utilizador Wallet funciona de forma completamente autónoma, utilizando a liquidez do seu nó LND subjacente.



**Conceito chave**: Todas estas carteiras partilham a liquidez global do seu nó Umbrel. Não se criam novos canais Lightning para cada Wallet - a LNbits actua como uma contabilidade inteligente Layer que gere a alocação de fundos dentro da sua infraestrutura Lightning existente. Esse é o poder do sistema multi-Wallet da LNbits.



### Início de sessão do utilizador



Saia da conta SuperUser (ícone no canto superior direito) e volte para a página de login do LNbits. Agora é possível fazer o login com as credenciais do novo usuário.



![Connexion utilisateur satoshi](assets/fr/13.webp)



Introduzir o nome de utilizador ("Satoshi") e a palavra-passe previamente definidos e clicar em "LOGIN". O utilizador passa a ter acesso direto ao seu Wallet pessoal, totalmente isolado do Interface de administração.



### Interface do utilizador Wallet



Uma vez ligado, o utilizador acede ao seu Interface a partir do Wallet Lightning.



![Interface wallet utilisateur](assets/fr/14.webp)



O Interface possui :




- Saldo atual**: Apresentado em Sats e na moeda escolhida (CUC, neste exemplo)
- Principais acções**: "COLAR PEDIDO" (colar uma fatura para pagar), "CRIAR Invoice" (generate um recibo), ícone QR (leitura rápida)
- Histórico de transacções** : Lista completa de todos os pagamentos e recibos
- Painel lateral direito**: Opções de configuração e acesso



### Acesso móvel Wallet



O painel do lado direito oferece uma caraterística particularmente prática: o acesso móvel ao Wallet. Desdobre a secção "Acesso móvel" para descobrir as opções disponíveis.



![Mobile Access](assets/fr/15.webp)



A LNbits propõe várias formas de utilizar este Wallet num smartphone:



**Opção 1: Aplicações móveis compatíveis




- Descarregar **Zeus** ou **BlueWallet** da App Store ou do Google Play
- Ativar a extensão **LndHub** no LNbits para este Wallet
- Digitalize o código QR do LndHub com a aplicação móvel para ligar o Wallet



**Opção 2: Acesso direto através do browser móvel**




- O código QR apresentado em "Exportar para telemóvel com código QR" contém o URL completo do Wallet com autenticação integrada
- Digitalize este código QR a partir do seu smartphone para abrir o Wallet diretamente no seu browser móvel
- Adicionar página ao ecrã inicial para acesso rápido



**Segurança importante**: Este URL contém as chaves do API para acesso total ao Wallet. Nunca o partilhe publicamente. Trate este código QR como trataria as suas chaves privadas do Bitcoin - qualquer pessoa que leia este código QR obtém acesso total ao Wallet.



Este recurso móvel transforma sua instância LNbits Umbrel em um verdadeiro servidor Lightning Wallet para você e seus amigos, mantendo total soberania sobre seus fundos graças ao seu nó auto-hospedado.



### Partilha do acesso do utilizador



O principal caso de utilização para esta configuração multi-utilizador é **partilhar carteiras com a sua família ou círculo próximo**. Depois de criar um utilizador com um Wallet dedicado (como "Satoshi" no nosso exemplo), pode partilhar estas credenciais de início de sessão com membros de confiança do seu agregado familiar.



**Segurança de acesso na Umbrel**: O acesso à sua instância LNbits na Umbrel é naturalmente protegido, pois só pode ser acessado :




- Na sua rede local** : Os membros do seu agregado familiar ligados à mesma rede WiFi/Ethernet podem aceder à instância
- Via VPN**: Se utilizar uma VPN como a Tailscale configurada no seu servidor Umbrel, os utilizadores autorizados podem obter acesso remoto seguro



Este duplo Layer de proteção (acesso à rede + autenticação do utilizador) torna a opção "Permitir a criação de novos utilizadores" menos crítica na Umbrel. Apenas as pessoas que já têm acesso à sua rede ou VPN podem aceder ao início de sessão Interface.



**Cenário típico**: Cria-se uma conta "pai", uma conta "mãe", uma conta "empresa" e assim por diante. Cada membro da família tem o seu próprio Wallet Lightning isolado, enquanto beneficia da liquidez partilhada do seu nó Umbrel. Basta partilhar o nome de utilizador e a palavra-passe - o utilizador pode então ligar-se a partir de qualquer dispositivo na sua rede local ou através da sua VPN Tailscale. Para mais informações, consulte o nosso tutorial Tailscale dedicado:



https://planb.academy/tutorials/computer-security/communication/tailscale-9acbd7de-04d9-40f6-ab80-35f0dfedb632

### Explorar as extensões disponíveis



Volte ao Interface SuperUser e aceda ao menu "Extensões" no painel lateral esquerdo para descobrir todo o ecossistema de extensões do LNbits.



![Extensions disponibles](assets/fr/16.webp)



O LNbits oferece um rico catálogo de extensões que transformam sua instância em uma verdadeira plataforma de serviços do Lightning:





- Jukebox**: Sistema de jukebox alimentado por Sats (pagamentos Spotify)
- Tickets de suporte**: Sistema de suporte pago (receba Satss para responder a perguntas)
- TPoS**: Terminal de ponto de venda móvel e seguro para retalhistas
- User Manager**: gestão avançada de utilizadores e do Wallet (que acabámos de utilizar)
- Eventos**: Venda e validação de bilhetes para eventos
- Dispositivos LNURLD**: Gestão de pontos de venda, ATMs, comutadores ligados
- SMTP**: Permitir que os utilizadores enviem e-mails e ganhem Satss
- Boltcards**: Programação de cartões NFC para pagamentos Lightning tap-to-pay
- NostrNip5**: Criar endereços NIP5 para os seus domínios
- Pagamentos divididos**: Distribuição automática de pagamentos entre várias carteiras



Cada extensão é activada com um único clique a partir deste Interface. As extensões marcadas com "FREE" são gratuitas, enquanto algumas estão disponíveis em versões "PAGAS". Explore o catálogo para identificar as que correspondem às suas necessidades - seja para negócios, gestão familiar ou para experimentar as capacidades do Lightning Network.



## Vantagens e limitações



**Vantagens**: Soberania financeira (controlo total sobre fundos/chaves/dados), flexibilidade arquitetónica (migração VPS→Full node sem perdas), sistema de extensão profissional, Interface intuitivo.



**Limitações** : Software em versão beta (cuidado com as quantidades), segurança sob a responsabilidade do administrador, URLs que contêm chaves API sensíveis (HTTPS obrigatório), gestão de múltiplos utilizadores implica responsabilidade de custódia.



## Melhores práticas



**Backups**: seed PHOENIXD/credenciais LND, base de dados LNbits, ficheiros `.env`. Automatizar diariamente, manter fora do servidor de produção, encriptado. Testar restaurações regularmente.



**Manutenção**: Verificar regularmente se há actualizações (LNbits, backend Lightning, sistema operativo). Verifique sempre as notas de lançamento antes das principais actualizações.





- Na Umbrel**: A App Store notifica-o automaticamente de novas versões. Sincronizar extensões através de "Gerir extensões" > "Atualizar tudo". Verificar a inclusão da base de dados SQLite nas cópias de segurança automáticas da Umbrel.
- Em VPS**: Atualizar manualmente com `cd lnbits && git pull && uv sync --all-extras && sudo systemctl restart lnbits`. Monitorar os logs do sistema: `sudo journalctl -u lnbits -f`.



## Conclusão



A auto-hospedagem da LNbits oferece um caminho concreto para a soberania financeira da Lightning. O VPS+PHOENIXD oferece uma solução leve para serviços rápidos, integração total da Umbrel com o nó Bitcoin existente. A arquitetura escalável permite a evolução de um simples Wallet multiutilizador para casos de utilização empresarial sofisticados.



A auto-hospedagem implica responsabilidade: fazer backup das sementes, proteger o acesso, começar com quantidades modestas. Com essas precauções, o LNbits se torna uma solução robusta para a economia Lightning, preservando a descentralização e a autonomia.



## Recursos



### Documentação oficial




- [Documentação LNbits](https://docs.lnbits.org)
- [LNbits GitHub](https://github.com/lnbits/lnbits)
- [PHOENIXD GitHub](https://github.com/ACINQ/PHOENIXD)
- [Guia de instalação oficial] (https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)



### Guias comunitários




- [Configuração inicial do servidor Ubuntu](https://danielpcostas.dev/ubuntu-server-initial-configuration-a-step-by-step-guide/) por Daniel P. Costas (segurança VPS passo-a-passo)
- [Instalação do LNbits + PHOENIXD no Ubuntu VPS](https://danielpcostas.dev/install-lnbits-PHOENIXD-vps-ubuntu/) por Daniel P. Costas (guia completo)
- [Servidor LNbits na Clearnet](https://ereignishorizont.xyz/lnbits-server/en/) por Axel
- [LNbits em VPS](https://github.com/TrezorHannes/vps-lnbits) por Hannes