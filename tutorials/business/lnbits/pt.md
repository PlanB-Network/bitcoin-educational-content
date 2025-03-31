---
name: LNbits
description: Plataforma de contabilidade para comerciantes
---
![presentation](assets/lnbits-intro.webp)

# Sistema de contabilidade

O LNbits está repleto de ferramentas para controlar e canalizar as suas entradas e saídas de fundos, ligar a sua loja virtual ou mesmo dispositivos como uma carteira de hardware ou uma caixa multibanco que tenha construído. Os tipos de utilizadores incluem:


- Os proprietários de carteiras que pretendam utilizar o LNbits como interface para a gestão dos seus fundos, bem como as suas funcionalidades adicionais.
- Comerciantes ou prestadores de serviços online e offline que pretendam aceitar pagamentos Bitcoin onchain e Lightning Network.
- Desenvolvedores que desejam criar aplicativos Lightning Network.
- Operadores de nós que pretendam integrar o seu nó no sistema LNbits para fins contabilísticos.
- Todos eles têm necessidades diferentes. Construímos o LNbits de forma modular para que cada utilizador possa utilizar as nossas funcionalidades da forma que mais lhe convém.

# Gestor de carteiras

O LNbits é um sistema de contabilidade gratuito e de código aberto - não é um gestor de nós. A gestão de canais é o domínio do nó Lightning que está ligado ao LNbits como uma fonte de financiamento como o LND ou o c-lightning. Os utilizadores Superuser ou Admin do sistema LNbits são responsáveis pela gestão da acessibilidade e configuração das funcionalidades de contabilidade e extensões internas.

O LNbits actua como uma interface entre o utilizador e o nó Lightning, fornecendo uma forma simples e fácil de gerir e interagir com a rede de pagamentos.

Pense no LNbits como uma "estrutura modular wordpress" para o seu nó. Uma plataforma fácil de gerir, baseada em extensões que pode combinar para vários casos de utilização.

Pense no LNbits como o seu próprio software de gestão financeira bancária. O seu nó oferece canais de pagamento e o LNbits estende o seu nó para poder executar mais do que uma carteira lightning que vem com o seu nó. Essas carteiras não precisam necessariamente pertencer a você. Digamos que tu, como executor do nó LN, já tens liquidez e fundos suficientes para o canal e agora queres oferecer alguns serviços bancários bitcoin aos teus amigos, família, loja própria ou outros comerciantes regulares.

Oferecer-lhes-á uma forma simples de abrir uma "conta bancária" no seu nó sem ter acesso a outras carteiras no seu nó e a toda a liquidez do seu nó, mas apenas à sua parte. O seu nó (o banco) actua apenas como um fornecedor de transporte para os seus pagamentos (entrada/saída).

NOTA: todos os fundos que os seus "clientes" depositarem nas suas contas bancárias LNbits no seu nó, irão diretamente para os canais LN do seu nó. Isso significa que VOCÊ é o verdadeiro dono desses fundos. Terás uma grande responsabilidade pelos seus fundos. Não sejas mau e fujas com os fundos, não sejas mau e cobres taxas elevadas. Queremos foder os banqueiros fiat, não nos fodermos uns aos outros (utilizadores de bitcoin).

# Plataforma de demonstração

A demonstração pode ser encontrada em [https://legend.lnbits.com](https://legend.lnbits.com). Ela é totalmente funcional e pode ser usada para aprender sobre a Lightning Network e os recursos do LNbits e do LNURL em geral. Embora não possamos impedi-lo, gostaríamos de pedir-lhe que não o utilize para a sua configuração de produção. Não só estamos a trabalhar nos servidores frequentemente para testar novas funcionalidades, mas também gostaríamos de encorajar-te a correr o teu próprio nó e o LNbits de uma forma soberana. Se achas que gerir um nó é demasiado exigente de momento, podes ligar o LNbits a um serviço de custódia de fundos na nuvem como o Opennode, Luna ou Votage ou ao Lightning Tipbot no Telegram, só para citar alguns.

# Folheto LNbits

Quer dar algumas informações de base a um comerciante ou a um amigo construtor? Temos o prazer de anunciar o nosso primeiro desdobrável para uso de todos. O tamanho é um formato de folheto globalmente típico com 6 páginas (2 dobras) e uma largura de 3508 e uma altura de 2480px.

LNbits para comerciantes: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)

