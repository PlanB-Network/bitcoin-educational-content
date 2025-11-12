---
name: Servidor BTCPay
description: Aceitar pagamentos BTC sem intermediários
---

![cover](assets/cover.webp)



![video](https://youtu.be/KqsM-n-e4aY)



O BTCPay Server é um software gratuito e de código aberto criado por Nicolas Dorier que permite a aceitação de pagamentos em bitcoin sem intermediários. Concebido para oferecer autonomia e soberania financeira, instala-se no seu próprio servidor e permite uma gestão completa das transacções, desde a faturação à validação dos pagamentos on-chain ou Lightning Network, passando pela contabilidade. Integra-se facilmente em sítios de comércio eletrónico (WooComerce, Shopify, etc.) ou pode ser utilizado como terminal de pagamento para lojas físicas (*POS*).



O BTCPay Server é sem dúvida a solução mais avançada para os comerciantes que desejam aceitar bitcoin. É o software mais completo e robusto em termos de segurança, soberania e confidencialidade. Por outro lado, é também o mais complexo de instalar e manter. Existem também alternativas mais simples: algumas são totalmente custodiais, como o OpenNode, enquanto outras oferecem um compromisso interessante entre a facilidade de utilização e a soberania, como o Swiss Bitcoin Pay :



https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

O objetivo deste tutorial é guiá-lo passo a passo através da instalação, configuração e utilização do BTCPay Server, para que possa implementar uma infraestrutura de pagamento segura e independente, de acordo com a filosofia do Bitcoin.



## Caraterísticas do servidor BTCPay



As soluções centralizadas de ponto de venda Bitcoin, como *OpenNode*, por exemplo, oferecem facilidade de uso, mas dependem de uma empresa terceirizada, pois não podem ser auto-hospedadas e são, na maioria dos casos, proprietárias. Embora facilitem a criação de pagamentos, implicam comissões e expõem os seus utilizadores a mais riscos do que uma solução como o BTCPay Server, tanto em termos de custódia de fundos como de confidencialidade.



O BTCPay Server destina-se a comerciantes online ou físicos, associações e organizações sem fins lucrativos que pretendam receber donativos em bitcoins. É também uma solução ideal para proprietários e criadores de projectos que procuram apoio direto da sua comunidade.



As caraterísticas especiais do BTCPay Server incluem :




- a sua **completa autonomia**,
- a ausência de um procedimento **KYC**,
- controlo total dos fundos**,
- a **eliminação das taxas de plataforma**.



Ao tornar-se o seu próprio processador de pagamentos, elimina qualquer dependência de um terceiro centralizado entre si e os seus clientes. Pode aceitar pagamentos diretamente em bitcoins e facturas de pagamento generate. Isso garante que nem você nem sua empresa possam ser banidos por ninguém. Desempenha o papel de banco e de processador de pagamentos, sem ter de pagar comissões a um intermediário por cada transação.



As taxas de transação para **on-chain** mantêm-se, mas podem ser reduzidas utilizando a rede **Liquid** ou **Lightning**.



Para além disso :




- Interface e facturas totalmente personalizáveis;
- Suporte nativo **Tor** para uma maior confidencialidade;
- Suporte para **crowdfunding**, **POS** e **botões de pagamento**;
- Compatível com muitas moedas ;
- Bitcoin pagamentos diretos e peer-to-peer ;
- Controlo total sobre as suas chaves privadas;
- Privacidade reforçada ;
- Segurança reforçada ;
- Software auto-hospedado ;
- Suporte para **SegWit** e **Rede Lightning** ;
- Carteira interna, baseada em nós, com integração de carteiras de hardware.



## Instalar e configurar o servidor BTCPay



### Escolher o modo de alojamento



O BTCPay Server pode ser instalado de várias maneiras diferentes. Dependendo das suas necessidades e recursos, existem três opções principais:




- Servidor BTCPay alojado por um terceiro**: utiliza uma plataforma que aloja o serviço por si. É simples, mas normalmente não é gratuito.
- Servidor BTCPay auto-hospedado num servidor em nuvem** (por exemplo, através de [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) ou qualquer outro fornecedor). Esta é a solução recomendada para a maioria dos comerciantes novatos.
- BTCPay Server instalado no seu próprio hardware (localmente)** : num computador, mini-PC ou Umbrel. Este método é mais técnico, mas oferece total independência.



https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

Para um comerciante em fase de arranque, a **implantação num servidor em nuvem** é o melhor compromisso entre autonomia, simplicidade e segurança, sem ter de gerir toda a infraestrutura técnica.



O servidor BTCPay pode ser implementado rapidamente a partir de um certo número de fornecedores de alojamento. Entre eles, o **Voltage** destaca-se como uma solução de referência para os utilizadores que necessitam de uma infraestrutura **fiável**, **profissional** e **soberana**.



### Criar uma instância do servidor BTCPay em Voltage



*a *Voltage** é uma plataforma de alojamento Bitcoin e Lightning pronta a utilizar que lhe permite implementar instantaneamente o seu próprio servidor BTCPay, sem configuração complexa ou manutenção do servidor.



Visite o [sítio Web oficial da Voltage] (https://voltage.cloud).



![capture](assets/fr/03.webp)



Criar uma **conta de utilizador** com um endereço de correio eletrónico válido e uma palavra-passe forte.



![capture](assets/fr/04.webp)



Voltage oferece um **teste gratuito de 7 dias**. Note que após os 7 dias de teste gratuito, será convidado a subscrever uma assinatura fixa de **$25 por mês** para continuar a **manter os seus nós activos**.



Depois de criar a sua conta Voltage e iniciar sessão pela primeira vez, será redireccionado para a página inicial, que tem duas secções principais:




- Uma secção **Infraestrutura** para gerir os nós Lightning, Bitcoin Core, BTCPay Server e outros serviços Bitcoin na nuvem;
- e uma secção **Pagamentos** que lhe permite aceder ao API Lightning da Voltage para integrar os pagamentos Bitcoin em aplicações personalizadas.



Para implementar a sua instância **BTCPay Server**, clique em **Acesso à infraestrutura**. É aqui que pode criar, gerir e monitorizar todos os seus serviços, incluindo o seu nó Bitcoin e o servidor BTCPay.



#### Criar um grupo



Antes de poder implementar um serviço, a plataforma pedir-lhe-á para **criar um grupo**. Um **grupo** (espaço de trabalho) é um espaço de trabalho que agrupa todos os seus serviços Bitcoin e Lightning (por exemplo, um nó, um servidor BTCPay, um explorador, etc.). É um pouco como uma pasta que contém os seus vários projectos.



![capture](assets/fr/05.webp)



Para efeitos deste tutorial, o grupo que criámos chamar-se-á **Genesis**. Pode adicionar uma fotografia de perfil, se desejar. Depois de fazer isso, clique no botão **Criar**. Pode convidar outros utilizadores para se juntarem ao grupo e até alterar o nome do grupo, se desejar.



Na página inicial do grupo, aparecem várias opções:




- Nós Lightning** : para implementar um nó Lightning completo (LND) ;
- Nós principais do Bitcoin** : para lançar um nó completo do Bitcoin ;
- Servidor BTCPay** : para alojar uma instância BTCPay pronta a utilizar;
- Contas Nostr**: para gerir as identidades Nostr.



Ativar a **autenticação dupla (2FA)** para proteger a sua conta e os seus serviços (o botão é visível a vermelho se estiver desativado).



![capture](assets/fr/06.webp)



Clique em **BTCPay Server** entre as opções, depois em **Launch a BTCPay Store**.



![capture](assets/fr/07.webp)



Voltage pedir-lhe-á então para **criar e configurar a sua instância de servidor BTCPay** escolhendo um **nome de serviço** (1) e activando os pagamentos Lightning (2).



Precisará de um nó Lightning se decidir aceitar pagamentos Lightning.



Se ainda não tiver um nó Bitcoin ou Lightning, o Voltage irá sugerir-lhe que crie um automaticamente.



Clique em **Criar um nó de raio** (3) .



![capture](assets/fr/08.webp)



Uma vez na interface de criação de nós, ser-lhe-á pedido que escolha entre os layouts **padrão** e **profissional**.



Pode criar um nó real (**Mainnet**) ou um nó de teste (**Testnet**). Em seguida, clicar no botão **Continuar**.



![capture](assets/fr/09.webp)



Para este tutorial, vamos utilizar o plano padrão. Introduza o **nome do nó**, uma **palavra-passe** e prima o botão **Criar**.



![capture](assets/fr/10.webp)



Após alguns instantes, o teu nó estará operacional e poderás abrir um canal livre com uma capacidade de receção de 500.000 sats.



![capture](assets/fr/11.webp)



Um pouco mais abaixo, à direita, encontrará todas as informações necessárias sobre o seu nó!



![capture](assets/fr/12.webp)



Agora que temos o nosso nó Lightning instalado e a funcionar, vamos voltar a instalar o nosso servidor BTCPay. Agora você pode clicar no botão **Criar BTCPay**.



![capture](assets/fr/13.webp)



Será aberta uma página com os seus dados de início de sessão predefinidos, juntamente com uma mensagem que lhe pede para alterar a sua palavra-passe inicial. Depois de fazer isso, clique no botão **Login Now** para aceder à sua interface.



![capture](assets/fr/14.webp)



E pronto! Seu servidor BTCPay está pronto para ser usado. Será redireccionado diretamente para a página de login do seu servidor BTCPay.



![capture](assets/fr/15.webp)



Uma vez iniciada a sessão, configure a sua primeira **loja**:





- Dar-lhe um **nome**.





- Selecionar a **moeda por defeito** (EUR, USD, CFA, etc.).





- Selecione um **fornecedor de taxas de câmbio** (por exemplo, CoinGecko).



![capture](assets/fr/16.webp)



Será então redireccionado para o painel de controlo da sua loja. Na interface do painel de controlo, verá que o botão **Criar a sua loja** está marcado a verde, uma vez que esta etapa já foi concluída.



![capture](assets/fr/17.webp)



Um pouco mais abaixo, temos os botões **Configurar wallet** e **Configurar nó Lightning**. No nosso caso, já nos ligámos a um nó Lightning que funciona com tensão. Por isso, não precisamos de o fazer aqui.



Passemos à configuração de um portefólio. Clique no botão **Configurar um portefólio**.



Uma vez que estamos apenas a começar com o BTCPay Server, vamos ligar um wallet existente. Por isso, prima **Ligar uma carteira existente**.



![capture](assets/fr/18.webp)



De seguida, deve escolher o seu **método de importação**. Entre as opções disponíveis, selecionar **Introduzir chave pública alargada**.



![capture](assets/fr/19.webp)



Ao associar um wallet existente, pode receber os seus pagamentos **diretamente neste wallet externo**, sem que o servidor BTCPay tenha acesso à sua chave privada. Assim, mesmo que o servidor fosse hackeado ou a chave pública (`xpub`) comprometida, um atacante poderia ver o seu histórico de transacções, mas seria **impossível aceder aos seus fundos**.



Depois de clicar no botão **Enter extended public key**, será **redireccionado** para a página onde deve fornecer esta chave.



Agora vamos recuperar a **chave pública alargada**.



### Ligação de um Bitcoin wallet



Para receber os seus pagamentos, tem de ligar um Bitcoin wallet à sua loja. Para o efeito, existem várias opções:





- Carteira de hardware** (Ledger, Trezor, Coldcard...) ;





- Carteira de software** (Blockstream App, Ashigaru, Electrum, Sparrow...)





- Servidor BTCPay** interno wallet (não recomendado, pois é menos seguro e expõe mais os seus fundos em caso de pirataria do servidor).



Neste tutorial, vamos utilizar uma **carteira de software**, que é mais acessível para a configuração inicial. Pode escolher entre um certo número de aplicações compatíveis: **Electrum**, **Phoenix**, **Zeus**, **Muun**, etc.



Para a demonstração, utilizaremos o **Electrum**. Abra o **Electrum**, clique em **Portfolio** e depois em **Information** :



![capture](assets/fr/20.webp)



Em seguida, copie a **chave pública principal (xpub)**.



![capture](assets/fr/21.webp)



Depois de ter copiado a chave pública principal, cole-a no campo fornecido na página do servidor BTCPay.



![capture](assets/fr/22.webp)



Após a verificação, será redireccionado para o painel de controlo da sua loja.



![capture](assets/fr/23.webp)



### Gerar um ponto de venda (PdV)



Depois de ter configurado a sua loja e a sua carteira, pode agora configurar um **Ponto de venda (PdV)** para começar a receber pagamentos Bitcoin diretamente dos seus clientes.



Esta funcionalidade integrada do **BTCPay Server** é ideal para **comerciantes, artesãos, restauradores ou prestadores de serviços** que pretendam aceitar Bitcoin **sem um sítio Web** ou competências técnicas especiais.



### Qual é o ponto de venda?



O **PoS** é uma **interface POS simplificada** que actua como um **terminal de pagamento Bitcoin**.


Permite-lhe :




- Criar um **menu de produtos ou serviços** com preços fixos.
- Gerar uma **fatura instantânea com código QR** para digitalizar.
- Partilhar um **URL de pagamento** acessível através de smartphone, tablet ou computador.



Por outras palavras, o PoS transforma o seu servidor BTCPay numa **interface de vendas diretas**, onde cada pagamento é recebido **no seu próprio Bitcoin wallet**, sem intermediários.



### Configuração do PoS



No painel de controlo BTCPay, clique em **PLUGINS** e depois em **Point of sale**.



Em seguida, clique em **Criar uma nova aplicação PoS**. Esta ação adiciona uma **nova aplicação** à sua loja BTCPay, como se estivesse a instalar um mini site de vendas interno.



Abre-se uma página para criar a sua aplicação. Defina um **nome da aplicação**: trata-se de um nome interno, visível apenas no seu painel de controlo (por exemplo, _Shoe Shop_).



Clique em **Criar** para validar.



![capture](assets/fr/24.webp)



Uma vez criado, será redireccionado para a página **Configuração detalhada** do ponto de venda.



### Personalize a sua interface de vendas



Nesta página, pode definir os elementos essenciais do seu PdS:





- Nome da aplicação** (nome de gestão interna, pode ser alterado em qualquer altura).





- Título do ecrã** (o que os seus clientes verão no topo da página).





- Estilo de ponto de venda** (o modo **Descrição** é adequado para serviços como cortes de cabelo ou refeições, enquanto o modo **Catálogo de produtos** é ideal para lojas que oferecem vários artigos).





- Moeda de apresentação** (escolher **XOF**, **EUR** ou **USD** de acordo com os seus preços habituais).





- Lista de produtos** (adicione aqui os seus produtos, descrições e preços).



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



### Guardar e testar o seu PdS



Quando tiver terminado a configuração, clique em **Guardar** para guardar as definições e, em seguida, em **Ver** para pré-visualizar o seu PdS.



Verá uma página que apresenta os seus produtos, com cada botão a corresponder a um artigo ou serviço.



Assim que um cliente seleciona um produto :



1. BTCPay gera automaticamente uma fatura Bitcoin ou Lightning**.



2. Aparece no ecrã um **código QR**.



3. Os clientes podem **digitalizar e pagar diretamente** com o seu Bitcoin wallet.




![capture](assets/fr/27.webp)



### Resultado final



Dispõe agora de um **Ponto de Venda Bitcoin** completo que pode :





- Abrir a partir de um smartphone ou tablet na sua loja ;





- Apresentação num ecrã para o cliente digitalizar ;





- Ou partilhar através de um **URL** público, como uma página de encomenda simplificada.



Em cada pagamento, o montante é automaticamente creditado no **seu próprio BTCPay wallet**, sem intermediários ou taxas de terceiros.


Isto transforma o seu PoS num **terminal de pagamento Bitcoin autónomo**.




## Utilização quotidiana



Antes de levantar quaisquer pagamentos reais, recomendamos que efectue **um teste** para verificar se tudo está a funcionar corretamente.



### Testar um pagamento





- Crie uma fatura** a partir da sua interface PdV (por exemplo, um produto de 1 satoshi ou uma pequena quantia).





- Digitalizar o código QR no ecrã** utilizando um Bitcoin ou um Lightning wallet (como **Phoenix**, **Muun** ou **Wallet do Satoshi**).




![capture](assets/fr/28.webp)





- Valide o pagamento** no seu wallet: a transação é enviada instantaneamente.





- Regressar ao servidor BTCPay**: a fatura aparecerá como **Paga** na lista.



![capture](assets/fr/29.webp)



Parabéns! O seu ponto de venda está agora **funcional**. Pode começar a receber pagamentos Bitcoin dos seus clientes, de forma simples, rápida e sem intermediários.



### Criar uma fatura para um cliente



No menu **Facturas**, clicar em **Nova fatura**.



![capture](assets/fr/30.webp)



Introduza o **montante** e a **moeda local** (o BTCPay calcula automaticamente o equivalente em BTC), bem como outras informações sobre o produto.



![capture](assets/fr/31.webp)



Partilhar o **código QR** ou **URL** com o cliente.



![capture](assets/fr/32.webp)



### Acompanhar os pagamentos recebidos



Ainda no menu **Facturas**, verá uma lista de todas as suas transacções.


Os estados possíveis são :





- Pendente**: pagamento ainda não confirmado.





- Pago**: pagamento confirmado.





- Vencida**: fatura não paga até à data de vencimento.



### Reembolsar um cliente



No menu **Facturas**, selecionar a fatura a reembolsar.



![capture](assets/fr/33.webp)



Clique em **Refund** e introduza o endereço Bitcoin fornecido pelo cliente.



![capture](assets/fr/34.webp)



![capture](assets/fr/35.webp)



### Relatórios e exportação de dados



BTCPay Server permite-lhe **exportar as suas transacções** (em formato CSV ou Excel). Isto é muito prático para o seu acompanhamento contabilístico e de caixa registadora.



![capture](assets/fr/36.webp)



No menu **Relatórios**, clique em **Exportar**: todas as suas transacções serão guardadas num ficheiro CSV, que poderá consultar localmente.



## Segurança e boas práticas



A autonomia conferida pelo servidor BTCPay (soberania total sobre os seus fundos) é uma verdadeira força. Mas com esta liberdade vem uma maior responsabilidade em termos de segurança. Ao gerir os seus próprios pagamentos, assume o papel do seu próprio banco. É por isso que é imperativo adotar as melhores práticas para proteger os seus fundos, os seus dados e a sua infraestrutura. Eis os principais pontos a ter em conta.



### Acesso seguro ao seu servidor





- Utilize uma palavra-passe forte: combine letras maiúsculas e minúsculas, números e caracteres especiais. Evite reutilizar uma palavra-passe existente.
- Ativar a autenticação de dois factores (2FA) para aceder à sua interface BTCPay.
- Actualize regularmente o seu sistema operativo, a sua instância BTCPay Server e as suas dependências (Docker, Bitcoin node, Lightning node...). As actualizações corrigem frequentemente as vulnerabilidades de segurança.



### Gestão e cópia de segurança de chaves privadas





- Guarde as suas chaves privadas e seedphrases offline, em suportes físicos (papel ou metal).
- De preferência, utilizar um hardware wallet.
- Mantenha várias cópias das suas cópias de segurança, em locais físicos separados e protegidos.



### Pagamentos seguros e confidencialidade





- Utilize a rede Tor ou uma VPN para ocultar o endereço IP do seu servidor e proteger a sua privacidade.
- Desactive as portas desnecessárias no seu servidor e restrinja as ligações SSH apenas a endereços de confiança.
- Ativar HTTPS (certificado SSL) para todas as ligações à sua interface web BTCPay.
- Nunca partilhe a sua interface de administração com pessoal não formado em gestão de carteiras Bitcoin.



### Implementar as melhores práticas para a rede Lightning



A sua loja está ligada a um **nó Lightning alojado em Voltage**, o que simplifica consideravelmente a gestão técnica da rede. No entanto, continua a ser importante adotar **boas práticas de monitorização e segurança**:





- Guarde o login e as chaves de acesso API** do seu nó Voltage (que permitem a ligação ao BTCPay).
- Proteja a sua conta Voltage** com autenticação de dois factores e uma palavra-passe forte.
- Monitorize o estado do nó e do canal** a partir do seu painel de controlo Voltage: isto ajuda-o a detetar quaisquer anomalias ou dessincronização.
- Evite partilhar as suas credenciais API** ou expô-las publicamente (por exemplo, no código do site).
- Em caso de migração, basta **reconfigurar a ligação entre BTCPay e Voltage**: não é necessário fechar manualmente nenhum canal.



Com o Voltage, beneficia de uma infraestrutura **segura, altamente disponível** e **com cópia de segurança automática**, mantendo ao mesmo tempo a **superioridade total sobre os seus pagamentos Lightning**.



### Organizar e estruturar os procedimentos internos





- Definir uma política de gestão de acessos clara: quem pode criar uma fatura, visualizar pagamentos, aceder ao nó, etc.
- Documente os seus procedimentos de cópia de segurança e restauro para poder reagir rapidamente em caso de incidente.
- Teste regularmente o restauro das suas cópias de segurança para se certificar de que estão a funcionar corretamente.
- Formar o seu pessoal ou colaboradores em matéria de segurança operacional básica: vigilância contra phishing, utilização de palavras-passe seguras, respeito pela confidencialidade.



### Supervisionar e estabelecer a manutenção contínua





- Monitorizar continuamente a atividade do seu servidor utilizando ferramentas de registo ou de monitorização.
- Agende uma revisão periódica da segurança: verifique as actualizações, o acesso, as cópias de segurança e a consistência das transacções.



Parabéns! Chegou ao fim deste tutorial. Agora já pode familiarizar-se com o BTCPay Server, facilitando a gestão da sua loja.



Para saber mais, recomendo que faça o nosso curso de formação completo sobre a integração do Bitcoin na sua empresa:



https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a