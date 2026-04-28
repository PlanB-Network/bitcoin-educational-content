---
name: Peach
description: Guia completo para usar o Peach e negociar bitcoins no P2P
---

![cover](assets/cover.webp)





## Introdução



As trocas peer-to-peer (P2P) sem KYC são essenciais para preservar a confidencialidade e a autonomia financeira dos utilizadores. Permitem transacções diretas entre indivíduos sem necessidade de verificação de identidade, o que é crucial para quem valoriza a privacidade. Para uma compreensão mais aprofundada dos conceitos teóricos, ver o curso BTC204:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### 1. O que é o Peach?



O Peach é uma plataforma de troca P2P que permite aos utilizadores comprar e vender bitcoins sem KYC. Oferece uma interface intuitiva e recursos de segurança avançados. Em comparação com outras soluções, como Bisq, HodlHodl e Robosat, o Peach destaca-se pela sua facilidade de utilização.


Um sistema de caução multisignatureza (2-2) garante a segurança dos fundos durante as transacções. O Peach suporta vários métodos de pagamento e possui um sistema de reputação para orientar os comerciantes nas suas acções. Como é habitual nas plataformas P2P, é importante manter uma boa reputação para manter a credibilidade junto de outros comerciantes.



### 2. Privacidade e dados recolhidos



**Que informações é que o Peach recolhe?



O Peach esforça-se por armazenar o mínimo absoluto de dados sobre os seus utilizadores. Aqui está uma visão geral dos dados armazenados nos nossos servidores:





- Um hash do seu identificador único de aplicação (AdID)
- Um hash dos seus dados de pagamento
- As suas conversas encriptadas
- Dados de transação para garantir que os utilizadores anónimos não excedem o limite de negociação (tipos de métodos de pagamento utilizados, montantes de compra e venda)
- Addresses utilizados para enviar e receber da conta de garantia
- Dados de utilização (Firebase e Google Analytics), apenas com o seu consentimento



Como lembrete, um hash é um dado tornado irreconhecível, semelhante à encriptação. Os mesmos dados produzirão sempre o mesmo hash, tornando possível detetar duplicados sem conhecer os dados originais.



*Para uma explicação mais pormenorizada sobre o hashing, siga este curso:*



https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

**Quem pode ver os meus dados de pagamento?





- Apenas a sua contraparte pode ver os seus dados de pagamento
- Os dados são transmitidos através de servidores Peach, mas são totalmente encriptados de ponta a ponta
- Em caso de litígio, os seus dados de pagamento e o histórico de conversações serão visíveis para o mediador Peach designado



## Instalação e configuração



### 1. Instalar a aplicação Peach



![Installation de Peach](assets/fr/01.webp)