LNbits para construtores: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)

# Algumas noções básicas

O LNbits funciona com base no protocolo LNURL, o que significa que os pedidos são válidos de duas formas: ou como https:// clearnet link (não são permitidos certificados auto-assinados) ou como http:// v2/v3 onion link. Para oferecer serviços LNbits, como códigos QR LNURLp/w ou cartões NFC, que podem ser usados na natureza, é necessário abrir o LNbits para a clearnet (https).

Antes de instalar o LNbits, certifique-se de que leu e compreendeu os seguintes guias gerais sobre o que é o LNbits e quais as possibilidades que ele abre para si.


- [Guia LND] (https://docs.lightning.engineering/) | Instalação do LND
- [Exemplo de configuração LND] (https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | Definições LND
- [Guia da CLN](https://docs.corelightning.org/docs/installation) | Instalar a CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Gerir uma torre de vigia](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | Muito importante!

Guias mais pormenorizados sobre a utilização de LNbits em cenários de casos de utilização específicos aqui:


- [Getting Started with LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Guia do Substack
- [ToDos para a sua segurança com LNbits](https://youtu.be/i5FQf96e6zg) | Vídeo do Youtube
- [Bancos privados na Lightning Network](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | Guia de substabelecimento
- [Executar carteiras de custódia para os seus amigos e família](https://darthcoin.substack.com/p/the-bank-of-lnbits) | Guia de substabelecimento
- [LNbits para um pequeno restaurante / hotel](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Guia Substack
- [Usando o copiloto do LNbits Streamer](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Guia do Substack
- [Inicie o seu Mercado NOSTR com LNbits] (https://darthcoin.substack.com/p/lnbits-nostr-market) | Guia do Subconjunto
- [Utilizar o LNbits para projectos escolares ou eventos festivos] (https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Guia de substabelecimento

# Instalar o LNbits

## Guia básico de instalação

O LNbits pode ser instalado em qualquer máquina com sistema operativo Linux. Não requer uma máquina ou servidor potente, apenas memória RAM suficiente e algum espaço em disco para a base de dados. Pode ser executado separadamente de um nó BTC/LN (PC local ou VPS remoto) ou em conjunto na mesma máquina com o nó ou já instalado numa máquina de software de nó de pacote.

É possível escolher entre os gerenciadores de pacotes mais comuns, como o poetry e o nix. Por padrão, o LNbits usará o SQLite como banco de dados. Também é possível usar o PostgreSQL, que é recomendado para aplicações com alta carga. [Aqui está um guia para instalação básica usando poetry ou nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).

Para todos os novatos, encontrarão guias passo-a-passo mais detalhados para colocar os seus LNbits a funcionar em ambientes específicos:


- [LNbits na clearnet](https://ereignishorizont.xyz/lnbits-server/en/) por Axel
- [LNbits num VPS](https://github.com/TrezorHannes/vps-lnbits) por Hannes
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) por Leo

Também pode encontrar um vídeo sobre a [Configuração em docker num VPS com PostgreSQ, LightningTipBot como fonte de financiamento utilizando nginx] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).

[Mais cenários de instalação aqui] (https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).

Para nós de software de pacote, consulte a sua documentação específica sobre LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)

## LNbits SaaS

Se não estiveres interessado nas questões técnicas e não quiseres alojar a tua fonte de financiamento nem os teus próprios lnbits, existe uma [versão LNbits SaaS](https://saas.lnbits.com) (Software-as-a-service) que podes usar. É basicamente como o LNbits numa nuvem, mas podes definir a fonte de financiamento (por exemplo, o teu Node, uma carteira LNbits, o LNtipbot, fakewallet, etc.) e as variáveis de ambiente - o que não acontece noutras soluções na nuvem.

[Aqui está um guia pormenorizado sobre como utilizar o LNbits SaaS para casos de utilização específicos](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).

## Fontes de financiamento

O LNbits não é um software de gestão de nós, mas sim um sistema de contabilidade orientado para os LN sobre uma fonte de financiamento LND ou CLN. Após a primeira instalação, pode visitar o seu LNbits em http://localhost:5000/.

Para modificar a fonte de financiamento, vá ao seu super-user-URL e selecione uma fonte de financiamento em "Manage Server" ou edite o ficheiro .env modificando `LNBITS_BACKEND_WALLET_CLASS` para a fonte que necessita se definir `adminUI=TRUE` no `.env`.

Você encontrará o arquivo .env dentro da sua pasta lnbits/ ou lnbits/apps/data estendendo o comando para listar arquivos no seu diretório com `ls -a`.

Poderá também ser necessário instalar pacotes adicionais ou executar passos de configuração adicionais, selecionando a fonte de financiamento pretendida. Depois de reiniciar, a sua nova configuração estará ativa.

Que fontes de financiamento posso utilizar para o LNbits?

O LNbits pode ser executado em cima de muitas fontes de financiamento de lightning-network. Atualmente há suporte para CoreLightning, LND, LNbits, LNPay, OpenNode, com mais sendo adicionados regularmente.

É importante escolher uma fonte que tenha uma boa liquidez e bons pares ligados. Se utilizar LNbits para serviços públicos, os pagamentos dos seus utilizadores só então poderão fluir alegremente em ambas as direcções.

Uma carteira backend (fonte de financiamento) pode ser configurada usando as seguintes variáveis de ambiente do LNbits no arquivo `.env` ou dentro da sua conta de superusuário na seção Manage-Server.

Se pretender utilizar a versão .env, pode encontrar os parâmetros aqui:

### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-rpc
- Faísca (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - `SPARK_TOKEN`: chave_de_acesso_secreto

### Daemon da rede Lightning


- LND (REPOUSO)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon ou Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: porta
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon ou Bech64/Hex

Também pode utilizar um macaroon encriptado por AES (mais informações), utilizando


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Para encriptar o seu macaroon, execute `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.

### LNbits (outra instância de LNbits)


- Instância LNbits alojada num servidor em nuvem ou no seu próprio servidor doméstico
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!!! NÃO utilizar este para fins de produção / comerciais, apenas para testes !!!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Relâmpago TipBot

Para ligar o seu [Lightning Tipbot] (https://t.me/LightningTipBot) a partir do Telegram, terá de definir o seguinte parâmetro:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: Para obter a chave, você precisará executar /api em um chat privado com o LightningTipbot no Telegram uma vez.

Veja também este tutorial de como instalar [LNbits com LightningTipBot via vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)

### IBEX HUB

Registe-se [aqui] (https://ibexpay.ibexmercado.com/onboard) e obtenha as suas chaves/tokens a partir daí, o ponto final é https://ibexpay-api.ibexmercado.com.

Para mais informações, consultar [IBEX API-Documentation] (https://ibexpay-api.readme.io/reference/getting-started-with-your-api).

### LNPay

Para que o ouvinte de facturas funcione, é necessário ter um URL acessível ao público no seu LNbits e configurar um [LNPay webhook](https://dashboard.lnpay.co/webhook/) apontando para `<your LNbits host>/wallet/webhook` com o evento "Wallet Receive" e sem segredo. A configuração `https://mylnbits/wallet/webhook` será o url do endpoint que será notificado sobre qualquer pagamento.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey

### Nó aberto

Para que a fatura funcione, é necessário ter um URL acessível ao público no seu LNbits. A definição do webhook é opcional.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey

### Alby

Alby é uma extensão de browser com funcionalidades de carteira LN e conta LNDHUB que pode ser usada como fonte de financiamento para LNbits. [Mais detalhes aqui](https://getalby.com/).

Para que a fatura funcione, é necessário ter um URL acessível ao público no seu LNbits. Não é necessária qualquer configuração manual do webhook. Pode gerar um token de acesso Alby aqui: https://getalby.com/developer/access_tokens/new


- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken

## Guias adicionais / de resolução de problemas

Seguem-se algumas instruções adicionais, caso necessite delas. Clique na seta para expandir a descrição.

### O Killswitch 🚨

Ultimamente tem havido tantos bugs perigosos, não só em todo o espaço, mas também no LNbits, que decidimos fazer algo a esse respeito. Agora pode optar por receber avisos e/ou tomar medidas diretas, quando uma vulnerabilidade ou um bug que possa levar à perda de fundos ocorrer novamente.

![killswitchn](assets/lnbits-killswitch.webp)

Se mudar para void-wallet, todos os tipos de utilizador na instância verão um banner amarelo onde normalmente se encontra o aviso "LNbits is in Beta" junto à área de tema/idioma à direita - e é a dica mais óbvia de que algo aconteceu. Dê uma olhada na sua nova aba de servidor destacada em verde na parte esquerda da janela.

Como ele funciona? Quando o killswitch está ativado, um repositório secreto do github apenas disponível para a equipa principal do LNbits será verificado num intervalo de X minutos (que pode ser especificado). Se um bug vulnerável for publicado neste repositório, ele serve como um sinal que aciona o killswitch em todas as instalações que se inscreveram e transita sua instância do lnbits para usar a void wallet. Se as nuvens tiverem desaparecido e tiveres instalado a atualização de segurança, podes definir a tua fonte de financiamento para o teu nó, carteira ou o que quer que estejas a usar novamente, também através da secção Gerir Servidor. Este wiki tem uma secção sobre como mudar as fontes de financiamento se não souberes o que configurar.

### Diferença entre administrador e superutilizador

A interface de administração do LNbits permite que você altere as configurações do LNbits através do frontend do LNbits. Ela é desabilitada por padrão e a primeira vez que você define a variável de ambiente `LNBITS_ADMIN_UI=true` no arquivo `.env`, as configurações são inicializadas e serão utilizadas. A partir daí, as configurações de acordo com o banco de dados em vez daquelas do arquivo .env são usadas.

### Super Utilizador

Com a IU de administração, introduzimos o superutilizador que tem acesso ao servidor, pelo que pode alterar as definições que podem fazer com que o servidor falhe ou deixe de responder através do frontend e da API, como, por exemplo, alterar a fonte de financiamento. O superutilizador só é armazenado na tabela de definições da base de dados. Depois de as definições serem "repostas para as predefinições" e reiniciadas, é criado um novo superutilizador. Também adicionámos um decorador para as rotas da API para verificar a existência de um superutilizador. O seu ID nunca é enviado através da API e do frontend e apenas recebe um bool (sim/não) se é super utilizador ou não.

Apenas o superutilizador está autorizado a transferir satoshis para diferentes carteiras através da secção "Top Up".

Também pode enviar o super utilizador através de um webhook para outro serviço quando este for criado. Mais informações aqui https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`

No frontend, encontrará também a possibilidade de alterar a imagem da loja que é mostrada na página "criar carteira", abrindo a secção Gerir servidor e escolhendo Tema -> Logótipo personalizado.

### Utilizadores administradores

Variável de ambiente: `LNBITS_ADMIN_USERS`, lista de IDs de utilizadores separados por vírgulas. Os utilizadores administradores podem alterar as definições na interface de administração - com exceção das definições de fonte de financiamento, porque isso exigiria um reinício do servidor e poderia tornar o servidor potencialmente inacessível. Também têm acesso a todas as extensões que lhes são dedicadas em `LNBITS_ADMIN_EXTENSIONS`.

### Utilizadores permitidos

Variável de ambiente: `LNBITS_ALLOWED_USERS`, lista de IDs de usuários separados por vírgula. Ao definir esses usuários, o LNbits não poderá mais ser utilizado pelo público. Apenas os usuários definidos e os administradores podem acessar o frontend do LNbits.

#### Atualizar LNbits

Uma atualização normal da sua instância local do LNbits é simplesmente copiar e colar os seguintes comandos CLI:

```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```

Se executar o Raspiblitz ou o MyNode, poderá precisar adicionalmente de um

```
sudo systemctl restart lnbits
```

no final, porque ele executa o LNbits como um serviço.

Na Umbrel/Citadel, os comandos seriam

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```

#### Migração de SQLite para PostgreSQL

Se já tem o LNbits instalado e a correr numa base de dados SQLite, recomendamos vivamente que migre para postgres se estiver a planear correr o LNbits em escala.

Está incluído um script que pode efetuar a migração facilmente. É necessário ter o Postgres já instalado e deve haver uma password para o utilizador (ver guia de instalação do Postgres acima). Além disso, sua instância do LNbits precisa rodar uma vez no Postgres para implementar o esquema do banco de dados antes que a migração possa funcionar:

```
# STOP LNbits
# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit
# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Esperemos que agora tudo funcione e seja migrado... Inicie o LNbits novamente e verifique se tudo está a funcionar corretamente.

#### Cópia de segurança e restauro da base de dados

Consulte [este guia muito pormenorizado sobre o processo de cópia de segurança e restauro] (https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).

#### Financiar a minha carteira LNbits a partir do meu nó não funciona

Se quiser enviar sats a partir do mesmo nó que é a fonte de financiamento dos seus LNbits, terá de editar o ficheiro lnd.conf.

Os parâmetros a incluir são: `allow-circular-route=1`

Faça-o na secção Opções de aplicação do seu lnd.conf. Caso contrário, o início do LND poderá falhar nalgum nó do pacote.

NOTA: Recomenda-se a utilização da nova extensão adminUI com a opção "TopUp" para adicionar fundos a uma conta LNbits.

#### Erro 426

Recebi o erro: "lnurl precisa de ser entregue através de um domínio https publicamente acessível ou tor. é necessária a atualização 426"</summary>

Esse erro geralmente ocorre porque seu LNbits por trás de um túnel ngnix não está encaminhando o endereço LNURL corretamente. Pare seu LNbits e edite o arquivo .env adicionando esta linha:

`FORWARDED_ALLOW_IPS=*`

Além disso, se utilizar uma configuração ngnix, certifique-se de que tem estes cabeçalhos na configuração ngnix:

```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```

#### Erro de rede

Obtive "erro de https", erro de rede" ou outros quando digitalizei um QR</summary>

Más notícias, este é um erro de encaminhamento que pode ter várias razões. Primeiro, verifica o LNURL do QR com o [Lightning Decoder] (https://lightningdecoder.com/), se encontrares algo estranho. Vamos tentar alguns dos problemas mais possíveis e suas soluções.

O LNbits é executado apenas através do Tor, não é possível abri-lo num domínio público como lnbits.yourdomain.com


- Dado que queres que a tua configuração se mantenha assim, abre a tua carteira LNbits usando o .onion URI e cria-a novamente. Desta forma, o QR é gerado para ser acessível através deste URI .onion, portanto, apenas via tor. Não geres esse QR a partir de um URI .local, porque não será acessível através da Internet - apenas a partir da tua LAN doméstica.
- Abra a aplicação da carteira LN que utilizou para digitalizar o QR e, desta vez, utilize o tor (ver definições da aplicação da carteira). Se a aplicação não oferecer o tor, pode usar o Orbot (Android). Consulte a secção de instalação para obter instruções detalhadas sobre como abrir os seus LNbits para clearnet/https.

#### Impedir que outros gerem carteiras nos meus LNbits

Quando se corre o LNbits na clearnet, basicamente toda a gente pode gerar uma carteira nele. Uma vez que os fundos do teu nó estão ligados a estas carteiras, podes querer evitar isso. Há duas maneiras de o fazer:

Configurar os utilizadores e extensões permitidos no ficheiro `.env` ([veja o exemplo de env aqui](https://github.com/lnbits/lnbits/blob/main/.env.example)). Isso só funciona se você usar a configuração `adminUI=FALSE` no .env, caso contrário você precisa fazer isso na seção Manage Server -> Users -> Allowed Users. Todos os outros não serão permitidos depois.

#### Personalizar o prazo de validade da fatura

Agora é possível gerar facturas com um prazo de validade personalizado. Compatível com backends: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet até agora!

Pode definir `LIGHTNING_INVOICE_EXPIRY` no seu ficheiro .env ou utilizar a AdminUI para alterar o valor predefinido para todas as facturas. Existe também um novo campo no ponto de extremidade /api/v1/payments onde pode definir a expiração nos dados JSON.

## Carteira-URL eliminada

### Carteira no servidor de demonstração legend.lnbits

Guarde sempre uma cópia da sua wallet-URL, Export2phone-QR ou LNDhub para as suas próprias carteiras num local seguro. O LNbits NÃO PODE ajudá-lo a recuperá-las quando perdidas.

### Carteira na sua própria fonte/nó de financiamento

Guarde sempre uma cópia da sua wallet-URL, Export2phone-QR ou LNDhub para as suas próprias carteiras num local seguro. Pode encontrar todos os utilizadores do LNbits e IDs de carteiras na sua extensão de gestão de utilizadores do LNbits ou na sua base de dados sqlite. Para editar ou ler a base de dados do LNbits, vá para a pasta LNbits /data e procure o ficheiro chamado sqlite.db. Pode abri-lo e editá-lo com o Excel ou com um editor SQL dedicado como o [SQLite browser](https://sqlitebrowser.org/).

Também pode descarregar as carteiras via cli e ver todas as carteiras da sua base de dados.

```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```

O resultado terá o seguinte aspeto

```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

e pretende colocar estes valores num url como este

```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```

Substitua f8a43fc363ea428db5c53b3559935f1f pelo valor que vem antes do nome (no nosso exemplo f8a43fc363ea428db5c53b3559935f1f) e 1280ff5910a9c485a782a2376f338b6c é o seu utilizador e deve tornar-se o valor apresentado a seguir ao nome. Para sair do sqlite3 coloque

```
.quit
```

#### LNURL para um endereço relâmpago e vice-versa

Experimente este [codificador](https://lnurl-codec.netlify.app/) da fiatjaf ou [este](https://lightningdecoder.com/). Para pagar ou verificar um LNURLp, pode também utilizar [LNurlpay](https://wwww.lnurlpay.com/). Deve indicar HTTPS e não HTTP.

#### Configurar um comentário que as pessoas vêem quando pagam ao meu LNURLp QR

Quando cria um LNURL-p, por defeito, a caixa de comentários não é preenchida. Isto significa que não é permitido anexar comentários aos pagamentos.

Para permitir comentários, adicione o comprimento de caracteres da caixa, de 1 a 250. Assim que colocar um número, a caixa de comentários será apresentada no processo de pagamento. Também pode editar um LNURL-p já criado e acrescentar esse número.

![lnbits comments](assets/lnbits-comments.webp)

#### Depositar BTC onchain em LNbits

Existem duas maneiras de trocar sats de onchain BTC para LN BTC (resp. para LNbits).

##### Através de um serviço de troca externo.

Outros utilizadores que não tenham acesso ao seu LNb its podem usar um serviço de troca como [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) ou [ZigZag](https://zigzag.io/). Isto é útil se fornecer apenas facturas LNURL/LN a partir da sua instância LNbits, mas um pagador apenas tem sats onchain, pelo que terá de trocar esses sats primeiro do seu lado. O procedimento é simples: o utilizador envia btc onchain para o serviço de swap e fornece a fatura LNURL / LN do LNbits como destino do swap.

##### Utilizar a extensão Onchain e Boltz LNbits.

Tenha em mente que esta é uma carteira separada, não a carteira LN btc que é representada pela LNbits como "a sua carteira" na sua fonte de financiamento LN. Esta carteira onchain pode ser usada também para trocar LN btc para (por exemplo, a tua hardwarewallet) usando a extensão LNbits Boltz ou Deezy. Se tens uma loja online que está ligada à tua LNbits para pagamentos de LN, é muito útil drenar regularmente todos os sats de LN para a onchain. Isto leva a mais espaço nos teus canais LN para poderes receber novos sats frescos.

Procedimento para quem não tem uma carteira de hardware bitcoin:


- Use a carteira Electrum ou Sparrow para criar uma nova carteira onchain e guarde a semente de backup num local seguro.
- Aceda às informações da carteira e copie o xpub.
- Vai a LNbits - extensão Onchain e cria uma nova carteira só para relógios com esse xpub.
- Vai a LNbits - Tipjar extension e cria um novo Tipjar. Seleciona também a opção onchain para além da carteira LN.
- Opcional - Vai a LNbits - extensão SatsPay e cria um novo débito para onchain btc. Podes escolher entre onchain e LN ou ambos. Será então criada uma fatura que pode ser partilhada.
- Opcional - Se utilizar o seu LNbits ligado a uma página Wordpress + Woocommerce, assim que criar/ligar uma carteira só de relógios à sua carteira de loja LN btc, o cliente terá ambas as opções de pagamento no mesmo ecrã.

Quando se recebe um pagamento em LNbits, o registo da transação apresentará apenas um tipo de transação retomada.

![lnbits payment details](assets/lnbits-payment-details.webp)

No resumo da transação, encontrará uma pequena seta verde para os fundos recebidos e uma seta vermelha para os fundos enviados.

Se clicar nessas setas, uma janela de detalhes mostra as mensagens anexas, bem como o nome do remetente, se este for indicado.

Para configurar um nome para aparecer nos pagamentos, no LNbits isto não é atualmente possível de fazer - mas sim de receber. Isto só é possível se a carteira LN do remetente suportar [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) como [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).

Verá então um pseudónimo na secção de detalhes das suas transacções LNbits (clique nas setas). Nota que podes dar qualquer nome e que este pode não estar relacionado com o nome do verdadeiro remetente, se o receberes.

![lnbits namedesc](assets/lnbits-namedesc.webp)

Para importar a tua conta LNbits para uma aplicação de carteira, abre o teu LNbits com a conta/carteira que queres usar, vai a "gerir extensões" e ativa a extensão LNDHUB. Abra a extensão LNDHUB, escolha a carteira que deseja usar e digitalize o QR "admin" ou "invoice only", dependendo do nível de segurança que deseja para essa carteira.

Você pode usar [Zeus](https://zeusln.app/) ou [Bluewallet](https://bluewallet.io/) como aplicativos de carteira para uma conta lndhub onde BW suporta mais de uma carteira.

Ao fazer isso, recomendamos também definir o URI da rede LN para o do seu próprio nó. Se a tua instância LNbits é apenas Tor, também tens de usar estas aplicações com o Tor ativado. Também neste caso tens de abrir a página do LNbits através do teu endereço Tor .onion.

Se você tiver um erro "unsupported hash type" (tipo de hash não suportado) ao usar um ypub na extensão On-chain, verifique se sua instância do LNbits está usando python 3.10, pois ela pode ser afetada por [este problema](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python). Edite o openssl.cnf como descrito na resposta do stackoverflow e reinicie seu LNbits.

## Ferramentas e construção com LNbits

O LNbits tem todo o tipo de [APIs abertas](https://legend.lnbits.com/docs) e ferramentas para programar e ligar a uma série de dispositivos diferentes para um zilião de casos de utilização.

Se és novo na construção, começa com estas [MakerBits presentations](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) de Ben Arc sobre a construção de gadgets baseados em LNbits.

### IMPORTANTE:


- O LNbits funciona com base no protocolo LNURL, cujos pedidos são válidos de duas formas: ou como https:// clearnet link (não são permitidos certificados auto-assinados) ou como http:// v2/v3 onion link. Para oferecer serviços LNbits, como códigos QR LNURLp/w ou cartões NFC, que podem ser usados na natureza, é necessário abrir o LNbits para a clearnet (https).
- Utilize apenas cabos de dados para alimentar a sua esp32. Nem todos os cabos suportam dados para além de alimentar o esp. Não seria o primeiro se o cabo que veio com o esp fosse apenas de alimentação
- Certifique-se de que não utiliza um concentrador USB com outros dispositivos ligados. Isto pode levar a efeitos estranhos que são difíceis de depurar (por exemplo, não arrancar ou parar).
- Para realizar projectos esp com um MacOS é necessário um driver UART Bridge. Se tiver problemas com o driver em sistemas Mac ou Linux, pode encontrá-los aqui ou, se estiver envolvido um ecrã TTGO, este aqui. Se estiver no Windows e tiver problemas de ligação, certifique-se de que descarrega a versão ANTIGA 11.1.0, porque a mais recente não funciona! Também pode encontrar um terminal série aqui para verificar a sua ligação - defina a velocidade de transmissão para 115200.
- Embora seja muito mais cómodo utilizar a Platform.io (por exemplo, as dependências são instaladas automaticamente), recomendamos a utilização do Arduino para todos os principiantes na construção.
- Ecrã TT-Go S3: A cor do separador da película protetora do ecrã indica-lhe qual o controlador utilizado para o construir (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ...). Guarde-o para poder depurar se se programar e o ecrã não apresentar os gráficos corretamente, por exemplo, cores erradas, imagens espelhadas ou pixéis perdidos nas extremidades. Se alguma vez precisares de o fazer, há um guia épico sobre o ajuste para diferentes ecrãs
- Utilizar sempre lnurl239xx em minúsculas em vez de LNURLl239xx
- A adição de lightning:lnurl1234xyz criará um QR que solicita a abertura da carteira do utilizador para esta fatura na leitura (última aplicação lightning instalada no iOS, definição no Android)
- Se estiver a fazer o flash de um esp32 via web, só funcionará com estes browsers (TL:DR Chrome, Edge & Opera).
- Tenha em atenção esta referência PIN-OUT para o esp
- Quando utilizar FOSSoftware ou FOSGuides, por favor, ligue sempre ao autor. Toda a gente gosta de ver o seu bebé crescer e isso também dá início a uma cadeia de construção que é bastante impressionante de ver :)

Vem ao [Grupo de Telegramas Makerbits] (https://t.me/makerbits) se precisares de ajuda com um projeto - nós ajudamos-te!

![lnbits hackathlon](assets/lnbits-hackathlon.webp)

Aqui estão algumas categorias de projectos que pode construir com o LNbits:


- [Dispositivo de assinatura Nostr](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Máquina Archade](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Piggy Relâmpago](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Carteira de hardware] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [Máquina de venda automática] (https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora e a rede em malha](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)
- [AJUDANTES E RECURSOS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Mais exemplos de projectos "Powered by LNbits" aqui] (https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Casos de utilização para LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)