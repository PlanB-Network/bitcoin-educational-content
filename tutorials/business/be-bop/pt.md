---
name: ser-BOP
description: Guia prático para rentabilizar o seu negócio com o be-BOP
---

![cover-bebop](assets/cover.webp)



*a *be-BOP** é uma plataforma de comércio eletrónico concebida para empreendedores que pretendam vender online e offline, com total autonomia, aceitando pagamentos em Bitcoin, através de uma conta bancária e em Dinheiro. A solução é também útil para qualquer tipo de organização que pretenda recolher donativos ou rentabilizar as suas diversas actividades.



A solução é simples, leve e autónoma. Permite a criação de uma loja online, mesmo num ambiente onde os serviços financeiros tradicionais são limitados ou inexistentes. De facto, o **be-BOP** foi concebido para funcionar eficazmente com ou sem acesso a bancos, utilizando o Bitcoin como infraestrutura de pagamento.



Neste tutorial, vamos guiá-lo passo a passo através do:





- Crie a sua primeira loja online com **be-BOP**
- Personalize a sua montra e os seus produtos
- Configurar os métodos de pagamento disponíveis
- Compreender as melhores práticas para vender eficazmente em linha com **be-BOP**



Este tutorial não requer competências técnicas avançadas. Destina-se a programadores, bem como a artesãos, comerciantes, cooperativas ou empresários que pretendam iniciar o comércio digital de forma soberana e resiliente.



## Pré-requisitos para instalar o be-BOP no seu próprio servidor



Antes de iniciar a instalação do be-BOP, certifique-se de que possui a seguinte infraestrutura técnica. Estes Elements são essenciais para o correto funcionamento da plataforma:



### Armazenamento compatível com S3



o be-BOP utiliza um sistema de armazenamento para gerir ficheiros (como imagens de produtos). Isto requer acesso a um serviço S3, como o:





- [MinIO](https://min.io/) auto-hospedado
- Amazon S3 (AWS)
- Armazenamento de objectos Scaleway



Terá de configurar um balde e fornecer as seguintes informações:





- S3_BUCKET**: nome do balde
- S3_ENDPOINT_URL**: ligação de acesso ao seu serviço S3
- S3_KEY_ID** e S3_KEY_SECRET: os seus códigos de acesso
- S3_REGION**: a região do seu serviço S3



### Base de dados MongoDB em modo ReplicaSet



o be-BOP utiliza o MongoDB para armazenar dados de lojas, utilizadores, produtos e outros.



Tem duas opções:





- Instalar o MongoDB localmente com o modo **ReplicaSet ativado**
- Utilizar um serviço em linha como o **MongoDB Atlas**



São necessárias as seguintes variáveis:





- MONGODB_URL**: ligação à base de dados Address
- MONGODB_DB**: nome da base de dados



## Ambiente Node.js



o be-BOP funciona com Node.js. Certifique-se de ter **Node.js** versão 18 ou superior e **Corepack** habilitado (necessário para gerenciar gerenciadores de pacotes como o pnpm). O comando a ser executado é `corepack enable`



### Git LFS instalado



Alguns recursos (como imagens grandes) são gerenciados via Git LFS (Large File Storage). Certifique-se de ter o Git LFS instalado em sua máquina com o comando `git lfs install`. Uma vez que estes pré-requisitos estejam prontos, você está pronto para passar para o próximo passo: fazer o download e configurar o be-BOP.



**Nota:** Um guia técnico para a implantação de software está disponível num tutorial separado.



## Criar uma conta de Super-Administrador



A primeira vez que o be-BOP é lançado, é criada uma conta **Super Admin**. Esta conta tem todas as autorizações necessárias para gerir as funções de back-office. Para criar uma conta, siga estes passos:





- Aceda a `yourresiteweb/admin/login`
- Criar uma conta de super-administrador com um início de sessão e uma palavra-passe seguros



Esta conta dá-lhe acesso a todas as funções de back-office. Uma vez criada, pode iniciar sessão introduzindo o seu nome de utilizador e a sua palavra-passe.



![login](assets/fr/001.webp)



## Configuração e segurança do back-office



Antes de configurar a ligação back-office do Interface, é necessário criar um Hash único. Este fornece proteção contra agentes maliciosos que tentam roubar a ligação de ligação ao seu administrador do Interface.



Para criar o Hash, aceda a `/admin/Settings`. Na secção dedicada à segurança (por exemplo, "Admin Hash"), defina uma cadeia de caracteres única (Hash). Uma vez registado, o URL do back-office será modificado (por exemplo, `/admin-yourhash/login`) para restringir o acesso a pessoas não autorizadas.



![hash-login](assets/fr/002.webp)



2.2. Ativar o modo de manutenção (se necessário)



Ainda em /admin/Settings, (Settings > General via Interface graphics), verifique a opção "enable maintenance mode" na parte inferior da página.



![maintenance-mode](assets/fr/003.webp)



Se necessário, pode especificar uma lista de endereços IPv4 autorizados (separados por vírgulas) para permitir o acesso ao front office durante a manutenção. O back office permanece acessível aos administradores.



![ip-bebop](assets/fr/004.webp)



## Configuração das comunicações



Para que o be-BOP possa enviar notificações (por exemplo, para encomendas, registos ou mensagens do sistema), é necessário configurar pelo menos um método de comunicação. Estão disponíveis duas opções: correio eletrónico (SMTP) ou Nostr.



### Configuração SMTP (correio eletrónico)



o be-BOP pode enviar mensagens de correio eletrónico através de um servidor SMTP. Necessitará de credenciais SMTP válidas, muitas vezes fornecidas por um serviço de correio eletrónico (por exemplo, Mailgun, Gmail, etc.).



Eis o que precisa de saber:



SMTP_HOST: Servidor SMTP Address (por exemplo, smtp.mailgun.org)



SMTP_PORT: a porta a utilizar (frequentemente 587 ou 465)



SMTP_USER: o seu nome de utilizador (normalmente um e-mail Address)



SMTP_PASSWORD: a sua palavra-passe ou chave API



SMTP_FROM: a mensagem de correio eletrónico Address que aparecerá como remetente




### Configuração Nostr



o be-BOP permite-lhe enviar notificações através do protocolo Nostr, uma infraestrutura de mensagens descentralizada. Para isso, é necessário generate ou Supply de uma chave privada Nostr (NSEC). Pode generate esta chave diretamente através do Interface do be-BOP, na secção dedicada ao Nostr. Quando estes Elements estiverem corretamente configurados, o be-BOP poderá enviar automaticamente mensagens e alertas aos seus utilizadores.



## Métodos de pagamento compatíveis



a be-BOP é compatível com várias soluções de pagamento, permitindo-lhe oferecer aos seus clientes uma maior flexibilidade. Veja aqui o que precisa para configurar o método de pagamento que mais lhe convém.



### Bitcoin Onchain



o be-BOP permite-lhe aceitar pagamentos Bitcoin diretamente no Blockchain (On-Chain), de forma simples e segura.



**Passos de configuração:**





- Aceder ao menu **Configurações de pagamento**
- Clique em **Bitcoin Nodeless** para aceder aos parâmetros de pagamento do On-Chain.
- Preencher os seguintes campos:



| Champ                  | Description                                               | Exemple à utiliser                              |
|------------------------|-----------------------------------------------------------|--------------------------------------------------|
| **BIP Standard**       | Le type d’adressage utilisé                               | BIP84 (pour les adresses au format bech32 commençant par `bc1`) |
| **Clé publique étendue** | Votre Zpub (ou Xpub selon le portefeuille utilisé)        | `zpub...` (extrait de votre portefeuille Bitcoin) |
| **Derivation Index**   | L’index de départ pour la génération des adresses         | `1`                                              |
| **Mempool URL**        | L’URL du service mempool utilisé pour suivre les transactions | `https://mempool.space`                         |

![payment-nodeless](assets/fr/005.webp)



**Dica:** Para obter a sua chave pública alargada (Zpub), pode consultar as definições avançadas do seu Bitcoin Wallet (Sparrow wallet, BlueWallet, Specter, etc.). Certifique-se de que o seu Wallet é **não só de leitura** se pretender utilizar o histórico de transacções.



### Lightning Network



o be-BOP também pode aceitar pagamentos instantâneos Bitcoin graças ao Lightning Network. Atualmente, estão disponíveis duas opções de configuração:



**Phoenixd**



Aceda ao menu `Configurações de pagamento`, clique em `Phoenixd`



![phoenixd](assets/fr/006.webp)



Terá então de introduzir **a palavra-passe ou a autenticação token** que o liga à sua instância Phoenixd, um backend desenvolvido pela Acinq que lhe permite gerir pagamentos Lightning com o seu próprio nó, mas sem a complexidade da gestão de canais de pagamento.



**Pagamento do Bitcoin suíço



Se não quiser gerir um nó Lightning, o **Swiss Bitcoin Pay** é uma solução pronta a utilizar e fácil de configurar, ideal para começar a aceitar pagamentos Lightning sem uma infraestrutura complexa.



Etapas de configuração:





- No menu "Definições de pagamento", clicar em "Swiss Bitcoin Pay"
- Inicie sessão na sua conta Swiss Bitcoin Pay (ou crie uma se ainda não tiver uma).
- Introduzir a chave API fornecida pelo Swiss Bitcoin Pay e clicar em "Guardar"



Uma vez configurado, o be-BOP emitirá automaticamente facturas generate Lightning para os seus clientes, e receberá os pagamentos diretamente na sua conta Swiss Bitcoin Pay. Esta solução é ideal para os utilizadores que pretendem evitar a complexidade técnica de um nó pessoal e, ao mesmo tempo, aceitar pagamentos rápidos e de baixo custo.



![swissbtcpay](assets/fr/007.webp)



### PayPal



Para além do Bitcoin, a be-BOP também permite aceitar pagamentos em dinheiro através do PayPal, uma solução internacional bem conhecida e amplamente utilizada.



Etapas de configuração:





- Aceder ao menu "Definições de pagamento
- Clique em `PayPal
- Na sua conta Paypal (secção de programador), introduza o `Client ID` e o `Secret`
- Selecione a moeda da sua escolha (por exemplo, **USD**, **EUR**, **XOF**, etc.)
- Clique em "guardar



![paypal](assets/fr/008.webp)



**Nota:** É necessário ter uma conta comercial PayPal para generate estes identificadores. Pode obtê-los através do portal [developer] (https://developer.paypal.com)



### SumUp



O software integra agora a solução de pagamento **SumUp**, permitindo-lhe aceitar pagamentos com cartão de crédito de forma simples, segura e eficaz. Para beneficiar desta funcionalidade, é necessário efetuar uma primeira configuração. Eis as etapas a seguir, numeradas para uma implementação clara e progressiva:





- Comece por introduzir a sua **Chave API**, uma chave confidencial fornecida pela SumUp quando criou a sua conta de programador. Esta chave estabelece uma ligação segura entre a sua conta SumUp e o software.
- Preencha o campo `Código do Comerciante` com o código único que identifica o seu negócio dentro da plataforma SumUp. Este código é essencial para associar transacções ao seu negócio.
- No campo "Moeda", escolha a moeda principal que utiliza para as suas transacções (por exemplo, **EUR**, **USD**, **CDF**, etc.).
- Depois de todos os campos terem sido preenchidos corretamente, clique no botão `Salvar` para guardar as suas definições. O sistema estabelecerá então a ligação com a sua conta SumUp, e o seu software estará pronto a aceitar pagamentos.



![payment-sumup](assets/fr/009.webp)



Após esta configuração, a integração **SumUp** estará ativa e operacional, permitindo-lhe levantar rapidamente dinheiro e acompanhar as suas transacções diretamente a partir do software.



### Riscas



o be-BOP também oferece integração total com **Stripe**, uma das plataformas de pagamento online mais populares. O Stripe permite-lhe aceitar pagamentos online através de cartão de crédito, Wallet digital e vários outros métodos de pagamento. Veja aqui como activá-lo:





- Introduza a **chave secreta** fornecida no painel de controlo do Stripe.
- Preencha o campo **Chave pública**, também fornecido pelo Stripe.
- Selecionar a **moeda principal**.
- Guarde a configuração e, em seguida, clique em `Guardar`.



![payment-stripe](assets/fr/010.webp)



⚠️ **Observação:** É essencial conhecer o regime de IVA aplicável à sua atividade (por exemplo: venda sujeita a IVA no país do vendedor, isenção justificada ou venda à taxa de IVA do país do comprador) para configurar corretamente as opções de faturação no **be-BOP**.



## Configuração da moeda



*o *be-BOP** oferece uma gestão avançada da moeda e está adaptado a ambientes com várias moedas e a requisitos contabilísticos específicos. Para garantir a coerência das operações financeiras e dos relatórios, é essencial configurar corretamente as diferentes moedas utilizadas no sistema. Eis os passos a seguir para esta configuração:





- Selecionar a **moeda principal** (`Moeda principal`)
- Selecione `Moeda secundária
- Definir **moeda de referência** (`Moeda de referência do preço`)
- Indicar a "moeda de contabilização



Depois de todas as moedas terem sido corretamente configuradas, o software assegura a conversão automática e exacta das transacções em várias moedas, mantendo uma coerência contabilística rigorosa.



![settings-currencies](assets/fr/011.webp)



## Configuração do acesso de recuperação por correio eletrónico ou Nostr



Ainda em `/admin/settings`, através do módulo **ARM**, certifique-se de que a conta de super-administrador inclui um **email Address** ou um **recovery pub**, facilitando assim o procedimento em caso de esquecimento da palavra-passe.



![settings-users](assets/fr/012.webp)



## Definições de idioma



O software oferece uma capacidade multilingue para se adaptar a um público internacional e melhorar a experiência do utilizador. Para ativar a funcionalidade multilingue, é importante configurar as línguas disponíveis e definir uma **língua predefinida**.



![settings-languages](assets/fr/13.webp)



## Interface e configuração da identidade no be-BOP



*o *be-BOP** fornece aos designers todas as ferramentas de que necessitam para conceber um sítio Web. O primeiro passo é abrir a secção `Admin > Merch > Layout` nas configurações. Comece por configurar a **Barra de Topo**, a **Barra de Navegação** e o **Rodapé**.



### Le Top Bar



A configuração **Top Bar** permite-lhe personalizar a identidade visual do seu software, apresentando informações chave logo na primeira linha do Interface. Isto reforça o reconhecimento da marca e fornece um contexto claro para os utilizadores.



#### Etapas de configuração:





- No campo "Nome da marca", introduza o nome da sua empresa, organização ou produto. Este nome aparecerá no topo do Interface e representará a sua principal identidade visual.
- Indicar o título do sítio Web**: o título escolhido deve resumir o objetivo da plataforma. Este título pode aparecer no cabeçalho ou no separador do navegador.
- Adicionar descrição do sítio Web**: é aqui que introduz uma breve descrição da sua iniciativa. Esta descrição ajuda a contextualizar a ferramenta para os utilizadores e também pode ser utilizada para fins de SEO.



Uma vez introduzidas estas informações, a **Barra superior** apresentará uma apresentação clara, profissional e coerente da sua solução.



#### Ligações na barra superior



A secção `Links` da Barra de Topo permite-lhe adicionar atalhos para páginas importantes na sua aplicação ou em sites externos. Estas ligações são apresentadas diretamente na barra superior, oferecendo aos seus utilizadores um acesso rápido e estruturado.



#### Etapas de configuração:





- Introduzir o nome da hiperligação (Texto)**: no campo `Texto`, introduza o nome ou a etiqueta da hiperligação tal como aparecerá (por exemplo, Página inicial, Contacto, Ajuda...).
- Indicar link Address (Url)**: no campo `Url`, introduzir o Address completo da página de destino (interna ou externa).
- Adicionar outros links se necessário**: cada linha de configuração permite-lhe adicionar um link adicional utilizando os campos `Text` e `Url`.
- Guardar ligações**: quando todas as ligações tiverem sido introduzidas, clique no botão "Adicionar ligação à barra superior" para as guardar.



Esta configuração permite-lhe oferecer uma navegação clara, fluida e acessível através das diferentes secções do seu sítio Web ou de recursos complementares.



![settings-topbar](assets/fr/014.webp)



### La Nav Bar



A secção **Navbar** permite-lhe configurar o menu de navegação principal do seu be-BOP, normalmente localizado na parte lateral ou superior do Interface. Este menu guia os utilizadores para as várias páginas e funções da aplicação. A configuração do link é simples e intuitiva. Funciona da seguinte forma:





- Introduzir o nome da ligação (`Texto`)**: na linha de configuração, comece por preencher o campo `Texto`. Este corresponde ao nome da ligação apresentada na barra de navegação (exemplos: *Dashboard*, *Users*, *Settings*...).
- Introduzir o Address do link (`Url`)**: ao lado do campo `Texto`, encontra-se o campo `Url`. Neste campo, introduza o Address da página para a qual o link deve redirecionar. Pode ser uma rota interna ou uma ligação a uma página externa.
- Adicionar várias ligações, se necessário**: por baixo da primeira linha, estão disponíveis novos campos `Texto` e `Url` para adicionar tantas ligações quantas as necessárias. Cada linha representa uma ligação de navegação adicional.
- Guardar ligações**: depois de ter introduzido todos os Elements, clique no botão `Adicionar ligação à barra de navegação` para guardar e apresentar os resultados na barra de navegação.



Esta configuração permite uma estruturação eficiente do acesso a diferentes partes do software, melhorando a ergonomia e a experiência do utilizador.



![navbar](assets/fr/015.webp)



### O rodapé



A secção **Footer** permite-lhe personalizar o rodapé do seu software, acrescentando informações ou ligações úteis. Antes de configurar as ligações, comece por ativar uma opção específica:





- Ativar a exibição da etiqueta "Powered by be-BOP "**: ativar o botão `Display Powered by be-BOP` para exibir esta etiqueta no rodapé.
- Introduzir o nome da ligação (`Texto`)**: preencher o campo `Texto`, que corresponde ao texto da ligação no rodapé (exemplos: *Termos*, *Privacidade*, *Contacto*...).
- Indicar o Address da ligação (`Url`)**: no campo `Url`, introduzir o Address da página de destino (interna ou externa).
- Adicione mais ligações se necessário**: utilize as linhas adicionais para criar tantas ligações quantas desejar.
- Guardar ligações**: clique no botão "Adicionar ligação de rodapé" para guardar ligações.



![footer](assets/fr/016.webp)



### Personalização visual



**⚠️ Não se esqueça de definir os logótipos para os temas claros e escuros, bem como o favicon, através de** `Admin > Mercadorias > Imagens`.



Eis como personalizar o aspeto e a sensação do seu sítio:



#### Ir para a secção Imagens



Menu `Admin` > `Merch` > `Fotos`.



#### Adicionar uma nova imagem



Clique em "Nova imagem".



#### Selecionar um ficheiro local



Clique em `Choose Files` e, em seguida, selecione uma imagem do seu disco Hard.



#### Selecionar o ficheiro a importar



Faça duplo clique sobre a imagem a importar (logótipo claro, logótipo escuro ou favicon).



#### Nomear a imagem



Preencher o campo `Nome da imagem`.



#### Adicionar imagem



Clique em `Adicionar` para finalizar a importação.



![pictures](assets/fr/017.webp)



### Configuração da identidade do vendedor



#### Definições de identidade



Acessível através de `Administração > Identidade` (ou `Configurações > Identidade`), esta secção permite-lhe configurar as informações administrativas e jurídicas da sua empresa.



#### Informação jurídica





- Nome da empresa**: nome oficial da empresa.
- ID da empresa**: identificador legal ou número de registo (RCCM, SIRET...).



#### Negócio Address





- Rua**: Address postal (rua, número...).
- País**: país.
- Estado**: província ou região.
- Cidade**: cidade.
- Código postal**: código postal.



#### Informações de contacto





- Email**: email profissional Address.
- Telefone**: número de telefone da empresa.



#### Conta bancária





- Nome do titular da conta**: nome do titular da conta.
- Titular da conta Address**: Address do titular.
- IBAN**: Número internacional de conta bancária.
- BIC**: Código SWIFT/BIC.



![bank-account](assets/fr/019.webp)



#### Faturação





- Clique em `Preencher com as informações da loja principal` para pré-preencher os dados.
- Informação do emitente no canto superior direito**: campo para informações jurídicas/fiscais visíveis nas facturas.
- Clique em `Update` para guardar as alterações.



**Nota:** também pode introduzir informações adicionais para serem apresentadas no Invoice, de acordo com as suas necessidades.



![vat](assets/fr/019.webp)



![issuer-info](assets/fr/020.webp)



#### Loja física Address



Para quem tem uma loja física, adicione um Address completo específico em `Admin > Definições > Identidade` ou numa secção dedicada. Deste modo, poderá ser apresentado nos documentos oficiais e no rodapé, se necessário.



![seller-id](assets/fr/021.webp)



## Gestão de produtos



### Criar um novo produto



Aceder a `Administração > Mercadoria > Produtos` para acrescentar ou modificar um produto. Preencha os seguintes campos:



#### Informações de base





- Nome do produto**: nome do produto (por exemplo, *BOP T-shirt edição limitada*).
- Slug**: Identificador de URL sem espaços (por exemplo, `tshirt-bop-edition-limitee`).
- Alias** *(opcional)*: útil para uma adição rápida ao cesto através de um campo específico.



![product-config](assets/fr/028.webp)



#### Preços





- Preço Montante**: preço do produto (por exemplo, `25.00`).
- Moeda do preço**: moeda (EUR, USD, BTC, etc.).
- Produtos especiais**:
  - este é um produto gratuito.
  - este é um produto do tipo "pague o que quiser".



#### Opções de produtos





- Produto único (standalone)**: só é possível uma adição por encomenda (por exemplo, donativo, bilhete de entrada).
- Produto com variações**:
  - Não verificar `Standalone`.
  - Marcar `Produto com ligeiras variações (sem diferença de stock)`.
  - Adicionar:
    - Nome** (por exemplo, *Tamanho*),
    - Valores** (por exemplo: S, M, L, XL),
    - Diferenças de preço** se aplicável (por exemplo: `+2 USD` para XL).



![product-details](assets/fr/029.webp)



## Gestão de stocks



### Opções avançadas ao criar um produto (stock, entrega, bilhetes, etc.)



#### Produto com stock limitado



Se o seu produto não estiver disponível em quantidades ilimitadas, selecione `O produto tem um stock limitado`. Esta opção ativa o acompanhamento automático das quantidades restantes. Quando esta caixa é assinalada, aparece um campo para indicar o **estoque disponível**.



O sistema gere:





- Existências reservadas** → produtos em cabazes ainda não pagos
- Stock vendido** → produtos já comprados



**Tempo de reserva do cesto**: Quando um cliente adiciona um produto ao seu cesto, este fica "reservado" durante um período de tempo limitado. Pode modificar este tempo em: `Administração > Configuração > Reserva do carrinho` (valor em minutos)



#### Produto a ser entregue?



Marcar `O produto tem um componente físico que será enviado para o Address do cliente`. Esta opção é útil para todos os produtos a serem enviados fisicamente (livros, t-shirts, etc.)



#### Outras opções





- Bilhete**: assinalar se o produto for um bilhete para um evento
- Reserva**: verificar se se trata de uma faixa horária de reserva (por exemplo: sessão, marcação)



![product-options](assets/fr/030.webp)



### Definições de ação (em baixo)



Esta secção determina **onde** e **como** o produto pode ser visto e comprado:



| Plateforme        | Produit visible | Ajoutable au panier |
|-------------------|------------------|----------------------|
| Eshop (site public)        | ✔️              | ✔️                  |
| Retail POS (point de vente)| ✔️              | ✔️                  |
| Google Shopping            | ✔️              | ✔️                  |
| Nostr-bot (vente via bot)  | ✔️              | ✔️                  |

Marque apenas os canais que pretende utilizar.



## Criação e personalização de páginas e widgets CMS



### Páginas obrigatórias do CMS



Aceda a `Admin > Mercadoria > CMS`. Verá uma lista das páginas existentes e pode adicionar novas páginas com **Adicionar página CMS**.



As páginas CMS são importantes para:





- Informar os seus visitantes (por exemplo, termos de utilização)
- Cumprir a lei (por exemplo, política de privacidade)
- Explicar certas caraterísticas da loja (por exemplo, recolha de IP, 0% de IVA)



Pode acrescentar outras páginas, se necessário:





- Sobre nós / Quem somos
- Apoiar-nos / Donativos
- FAQ
- Contacto
- etc.



**Dica: Clique em cada ligação ou ícone para modificar o **conteúdo**, o **título** ou a **visibilidade do site** de cada página.



### Layout e gráfico Elements



Aceder a: `Admin > Mercadoria > Layout`. Pode personalizar o visual Elements do seu site:



![product-options](assets/fr/032.webp)



#### Barra superior





- Modificar ou eliminar ligações (EX: INÍCIO, SOBRE NÓS,...)
- Navegação entre as principais secções do sítio



#### Navbar (barra de navegação principal)





- Presente na área cinzenta por baixo da barra superior
- Contém acesso rápido a: `Config`, `Configurações de pagamento`, `Transação`, `Gestão de nós`, `Widgets`, etc.
- Apenas diretores



#### Rodapé





- Editável a partir de `Admin > Mercadoria > Layout`
- Contém: informações de contacto, ligações úteis, avisos legais...



#### Personalizar imagens



Ir para: `Admin > Mercadorias > Imagens`



Pode:





- Alterar o **logótipo principal**
- Modificar ou acrescentar um esquema **imagens**



#### Descrição do sítio



Também modificável em `Imagens`, permite-lhe apresentar um **resumo ou slogan** no cabeçalho ou no rodapé, consoante o tema.



**Nota:** isto permite-lhe ajustar o aspeto à sua identidade de marca (educativa, comercial ou comunitária).



### Integração de widgets em páginas CMS



Os widgets** enriquecem as suas páginas CMS com Elements dinâmicos ou visuais.



#### Criação de widgets



Ir para: `Administração > Widgets`



Exemplos de widgets disponíveis:





- Challenges**: desafios ou missões
- Etiquetas**: categorias ou palavras-chave
- Sliders**: carrosséis de imagens
- Especificações**: Tabelas de especificações
- Formulários**: formulários (contacto, feedback, etc.)
- Contagem decrescente**: temporizadores
- Galerias**: galerias de imagens
- Tabelas de classificação**: classificações dos utilizadores



![widgets](assets/fr/033.webp)



#### Integração em páginas CMS



Utilize **códigos de acesso** no conteúdo das suas páginas CMS:



| Objectif                 | Balise à insérer                      |
|--------------------------|---------------------------------------|
| Afficher un produit      | `[Product=slug?display=img-1]`        |
| Afficher une image       | `[Picture=slug width=100 height=100 fit=contain]` |
| Intégrer un slider       | `[Slider=slug?autoplay=3000]`         |
| Ajouter un challenge     | `[Challenge=slug]`                    |
| Ajouter un compte à rebours | `[Countdown=slug]`                 |
| Intégrer un formulaire   | `[Form=slug]`                         |

**Parâmetros actuais**:





- `slug`: identificador único do widget
- `display=img-1`: imagem específica do produto
- `width`, `height`, `fit`: dimensões e estilo da imagem
- autoplay=3000`: tempo em ms entre dois diapositivos



**Vantagens**:





- Fácil de inserir (copiar e colar)
- Dinâmico: qualquer modificação do widget é automaticamente reflectida
- Não é necessário um programador



## Gestão de encomendas e relatórios



### Acompanhamento da encomenda



Para ver e gerir encomendas anteriores, vá a: `Administração > Transação > Encomendas`



Aqui encontrará a **lista completa das encomendas** efectuadas no seu sítio.



![orders](assets/fr/034.webp)



#### Visualização e pesquisa



O Interface permite-lhe pesquisar e filtrar encomendas de acordo com vários critérios:





- número de ordem: número de ordem
- pseudónimo do produto: identificador ou nome do produto
- meio de pagamento": meio de pagamento utilizado (cartão, criptomoeda, etc.)
- `Email`: e-mail do cliente



Estes filtros facilitam as pesquisas rápidas e a gestão direcionada.



#### Detalhes de cada encomenda



Ao clicar numa encomenda, pode aceder a um ficheiro completo que contém:





- Produtos encomendados
- Informação ao cliente
- Entrega Address (se aplicável)
- Quaisquer notas associadas à encomenda



#### Acções possíveis sobre uma ordem



Pode:





- Confirmar a encomenda (se pendente)
- Anular uma encomenda (em caso de problema ou de pedido do cliente)
- Adicionar **rótulos** (para organização interna)
- Consultar/acrescentar **notas internas**



**Nota:** esta secção é essencial para uma boa logística e para as relações com os clientes.



### Relatórios e exportação



Para aceder às estatísticas de vendas e pagamentos:


administrador > Definições > Relatórios



![reporting](assets/fr/035.webp)



Aqui encontrará uma visão geral da sua atividade, sob a forma de **relatórios mensais e anuais**.



#### Conteúdo do relatório



Os relatórios estão divididos em secções:





- Detalhe da encomenda**: número de encomendas, estado (confirmado, cancelado, pendente), evolução
- Detalhe do produto**: produtos vendidos, quantidades, produtos populares
- Detalhe do pagamento**: montantes cobrados, repartição por método de pagamento



#### Exportação de dados



Cada secção inclui um botão **Exportar CSV**, que lhe permite:





- Descarregar dados em formato CSV
- Abra-os no Excel, no Google Sheets, etc.
- Arquivamento para uso administrativo ou contabilístico
- Utilize-os para relatórios internos



**Nota:** ideal para acompanhamento do desempenho, contabilidade e apresentações.



## Configuração do sistema de mensagens Nostr (opcional)



![nostr-config](assets/fr/036.webp)



A plataforma suporta o protocolo **Nostr** para certas funções avançadas:





- Notificações descentralizadas
- Iniciar sessão sem palavra-passe
- Administração de luz Interface



### Gerar e adicionar a chave privada do Nostr



Ir para:


admin > Gerenciamento de nós > Nostr





- Clique em **Criar nsec** se ainda não tiver um.
- O sistema pode generate-lo automaticamente.
- Em alternativa, pode utilizar uma chave existente (por exemplo, de Damus ou Amethyst).



Seguinte:





- Copiar a chave `nsec
- Adicione-o ao seu arquivo `.env.local` (ou `.env`): ```env NOSTR_PRIVATE_KEY=SuaNsecIciKey



### Funcionalidades activadas com o Nostr



Uma vez configurado, estão disponíveis várias funções:



**Notificações via Nostr**





- Enviar alertas para encomendas, pagamentos ou eventos do sistema
- Para administradores ou utilizadores



**Administração de luz Interface





- Acessível através de um cliente Nostr
- Permite uma gestão rápida e de fácil utilização em dispositivos móveis



**Ligação sem palavra-passe





- Iniciar sessão através de uma ligação segura (enviada via Nostr)
- Maior segurança e fluidez para o utilizador



## Personalização do design e do tema



Para adaptar o aspeto da sua loja à sua carta gráfica, vá a `Administração > Mercadoria > Tema`



Aqui encontra todas as opções para **criar** e **configurar** um tema personalizado.



### Criar um tema



![theme](assets/fr/037.webp)



Ao criar ou modificar um tema, o utilizador pode definir:





- Cores**: para botões, fundos, texto, ligações, etc.
- Tipos de letra**: escolha de tipos de letra para títulos, parágrafos, menus
- Estilos gráficos**: limites, margens, espaçamento, formas de blocos



### Secções personalizáveis



Cada parte do sítio pode ser ajustada de forma independente:





- Cabeçalho**: barra de navegação superior
- Corpo**: conteúdo principal
- Rodapé**: fundo da página



**Nota:** esta granularidade garante a coerência entre os visuais do sítio e a identidade da sua marca.



### Ativação do tema



Quando o tema estiver configurado:





- Clique em **Guardar**
- Activá-lo como **tema principal** da loja



**Nota:** o tema ativo é o que estará visível para os visitantes.



## Configuração de modelos de correio eletrónico



A plataforma permite-lhe personalizar as mensagens de correio eletrónico enviadas automaticamente aos utilizadores. Aceda a: `Administração > Configurações > Modelos`



![emails-templates](assets/fr/038.webp)



### Criar / editar modelos



Cada correio eletrónico (confirmação de encomenda, palavra-passe esquecida, etc.) tem:





- Assunto**: o assunto da mensagem de correio eletrónico (por exemplo, "A sua encomenda foi validada")
- Corpo HTML**: Conteúdo HTML apresentado na mensagem de correio eletrónico



**Nota:** pode inserir texto, imagens, ligações, etc., conforme necessário.



### Utilização de variáveis dinâmicas



Para tornar as mensagens electrónicas dinâmicas, insira variáveis como:





- `{orderNumber}}`: substituído pelo número de encomenda atual
- `{invoiceLink}}: ligação para o Invoice
- `{websiteLink}}: URL do seu sítio web



**Nota:** estas etiquetas são automaticamente substituídas quando enviadas.



### Dicas avançadas





- Criar mensagens de correio eletrónico **responsivas** para facilitar a leitura em dispositivos móveis
- Adicionar **botões de ação** (pagar, descarregar, acompanhar a encomenda)
- Teste os seus e-mails enviando-os a si próprio antes de os publicar



## Configuração de etiquetas e widgets específicos



### Gestão de etiquetas



As etiquetas podem ser utilizadas para estruturar e enriquecer o seu conteúdo. Para aceder a elas: `Administração > Widgets > Etiqueta`



![tags-config](assets/fr/039.webp)



### Criar uma etiqueta



Preencher os seguintes campos:





- Nome da etiqueta**: nome da etiqueta apresentada
- Slug**: identificador único (sem espaços ou acentos)
- Família de etiquetas**: agrupa etiquetas por categoria



![targsconfig](assets/fr/040.webp)



#### Famílias disponíveis:





- criadores": autores ou produtores
- retalhistas: vendedores ou pontos de venda
- `Temporal`: períodos ou datas
- eventos: eventos associados



### Campos facultativos



Estes campos podem ser utilizados para enriquecer uma etiqueta como se fosse uma página de conteúdo:





- Título
- Subtítulo
- Conteúdo curto**
- Conteúdo integral** (em francês)
- CTAs** (botões de ação)



### Utilizar etiquetas



As etiquetas podem ser:





- Atribuído a produtos
- Integrado nas páginas CMS com uma etiqueta: [Tag=slug?display=var-1]



## Configuração de ficheiros descarregáveis



Para oferecer documentos descarregáveis aos seus clientes: `Admin > Mercadoria > Ficheiros`



### Adicionar um ficheiro



1. Clique em **Novo ficheiro**


2. Informar:




   - Nome do ficheiro** (por exemplo, *Guia de instalação*)
   - Ficheiro a carregar** (PDF, imagem, Word...)



**Nota:** uma vez adicionada, a plataforma gera automaticamente uma **ligação permanente**.



### Utilizar a ligação



Esta ligação pode então ser inserida no:





- Página CMS** (como ligação de texto ou botão)
- Um **cliente de correio eletrónico** (através de um modelo)
- Uma **folha do produto** (por exemplo, descarregamento do manual)



É ideal para fornecer *manuais de utilizador, guias técnicos, fichas de produtos...* sem necessidade de alojamento externo.



## Nostr-bot



A plataforma oferece uma integração avançada com o protocolo **Nostr**, através de um bot automatizado.



Aceder a: Gestão de nós > Nostr



### Principais caraterísticas



#### Gestão de relés





- Adicionar ou remover **relays** utilizados pelo bot
- Otimizar o **alcance** e a **fiabilidade** das mensagens enviadas



#### Mensagem de introdução automática





- Ativar uma mensagem automática na **primeira interação do utilizador**
- Ideal para:
  - Apresentar o seu serviço
  - Enviar uma ligação útil (por exemplo, FAQ, contacto, encomenda)



#### Certificação do seu `npub





