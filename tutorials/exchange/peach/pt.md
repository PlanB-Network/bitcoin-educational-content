---
name: Pêssego
description: Guia completo para utilizar a Peach e trocar bitcoins P2P
---
![cover](assets/cover.webp)

![peach](https://youtu.be/ziwhv9KqVkM)

## Introdução

As trocas peer-to-peer (P2P) sem KYC são essenciais para preservar a confidencialidade e a autonomia financeira dos utilizadores. Permitem transacções diretas entre indivíduos sem necessidade de verificação de identidade, o que é crucial para quem valoriza a privacidade. Para uma compreensão mais aprofundada dos conceitos teóricos, consulte o curso BTC204:

https://planb.network/courses/btc204
### 1. O que é o Peach?

Peach é uma plataforma de troca P2P que permite aos utilizadores comprar e vender bitcoins sem KYC. Ele oferece uma interface intuitiva e recursos avançados de segurança. Em comparação com outras soluções como Bisq, HodlHodl e Robosat, Peach se destaca por sua facilidade de uso e taxas baixas.

### 2. Privacidade e recolha de dados

**Que informações é que a Peach recolhe?

A Peach esforça-se por armazenar o mínimo absoluto de dados sobre os seus utilizadores. Aqui está uma visão geral dos dados armazenados nos seus servidores:


- Um hash do seu identificador único de aplicação (AdID)
- Um hash dos seus dados de pagamento
- As suas conversas encriptadas
- Dados de transação para garantir que os utilizadores anónimos não excedem o limite de negociação (tipos de métodos de pagamento utilizados, montantes de compra e venda)
- Endereços utilizados para enviar e receber da conta de garantia
- Dados de utilização (Firebase e Google Analytics), apenas com o seu consentimento

Para relembrar, um hash são dados que se tornam irreconhecíveis, à semelhança da encriptação. Os mesmos dados produzirão sempre o mesmo hash, tornando possível detetar duplicados sem conhecer os dados originais.

*Para mais informações sobre hashing, pode seguir este curso:*

https://planb.network/courses/cyp201
**Quem pode ver os meus dados de pagamento?


- Apenas a sua contraparte pode ver os seus dados de pagamento
- Os dados são transmitidos através de servidores Peach, mas são totalmente encriptados de ponta a ponta
- Em caso de litígio, os seus dados de pagamento e o histórico de conversações serão visíveis para o mediador Peach designado

## Instalação e configuração

### 1. Instalar a aplicação Peach

![Installation de Peach](assets/fr/01.webp)


- Descarregar a aplicação a partir de [Peach Bitcoin] (https://peachbitcoin.com/fr/quick-start/).
- Siga as instruções de instalação no seu dispositivo.
- Durante a instalação, ser-lhe-á pedido que escolha se pretende partilhar determinados dados para melhorar a aplicação Peach (imagem 1)
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


- Início** : O ecrã principal para comprar e vender bitcoins. É aqui que pode criar novas transacções e aceder às ofertas disponíveis.
- Carteira**: A sua carteira de bitcoin integrada que lhe permite :
 - Verificar o seu saldo
 - Receber bitcoins
 - Enviar bitcoins
 - Ver o seu histórico de transacções
- Transacções** : O seu centro de gestão comercial onde encontrará :
 - As suas transacções actuais
 - Um historial completo das suas trocas
 - O estado de cada transação
- Definições** : O centro de configuração da sua conta para :
 - Gerir os seus métodos de pagamento
 - Configurar as suas cópias de segurança
 - Personalizar as suas preferências
 - Acesso a ajuda e apoio

### 3. Configurar os seus métodos de pagamento

![Accès aux paramètres de paiement](assets/fr/03.webp)

Aceder aos métodos de pagamento através do separador Definições (imagem 8)

**Pagamentos em linha

![Configuration des paiements en ligne](assets/fr/04.webp)


- Clique no botão para adicionar um novo método de pagamento
- Escolha a sua moeda
- Selecione o seu método de pagamento preferido

*Tipos de métodos de pagamento disponíveis:*

***Transferências bancárias disponíveis: ***


- SEPA (normal ou instantâneo)
- Preencha os seus dados bancários SEPA

***Aceitam-se carteiras online :***


- Várias opções disponíveis consoante o seu país (Revolut, Paypal, Wise, Strike, etc.)
- Siga as instruções para adicionar os seus dados de início de sessão

***O cartão de oferta que pode ser utilizado: ***


- Amazon
- Introduzir o país de emissão do cartão e outras informações necessárias

***Opções de pagamento nacionais:***

Sistemas de pagamento específicos de cada país :


- Satispay (Itália)
- MB Way (Portugal)
- Bizum (Espanha)
- Pagamentos mais rápidos (Reino Unido)

***Pagamentos presenciais:***

![Configuration des paiements en personne](assets/fr/05.webp)


- Selecione "Meetup
- Em seguida, selecione o seu encontro na lista

### Modo de utilização


- É possível configurar vários métodos de pagamento em simultâneo
- Quanto mais métodos adicionar, maior será o leque de ofertas a que terá acesso
- Verifique se as suas informações estão corretas antes de se registar
- Pode alterar ou eliminar os seus métodos de pagamento em qualquer altura

**Nota de segurança**: As suas informações de pagamento são encriptadas e só são partilhadas com o seu parceiro de troca durante uma transação.

### 4. Como proteger a sua carteira

**Compreender a sua conta Peach

Uma conta Peach não é uma conta tradicional de início de sessão e palavra-passe. Trata-se de um ficheiro armazenado localmente no seu telemóvel, o que significa que a Peach não precisa de armazenar os seus dados nem de conhecer a sua identidade: o controlo é seu. Este ficheiro contém todos os seus dados, desde as chaves da sua carteira bitcoin até aos seus dados de pagamento.

Esta abordagem garante uma maior confidencialidade, mas também implica uma maior responsabilidade. Perder o telemóvel sem uma cópia de segurança significa perder o acesso à sua conta Peach e aos seus fundos. Por isso, é crucial fazer uma cópia de segurança deste ficheiro e protegê-lo com uma palavra-passe forte.

**Crie as suas cópias de segurança

![Accéder aux sauvegardes](assets/fr/13.webp)


- Aceder às definições a partir do separador no canto inferior direito do ecrã inicial
- Selecione a opção "cópias de segurança" no menu de definições

![Processus de sauvegarde](assets/fr/06.webp)

Estão disponíveis dois tipos de cópia de segurança:

**Guardar ficheiro de conta (imagem 14)**


- Clique em "Criar nova cópia de segurança"
- Crie uma palavra-passe forte para encriptar o seu ficheiro de cópia de segurança
- Guardar este ficheiro num local seguro

A cópia de segurança do ficheiro restaura a sua conta Peach completa, incluindo o ficheiro :


- A sua carteira
- Os seus métodos de pagamento
- História da conversa
- Dados de pagamento
- Histórico de transacções com detalhes da contraparte

**Guardar a frase de recuperação (imagem 15)**


- Siga as instruções para apresentar a sua frase de recuperação
- Escreva cuidadosamente as palavras na ordem correta
- Guarde esta cópia de segurança num local seguro, de preferência diferente do ficheiro da conta

A frase de recuperação apenas recupera :


- Acesso à sua conta
- Os seus fundos em bitcoin

Perderá :


- História da conversa
- Dados de pagamento
- Informações da contraparte no histórico de transacções

Para uma segurança óptima, recomendamos que efectue ambos os tipos de cópia de segurança.

## Comprar e vender Bitcoins

### 1. Como comprar Bitcoins

![Création et vue des offres](assets/fr/07.webp)


- No ecrã inicial, clique no botão "Comprar" (imagem 16)
- Configure a sua compra de acordo com as suas preferências (imagem 17)
- Consultar a lista de ofertas disponíveis (imagem 18)

![Sélection et confirmation d'achat](assets/fr/08.webp)


- Selecionar a oferta mais adequada para si (imagem 19)
- Efetuar o pagamento pelo método acordado
- Confirmar o pagamento na aplicação e avaliar a transação (imagem 20)

![Réception des bitcoins](assets/fr/09.webp)


- Acompanhar o estado da sua transação
- Verificar a confirmação da receção de bitcoins
- Os fundos estarão disponíveis na sua carteira Peach

### 2. Como vender Bitcoins

![Création d'un ordre de vente](assets/fr/10.webp)


- Configure a sua oferta de venda (imagem 24)
- Financiar a transação enviando os bitcoins para o endereço fornecido (imagem 25)
- Aguardar a confirmação da transação (imagem 26)
- A sua oferta está agora visível para os compradores (imagem 27)

![Attente du paiement](assets/fr/11.webp)


- Monitorizar o estado da sua oferta
- Aguardar a confirmação do pagamento por parte do comprador
- Verificar os detalhes da transação

![Finalisation de la vente](assets/fr/12.webp)


- Verificar o estado do pagamento
- Confirmar a receção do pagamento
- Avaliar a transação
- Os bitcoins são automaticamente libertados para o comprador

**Dicas para uma transação bem sucedida


- Responder rapidamente às mensagens da sua contraparte
- Verificar cuidadosamente os dados de pagamento
- Não hesite em recorrer ao serviço de mediação se tiver um problema

**Nota de segurança**: Nunca confirme a receção de um pagamento sem ter verificado que o mesmo foi recebido na sua conta.

## Vantagens e desvantagens

### Benefícios do pêssego


- Não é necessário KYC**: Preserva a confidencialidade do utilizador.
- Sem acesso a dados bancários**: A Peach não tem acesso aos seus dados bancários ou à sua identidade.
- Interface intuitiva**: Fácil de utilizar para utilizadores intermédios.
- Código aberto** : O código-fonte é público e verificável pela comunidade.

### Desvantagens do pêssego


- Liquidez limitada**: Menor volume de transacções do que as plataformas mais estabelecidas.
- Risco regulamentar** : A aplicação é gerida por uma empresa suíça. Por conseguinte, está sujeita à regulamentação suíça, que pode evoluir e eventualmente censurar a aplicação.

## Recursos úteis


- Vídeo explicativo francês: [YouTube](https://youtu.be/ziwhv9KqVkM)
- Guia de início rápido: [Peach Bitcoin](https://peachbitcoin.com/fr/quick-start/)