- Descarregue a aplicação a partir de [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/). No iOS, terá primeiro de instalar a aplicação [testflight](https://apps.apple.com/us/app/testflight/id899247664).
- Siga as instruções de instalação no seu dispositivo.
- Durante a instalação, ser-lhe-á pedido que escolha se pretende partilhar determinados dados para melhorar a aplicação Peach. (imagem 1)
- No ecrã seguinte (imagem 2), existem duas opções:
 - Se for um novo utilizador, clique em "Novo utilizador" para criar um novo perfil
 - Se já tiver uma conta, utilize "Restaurar" para restaurar o seu perfil existente
- Se tiver um código de referência, pode introduzi-lo aqui.
- Para restaurar uma conta existente (imagem 3), é necessário :
 - O seu ficheiro de cópia de segurança
 - A palavra-passe para desencriptar este ficheiro



### 2. Visão geral dos ecrãs principais



A aplicação Peach está organizada em torno de quatro ecrãs principais acessíveis a partir da barra de navegação inferior:



![Navigation dans l'application](assets/fr/02.webp)





- Página inicial (4)** : O ecrã principal a partir do qual pode optar por comprar ou vender, criar novas transacções e aceder às ofertas disponíveis:
 - criar ofertas com os dois botões abaixo (criar compra / criar venda)
 - tirar partido das ofertas existentes criadas por outros utilizadores, utilizando os dois botões abaixo ("Comprar"/"Vender").





- Wallet (5)** : O seu wallet de bitcoin integrado que lhe permite :
 - Verificar o seu saldo
 - Receber bitcoins
 - Envoyer bitcoins (com controlo de moedas)
 - Ver o seu histórico de transacções
 - Financiamento das suas vendas





- Negociações (6)**: os seus contratos actuais e passados, em três separadores:
 - Compras em curso
 - Vendas em curso
 - O historial das suas trocas





- Definições (7)** : O hub de configuração para
 - Ver o seu perfil (reputação, distintivos, limites, etc.)
 - Gerir a segurança (cópia de segurança, pin)
 - Gerir os seus métodos de pagamento
 - Contactar o apoio
 - Alterar a língua
 - etc.



### 3. Configurar os seus métodos de pagamento



![Accès aux paramètres de paiement](assets/fr/03.webp)



Pode gerir os seus métodos de pagamento nas definições (imagem 8)



O Peach oferece pagamentos em linha e pagamentos presenciais (apenas em encontros registados).



**Pagamentos em linha



**Importante


para proteger os utilizadores, o Peach exige que a origem dos fundos corresponda à anunciada. Cabe aos comerciantes assegurarem-se de que tal é o caso, para sua própria proteção.



![Configuration des paiements en ligne](assets/fr/04.webp)



Para adicionar um método :




- No separador "online", clique em "adicionar uma moeda/método"
- Escolha a sua moeda
- Selecione o seu método de pagamento preferido



*Tipos de métodos de pagamento disponíveis:*



***Para transferências bancárias: ***




- SEPA (normal ou instantâneo)
- Preencha os seus dados bancários SEPA.



***Aceitam-se wallets em linha :***




- Várias opções disponíveis consoante o seu país (Revolut, Paypal, Wise, Strike, etc.)
- Siga as instruções para adicionar os seus dados de início de sessão



*cartão oferta utilizável:*** cartão oferta utilizável:*** cartão oferta utilizável:*** cartão oferta utilizável:*** cartão oferta utilizável:*** cartão oferta utilizável:*** cartão oferta utilizável:***




- Amazon, Steam, etc.
- Introduzir o país de emissão do cartão e outras informações necessárias



***Opções de pagamento nacionais:***


Sistemas de pagamento específicos de cada país :




- Satispay (Itália)
- MB Way (Portugal)
- Bizum (Espanha)
- Pagamentos mais rápidos (Reino Unido)
- etc.



***Para pagamentos presenciais: ***



![Configuration des paiements en personne](assets/fr/05.webp)





- Selecione "Meetup" (imagem 12)
- Em seguida, selecione o seu encontro na lista (imagem 13)



### Modo de utilização





- Pode adicionar vários métodos de pagamento
- Quanto mais métodos adicionar, maior será o leque de ofertas a que terá acesso
- Verifique a exatidão das suas informações antes de se registar
- Pode alterar ou eliminar os seus métodos de pagamento em qualquer altura



**Nota de segurança**: As suas informações de pagamento são encriptadas e só são partilhadas com o seu parceiro de troca durante uma transação, exceto em caso de litígio, em que um mediador Peach também terá acesso.



### 4. Como proteger a sua carteira



**Compreender a sua conta Peach



Uma conta Peach não tem nome de utilizador e palavra-passe. É um ficheiro armazenado localmente no seu telefone, o que significa que o Peach não precisa de armazenar os seus dados ou de conhecer a sua identidade: você está no controlo. Este ficheiro contém todos os seus dados: incluindo as 12 palavras de recuperação de bitcoin, chaves PGP, detalhes de pagamento e assim por diante. Por isso, é crucial guardar este ficheiro e protegê-lo com uma palavra-passe __robust__.



Esta abordagem garante um certo grau de confidencialidade e deixa a responsabilidade pela gestão dos dados e das cópias de segurança nas mãos do utilizador. Perder o seu telemóvel sem uma cópia de segurança significa perder o acesso à sua conta Peach e aos seus fundos.



**Crie as suas cópias de segurança






- Aceder às definições a partir do separador no canto inferior direito do ecrã inicial
- Selecione a opção "cópias de segurança" no menu de definições



![Processus de sauvegarde](assets/fr/06.webp)



Estão disponíveis dois tipos de cópia de segurança:



**Guardar ficheiro de conta (imagem 14)**




- Clique em "Criar nova cópia de segurança"
- Criar uma palavra-passe **forte** para encriptar o ficheiro de cópia de segurança
- Envie este ficheiro para um local que garanta a sua redundância em caso de perda do telemóvel.



A cópia de segurança do ficheiro restaura a sua conta Peach completa, incluindo :




- A sua carteira
- Os seus métodos de pagamento
- Dados de pagamento
- Histórico de transacções com detalhes das contrapartes e conversas com elas



**Guardar a frase de recuperação (imagem 15)**




- Siga as instruções para apresentar a sua frase de recuperação
- Escreva cuidadosamente as palavras na ordem correta
- Guarde esta cópia de segurança num local seguro, de preferência diferente do ficheiro da conta



A frase de recuperação permite-lhe recuperar :




- A sua reputação, os seus negócios
- Os seus fundos em bitcoin



Mas **NÃO** o seguinte:




- As suas conversas actuais e passadas
- Dados de pagamento
- Informações da contraparte no histórico de transacções




## Comprar e vender bitcoins



### 1.a Como comprar bitcoins: Aceitar uma oferta de venda



O primeiro reflexo de um comprador deve ser verificar as ofertas de venda que já estão financiadas com bitcoin.



![Vue des offres de vente et filtres](assets/fr/07.webp)





- No ecrã inicial, clique no botão "Comprar" (imagem 16)
- Pode então consultar uma lista de bitcoins que foram colocados no sistema de garantia e estão prontos para venda (imagem 17). Pode ver o montante, o preço (em % relativamente ao mercado KYC), os métodos de pagamento e as moedas aceites.
- Utilize filtros para classificar e ordenar as ofertas (imagem 18).
- Nota: o botão na parte inferior da página de filtros permite-lhe receber uma notificação quando for publicada uma oferta que corresponda aos seus filtros; e o botão "reiniciar", que simplesmente limpa todos os filtros (imagem 18).



![Sélection et confirmation d'achat](assets/fr/08.webp)





- Ver a oferta que lhe convém e enviar um pedido de troca (imagem 19)
- Pode efetuar vários pedidos de troca, e a primeira oferta positiva anulará os outros pedidos.
- Efetuar o pagamento pelo método acordado.


**Lembrete:** a origem dos fundos deve corresponder à que especificou quando adicionou o método de pagamento.




- Confirme o seu pagamento na aplicação assim que estiver concluído**.
- Aguardar que o vendedor receba o pagamento e declará-lo como tal (imagem 20)
- Por fim, avalie a sua experiência com o vendedor (imagem 21)



![Réception des bitcoins](assets/fr/09.webp)





- Acompanhar o estado da sua transação
- Verificar a confirmação da receção de bitcoins
- Os fundos estarão disponíveis na sua carteira Peach (imagem 22 e 23)



### 1.b Como comprar bitcoins: Criar uma oferta



Se não conseguir encontrar uma oferta de venda adequada, pode criar uma oferta de compra. Uma vez que isto não compromete qualquer bitcoin nesta fase, terá menos hipóteses de encontrar um parceiro de troca, especialmente se o seu historial e reputação forem fracos ou inexistentes. Para remediar esta situação, é importante, ao criar a oferta, *fazer uma oferta de alto valor* para motivar os vendedores a selecionar a sua oferta. Vamos continuar:



![Creation d'ordre d'achat](assets/fr/10.webp)





- No ecrã inicial, clique no botão "Criar uma oferta de compra" (imagem 24)
- Adicione um método de pagamento, se ainda não o tiver feito, e introduza as suas preferências (quantidade, prémio, etc.) (imagem 25).


A opção "instantâneo" permite-lhe aceitar automaticamente um pedido de troca.




 - Clique novamente em "criar uma oferta" para continuar
- Uma vez criado, é a vez de os vendedores virem ter consigo com um pedido de troca. Pode fechar e sair da aplicação sem preocupações.
- Pode alterar o prémio se não receber nenhum pedido. Lembre-se: um prémio mais elevado motivará os vendedores a procurarem a sua oferta (imagem 26).
- Encontrará a sua oferta no separador "Comprar", que por sua vez se encontra na janela "Exchange" (fig. 27)



![Reception d'une demande de vente, messagerie](assets/fr/11.webp)





- Quando receber um pedido de compra (fig. 28) (e se não tiver desativado a troca instantânea na fig. 25), aceite a troca depois de verificar a reputação do vendedor. Se a negociação instantânea estiver activada, salte diretamente para a imagem 29.
- O vendedor deve então colocar o bitcoin no sistema de garantia ("financiar o cofre"). (imagem 29)
- De seguida, pague ao vendedor no destino indicado na Fig. 30, através do seu sistema bancário pessoal. Não arraste o cursor "Efectuei o pagamento" até o ter feito!
- Pode comunicar com o vendedor através do sistema de mensagens (P2P encriptado). Em caso de problema, pode abrir um litígio clicando no ícone situado no canto superior direito (imagem 31). Um mediador Peach entrará então na discussão.



![Offre de vente completée](assets/fr/12.webp)





- Assim que o vendedor tiver recebido o dinheiro, comunicará o facto e o sistema de depósito de garantia libertará o bitcoin, que estará a caminho do seu wallet (por defeito, através do GroupHug, o sistema de agrupamento de transacções do Peach, que funciona uma vez por dia),
- Avalie a sua experiência com o vendedor



É isso mesmo!



**Nota para novos compradores:** os vendedores baseiam as suas transacções na reputação dos compradores e tendem a evitar ofertas de compradores sem transacções concluídas. É mais fácil, numa primeira fase, construir uma reputação aceitando ofertas de venda existentes.




### 2.a Como vender bitcoins: Criar uma venda



A forma mais rápida e fácil de vender no Peach é **criar uma oferta de venda**.



![Création d'un ordre de vente](assets/fr/13.webp)





- Na página inicial, clique em "Criar uma oferta de venda" (imagem 32)
- Configure a sua oferta, certifique-se de que insere um método de pagamento e os parâmetros corretos


pode também :




  - criar várias ofertas idênticas
  - ativar a "troca instantânea" para que o primeiro comprador que aparecer possa aceitar o contrato (sem a sua confirmação) e proceder ao pagamento.
  - escolher um endereço de reembolso
  - financiar o tronco do seu wallet Peach
- Financiar a transação enviando os bitcoins para o endereço fornecido (imagem 34)
- Aguarde a confirmação da transação. Uma vez efectuada, a sua oferta ficará visível no mercado.



![Attente du paiement](assets/fr/14.webp)





- Esperar que um comprador aceite a sua oferta. Considere a possibilidade de aumentar o prémio (%) se quiser acelerar o processo (imagem 36)
- Depois de receber um pedido de troca, verifique a reputação do comprador. Avalie por si próprio se o perfil é adequado para si e clique em "aceitar" se for o caso. (37)
- Agora é a vez de o comprador efetuar o pagamento do banco dele para o seu. Em seguida, o comprador envia-lhe o pagamento. Não hesite em contactar o comprador no chat.
- depois de verificar que os fundos foram recebidos pelo seu banco*, liberte os fundos clicando no botão "recebi o pagamento" (imagem 38). Nunca confirme a receção de um pagamento antes de verificar se o mesmo foi recebido na sua conta.
- Avaliar a transação
- Os Bitcoin são automaticamente libertados para o comprador,



Aqui está!



**Notas de segurança e dicas para uma transação bem sucedida:**




 - Observar os dados do comprador e verificar se a origem dos fundos corresponde à descrita no Peach. Se a origem dos fundos não corresponder à anunciada, ir ao Chat e abrir uma discussão (imagem 39) e devolver os fundos à sua origem.
 - Seguir as instruções do gato amarelo.
 - Responder rapidamente às mensagens da sua contraparte
 - ter cuidado com a atitude do comprador, especialmente quando se trata de um perfil com pouca experiência
 - Não hesite em recorrer ao serviço de mediação se tiver um problema



### 2.b Como vender bitcoins: fazer uma oferta



Também é possível ver e selecionar ofertas de compra. É preciso ter especial cuidado, pois é aqui que se encontra a maior parte dos burlões.



![Prendre une offre d'achat](assets/fr/15.webp)





- Na página inicial, clicar em "Vendas" (imagem 40)
- Utilize os filtros para visualizar e selecionar as ofertas mais atractivas (imagem 41)



![vérification de la réputation](assets/fr/16.webp)





- antes de solicitar uma transação, recomendamos que avalie a adequação do perfil do comprador. Pode clicar numa oferta e depois no ID do utilizador para ver o seu perfil. Por exemplo, a oferta da imagem 42 pode ser considerada "arriscada" (novo utilizador, montante relativamente elevado). O "risco" que corre ao aceitar esta oferta é simplesmente o de perder tempo, desde que não cometa o erro de libertar os bitcoins sem ter recebido o dinheiro. Pode ainda depositar os bitcoins no cofre.


A da imagem 43, por outro lado, provém de um comerciante experiente (imagem 44), sem litígios no seu historial. Trata-se, portanto, de uma oferta menos arriscada.



![Match avec vendeur](assets/fr/17.webp)





- Uma vez solicitada a oferta, se o comprador aceitar o seu pedido, a aplicação conduzi-lo-á à imagem 34, onde poderá continuar a negociação como descrito abaixo.




## Vantagens e desvantagens



### Vantagens do Peach





- Não é necessário KYC**: Preserva a confidencialidade do utilizador.
- Sem acesso aos dados bancários**: O Peach não tem acesso aos seus dados bancários ou à sua identidade.
- Interface intuitivo**: Fácil de utilizar para utilizadores intermédios.
- Código aberto** : O código-fonte é público e verificável pela comunidade.



### Desvantagens do Peach





- Liquididade limitada**: Menor volume de transacções do que as plataformas mais estabelecidas.
- Risco regulamentar** : A aplicação é gerida por uma empresa suíça. Por conseguinte, está sujeita à regulamentação suíça, que pode evoluir e, eventualmente, censurar a aplicação.



## Recursos úteis





- Vídeo explicativo francês: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Guia de início rápido: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)
- [Support telegram](t.me/peachtopeach) (cuidado com os burlões, os administradores nunca vos escreverão primeiro por mensagem privada)