- Adicionar um **logo** e um **nome público**
- Ligação a um **domínio web verificado**
- Aumenta a credibilidade e o reconhecimento da sua identidade Nostr



### Casos de utilização do Nostr-bot





- Envio de **confirmações de encomenda** para si
- Resposta automática a **eventos (por exemplo, nova encomenda)**
- Criar uma **interação descentralizada com o cliente**



## Sobrecarga de etiquetas de tradução



be-BOP é multilingue (FR, EN, ES...), mas pode adaptar as traduções às suas necessidades.



Para o fazer, aceda a: `Configurações > Idioma`



### Carregamento e edição



Os ficheiros de tradução estão em JSON. Pode:





- Descarregar** ficheiros de línguas
- Alterar** textos existentes
- Adicionar** as suas próprias traduções



Ligação aos ficheiros originais:


[https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations] (https://github.com/be-BOP-io-SA/be-BOP/tree/main/src/lib/translations)



**Exemplo:** substituir `Adicionar ao carrinho` por `Ajouter au panier` ou `Acheter`.



## Trabalho em equipa e ponto de venda (POS)



### Gestão de utilizadores e direitos de acesso



#### Criar funções



Aceder a: `Administração > Definições > ARM`



Clique em **Criar uma função** para criar uma função (por exemplo, `Super Admin`, `POS`, `Ticket checker`).



Cada função contém:





- acesso de escrita**: acesso de escrita
- acesso de leitura**: acesso de leitura
- acesso proibido**: secções interditas



#### Criação de utilizadores



No mesmo menu `Admin > Definições > ARM`, adicione um utilizador com:





- login
- pseudónimo
- recuperação de correio eletrónico
- (opcional) `recovery npub` para ligação via Nostr



Atribuir uma função previamente definida.



![pos-users](assets/fr/045.webp)



Os utilizadores só de leitura** verão os menus em *italic* e não poderão modificar o conteúdo.



## Configuração do ponto de venda (POS)



### Atribuição da função POS



Para dar a um utilizador acesso ao POS, atribuir a função `Point of Sale (POS)` em: `Admin > Config > ARM`



O utilizador pode ligar-se através do URL seguro: `/pos` ou `/pos/touch`



### Caraterísticas específicas dos POS



Be-BOP oferece um Interface dedicado às vendas físicas (loja, evento, etc.).



#### Adição rápida através de um pseudónimo



Em `/cart`, um campo permite-lhe adicionar um produto:





- Através da leitura de um **código de barras** (ISBN, EAN13)
- Introduzindo um **alias de produto** manualmente



**Nota:** o produto é automaticamente adicionado ao cesto.



#### Meios de pagamento



POS suporta:





- Espécies
- Cartão de crédito
- Lightning Network (criptografia)
- Outros de acordo com a configuração



Estão disponíveis duas opções avançadas:





- Isenção de IVA**: aplicável mediante justificação (ONG, estrangeiros...)
- Desconto de oferta**: desconto excecional com comentário obrigatório



#### Visualização do lado do cliente



O URL `/pos/session` destina-se a um **ecrã secundário** (HDMI, tablet...):



Cartaz:





- Produtos em curso
- Montante total
- Modo de pagamento
- Descontos aplicados



**Nota:** o cliente segue a encomenda em direto, enquanto o vendedor a regista em `/pos`.



### Resumo do POS



| Fonction                         | Description                                             |
|----------------------------------|---------------------------------------------------------|
| Rôle POS                         | Assigné via ARM                                         |
| Interface principale             | `/pos` ou `/pos/touch`                                 |
| Affichage client (écran 2)       | `/pos/session`                                         |
| Paiement                         | Espèces, carte, Lightning, etc.                         |
| Ajout produit                    | Alias ou scan code-barres                              |
| Remises / TVA                    | Sur justification managériale obligatoire              |


Obrigado por seguir cuidadosamente este tutorial.