---
name: Dominando o BTC Pay Server
goal: Configurar uma instância do BTC Pay Server para um negócio local
objectives:
- Compreender os fundamentos do papel do BTCPay Server no processamento de pagamentos
- Dominar o funcionamento interno do processo de configuração do BTCPay Server
- Implementar o BTCPay Server em ambientes baseados em nuvem e nós
- Tornar-se um operador de BTC Pay Server
---
# Jornada para a Soberania Financeira

A confiança é frágil, especialmente quando se trata de dinheiro. Este curso introdutório guia você através do BTCPay Server, uma ferramenta poderosa que permite aceitar pagamentos em Bitcoin sem depender de terceiros. Você aprenderá os fundamentos de se tornar um operador do BTCPay Server

Criado por Alekos e Bas, e adaptado por melontwist e asi0, este curso revela como indivíduos e empresas estão construindo alternativas aos sistemas de pagamento tradicionais. Seja você curioso sobre Bitcoin ou pronto para operar infraestruturas de pagamento para empresas, você descobrirá habilidades práticas que desafiam o status quo. Pronto para explorar como é realmente a independência financeira?
+++
# Introdução


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Visão geral do curso


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Bem-vindo ao curso POS 305 no servidor BTCPay!


O objetivo desta formação é ensinar-lhe como instalar, configurar e utilizar o BTCPay Server na sua empresa ou organização. O BTCPay Server é uma solução de código aberto que lhe permite processar pagamentos Bitcoin de forma autónoma, segura e económica. Este curso destina-se principalmente a utilizadores avançados que pretendam dominar a auto-hospedagem do BTCPay Server para integração total nas suas operações diárias.


**Secção 1: Introdução ao servidor BTCPay

Começaremos com uma apresentação geral do BTCPay Server, incluindo o ecrã de início de sessão, a gestão de contas de utilizador e a criação de uma nova loja. Esta introdução ajudá-lo-á a compreender o BTCPay Server Interface e a compreender as funcionalidades básicas necessárias para começar a utilizar esta ferramenta.


**Secção 2: Introdução à segurança das chaves Bitcoin

A segurança dos seus fundos Bitcoin é muito importante. Nesta secção, vamos explorar a geração de chaves criptográficas, o uso de carteiras de hardware para proteger essas chaves, e como interagir com as suas chaves através do BTCPay Server. Aprenderá também a configurar um BTCPay Server Lightning Wallet para otimizar as suas transacções.


**Secção 3: Servidor BTCPay Interface**

Esta parte irá guiá-lo através do utilizador do BTCPay Server Interface. Aprenderá a navegar no painel de controlo, a configurar as definições da loja e do servidor, a gerir pagamentos e a tirar partido dos plugins integrados. O objetivo é fornecer-lhe as ferramentas necessárias para personalizar a sua instalação de acordo com as suas necessidades específicas.


**Secção 4: Configuração do servidor BTCPay

Por fim, vamos nos concentrar na instalação prática do BTCPay Server em vários ambientes. Quer esteja a utilizar LunaNode, Voltage ou um nó Umbrel, aprenderá os passos essenciais para implementar e configurar o seu BTCPay Server, tendo em conta as especificidades de cada ambiente.


Pronto para dominar o BTCPay Server e fazer crescer o seu negócio? Vamos lá!


## Aclamação crítica para o Bitcoin do autor e o servidor BTCPay


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Vamos começar por entender o que é o servidor BTCPay e suas origens. Valorizamos a transparência e certos padrões para formar confiança no espaço Bitcoin.

Um projeto no espaço quebrou estes valores. O principal desenvolvedor do BTCPay Server, Nicolas Dorier, levou isso para o lado pessoal e fez a promessa de torná-los obsoletos. Aqui estamos nós, muitos anos depois, e a trabalhar para este futuro, totalmente open-source, todos os dias.


> Isto é mentira, a minha confiança em ti foi quebrada, vou tornar-te obsoleto.
> Nicolas Dorier

Depois das palavras ditas por Nicolas, era altura de começar a construir. Uma quantidade significativa de trabalho foi feita no que agora chamamos de BTCPay Server. Mais pessoas quiseram contribuir para este esforço. Os mais conhecidos são r0ckstardev, MrKukks, Pavlenex, e o primeiro comerciante a usar o software, astupidmoose.


O que significa "open source" e o que é necessário para um projeto deste tipo?


FOSS significa Free & Open-Source Software (software livre e de código aberto). O primeiro refere-se a termos que permitem a qualquer pessoa copiar, modificar e até distribuir versões (mesmo com fins lucrativos) do software. O segundo refere-se à partilha aberta do código fonte, encorajando o público a contribuir e a melhorá-lo.

Isto atrai utilizadores experientes que estão entusiasmados em contribuir para o software que já utilizam e do qual retiram valor, acabando por se revelar mais bem sucedido na adoção do que o software proprietário. É consistente com o ethos do Bitcoin de que "a informação anseia por ser livre" Reúne pessoas apaixonadas que formam uma comunidade e é simplesmente mais divertido. Tal como o Bitcoin, o FOSS é inevitável.


### Antes de começarmos


Este curso é composto por várias partes. Muitas serão tratadas pelo seu professor, ambientes de demonstração a que terá acesso, um servidor alojado para si e, possivelmente, um nome de domínio. Se concluir este curso de forma independente, tenha em atenção que os ambientes rotulados como DEMO não estarão disponíveis para si.

NB. Se seguir este curso numa sala de aula, os nomes dos servidores podem ser diferentes, dependendo da configuração da sala de aula. As variáveis nos nomes dos servidores podem ser diferentes devido a este facto.


### Estrutura do curso


Cada capítulo tem objectivos e avaliações de conhecimentos. Neste curso, abordaremos cada um deles e forneceremos um resumo das principais caraterísticas no final de cada bloco de lições (ou seja, capítulo). As ilustrações são apresentadas para fornecer feedback visual e reforçar os conceitos-chave num aspeto visual. Os objectivos são definidos no início de cada bloco de lições. Estes objectivos vão para além de uma lista de verificação. Fornecem-lhe um guia para um novo conjunto de competências. As Avaliações de Conhecimentos são progressivamente mais desafiantes, à medida que a configuração do seu Servidor BTCPay fica completa.


### O que é que os alunos recebem com o curso?


Com o curso BTCPay Server, um estudante pode compreender os princípios básicos, técnicos e não técnicos, do Bitcoin. A formação extensiva na utilização do Bitcoin através do BTCPay Server permitirá aos estudantes operar a sua própria infraestrutura Bitcoin.


### Endereços Web importantes ou oportunidades de contacto


A BTCPay Server Foundation, que permitiu que Alekos e Bas escrevessem este curso, fica em Tóquio, Japão. A fundação BTCPay Server pode ser contactada através do website listado.



- https://foundation.btcpayserver.org
- Participar nos canais de conversação oficiais: https://chat.btcpayserver.org


## Introdução ao Bitcoin


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Compreensão do Bitcoin através de exercícios na sala de aula


Este é um exercício de sala de aula, por isso, se fores tu a fazer este curso, não o podes realizar, mas podes fazer este exercício na mesma. Para realizar esta tarefa, é necessário um mínimo de 9 a 11 pessoas.


O exercício começa depois de ver a introdução "Como funciona o Bitcoin e o Blockchain" da BBC.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::


Este exercício requer um mínimo de nove participantes. Este exercício tem como objetivo proporcionar uma compreensão física do funcionamento do Bitcoin. Ao desempenhar cada papel na rede, terá uma forma interactiva e lúdica de aprender. Este exercício não envolve o Lightning Network.


### Exemplo: Necessita de 9 / 11 pessoas


Os papéis são:



- 1 Cliente
- 1 Comerciante
- 7 a 9 nós Bitcoin


**A configuração é a seguinte:**


Os clientes compram um produto na loja com Bitcoin.


**Cenário 1 - Sistema bancário tradicional



- Preparar:
  - Ver diagramas/explicação no Figjam em anexo - [Esquema da atividade](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Peça a três alunos voluntários para desempenharem os papéis de Cliente (Alice), Comerciante (Bob) e Banco.
- Representar a sequência dos acontecimentos:
  - Cliente - está a navegar na loja em linha e encontra um artigo por 25 dólares que pretende comprar e informa o comerciante de que gostaria de o fazer
  - Comerciante - pede o pagamento.
  - Cliente - envia as informações do cartão para o comerciante
  - Comerciante - envia informações ao Banco (identificando a sua própria identidade e a identidade/informação), solicitando o pagamento de
  - O banco recolhe informações sobre o cliente e o comerciante (Alice e Bob) e verifica se o saldo do cliente é suficiente.
  - Deduz \$25 da conta do Alice, adiciona \$24 à conta do Bob, recebe \$1 pelo serviço
  - O comerciante recebe um sinal de positivo do banco e envia o artigo ao cliente.
- Comentários:
  - O Bob e o Alice devem ter uma relação com um banco.
  - O banco recolhe informações de identificação sobre o Bob e o Alice.
  - O Banco sofre um corte.
  - O banco deve ser responsável pela custódia do dinheiro de cada participante em qualquer altura.


**Cenário 2 - Sistema Bitcoin



- Preparar:
  - Ver diagramas/explicação no Figjam em anexo - [Esquema da atividade](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Substituir o Banco por nove alunos que desempenharão o papel de um Computador (Bitcoin Nodos/Miners) numa rede para substituir o Banco.
- Cada um dos 9 computadores tem um registo histórico completo de todas as transacções passadas já efectuadas (portanto, saldos exactos sem falsificações), bem como um conjunto de regras:
  - Verificar se a transação está devidamente assinada (thekeyfitsthelock)
  - Difundir e receber transacções válidas para os pares na rede, rejeitar as inválidas (incluindo as que tentam gastar os mesmos fundos duas vezes)
- Atualizar/adicionar registos periodicamente com novas transacções recebidas do computador "aleatório", desde que todos os conteúdos sejam válidos (nota: ignoramos, por enquanto, a componente Proof of Work de tudo isto, para simplificar); caso contrário, rejeitamo-las e continuamos como antes, até que o próximo computador "aleatório" envie uma atualização
  - O montante correto era recompensado se o conteúdo fosse válido.
- Representar a sequência dos acontecimentos:
  - Cliente - está a navegar na loja em linha e encontra um artigo que deseja por 25 dólares e informa o comerciante que pretende comprar
  - Comerciante - solicita o pagamento enviando ao cliente um Invoice/Address a partir do seu Wallet.
  - Cliente - constrói uma transação (envio de $25 de BTC para um Address fornecido pelo Comerciante) e transmite-a para a Rede Bitcoin.
- Computadores - recebem a transação e verificam-na:
  - Há pelo menos $25 de BTC no Address a ser enviado de
  - A transação é assinada corretamente ("desbloqueada" pelo cliente)
  - Se não for o caso, a transação não será propagada através da rede e, se for o caso, propaga-se e fica em espera.
  - Os comerciantes podem verificar se a transação está pendente e em espera.
- Um computador é escolhido "aleatoriamente" para propor a finalização da transação proposta, emitindo "um bloco" que a contém; se a transação for confirmada, receberá uma recompensa em BTC.
  - OPCIONAL/ADICIONADO - em vez de selecionar um computador aleatoriamente, simular o Mining fazendo com que os computadores lancem dados até que ocorra um resultado pré-determinado (por exemplo, o primeiro a tirar dois seis é selecionado)
  - Também pode representar o que aconteceria se dois computadores ganhassem aproximadamente ao mesmo tempo, resultando numa divisão em cadeia.
  - Os computadores verificam a validade, actualizam/adicionam registos aos seus livros de registo se as regras forem cumpridas e transmitem o bloco de transacções aos pares.
  - O computador escolhido aleatoriamente recebe uma recompensa por propor um bloco válido.
  - A transação de cheques do comerciante foi finalizada; assim, os fundos foram recebidos e o artigo foi enviado ao cliente.
- Comentários:
  - Note-se que não era necessária uma relação bancária prévia.
  - Não é necessário um terceiro para facilitar; substituído por código/incentivos.
  - Não há recolha de dados por ninguém fora do Exchange direto, e apenas a quantidade necessária deve ser trocada entre os participantes (por exemplo, envio Address).
  - Não é necessária qualquer confiança entre as pessoas (para além do comerciante que envia o artigo), tal como uma compra em numerário em muitos aspectos.
  - O dinheiro é propriedade direta dos indivíduos.
  - O Bitcoin Ledger é representado em dólares para simplificar, mas, na realidade, é BTC.
  - Simulamos a difusão de uma única transação, mas, na realidade, há várias transacções pendentes na rede e os blocos incluem milhares de transacções ao mesmo tempo. Os nós também verificam se não há transacções de gasto duplo pendentes (eu descartaria todas, exceto uma, neste caso).
- Cenários de batota:
  - E se o cliente não tivesse $25 BTC?
    - Não poderiam criar a transação porque "desbloquear" e "Ownership" são a mesma coisa, e os computadores verificam se a transação está devidamente assinada; caso contrário, rejeitam-na
  - E se o computador escolhido ao acaso tentar "alterar o Ledger"?
    - O bloco seria rejeitado, uma vez que todos os outros computadores têm um historial completo e notariam a alteração, violando uma das suas regras.
    - O Random Computer não receberia uma recompensa e nenhuma transação do seu bloco seria finalizada.


## Avaliação dos conhecimentos


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### KA Debate em sala de aula


Discuta algumas simplificações excessivas feitas no exercício de sala de aula no segundo cenário e descreva o que o sistema Bitcoin real faz em mais pormenor.


### KA Revisão do vocabulário


Defina os seguintes termos-chave introduzidos na secção anterior:



- Nó
- Mempool
- Dificuldade Objetivo
- Bloco


**Discutir em grupo o significado de alguns termos adicionais:**


Blockchain, Transação, Gasto Duplo, Problema dos Generais Bizantinos, Mining, Proof of Work (PoW), Hash Função, Block reward, Blockchain, Cadeia Mais Longa, Ataque de 51%, Saída, Bloqueio de Saída, Mudança, Satoshis, Chave Pública/Privada, Address, Criptografia de Chave Pública, Assinatura Digital, Wallet


# Apresentando o servidor BTCPay


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## Compreender o ecrã de login do servidor BTCPay


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Trabalhar com o servidor BTCPay


O objetivo deste bloco de curso é obter uma compreensão geral do software BTCPay Server. Num ambiente partilhado, recomenda-se que siga a demonstração do instrutor e consulte o BTCPay Server Coursebook para acompanhar o professor. Aprenderá a criar um Wallet através de vários métodos. Os exemplos incluem configurações Hot Wallet e carteiras de hardware ligadas através do BTCPay Server Vault. Estes objectivos ocorrem no ambiente Demo, apresentado e ao qual o professor do curso dá acesso.


Se seguir este curso sozinho, pode encontrar uma lista de hosts de terceiros para fins de demonstração em https://diretory.btcpayserver.org/filter/hosts. Aconselhamos vivamente a não utilizar estas opções de terceiros como ambientes de produção; no entanto, servem o objetivo correto para introduzir a utilização do Bitcoin e do servidor BTCPay.


Como um estagiário rockstar do BTCPay Server, você pode ter experiência anterior na configuração de um nó Bitcoin. Este curso é especificamente adaptado à pilha de software do servidor BTCPay.


Muitas das opções do BTCPay Server existem, de uma forma ou de outra, noutros softwares relacionados com o Bitcoin Wallet.


### Ecrã de login do servidor BTCPay


Quando o utilizador é recebido no ambiente de demonstração, é-lhe pedido para "Iniciar sessão" ou "Criar a sua conta" Os administradores do servidor podem desativar a funcionalidade de criar novas contas por razões de segurança. Os logótipos do BTCPay Server e as cores dos botões podem ser alterados porque o BTCPay Server é um software de código aberto. Um host de terceiros pode usar uma etiqueta branca no software e mudar toda a aparência.


![image](assets/en/001.webp)


### Janela Criar uma conta


A criação de contas no servidor BTCPay requer uma sequência de e-mail Address válida; example@email.com seria uma sequência válida para e-mail.


A palavra-passe tem de ter, pelo menos, 8 caracteres, incluindo letras, números e caracteres. Depois de definir a palavra-passe uma vez, terá de verificar se a palavra-passe é a mesma que foi introduzida no primeiro campo da palavra-passe.


Quando os campos Email e Password estiverem corretamente preenchidos, clique no botão 'Create Account' (Criar conta). Isto irá guardar o e-mail e a palavra-passe na instância do servidor BTCPay do instrutor.


![image](assets/en/002.webp)


**Nota!


Se seguir este curso de forma independente, a criação desta conta será provavelmente efectuada num anfitrião de terceiros; por conseguinte, voltamos a sublinhar que estes não devem ser utilizados como ambientes de produção, mas apenas para fins de formação.


### Criação de conta pelo administrador do servidor BTCPay


O administrador da instância do servidor BTCPay também pode criar contas para o servidor BTCPay. O administrador da instância do servidor BTCPay pode clicar em "Server Settings" (1), clicar no separador "Users" (2) e clicar no botão "+ Add User" (3) no canto superior direito do separador "Users". No Objetivo (4.3), aprenderá mais sobre o controlo de administrador das contas.


![image](assets/en/003.webp)


Como administrador, precisará do e-mail Address do utilizador e definirá uma palavra-passe padrão. Recomenda-se que o Administrador informe o utilizador para alterar esta palavra-passe antes de utilizar a conta por motivos de segurança. Se o Administrador não definir uma palavra-passe e o SMTP tiver sido configurado no servidor, o utilizador receberá um e-mail com uma ligação de convite para criar a sua conta e definir uma palavra-passe.


### Exemplo


Quando seguir o curso com um instrutor, siga a ligação fornecida pelo instrutor e crie a sua conta no ambiente de demonstração. Certifique-se de que o seu e-mail Address e a sua palavra-passe estão guardados em segurança; vai precisar destas credenciais de início de sessão para os restantes objectivos de demonstração deste curso.


O seu instrutor pode ter recolhido o e-mail Address antecipadamente e enviado uma ligação de convite antes deste exercício. Se for instruído, verifique o seu correio eletrónico.


Ao fazer o curso sem um instrutor, crie sua conta usando o ambiente de demonstração do BTCPay Server; vá para


https://Mainnet.demo.btcpayserver.org/login.


Esta conta só deve ser utilizada para fins de demonstração/formação e nunca para fins comerciais.


### Resumo das competências


Nesta secção, aprendeu o seguinte:



- Como criar uma conta num servidor alojado através do Interface.
- Como um administrador do servidor pode adicionar utilizadores manualmente nas definições do servidor.


### Avaliação dos conhecimentos


#### Revisão concetual da KA


Indicar as razões pelas quais a utilização de um servidor de demonstração é uma má ideia para fins de produção.


## Gerir a(s) conta(s) de utilizador


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Gestão de contas no servidor BTCPay


Depois de o proprietário de uma loja ter criado a sua conta, pode geri-la no canto inferior esquerdo da IU do servidor BTCPay. Por baixo do botão Conta, existem várias definições de nível superior.



- Modo escuro/claro.
- Alternar entre Ocultar informações sensíveis.
- Gerir conta.


![image](assets/en/004.webp)


### Modo escuro e claro


Os utilizadores do BTCPay Server podem escolher entre uma versão de modo Claro ou Escuro do UI. As páginas viradas para o cliente não serão alteradas. Elas usam as configurações preferidas do cliente em relação ao modo claro ou escuro.


### Alternar entre ocultar informações sensíveis


O botão Hide Sensitive Info fornece um rápido e simples Layer de segurança. Sempre que precisar de operar o seu BTCPay Server, mas pode haver pessoas a espreitar por cima do seu ombro num espaço público, active Hide Sensitive Info, e todos os valores no BTCPay Server serão escondidos. Alguém poderá olhar por cima do seu ombro, mas não poderá ver os valores com que está a lidar.


### Gerir conta


Depois de a conta de utilizador ter sido criada, é aqui que pode gerir palavras-passe, 2FA ou chaves de API.


### Gerir conta - Conta


Opcionalmente, actualize a sua conta com um e-mail Address diferente. Para garantir que o seu e-mail Address está correto, o BTCPay Server permite-lhe enviar um e-mail de verificação. Clique em guardar se o utilizador definir um novo e-mail Address e confirmar que a verificação funcionou. O nome de utilizador permanece o mesmo que o e-mail anterior.


Um utilizador pode decidir apagar toda a sua conta. Para tal, basta clicar no botão Eliminar no separador Conta.


![image](assets/en/005.webp)


**Nota!


Depois de alterar o e-mail, o nome de utilizador da conta não será alterado. O e-mail Address anteriormente fornecido continuará a ser o nome de início de sessão.


### Gerir conta - Palavra-passe


Um aluno pode querer alterar a sua palavra-passe. Pode fazê-lo indo ao separador "Password" (Palavra-passe). Aqui, é-lhe pedido que escreva a sua palavra-passe antiga e pode alterá-la para uma nova.


![image](assets/en/006.webp)


### Autenticação de dois factores (2fa)


Para limitar as consequências de uma palavra-passe roubada, pode utilizar a autenticação de dois factores (2FA), um método de segurança relativamente novo. Pode ativar a autenticação de dois factores através da opção Gerir conta e do separador Autenticação de dois factores. Tem de completar um segundo passo depois de iniciar sessão com o seu nome de utilizador e palavra-passe.


O BTCPay Server suporta dois métodos para ativar o 2FA: 2FA baseado em aplicações (Authy, Google, Microsoft Authenticators) ou através de dispositivos de segurança (FIDO2 ou LNURL Auth).


### Autenticação de dois factores - baseada em aplicações


Com base no sistema operativo do seu telemóvel (Android ou iOS), os utilizadores podem escolher entre as seguintes aplicações;


1. Descarregar um autenticador de dois factores.


   - Authy para [Android](https://play.google.com/store/apps/details?id=com.authy.authy) ou [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator para [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) ou [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator para [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) ou [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Depois de descarregar e instalar a aplicação Authenticator.


   - Digitalizar o código QR fornecido pelo servidor BTCPay
   - Ou introduza manualmente a chave gerada pelo servidor BTCPay na sua aplicação Authenticator.

3. A aplicação Authenticator fornecer-lhe-á um código único. Introduza o código único no BTCPay Server para verificar a configuração e clique em verificar para concluir o processo.


![image](assets/en/007.webp)


### Resumo das competências


Nesta secção, aprendeu o seguinte:



- Opções de gestão de contas e as várias formas de gerir uma conta numa instância do BTCPay Server.
- Como configurar a 2FA baseada em aplicações.


### Avaliação dos conhecimentos


#### Revisão concetual da KA


Descreva como a 2FA baseada em aplicações ajuda a proteger a sua conta.


## Criar uma nova loja


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Criar o assistente de loja


Quando um novo utilizador inicia sessão no BTCPay Server, o ambiente está vazio e precisa de uma primeira loja. O assistente de introdução do BTCPay Server dará ao utilizador a opção de "Criar a sua loja" (1). Uma loja pode ser vista como uma casa para as suas necessidades Bitcoin. Um novo BTCPay Server Node começará por sincronizar o Bitcoin Blockchain (2). Dependendo da infraestrutura em que executa o BTCPay Server, isto pode variar de algumas horas a alguns dias. A versão atual da instância é mostrada no canto inferior direito do seu BTCPay Server UI. Isso é útil para referência ao solucionar problemas.


![image](assets/en/008.webp)


### Criar o assistente de loja


A continuação deste curso começará com um ecrã ligeiramente diferente do da página anterior. Como o seu instrutor preparou o ambiente de demonstração, o Bitcoin Blockchain foi sincronizado antes e, portanto, não verá o estado de sincronização dos nós.


Um utilizador pode decidir apagar toda a sua conta. Para tal, basta clicar no botão Eliminar no separador Conta.


![image](assets/en/009.webp)


**Nota!


As contas BTCPay Server podem criar um número ilimitado de lojas. Cada loja é um Wallet ou "casa".


### Exemplo


Comece por clicar em "Criar a sua loja".


![image](assets/en/010.webp)


Isso criará sua primeira Home e painel de controle para usar o BTCPay Server.


(1) Depois de clicar em "Create your store", o BTCPay Server pedir-lhe-á que dê um nome à loja; pode ser qualquer coisa útil para si.


![image](assets/en/011.webp)


(2) De seguida, deve ser definida uma moeda de armazenamento predefinida, uma moeda fiduciária ou uma moeda denominada em Bitcoin ou Sats. Para o ambiente de demonstração, definimo-la como USD.


![image](assets/en/012.webp)


(3) Como último parâmetro na configuração da loja, o BTCPay Server exige que você defina uma "Fonte de preço preferencial" para comparar o preço do Bitcoin com o preço fiduciário atual, para que sua loja exiba a taxa Exchange correta entre o Bitcoin e a moeda fiduciária definida pela loja. Vamos manter o padrão no exemplo de demonstração e definir isso para o Kraken Exchange. O servidor BTCPay usa a API Kraken para verificar as taxas Exchange.


![image](assets/en/013.webp)


(4) Agora que estes parâmetros da loja foram definidos, clique no botão Criar e o BTCPay Server criará o painel de controlo da sua primeira loja, onde o assistente continuará.


![image](assets/en/014.webp)


Parabéns, criou a sua primeira loja e termina assim este exercício.


![image](assets/en/015.webp)


### Resumo das competências


Nesta secção, aprendeu:



- Criação de loja e configuração de uma moeda predefinida, combinada com preferências de fonte de preços.
- Cada "Store" é uma nova casa separada de outras lojas nesta instalação do BTCPay Server.


# Introdução à segurança das chaves Bitcoin


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Compreender a geração de chaves Bitcoin


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### O que está envolvido na geração de chaves Bitcoin?


As carteiras Bitcoin, quando criadas, criam o chamado "seed". No último objetivo, criou um "seed". A série de palavras geradas anteriormente também são conhecidas como frases Mnemonic. O seed é usado para derivar chaves Bitcoin individuais e usado para enviar ou receber Bitcoin. As frases seed nunca devem ser partilhadas com terceiros ou pares não confiáveis.


A geração do seed é efectuada de acordo com a norma industrial conhecida como "Hierarchical Deterministic" (HD).


![image](assets/en/016.webp)


### Endereços


O servidor BTCPay é construído para generate um novo Address. Isso alivia o problema de reutilização de chaves públicas ou Address. Usar a mesma chave pública torna o rastreamento de todo o seu histórico de pagamentos muito fácil. Pensar nas chaves como vouchers de uso único melhoraria significativamente a sua privacidade. Também utilizamos endereços Bitcoin, não os confundir com chaves públicas.


Um Address é derivado da chave pública através de um "algoritmo de hashing" A maioria das carteiras e transacções, no entanto, mostrarão endereços em vez de chaves públicas. Endereços são, em geral, mais curtos que chaves públicas e geralmente começam com `1`, `3`, ou `bc1`, enquanto chaves públicas começam com `02`, `03`, ou `04`.



- Os endereços que começam com `1.....` ainda são muito comuns. Como mencionado no capítulo "Criar uma nova loja", estes são endereços antigos. Este tipo de Address é destinado a transacções P2PKH. O P2Pkh usa a codificação Base58, o que torna o Address sensível a maiúsculas e minúsculas. A sua estrutura é baseada na chave pública com um dígito adicional como identificador.



- Os endereços que começam com `bc1...` estão lentamente a passar para os endereços muito comuns. Estes são conhecidos como endereços SegWit (nativos). Estes oferecem uma melhor estrutura de taxas do que os outros endereços mencionados. Os endereços SegWit nativos usam a codificação Bech32 e só permitem letras minúsculas.



- Os endereços que começam por `3...` continuam a ser normalmente utilizados pelas bolsas para os endereços de depósito. Estes endereços são mencionados no capítulo "Criação de uma nova loja", endereços SegWit agrupados ou aninhados. No entanto, podem também funcionar como um "Multisig Address". Quando utilizados como um SegWit Address, há algumas poupanças nas taxas de transação, mais uma vez, menos do que o SegWit nativo. Os endereços P2SH usam a codificação Base58. Isto torna-o sensível a maiúsculas e minúsculas, tal como o Address antigo.



- Os endereços que começam com `2...` são endereços Testnet. Eles são destinados a receber Testnet Bitcoin (tBTC). Nunca se deve confundir e enviar Bitcoin para estes endereços. Para fins de desenvolvimento, você pode enviar generate para um Testnet Wallet. Existem várias torneiras online para obter Testnet Bitcoin. Nunca compre Testnet Bitcoin. O Testnet Bitcoin é extraído. Esta pode ser uma razão para um programador usar o Regtest. Este é um ambiente de playground para desenvolvedores, faltando certos componentes de rede. O Bitcoin é, no entanto, muito útil para fins de desenvolvimento.


### Chaves públicas


Atualmente, as chaves públicas são menos utilizadas na prática. Ao longo do tempo, os utilizadores do Bitcoin têm vindo a substituí-las por endereços. Ainda existem e continuam a ser utilizadas ocasionalmente. As chaves públicas são, em geral, cadeias de caracteres muito mais longas do que os endereços. Tal como acontece com os endereços, começam com um identificador específico.



- Em primeiro lugar, `02...` e `03...` são identificadores de chave pública muito comuns codificados em formato SEC. Estes podem ser processados e transformados em endereços para receção, utilizados para criar endereços multi-sig, ou para verificar uma assinatura. As primeiras transacções Bitcoin utilizavam chaves públicas como parte de transacções P2PK.



- As carteiras HD, no entanto, usam uma estrutura diferente. `xpub...`, `ypub...` ou `zpub...` são chamadas de chaves públicas estendidas, ou xpubs. Essas chaves são usadas para derivar muitas chaves públicas como parte do HD Wallet. Como o seu xpub contém os registos de todo o seu histórico, ou seja, transacções passadas e futuras, nunca as partilhe com terceiros não confiáveis.


### Resumo das competências


Nesta secção, aprendeu o seguinte:



- As diferenças entre endereços e tipos de dados de chave pública e as vantagens da utilização de endereços em vez de chaves públicas.


### Avaliação dos conhecimentos


Descreva a vantagem de utilizar endereços novos para cada transação em comparação com a reutilização do Address ou os métodos de chave pública.


## Proteção de chaves com um Hardware Wallet


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Armazenamento de chaves Bitcoin


Depois de gerar uma frase seed, a lista de 12 a 24 palavras gerada neste livro requer backups e segurança adequados, pois essas palavras são a única maneira de recuperar o acesso a um Wallet. A estrutura das carteiras HD e a forma como gera endereços de forma determinística usando um único seed significa que todos os seus endereços criados terão backup usando esta lista de palavras Mnemonic, que representa o seu seed ou frase de recuperação.


Mantenha a sua frase de recuperação segura. Se for acedida por alguém, especificamente com intenções maliciosas, essa pessoa pode movimentar os seus fundos. Manter o seed seguro e protegido, lembrando também que é mútuo entre ambos. Existem vários métodos para armazenar chaves privadas Bitcoin, cada um com as suas próprias vantagens e desvantagens, em termos de segurança, privacidade, conveniência e armazenamento físico. Devido à importância das chaves privadas, os utilizadores do Bitcoin tendem a armazenar e manter em segurança estas chaves em "custódia própria", em vez de utilizarem serviços de "custódia" como os bancos. Dependendo do utilizador, este deve utilizar uma solução de armazenamento Cold ou um Hot Wallet.


### Hot e Cold armazenamento de chaves Bitcoin


Normalmente, as carteiras Bitcoin são denominadas em Hot Wallet ou Cold Wallet. A maioria dos compromissos reside na conveniência, facilidade de utilização e riscos de segurança. Cada um destes métodos também pode ser visto numa solução de custódia. No entanto, as soluções de compromisso neste caso baseiam-se sobretudo na segurança e na privacidade e ultrapassam o âmbito deste curso.


### Hot Wallet


As carteiras Hot são a forma mais conveniente de interagir com o Bitcoin através de software móvel, web ou desktop. O Wallet está sempre ligado à Internet, permitindo aos utilizadores enviar ou receber Bitcoin. No entanto, esta é também a sua fraqueza; o Wallet, como está sempre online, é agora mais vulnerável a ataques de hackers ou malware no seu dispositivo. No BTCPay Server, as carteiras Hot armazenam as chaves privadas na instância. Qualquer pessoa que aceda à sua loja BTCPay Server pode potencialmente roubar fundos desta Address se for maliciosa. Quando o BTCPay Server é executado num ambiente alojado, deve sempre considerar isto no seu perfil de segurança e de preferência não usar um Hot Wallet nesse caso. Quando o BTCPay Server é instalado em hardware de sua propriedade e protegido por si, o perfil de risco diminui significativamente, mas nunca desaparece completamente.


### Cold Wallet


As pessoas transferem o seu Bitcoin para um Cold Wallet porque este pode isolar as chaves privadas da Internet, protegendo-as assim de potenciais ameaças online. Remover a ligação à Internet da equação reduz o risco de malware, spyware e trocas de SIM. Considera-se que o armazenamento Cold é superior ao armazenamento Hot em termos de segurança e autonomia, desde que sejam tomadas precauções adequadas para evitar a perda das chaves privadas Bitcoin. O armazenamento Cold é mais adequado para grandes quantidades de Bitcoin, que não se destinam a ser gastas frequentemente devido à complexidade da configuração do Wallet.


Existem vários métodos de armazenamento de chaves Bitcoin no armazenamento Cold, desde carteiras de papel a carteiras cerebrais, carteiras de hardware ou, desde o início, um ficheiro Wallet. A maioria das carteiras usa o BIP 39 para generate a frase seed. No entanto, no âmbito do software Bitcoin core, ainda não se chegou a um consenso sobre a sua utilização. O software Bitcoin core ainda generate um arquivo Wallet.dat, que você precisa armazenar em um local offline seguro.


### Resumo das competências


Nesta secção, aprendeu:



- As diferenças entre as carteiras Hot e Cold em termos de funcionalidade e respectivas contrapartidas.


### Avaliação de conhecimentos Revisão concetual



- O que é um Wallet?



- Qual é a diferença entre as carteiras Hot e Cold?



- Descrever o que se entende por "gerar um Wallet"?


## Utilizar as teclas do Bitcoin


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### Servidor BTCPay Wallet


O BTCPay Server é composto pelas seguintes caraterísticas padrão do Wallet:



- Transacções
- Enviar
- Receber
- Verificar novamente
- Puxar pagamentos
- Pagamentos
- PSBT
- Definições gerais


### Transacções


Os administradores podem ver as transacções de entrada e de saída para o On-Chain Wallet ligado a esta loja específica na vista das transacções. Cada transação tem uma distinção entre os montantes recebidos e enviados. As transacções recebidas serão Green e as transacções enviadas serão vermelhas. Na vista de transacções do servidor BTCPay, os administradores também verão um conjunto de etiquetas padrão.


| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app-created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

### Como enviar


A função de envio do servidor BTCPay envia transacções do seu servidor BTCPay On-Chain Wallet. BTCPay Server permite múltiplas formas de assinar as suas transacções para gastar fundos. Uma transação pode ser assinada com;



- Hardware Wallet
- Carteiras que suportam o PSBT
- Chave privada HD ou sementes de recuperação.
- Hot Wallet


#### Hardware Wallet


O BTCPay Server tem suporte integrado para Hardware Wallet, permitindo-lhe utilizar o seu Hardware Wallet com o BTCPay Vault sem fuga de informação para aplicações ou servidores de terceiros. A integração do Hardware Wallet no BTCPay Server permite-lhe importar o seu Hardware Wallet e gastar os fundos recebidos com uma simples confirmação no seu dispositivo. As suas chaves privadas nunca saem do dispositivo e todos os fundos são validados contra o seu Full node, assegurando que não há fuga de dados.


#### Assinatura com um Wallet que suporta PSBT


PSBT (Partially Signed Bitcoin Transactions) é um formato de intercâmbio para transacções Bitcoin que ainda precisam de ser totalmente assinadas. O PSBT é suportado pelo servidor BTCPay e pode ser assinado com carteiras de hardware e software compatíveis.


A construção de uma transação Bitcoin totalmente assinada passa pelas seguintes etapas:



- Um PSBT é construído com entradas e saídas específicas, mas sem assinaturas
- O PSBT exportado pode ser importado por um Wallet que suporte este formato
- Os dados da transação podem ser inspeccionados e assinados utilizando o Wallet
- O ficheiro PSBT assinado é exportado do Wallet e importado para o servidor BTCPay
- O servidor BTCPay produz a transação final Bitcoin
- Verifica o resultado e transmite-o à rede


#### Assinatura com a chave privada HD ou Mnemonic seed


Se tiver criado um Wallet antes de utilizar o servidor BTCPay, pode gastar os fundos introduzindo a sua chave privada num campo apropriado. Defina um "AccountKeyPath" correto em Wallet> Settings; caso contrário, não poderá gastar.


#### Assinatura com um Hot Wallet


Se criou um novo Wallet ao configurar a sua loja e o activou como um Hot Wallet, este utilizará automaticamente o seed armazenado num servidor para assinar.


### RBF (Replace-by-fee)


O Replace-by-fee (RBF) é uma funcionalidade do protocolo Bitcoin que lhe permite substituir uma transação anteriormente transmitida (enquanto ainda não confirmada). Isto permite aleatorizar a impressão digital da transação do seu Wallet ou substituí-la por uma taxa mais elevada para mover a transação para um nível superior na fila de prioridade de confirmação (Mining). Isto substituirá efetivamente a transação original, uma vez que a taxa de comissão mais elevada terá prioridade e, uma vez confirmada, invalidará a transação original (sem gastos duplos).


Prima o botão "Definições avançadas" para ver as opções do RBF.


![image](assets/en/017.webp)



- Randomizar para maior privacidade, permite que a transação seja substituída automaticamente para aleatorizar a impressão digital da transação.
- Sim, assinalar a transação para RBF e ser substituída explicitamente (não substituída por defeito, apenas por entrada)
- Não, não permitir que a transação seja substituída.


### Seleção Coin


A seleção Coin é uma funcionalidade avançada de melhoria da privacidade que lhe permite selecionar as moedas que pretende gastar ao efetuar uma transação. Por exemplo, pagar com moedas que acabaram de sair de uma mistura de moedas.


A seleção Coin funciona nativamente com a funcionalidade de etiquetas Wallet. Isto permite-lhe etiquetar os fundos recebidos para uma gestão e despesas mais fáceis do UTXO.


BTCPay Server suporta BIP-329 para gestão de etiquetas. Se transferir de um Wallet que suporta BIP-329 e tiver definido etiquetas, o BTCPay Server irá reconhecê-las e importá-las automaticamente. Ao migrar servidores, esta informação pode também ser exportada e importada para o novo ambiente.


### Como receber


Ao clicar no botão de receber no BTCPay Server, é gerado um Address não utilizado que pode ser usado para receber pagamentos. Os administradores também podem criar um novo Address criando um novo "Invoice"


O BTCPay Server pedir-lhe-á sempre para usar o generate no próximo Address disponível para evitar a reutilização do Address. Depois de clicar em "generate next available BTC Address", o BTCPay Server gerou um novo Address e QR. Também lhe permite definir diretamente uma etiqueta para o Address para uma melhor gestão dos seus endereços.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Re-digitalizar


A funcionalidade Rescan baseia-se no "Scantxoutset" do Bitcoin core 0.17.0 para analisar o estado atual do Blockchain (chamado UTXO Set) em busca de moedas pertencentes ao esquema de derivação configurado. Uma nova verificação do Wallet aborda dois problemas comuns que os utilizadores do servidor BTCPay encontram frequentemente.


1. Problema de limite de lacunas - A maioria das carteiras de terceiros são carteiras leves que partilham um nó entre muitos utilizadores. Carteiras leves e que dependem do Full node limitam o número (normalmente 20) de endereços sem um saldo que eles rastreiam no Blockchain para evitar problemas de desempenho. O servidor BTCPay gera um novo Address para cada Invoice. Com o acima exposto em mente, após o BTCPay Server gerar 20 facturas consecutivas não pagas, o Wallet externo pára de buscar as transacções, assumindo que não ocorreram novas transacções. O seu Wallet externo não as mostrará quando as facturas forem pagas no dia 21, 22, etc. Por outro lado, internamente, o Wallet do servidor BTCPay rastreia qualquer Address que gera, juntamente com um limite de gap significativamente maior. Não depende de terceiros e pode sempre mostrar um saldo correto.

2. A solução do limite de intervalo - Se o seu [Wallet externo/existente](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) permite a configuração do limite de intervalo, a solução fácil é aumentá-lo. No entanto, a maioria das carteiras não o permite. As únicas carteiras que atualmente suportam a configuração do gap-limit de que temos conhecimento são Electrum, Wasabi e Sparrow wallet. Infelizmente, é provável que se depare com um problema com muitas outras carteiras. Para uma melhor experiência de utilizador e privacidade, considere usar o Wallet interno do servidor BTCPay em vez de carteiras externas.


#### O servidor BTCPay usa "mempoolfullrbf=1"


BTCPay Server usa "mempoolfullrbf=1"; nós adicionamos isso como padrão para a configuração do seu BTCPay Server. No entanto, também a tornámos uma caraterística que pode ser desactivada por si. Sem "mempoolfullrbf=1", se um cliente gastar duas vezes um pagamento com uma transação que não assinale o RBF, o comerciante só saberia após a confirmação.


Um administrador pode querer excluir esta definição. Com a seguinte cadeia de caracteres, é possível alterar a predefinição.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### Definições do servidor BTCPay Wallet


As configurações do Wallet no BTCPay Server fornecem uma visão geral clara e concisa das configurações gerais do seu Wallet. Todas estas configurações são pré-preenchidas se o Wallet foi criado com o BTCPay Server.


![image](assets/en/020.webp)


As definições do Wallet no BTCPay Server fornecem uma visão clara e concisa das definições gerais do seu Wallet. Todas estas configurações são pré-preenchidas se o Wallet foi criado com o BTCPay Server. As configurações do Wallet do BTCPay Server começam com o estado do Wallet. É um Wallet Watch-only ou um Hot? Dependendo do tipo de Wallet, as acções podem variar, incluindo a nova verificação do Wallet quanto a transacções em falta, a eliminação de transacções antigas do histórico, o registo do Wallet para ligações de pagamento ou a substituição e eliminação do atual Wallet ligado à loja. Nas configurações do Wallet do BTCPay Server, os administradores podem definir uma etiqueta para o Wallet para uma melhor gestão do Wallet. Aqui, o administrador também poderá ver o esquema de derivação, a chave da conta (xpub), a impressão digital e o caminho da chave. Os pagamentos nas definições do Wallet têm apenas duas definições principais. O pagamento é inválido se a transação não for confirmada dentro de (definir minutos) após a expiração do Invoice. Considerar o Invoice confirmado quando a transação de pagamento tiver um número X de confirmações. Os administradores também podem definir uma opção para apresentar as taxas recomendadas no ecrã de pagamento ou definir um objetivo de confirmação manual no número de blocos.


![image](assets/en/021.webp)


**Nota!


Se seguir este curso de forma independente, a criação desta conta será provavelmente efectuada num anfitrião de terceiros. Por conseguinte, sugerimos novamente que estes não devem ser utilizados como ambientes de produção, mas apenas para fins de formação.


### Exemplo


#### Configurar um Bitcoin Wallet no servidor BTCPay


O BTCPay Server oferece dois métodos para configurar um Wallet. Uma maneira é importar um Bitcoin Wallet existente. A importação pode ser feita ligando um Hardware Wallet, importando um ficheiro Wallet, introduzindo uma chave pública alargada, digitalizando o código QR de um Wallet ou, o que é menos favorável, introduzindo manualmente um Wallet recovery seed previamente criado. No BTCPay Server, também é possível criar um novo Wallet. Existem duas formas possíveis de configurar o BTCPay Server ao gerar um novo Wallet.


A opção Hot Wallet no BTCPay Server permite caraterísticas como 'PayJoin' ou 'Liquid'. Existe, no entanto, uma desvantagem: o seed de recuperação gerado para este Wallet será armazenado no servidor, onde qualquer pessoa com controlo administrativo o poderá obter. Como a sua chave privada é derivada do seu seed de recuperação, um agente malicioso pode obter acesso aos seus fundos actuais e futuros!


Para mitigar esse risco no servidor BTCPay, um administrador pode definir o valor em Configurações do servidor > Políticas > "Permitir que não administradores criem carteiras Hot para suas lojas" para "não", pois é o valor padrão. Para aumentar a segurança dessas carteiras Hot, o administrador do servidor deve ativar a autenticação 2FA nas contas que têm permissão para ter carteiras Hot. O armazenamento de chaves privadas num servidor público é uma prática perigosa e acarreta riscos significativos. Alguns deles são semelhantes aos riscos do Lightning Network (consulte o próximo capítulo sobre os riscos do Lightning Network).


A segunda opção que o BTCPay Server oferece para gerar um novo Wallet é criando um Watch-only wallet. O BTCPay Server irá generate suas chaves privadas uma vez. Depois de o utilizador confirmar que escreveu a sua frase seed, o BTCPay Server irá limpar as chaves privadas do servidor. Como resultado, sua loja agora tem um Watch-only wallet conectado a ela. Para gastar os fundos recebidos em seu Watch-only wallet, veja o capítulo Como enviar, seja usando o BTCPay Server Vault, PSBT (Partially Signed Bitcoin Transaction), ou, o menos recomendado, fornecendo manualmente sua frase seed.


Criou uma nova 'Loja' na última parte. O assistente de instalação continuará a pedir para "Set up a Wallet" (Configurar um Wallet) ou "Set up a Lightning node" (Configurar um nó Lightning). Neste exemplo, seguirá o processo do assistente "Set up a Wallet" (1).


![image](assets/en/022.webp)


Depois de clicar em "Set up a Wallet", o assistente continuará solicitando como deseja continuar; BTCPay Server agora oferece a opção de conectar um Bitcoin Wallet existente à sua nova loja. Se não tiver um Wallet, BTCPay Server sugere a criação de um novo. Este exemplo seguirá os passos para "criar um novo Wallet" (2). Siga os passos para saber como "Ligar um Wallet existente" (1).


![image](assets/en/023.webp)


**Nota!


Se fizer este curso numa sala de aula, tenha em atenção que o exemplo atual e o seed que gerámos são apenas para fins educacionais. Nunca deve haver qualquer quantidade substancial para além da necessária ao longo dos exercícios sobre estes endereços.


(1) Continuar o assistente "New Wallet" clicando no botão "Create a new Wallet".


![image](assets/en/024.webp)


(2) Depois de clicar em "Criar um novo Wallet", a janela seguinte do assistente apresentará as opções "Hot Wallet" e "Watch-only wallet" Se estiver a acompanhar um instrutor, o seu ambiente é uma Demo partilhada e só pode criar um Watch-only wallet. Repare na diferença entre as duas figuras abaixo. Como está no ambiente Demo, a acompanhar o instrutor, crie um "Watch-only wallet" e continue com o assistente "Novo Wallet".


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) Continuando o assistente do novo Wallet, encontra-se agora na secção Create BTC Watch-only wallet (Criar BTC Watch-only wallet). Aqui, podemos definir o "tipo de Address" do Wallet O BTCPay Server permite-lhe escolher o seu tipo de Address preferido; no momento da redação deste curso, continua a ser recomendado o uso de endereços bech32. Pode aprender mais em detalhe sobre endereços no primeiro capítulo desta parte.



- SegWit (bech32)
  - Os endereços SegWit nativos começam por `bc1q`.
  - Exemplo: `bc1qXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- Legado
  - Os endereços herdados são endereços que começam com o número `1`.
  - Exemplo: `15e15hXXXXXXXXXXXXXXXXXXXXXXXXXX`
- Taproot (Para utilizadores avançados)
  - Os endereços Taproot começam por `bc1p`.
  - Exemplo: `bc1pXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
- SegWit embrulhado
  - Os endereços embrulhados em SegWit começam por `3`.
  - Exemplo: `37BBXXXXXXXXXXXXXXXXX`


Escolha SegWit (recomendado) como o seu tipo preferido de Wallet Address.


![image](assets/en/027.webp)


(4) Ao definir o parâmetro para o Wallet, o servidor BTCPay permite que os utilizadores definam um passphrase opcional através do BIP39; não se esqueça de confirmar a sua palavra-passe.


![image](assets/en/028.webp)


(5) Depois de definir o tipo de Wallet do Address e possivelmente definir algumas opções avançadas, clique em Criar, e o servidor BTCPay irá generate o seu novo Wallet. Note que este é o último passo antes de gerar a sua frase seed. Certifique-se de que só faz isto num ambiente onde alguém não possa roubar a frase seed olhando para o seu ecrã.


![image](assets/en/029.webp)


(6) No ecrã seguinte do assistente, BTCPay Server mostra-lhe a frase Recovery seed para o seu Wallet recentemente gerado; estas são as chaves para recuperar o seu Wallet e assinar transacções. BTCPay Server gera uma frase seed de 12 palavras. Estas palavras serão apagadas do servidor após este ecrã de configuração. Este Wallet é especificamente um Watch-only wallet. Aconselha-se a não armazenar esta frase seed digitalmente ou por imagem fotográfica. Os utilizadores só podem avançar no assistente se reconhecerem ativamente que escreveram a sua frase seed.


![image](assets/en/030.webp)


(7) Depois de clicar em Done e proteger a frase Bitcoin seed recentemente gerada, o BTCPay Server actualizará a sua loja com o novo Wallet anexado e estará pronto para receber pagamentos. No User Interface, no menu de navegação esquerdo, repare como o Bitcoin está agora destacado e ativado sob o Wallet.


![image](assets/en/031.webp)


### Exemplo: Escrever uma frase seed


Este é um momento particularmente seguro para utilizar o Bitcoin. Como mencionado anteriormente, apenas o utilizador deve ter acesso ou conhecimento da sua frase seed. Como está a acompanhar um instrutor e uma sala de aula, o seed gerado só deve ser utilizado neste curso. Demasiados factores, incluindo olhares indiscretos de colegas de turma, sistemas inseguros e outros, tornam estas chaves apenas educativas e não fiáveis. No entanto, as chaves geradas devem ser guardadas para exemplos do curso.


O primeiro método que usaremos nessa situação, que também é o menos seguro, é escrever a frase seed na ordem correta. Um cartão de frase seed está incluído no material do curso fornecido ao aluno ou pode ser encontrado no GitHub do servidor BTCPay. Vamos usar este cartão para escrever as palavras geradas no passo anterior. Certifique-se de que as escreve na ordem correta. Depois de as ter escrito, compare-as com o que foi dado pelo software para se certificar de que as escreveu na ordem correta. Depois de as ter escrito, clique na caixa de verificação que indica que escreveu corretamente a sua frase seed.


### Exemplo: Armazenamento de uma frase seed num Hardware Wallet


Neste curso, abordamos o armazenamento de uma frase seed num Hardware Wallet. Seguir este curso com um instrutor pode, por vezes, incluir um dispositivo deste género. No curso, os materiais do guia compilaram uma lista de carteiras de hardware que seriam adequadas para este exercício.


Neste exemplo, utilizaremos o cofre do servidor BTCPay e um Blockstream Jade Hardware Wallet.


Também pode seguir um guia em vídeo sobre como ligar um Hardware Wallet.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::


Descarregar o BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Certifique-se de que descarrega os ficheiros corretos para o seu sistema específico. Os utilizadores de Windows devem descarregar o pacote [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), os utilizadores de Mac devem descarregar o pacote [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), e os utilizadores de Linux devem descarregar [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


Depois de instalar o BTCPay Server Vault, inicie o software clicando no ícone no seu Ambiente de Trabalho. Quando o BTCPay Server Vault estiver corretamente instalado e for iniciado pela primeira vez, pedirá permissão para ser utilizado com aplicações Web. Pedirá para conceder acesso ao BTCPay Server específico com que trabalha. Aceite estas condições. BTCPay Server Vault irá agora procurar o dispositivo de Hardware. Assim que o dispositivo for encontrado, o BTCPay Server reconhecerá que o Vault está a ser executado e que foi buscar o seu dispositivo.


**Nota!


Não forneça as suas chaves SSH ou conta de administrador do servidor a ninguém, exceto aos administradores, quando utilizar um Hot Wallet. Qualquer pessoa com acesso a estas contas terá acesso aos fundos do Hot Wallet.


### Resumo das competências


Nesta secção, aprendeu o seguinte:



- A vista de transação do Bitcoin Wallet e as suas várias categorizações.
- Estão disponíveis várias opções para o envio a partir de um Bitcoin Wallet, desde hardware a carteiras Hot.
- O problema do limite de diferença enfrentado quando se utiliza a maioria das carteiras e como corrigi-lo.
- Como criar um novo generate Bitcoin Wallet dentro do BTCPay Server, incluindo o armazenamento das chaves num Hardware Wallet e o backup da frase de recuperação.


Neste objetivo, aprendeu como criar um novo generate Bitcoin Wallet no servidor BTCPay. Ainda não abordámos a forma de proteger ou utilizar essas chaves. Numa rápida visão geral deste objetivo, aprendeu a configurar a primeira loja. Aprendeu como criar uma frase generate Bitcoin Recovery seed.


### Avaliação de conhecimentos Revisão prática


Descrever um método de geração de chaves e um esquema para as proteger, juntamente com as compensações/riscos do esquema de segurança.


## Servidor BTCPay Relâmpago Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Quando um administrador de servidor provisiona uma nova instância do BTCPay Server, ele pode configurar uma implementação Lightning Network, como LND, Core Lightning ou Eclair; veja a Parte Configurando o BTCPay Server para instruções de instalação mais detalhadas.


Se seguido por uma sala de aula, conectar um nó Lightning ao seu servidor BTCPay funciona através de um nó personalizado. Um usuário que não seja um administrador de servidor no BTCPay Server não poderá usar o Lightning node interno por padrão. Isso é para proteger o proprietário do servidor de perder seus fundos. Os administradores do servidor podem instalar um plugin para conceder acesso ao seu Lightning node através do LNBank; isto está fora do âmbito deste livro. Para obter mais informações sobre o LNBank, consulte a página oficial do plug-in.


### Ligar o nó interno (administrador do servidor)


O Administrador do Servidor pode usar o Nó Lightning interno do BTCPay Server. Independentemente da implementação do Lightning, a conexão com o nó interno do Lightning é a mesma.


Vá para uma loja de configuração anterior e clique em "Lightning" Wallet no menu da esquerda. O BTCPay Server oferece duas possibilidades de configuração: usar o nó interno (administrador do servidor apenas por defeito) ou um nó personalizado (ligação externa). Os administradores do servidor podem clicar na opção "Usar nó interno". Não é necessário efetuar mais nenhuma configuração. Clique no botão "Guardar" e observe a notificação que indica "Nó BTC Lightning atualizado". A loja tem agora capacidades Lightning Network com êxito.


### Ligar o nó externo (utilizador do servidor/proprietário da loja)


Por defeito, os proprietários de lojas não estão autorizados a utilizar o Lightning Node do administrador do servidor. A conexão precisa ser feita a um nó externo, seja um nó de propriedade do proprietário da loja antes de configurar um servidor BTCPay, um plugin LNBank se disponibilizado pelo administrador do servidor, ou uma solução de custódia como Alby.


Aceda a uma loja previamente configurada e clique em "Lightning" por baixo das carteiras no menu da esquerda. Como os proprietários de lojas não estão autorizados a utilizar o nó interno por predefinição, esta opção está a cinzento. A utilização de um nó personalizado é a única opção disponível por defeito para os proprietários de lojas.


O servidor BTCPay requer informações de conexão; a solução pré-fabricada (ou custodiante) fornecerá essas informações especificamente adaptadas a uma implementação do Lightning. No servidor BTCPay, os proprietários de lojas podem usar as seguintes conexões;



- C-lightning via TCPouUnixdomainsocketconnection.
- Carregamento relâmpago via HTTPS
- Eclair via HTTPS
- LND através do proxy REST
- LNDhub através da API REST


![image](assets/en/032.webp)


Clique em "testar conexão" para garantir que você inseriu corretamente os detalhes da conexão. Depois que a conexão for confirmada como boa, clique em "Salvar" e o BTCPay Server mostrará que a loja está atualizada com um Lightning Node.


### Gestão do nó interno do Lightning LND (Administrador do servidor)


Depois de conectar o nó interno do Lightning, os administradores do servidor notarão novos blocos no painel especificamente para informações do Lightning.



- Equilíbrio do raio
- BTC nos canais
  - Canais de abertura do BTC
  - Saldo local BTC
  - Saldo remoto BTC
  - BTC a fechar canais
- BTC On-Chain
  - BTC confirmado
  - BTC não confirmado
  - BTC reservado
- Serviços de iluminação
  - Ride the Lightning (RTL).


Ao clicar no logótipo Ride the Lightning no mosaico "Serviços Lightning" ou em "Lightning" por baixo das carteiras no menu esquerdo, os administradores de servidores podem aceder à RTL para a gestão de nós Lightning.


**Nota!


Falha na ligação do Lightning Node interno - Se a ligação interna falhar, confirme:


1. O nó Bitcoin On-Chain está totalmente sincronizado

2. O nó do relâmpago interno está "Ativado" em "Relâmpago" > "Definições" > "Definições do relâmpago BTC"


Se você não conseguir se conectar ao seu nó Lightning, você pode tentar reiniciar o seu servidor, ou ler mais detalhes na documentação oficial do servidor BTCPay; https://docs.btcpayserver.org/Troubleshooting/. Não é possível aceitar pagamentos Lightning na sua loja até que o seu Lightning node apareça "Online". Tente testar sua conexão Lightning clicando no link "Public Node Info".


### Relâmpago Wallet


Na opção Lightning Wallet na barra de menu à esquerda, os administradores do servidor encontrarão fácil acesso ao RTL, às suas informações de nó público e às configurações do Lightning específicas da sua loja do servidor BTCPay.


#### Informação do nó interno


Os administradores do servidor podem clicar na informação do nó interno para ver o estado do servidor (Online/Offline) e a cadeia de ligação para Clearnet ou Tor.


![image](assets/en/033.webp)


#### Alterar ligação


Para alterar o nó externo do Lightning, aceda a "Definições do Lightning" e clique em "Alterar ligação" (junto a "Informação do nó público"). Isso redefine a configuração existente. Introduza os novos detalhes do nó, clique em Guardar e a loja será actualizada em conformidade.


![image](assets/en/034.webp)


#### Serviços


Se o administrador do servidor decidir instalar vários serviços para a implementação do Lightning, eles serão listados aqui. Com uma implementação padrão do LND, os administradores terão o Ride The Lightning (RTL) como uma ferramenta padrão para gerenciamento de nós.


#### Definições do BTC Lightning Wallet


Depois de adicionar o nó do Lightning à loja em uma etapa anterior, os proprietários da loja ainda podem optar por desativá-lo para sua loja usando a opção Alternar na parte superior das configurações do Lightning.


![image](assets/en/035.webp)


#### Opções de pagamento relâmpago


Os proprietários de lojas podem definir os seguintes parâmetros para melhorar a experiência do Lightning para os seus clientes.



- Exibir os montantes dos pagamentos relâmpagos em Satoshis.
- Adicionar dicas de salto para canais privados ao Lightning Invoice.
- Unificar os códigos URL/QR de pagamento On-Chain e Lightning no checkout.
- Definir um modelo de descrição para facturas relâmpago.


#### LNURL


Os proprietários de lojas podem optar por usar ou não usar o LNURL. Um URL Lightning Network, ou LNURL, é um padrão proposto para interações entre o Lightning Payer e o beneficiário. Em resumo, um LNURL é um URL codificado em bech32 prefixado com LNURL. Espera-se que o Lightning Wallet decodifique a URL, entre em contato com a URL e aguarde um objeto JSON com mais instruções, principalmente uma tag que define o comportamento do LNURL.



- Ativar LNURL
- LNURL Modo clássico
  - Para compatibilidade com o Wallet, URL codificado em Bech32 (clássico) vs URL em texto claro (futuro)
- Permitir que o beneficiário faça um comentário.


### Exemplo 1


#### Conectar-se ao Lightning com o nó interno (Administrador)


Esta opção só está disponível se for o Administrador desta instância ou se o Administrador tiver alterado as predefinições para que os utilizadores possam utilizar o nó de iluminação interno.


Como administrador, clique em Lightning Wallet na barra de menu à esquerda. O BTCPay Server pedir-lhe-á que selecione uma de duas opções para ligar um Lightning Node: um nó interno ou um nó externo personalizado. Clique em "Usar nó interno" e, em seguida, clique em "Salvar"


#### Gerenciando seu Lightning node (RTL)


Depois de se conectar ao nó interno do Lightning, o servidor BTCPay será atualizado e mostrará uma notificação "BTC Lightning node updated", confirmando que você conectou o Lightning à sua loja.


O gerenciamento do nó de iluminação é uma tarefa para o administrador do servidor. Isso envolve o seguinte:


- Gerir a transação
- Gerir a liquidez
  - Liquidez de entrada
  - Liquidez de saída
- Gerir os pares e os canais
  - Pares ligados
  - Taxas de canal
  - Estado do canal
- Fazer cópias de segurança frequentes dos estados do canal.
- Verificação dos relatórios de encaminhamento
- Em alternativa, utilize serviços como o Loop.


Toda a gestão de nós Lightning é feita como padrão com RTL (assumindo que está a correr numa implementação LND). Os administradores podem clicar no seu Lightning Wallet no BTCPay Server e encontrar um botão para abrir a RTL. O Dashboard principal do BTCPay Server está agora atualizado com os Tiles Lightning Network, incluindo o acesso rápido à RTL.


### Exemplo 2


#### Ligar ao relâmpago com a Alby


Para estabelecer uma ligação com um depositário como a Alby, os proprietários de lojas devem começar por criar uma conta e visitar https://getalby.com/


![image](assets/en/036.webp)


Depois de criar a conta Alby, aceda à sua loja BTCPay Server.


Passo 1: Clique em "Configurar um nó Lightning" no Painel de Controlo ou em "Lightning" por baixo das carteiras.


![image](assets/en/037.webp)


Passo 2: Insira as suas credenciais de ligação Wallet fornecidas pela Alby. No painel de controlo da Alby, clique em Wallet. Aqui encontrará "Wallet Connection Credentials" (Credenciais de ligação Wallet). Copie estas credenciais. Cole as credenciais da Alby no campo de configuração da ligação no servidor BTCPay.


![image](assets/en/038.webp)


Passo 3: Depois de fornecer ao servidor BTCPay os detalhes da ligação, clique no botão "Testar ligação" para garantir que a ligação está a funcionar corretamente. Repare na mensagem "Connection to lightning node successful" no topo do seu ecrã. Isto confirma que tudo está a funcionar como esperado.


![image](assets/en/039.webp)


Passo 4: Clique em "Guardar" e a sua loja está agora ligada a um nó Lightning pela Alby.


![image](assets/en/040.webp)


**Nota!


Nunca confie a uma solução Lightning de custódia mais valor do que aquele que está disposto a perder.


### Resumo das competências


Nesta secção, aprendeu:



- Como conectar um nó do Lightning interno ou externo
- O conteúdo e a função de vários mosaicos relacionados com os raios no painel de controlo
- Como configurar o Lightning Wallet usando Surto de tensão ou Alby


### Avaliação dos conhecimentos Revisão prática


Descreva algumas das várias opções para ligar um Lightning Wallet à sua loja.


# Servidor BTCPay Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Visão geral do painel de controlo


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


BTCPay Server é um pacote de software modular. No entanto, existem normas a que cada BTCPay Server deve aderir, e estas normas irão reger a interação entre o Administrador e os utilizadores. Começando com o Dashboard. O principal ponto de entrada de cada servidor BTCPay após o login. O Dashboard fornece uma visão geral do desempenho da sua loja, o saldo atual do Wallet e as transacções dos últimos 7 dias. Como é uma vista modular, os Plugins podem utilizar esta vista para seu benefício e criar os seus mosaicos no Dashboard. Para este curso, apenas discutiremos plugins e aplicações padrão, juntamente com as suas respectivas vistas, em todo o BTCPay Server.


### Mosaicos do painel de controlo


Dentro da vista principal do painel de controlo do BTCPay Server estão disponíveis alguns blocos padrão. Estes blocos foram concebidos para que o proprietário ou administrador da loja possa gerir a sua loja rapidamente numa visão geral.



- Balança Wallet
- Atividade de transação
- Saldo do Lightning (se o Lightning estiver ativado na loja)
- Serviços Lightning (se o Lightning estiver ativado na loja)
- Transacções recentes.
- Facturas recentes
- Crowdfunds activos actuais
- Desempenho da loja / artigos mais vendidos.


### Balança Wallet


O mosaico Saldo do Wallet dá uma visão geral rápida dos fundos e do desempenho do seu Wallet. Pode ser visualizado em BTC ou em moeda Fiat num gráfico semanal, mensal ou anual.


![image](assets/en/041.webp)


### Atividade de transação


Ao lado do mosaico Saldo Wallet, o BTCPay Server mostra uma rápida visão geral dos Pagamentos pendentes, o número de Transacções nos últimos 7 dias e se a sua loja emitiu algum reembolso. Clicar no botão Manage (Gerir) leva-o à gestão dos pagamentos pendentes (saiba mais sobre pagamentos no capítulo BTCPay Server - Pagamentos).


![image](assets/en/042.webp)


### Equilíbrio do raio


Isto só é visível quando o Relâmpago está ativado.


Quando o Administrador permite o acesso ao Lightning Network, o painel de controlo do BTCPay Server tem agora um novo mosaico com a informação do seu Lightning node. Quanto BTC está em canais, como isso é equilibrado localmente ou remotamente (liquidez de entrada ou saída), se os canais estão fechando ou abrindo, e quanto Bitcoin é mantido On-Chain no nó relâmpago.


![image](assets/en/043.webp)


### Serviços de iluminação


Isto só é visível quando o relâmpago está ativo.


Além de ver seu saldo Lightning no painel do BTCPay Server, os administradores também verão o bloco para Lightning Services. Aqui, os administradores podem encontrar botões rápidos para ferramentas que usam para gerenciar seu nó Lightning; por exemplo, Ride the Lightning é uma das ferramentas padrão com o BTCPay Server para gerenciamento de nó Lightning.


![image](assets/en/044.webp)


### Transacções recentes


O mosaico Transacções recentes apresenta as transacções mais recentes da sua loja. Com um clique, o Administrador da instância do Servidor BTCPay pode agora ver a última transação e ver se é necessário prestar atenção à mesma.


![image](assets/en/045.webp)


### Facturas recentes


O mosaico Recent Invoices (Facturas recentes) apresenta as 6 últimas facturas geradas pelo seu servidor BTCPay, incluindo o estado e o montante Invoice. O mosaico também inclui um botão "Ver tudo" para aceder facilmente à visão geral completa do Invoice.


![image](assets/en/046.webp)


### Ponto de venda e Crowdfunds


Como o BTCPay Server fornece um conjunto de plugins ou aplicações padrão, o Point Of Sale e o Crowdfund são os dois principais plugins do BTCPay Server. Com cada loja e Wallet, um utilizador do BTCPay Server pode generate tantos Pontos de Venda ou Crowdfunds quanto achar necessário. Cada um criará um novo painel de controlo que mostra o desempenho dos plugins.


![image](assets/en/047.webp)


Repare na ligeira diferença entre um mosaico de Ponto de venda e de Crowdfund. O Administrador vê os itens mais vendidos no mosaico Ponto de venda. No mosaico Crowdfund, isto torna-se Top Perks. Ambos os mosaicos têm botões rápidos para gerir a respectiva aplicação e ver as facturas recentes criadas pelos principais artigos ou principais vantagens.


![image](assets/en/048.webp)


**!?Nota!?**


Os gráficos de saldos e transacções recentes só estão disponíveis para os métodos de pagamento On-Chain. As informações sobre os saldos e transacções do Lightning Network estão na lista de tarefas. A partir da versão 1.6.0 do servidor BTCPay, os saldos básicos do Lightning Network estão disponíveis.


### Resumo das competências


Nesta secção, aprendeu o seguinte:



- A disposição central dos mosaicos na página de destino principal é conhecida como Painel.
- Uma compreensão básica do conteúdo de cada mosaico.


### Revisão da avaliação de conhecimentos


Enumere o maior número possível de mosaicos de memória a partir do Painel de Controlo.


## Servidor BTCPay - Definições da loja


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


Dentro do software BTCPay Server, temos conhecimento de dois tipos de configurações. Configurações específicas do BTCPay Server Store, o botão de configurações encontrado na barra de menu à esquerda abaixo do Dashboard, e configurações do BTCPay Server, encontradas na parte inferior da barra de menu, logo acima de Account. As definições específicas do servidor BTCPay só podem ser visualizadas pelos administradores do servidor.


As definições da loja são compostas por vários separadores para categorizar cada conjunto de definições.



- Geral
- Tarifas
- Aspeto do checkout
- Tokens de acesso
- Utilizadores
- Funções
- Webhooks
- Processadores de pagamentos
- Emails
- Formulários


### Geral


No separador Definições gerais, os proprietários de lojas definem a sua marca e as predefinições de pagamento. Na configuração inicial da loja, foi atribuído um nome à loja; este será refletido nas Definições gerais em Nome da loja. Aqui, o proprietário da loja também pode definir o seu sítio Web para corresponder à marca e um ID da loja para o Administrador reconhecer na base de dados.


#### Marca


Como o BTCPay Server é FOSS, o proprietário de uma loja pode fazer uma marca personalizada para combinar com a sua loja. Defina a cor da marca, guarde os logótipos da sua marca e adicione CSS personalizado para as páginas públicas/voltadas para o cliente (facturas, pedidos de pagamento, pagamentos pull)


#### Pagamento


Nas definições de pagamento, os proprietários de lojas podem definir a moeda predefinida da loja (Bitcoin ou qualquer moeda fiduciária).


#### Permitir que qualquer pessoa crie facturas


Esta configuração é destinada a desenvolvedores ou construtores em cima do BTCPay Server. Com esta configuração activada para a sua loja, permite que o mundo exterior crie facturas na sua instância do BTCPay Server.


#### Adicionar taxa adicional (taxa de rede) às facturas


Uma caraterística do BTCPay para proteger os comerciantes de ataques Dust ou os clientes de incorrerem num custo elevado em taxas mais tarde, quando o comerciante precisa de movimentar uma grande quantidade de Bitcoin de uma só vez. Por exemplo, o cliente criou um Invoice por 20$ e pagou-o parcialmente, pagando 1$ 20 vezes até o Invoice estar totalmente pago. O comerciante tem agora uma transação maior, o que aumenta o custo do Mining se o comerciante decidir movimentar esses fundos mais tarde. Por padrão, o BTCPay aplica um custo de rede adicional ao valor total do Invoice para cobrir essa despesa para o comerciante quando o Invoice é pago em várias transações. O BTCPay oferece várias opções para personalizar este recurso de proteção. É possível aplicar uma taxa de rede:



- Apenas se o cliente efetuar mais do que um pagamento para o Invoice (no exemplo acima, se o cliente criou um Invoice por 20\$ e pagou 1\$, o total de Invoice devido é agora 19\$ + a taxa de rede. A taxa de rede é aplicada após o primeiro pagamento)
- Em cada pagamento (incluindo o primeiro pagamento, no nosso exemplo, o total será de 20\$ + taxa de rede imediatamente, mesmo no primeiro pagamento)
- Nunca adicionar taxa de rede (desactiva totalmente a taxa de rede)


Embora proteja contra transacções Dust, também pode refletir-se negativamente nas empresas se não for comunicada corretamente. Os clientes podem ter perguntas adicionais e pensar que lhes está a cobrar demasiado.


#### O Invoice caduca se o montante total não tiver sido pago após?


O temporizador do Invoice está definido para 15 minutos por defeito. O temporizador serve como mecanismo de proteção contra a volatilidade, uma vez que bloqueia o montante do Bitcoin de acordo com as taxas Bitcoin-to-fiat Exchange. Se o cliente não pagar o Invoice dentro do período definido, o Invoice é considerado expirado. O Invoice é considerado "pago" assim que a transação é visível no Blockchain (com zero confirmações) e é "concluído" quando atinge o número de confirmações definido pelo comerciante (geralmente 1-6). O temporizador é personalizável por minutos.


#### Considerar o Invoice pago mesmo que o montante pago seja X% inferior ao previsto?


Quando um cliente utiliza um Exchange Wallet para pagar diretamente um Invoice, o Exchange cobra uma pequena taxa. Isto significa que esse Invoice não é considerado totalmente concluído. O Invoice é marcado como "pago parcialmente". É possível definir aqui a taxa percentual se um comerciante quiser aceitar facturas mal pagas.


### Tarifas


No BTCPay Server, quando um Invoice é gerado, ele precisa sempre do preço mais atualizado e preciso do Bitcoin-to-fiat. Ao criar uma nova loja no BTCPay Server, os administradores são convidados a definir a sua fonte de preços preferida. Depois de a loja estar configurada, os proprietários da loja podem alterar a sua fonte de preços neste separador em qualquer altura.


#### Script avançado de regras de taxas de juro


Utilizado principalmente por utilizadores avançados. Se ativado, os proprietários de lojas podem criar scripts sobre o comportamento dos preços e a forma de cobrar aos seus clientes.


#### Ensaios


Um local de teste rápido para os seus pares de moedas preferidos. Esta funcionalidade também inclui a capacidade de verificar os pares de moedas predefinidos através de uma consulta REST.


### Aspeto do checkout


O separador Checkout Appearance começa com definições específicas do Invoice e um método de pagamento predefinido, e ativa métodos de pagamento específicos quando os requisitos definidos são cumpridos.


#### Definições do Invoice


Métodos de pagamento por defeito. O BTCPay Server, na sua configuração padrão, oferece três opções.



- BTC (On-Chain)
- BTC (LNURL-pay)
- BTC (off-chain e Lightning)


Podemos definir parâmetros para a nossa loja, em que um cliente só interage com o Lightning quando o preço é inferior a X e vice-versa para as transacções On-Chain, em que quando X é superior a Y, apresenta sempre a opção de pagamento On-Chain.


![image](assets/en/049.webp)


#### Finalizar a compra


A partir da versão 1.7 do BTCPay Server, um novo Checkout Interface, Checkout V2, foi introduzido. Desde que a versão 1.9 foi padronizada, os administradores e proprietários de lojas ainda podem definir o checkout para a versão anterior. Ao usar a opção "Usar o checkout clássico", o proprietário da loja pode reverter a loja para a sua experiência de checkout anterior. O BTCPay Server também tem um conjunto selecionado de predefinições para o comércio online ou uma experiência na loja.


![image](assets/en/050.webp)


Quando um cliente interage com a loja e gera um Invoice, há um tempo de expiração para o Invoice. Por defeito, o BTCPay Server define-o para 5 minutos, mas os administradores podem ajustá-lo de acordo com a sua preferência. A página de checkout pode ainda ser personalizada através da verificação dos seguintes parâmetros:



- Celebrar o pagamento com confetes
- Mostrar o cabeçalho da loja (nome e logótipo)
- Mostrar o botão "Pagar em Wallet
- Unificar os pagamentos On-Chain e off-chain URL/QRs
- Exibir montantes de pagamentos relâmpago em Satoshis
- Deteção automática do idioma no checkout


![image](assets/en/051.webp)


Quando a Deteção automática de idioma não está definida, o BTCPay Server, por defeito, mostrará o inglês. O proprietário da loja pode alterar esta predefinição para o seu idioma preferido.


![image](assets/en/052.webp)


Clique no menu pendente e os proprietários de lojas podem definir um título HTML personalizado para ser apresentado na página de checkout.


![image](assets/en/053.webp)


Para garantir que os clientes conhecem o seu método de pagamento, o proprietário de uma loja pode definir explicitamente o seu checkout para exigir sempre que os utilizadores escolham o seu método de pagamento preferido. Assim que o Invoice é pago, o BTCPay Server permite que o cliente regresse à loja virtual. Os proprietários de lojas podem definir este redireccionamento para ser aplicado automaticamente após o pagamento do cliente.


![image](assets/en/054.webp)


#### Receção pública


Nas definições de recibos públicos, o lojista pode definir as páginas de recibos como públicas, apresentando a lista de pagamentos na página de recibos e o código QR para que o cliente possa aceder facilmente.


![image](assets/en/055.webp)


### Tokens de acesso


Os tokens de acesso são utilizados para emparelhar com determinadas integrações de comércio eletrónico ou integrações personalizadas.


![image](assets/en/056.webp)


### Utilizadores


Os utilizadores da loja são o local onde o proprietário da loja pode gerir os membros do pessoal, as suas contas e o acesso à loja. Depois de os membros da equipa criarem as suas contas, o proprietário da loja pode adicionar utilizadores específicos à loja como utilizadores convidados ou proprietários. Para definir melhor a função do funcionário, consulte a secção seguinte sobre "Definições da loja do servidor BTCPay - Funções"


![image](assets/en/057.webp)


### Funções


O titular de uma loja pode não considerar as funções padrão do utilizador suficientemente significativas. Nas definições das funções personalizadas, o lojista pode definir as necessidades exactas de cada função na sua empresa.


(1) Para criar uma nova função, clique no botão "+ Adicionar função".


![image](assets/en/058.webp)


(2) Introduzir o nome da função, por exemplo, "Caixa".


![image](assets/en/059.webp)


(3) Configurar as permissões individuais para a função.



- Modificar as suas lojas.
- Gerir as contas Exchange ligadas às suas lojas.
  - Ver as contas Exchange ligadas às suas lojas.
- Gerir os seus pagamentos pull.
- Criar pagamentos pull.
  - Criar pagamentos pull não aprovados.
- Modificar facturas.
  - Ver facturas.
  - Criar um Invoice.
  - Crie facturas a partir dos para-raios associados às suas lojas.
- Ver as suas lojas.
  - Ver facturas.
  - Ver os seus pedidos de pagamento.
  - Modificar os webhooks das lojas.
- Modificar os seus pedidos de pagamento.
  - Ver os seus pedidos de pagamento.
- Utilize os para-raios associados às suas lojas.
  - Ver as facturas relâmpago associadas às suas lojas.
  - Crie facturas a partir dos para-raios associados às suas lojas.
- Depositar fundos nas contas Exchange ligadas às suas lojas.
- Levantar fundos das contas Exchange para a sua loja.
- Troque fundos nas contas Exchange da sua loja.


Quando a função é criada, o nome é fixo e não pode ser alterado depois de estar no modo de edição.


![image](assets/en/060.webp)


### Webhooks


No BTCPay Server, é razoavelmente fácil criar um novo "Webhook". Nas definições da loja BTCPay Server - separador Webhooks, o proprietário de uma loja pode facilmente criar um novo webhook clicando em "+ Criar Webhook". Os webhooks permitem que o BTCPay Server envie eventos HTTP relacionados com a sua loja para outros servidores ou integrações de comércio eletrónico.


![image](assets/en/061.webp)


Está agora na vista para criar um Webhook. Certifique-se de que sabe o seu URL de carga útil e cole-o no seu servidor BTCPay. Enquanto cola o URL do payload, por baixo mostra o segredo do webhook. Copie o segredo do webhook e forneça-o no endpoint. Quando tudo tiver sido definido, pode alternar no BTCPay Server para "Automatic redelivery" O BTCPay Server tentará entregar novamente qualquer entrega falhada após 10 segundos, 1 minuto e até 6 vezes após 10 minutos. Pode alternar entre cada evento ou especificar os eventos de acordo com as suas necessidades. Certifique-se de que ativa o webhook e carregue no botão "Add webhook" para o guardar.


![image](assets/en/062.webp)


Webhooks não são compatíveis com a API do Bitpay. Existem duas IPNs separadas (em termos de BitPay: "Instant Payment Notifications") no BTCPay Server.



- Webhookp
- Notificações


Utilize apenas o URL de notificação quando criar facturas através da API Bitpay.


### Processadores de pagamentos


Os processadores de pagamentos trabalham em conjunto com o conceito de pagamentos no BTCPay Server. Um agregador de pagamentos para agrupar várias transacções e enviá-las de uma só vez. Com os processadores de pagamentos, o proprietário de uma loja pode automatizar os pagamentos em lote. O BTCPay Server oferece dois métodos de pagamentos automatizados: On-Chain e off-chain (LN).


O proprietário da loja pode clicar e configurar ambos os processadores de pagamento separadamente. Um lojista pode querer executar o processador On-Chain apenas uma vez a cada X horas, enquanto o processador off-chain pode ser executado a cada poucos minutos. Para o On-Chain, também é possível definir um objetivo para o bloco que deve ser incluído. Por defeito, este é definido como 1 (ou o próximo bloco disponível). Repara que a definição do processador de pagamentos off-chain só tem o temporizador de intervalo e não tem um objetivo de bloco. Os pagamentos do Lightning Network são instantâneos.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Os proprietários de lojas só podem configurar o processador On-Chain se tiverem um Hot Wallet ligado à sua loja.


![image](assets/en/065.webp)


Depois de configurar um processador de pagamentos, pode removê-lo ou modificá-lo rapidamente voltando ao separador Processador de pagamentos nas definições do BTCPay Server Store.


**Nota


Processador de pagamentos On-Chain - O processador de pagamentos On-Chain só pode funcionar numa loja configurada com um Hot Wallet ligado. Se não houver um Hot Wallet conectado, o servidor BTCPay não possui as chaves Wallet e não será capaz de processar pagamentos automaticamente.


### Emails


BTCPay Server pode usar Emails para Notificações ou, quando configurado corretamente, para recuperar contas criadas na instância. Como padrão, BTCPay Server não envia um email quando a password é perdida, por exemplo.


![image](assets/en/066.webp)


Antes de o proprietário de uma loja poder definir regras de correio eletrónico para acionar eventos específicos na sua loja, deve primeiro definir algumas configurações básicas de correio eletrónico. O BTCPay Server requer essas configurações para enviar e-mails para eventos relacionados à sua loja ou para redefinições de senha.


O servidor BTCPay facilitou o preenchimento dessas informações usando a opção "Quick Fill":



- Gmail.com
- Yahoo.com
- Pistola de correio
- Escritório365
- SendGrid


Ao usar a opção de preenchimento rápido, o BTCPay Server preencherá previamente os campos para o servidor SMTP e a porta. Agora, o proprietário da loja só precisa de preencher as suas credenciais, incluindo um Email Address, Login (que é normalmente igual ao seu email Address), e a sua palavra-passe. A opção avançada nas definições de e-mail do servidor BTCPay é Desativar verificações de segurança do certificado TLS; por predefinição, esta opção está activada.


![image](assets/en/067.webp)


Com as regras de correio eletrónico, o proprietário de uma loja pode definir eventos específicos para acionar mensagens de correio eletrónico para endereços de correio eletrónico específicos.



- Invoice Criado
- Invoice Pagamento recebido
- Processamento do Invoice
- Invoice Expirado
- Invoice Liquidado
- Invoice inválido
- Pagamento do Invoice liquidado


Se o cliente tiver fornecido um e-mail Address, estes accionadores também podem enviar as informações para o cliente. Os proprietários de lojas podem pré-preencher a linha de assunto para deixar claro por que razão este e-mail aconteceu e o que o despoletou.


![image](assets/en/068.webp)


### Formulários


Como o BTCPay Server não recolhe quaisquer dados, o proprietário de uma loja pode querer adicionar um formulário personalizado à sua experiência de checkout; desta forma, o proprietário da loja pode recolher informações adicionais do seu cliente. O construtor de formulários do BTCPay Server consiste em duas partes: uma vista visual e uma vista de código mais avançada dos formulários.


Ao criar um novo formulário, o BTCPay Server abre uma nova janela solicitando informações básicas sobre o que deseja que seu novo formulário pergunte. Em primeiro lugar, o proprietário da loja precisa de dar um nome claro para o seu novo formulário; este nome não pode ser alterado depois de ser definido.


![image](assets/en/069.webp)


Depois de o proprietário da loja atribuir um nome ao formulário, pode também ativar o interrutor "Permitir a utilização pública do formulário" e este passará a Green. Isto assegura que o formulário é utilizado em todos os locais de contacto com o cliente. Por exemplo, se o proprietário de uma loja criar um Invoice separado, não através do seu ponto de venda, pode querer recolher informações do cliente. Esta opção permite que essas informações sejam recolhidas.


![image](assets/en/070.webp)


Todos os formulários começam com, pelo menos, um novo campo de formulário. O proprietário da loja pode escolher o tipo de campo que deve ser.



- Texto
- Número
- Palavra-passe
- Correio eletrónico
- URL
- Números de telefone
- Data
- Campos ocultos
- Conjunto de campos
- Uma área de texto para comentários abertos.
- Seletor de opções


Cada tipo tem os seus parâmetros a preencher. O lojista pode defini-los a seu gosto. Abaixo do primeiro campo criado, os lojistas podem adicionar novos campos a este formulário.


![image](assets/en/071.webp)


#### Formulários personalizados avançados


O BTCPay Server também lhe permite criar formulários em código. JSON, em particular. Em vez de olhar para o editor, os proprietários de lojas podem clicar no botão CODE (código) mesmo ao lado do editor e entrar no código dos seus formulários. Numa definição de campo, apenas os seguintes campos podem ser definidos; os valores dos campos são armazenados nos metadados do Invoice:


| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | If .fields.type is select, the list of selectable values                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | The text displayed for this option                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | The value of the field if this option is selected                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | The JSON property name of the field as it will appear in the invoice's metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | The default value of the field                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | if true, the field will be required                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | The label of the field                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Additional text to provide an explanation for the field.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address. |

O nome do campo representa o nome da propriedade JSON que armazena o valor fornecido pelo utilizador nos metadados do Invoice. Alguns nomes conhecidos podem ser interpretados e modificados para ajustar as definições do Invoice.


| Field name       | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

Pode preencher automaticamente os campos de um Invoice adicionando cadeias de consulta ao URL do formulário, como "?your_field=value".


Eis alguns casos de utilização para esta funcionalidade:



- Ajudar o utilizador a introduzir dados: Preencher previamente os campos com informações conhecidas do cliente para facilitar o preenchimento do formulário. Por exemplo, se já souber o e-mail Address de um cliente, pode pré-preencher o campo do e-mail para lhe poupar tempo.
- Personalização: Personalize o formulário com base nas preferências ou na segmentação do cliente. Por exemplo, se tiver diferentes níveis de clientes, pode pré-preencher o formulário com dados relevantes, como o nível de adesão ou ofertas específicas.
- Seguimento: Acompanhe a origem das visitas dos clientes utilizando campos ocultos e valores pré-preenchidos. Por exemplo, pode criar ligações com valores utm_media pré-preenchidos para cada canal de marketing (por exemplo, Twitter, Facebook, E-mail). Isto ajuda-o a analisar a eficácia dos seus esforços de marketing.
- Testes A/B: Preencha previamente os campos com valores diferentes para testar diferentes versões de formulários, permitindo-lhe otimizar a experiência do utilizador e as taxas de conversão.


### Resumo das competências


Nesta secção, aprendeu o seguinte:



- A disposição e as funções dos separadores nas Definições da loja
- Uma multiplicidade de opções para ajustar o tratamento de taxas Exchange subjacentes, pagamentos parciais, pagamentos ligeiramente inferiores e muito mais.
- Personalize a aparência do checkout, incluindo a cadeia principal dependente do preço versus a ativação do Lightning nas faturas.
- Gerir níveis de acesso à loja e permissões entre funções.
- Configurar e-mails automatizados e os seus accionadores
- Crie formulários personalizados para recolher informações adicionais do cliente no momento do checkout.


### Avaliações de conhecimentos


#### Revisão da KA


Qual é a diferença entre as Definições da loja e as Definições do servidor?


#### KA Hipotética


Descreva algumas opções que pode selecionar em Checkout Appearance > Invoice Settings, e porquê.


## BTCPay Server - Definições do servidor


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


O BTCPay Server consiste em duas vistas de definições diferentes. Uma é dedicada às definições da Loja e a outra às definições do Servidor. Esta última só está disponível para os administradores do servidor e não para os proprietários da loja. Os administradores do servidor podem adicionar utilizadores, criar funções personalizadas, configurar o servidor de correio eletrónico, definir políticas, executar tarefas de manutenção, verificar todos os serviços ligados ao BTCPay Server, carregar ficheiros para o servidor ou verificar os registos.


### Utilizadores


Tal como mencionado na parte anterior, os administradores do servidor podem convidar utilizadores para o seu servidor, adicionando-os ao separador Utilizadores.


### Funções personalizadas em todo o servidor


O BTCPay Server tem dois tipos de funções personalizadas: funções personalizadas específicas da loja e funções personalizadas em todo o servidor nas configurações do BTCPay Server. Ambas têm um conjunto semelhante de permissões; no entanto, se definidas através do separador Definições do servidor BTCpay - Funções, a função aplicada será em todo o servidor e aplicar-se-á a várias lojas. Observe uma etiqueta "Server-wide" para as funções personalizadas nas definições do servidor.


![image](assets/en/072.webp)


### Funções personalizadas em todo o servidor


Conjunto de permissões de funções personalizadas em todo o servidor;



- Modificar as suas lojas.
- Gerir as contas Exchange associadas às suas lojas.
  - Ver as contas Exchange associadas às suas lojas.
- Gerir os seus pagamentos pull.
- Criar pagamentos pull.
  - Criar pagamentos pull não aprovados.
- Modificar facturas.
  - Ver facturas.
  - Criar um Invoice.
  - Crie facturas a partir dos para-raios associados às suas lojas.
- Ver as suas lojas.
  - Ver facturas.
  - Ver os seus pedidos de pagamento.
  - Modificar os webhooks das lojas.
- Modificar os seus pedidos de pagamento.
  - Ver os seus pedidos de pagamento.
- Utilize os para-raios associados às suas lojas.
  - Ver as facturas relâmpago associadas às suas lojas.
  - Crie facturas a partir dos para-raios associados às suas lojas.
- Depositar fundos nas contas Exchange associadas às suas lojas.
- Levantar fundos das contas Exchange para a sua loja.
- Troque fundos nas contas Exchange da sua loja.


**!?Nota!?**


Quando a função é criada, o nome é fixo e não pode ser alterado depois de estar no modo de edição.


### Correio eletrónico


As definições de Correio eletrónico em todo o servidor são semelhantes às definições de Correio eletrónico específico da loja. No entanto, esta configuração lida não apenas com gatilhos para lojas ou logs de administrador, mas também com gatilhos para outros eventos. Esta configuração de e-mail também torna a recuperação de senha disponível no servidor BTCPay no login. Funciona de forma semelhante às definições específicas da Loja; os administradores podem rapidamente preencher os seus parâmetros de e-mail e introduzir as suas credenciais de e-mail, permitindo que o servidor envie e-mails.


![image](assets/en/073.webp)


### Políticas


Os administradores da política do Servidor BTCPay podem definir várias configurações em tópicos como Configurações de Utilizador Existente, Configurações de Novo Utilizador, Configurações de Notificação e Configurações de Manutenção. Estas destinam-se a registar novos utilizadores como administradores ou utilizadores regulares, ou a esconder o BTCPay Server dos motores de busca, adicionando-o ao cabeçalho do seu servidor.


![image](assets/en/074.webp)


#### Utilizador existente Definições


As opções disponíveis aqui são distintas das funções personalizadas. Estas permissões adicionais podem tornar uma loja ou o seu proprietário vulneráveis a ataques. Políticas que podem ser adicionadas a utilizadores existentes:



- Permitir que não-administradores usem o nó interno do Lightning em suas lojas.
  - Isto permitiria aos proprietários de lojas utilizar o nó Lightning do administrador do servidor e, por conseguinte, os seus fundos! Atenção, esta não é uma solução para dar acesso ao Lightning.
- Permitir que não-administradores criem carteiras Hot para as suas lojas.
  - Isto permitiria a qualquer pessoa com uma conta na sua instância do servidor BTCPay criar carteiras Hot e armazenar a sua recuperação seed no servidor do Administrador. Isto pode fazer com que o Administrador seja responsável pela retenção de fundos de terceiros!
- Permitir que os não-administradores importem carteiras Hot para as suas lojas.
  - À semelhança do tópico anterior sobre a criação de carteiras Hot, esta política permite a importação de um Hot Wallet, com os mesmos perigos mencionados na secção sobre a criação de carteiras Hot.


![image](assets/en/075.webp)


#### Definições de novos utilizadores


Podemos definir algumas definições importantes para gerir os novos utilizadores que chegam ao servidor. Podemos definir um e-mail de confirmação para novos registos, desativar a criação de novos utilizadores através do ecrã de início de sessão e restringir o acesso de não administradores à criação de utilizadores através da API.



- Exigir um e-mail de confirmação para o registo.
  - O administrador do servidor deve ter configurado um servidor de correio eletrónico.
- Desativar o registo de novos utilizadores no servidor
- Desativar o acesso de não-administradores ao ponto final da API de criação de utilizadores.


Por defeito, o BTCPay Server tem a opção "Disable new user registration on the server" (Desativar o registo de novos utilizadores no servidor) e desactivou o acesso de não-administradores ao endpoint API de criação de utilizadores. Isto é por segurança, para que pessoas aleatórias que tropeçam no seu login BTCPay não possam criar contas.


![image](assets/en/076.webp)


#### Definições de notificação


![image](assets/en/077.webp)


#### Definições de manutenção


O BTCPay Server é um projeto de código aberto que vive no GitHub. Sempre que o BTCPay Server lança uma nova versão do software, os administradores podem ser notificados de que uma nova versão está disponível. Os administradores também podem querer evitar que os motores de busca (como o Google, Yahoo e DuckDuckGo) indexem o domínio do BTCPay Server. Como o BTCPay Server é FOSS, os programadores de todo o mundo podem querer criar novas funcionalidades. BTCPay Server tem uma caraterística experimental que, quando activada, permite aos administradores usar caraterísticas não destinadas à produção, mas sim para fins de teste.



- Verifique os lançamentos no GitHub e notifique quando uma nova versão do BTCPay Server estiver disponível.
- Desencorajar os motores de busca de indexar este sítio
- Ativar funcionalidades experimentais.


![image](assets/en/078.webp)


#### Plugins


O BTCPay Server pode adicionar Plugins e expandir o seu conjunto de funcionalidades. Os plugins, por defeito, são carregados a partir do repositório do construtor de plugins do BTCPay Server. Um administrador, no entanto, pode optar por ver os plugins num estado de Pré-lançamento, e se o desenvolvedor do plugin o permitir, o administrador do servidor pode agora instalar versões beta de plugins.


![image](assets/en/079.webp)


##### Definições de personalização


Uma implementação padrão do BTCPay Server será acessível através do domínio configurado durante a instalação. No entanto, um administrador do servidor pode remapear o domínio raiz e apresentar uma das aplicações criadas a partir de uma loja específica. O administrador do servidor pode também mapear domínios específicos para aplicações específicas.



- Apresentar a aplicação na raiz do sítio Web
  - Apresenta uma lista de possíveis aplicações a mostrar no domínio raiz.


![image](assets/en/080.webp)



- Mapear domínios específicos para aplicações específicas.
  - Quando clica para configurar um domínio específico para aplicações específicas, o Administrador pode definir tantos domínios apontados para aplicações específicas quantos forem necessários.


![image](assets/en/081.webp)


#### Exploradores de blocos


O BTCPay Server, como padrão, vem com Mempool.space como seu Block explorer para transações. Quando o BTCPay Server gera um novo Invoice e uma transação está ligada a ele, o proprietário da loja pode clicar para abrir a transação. O BTCPay Server irá, por defeito, apontar para o Mempool.space como um Block explorer; no entanto, um Administrador de servidor pode alterar isto para a sua opção preferida.


![image](assets/en/082.webp)


### Serviços


O separador "BTCPay Server settings: Serviços" é uma visão geral dos componentes que o seu servidor BTCPay utiliza. Os serviços que o seu servidor BTCPay expõe podem variar dependendo do método de implementação.


Um administrador do servidor BTCPay pode clicar em "Ver informação" atrás de cada serviço para o abrir e definir definições específicas.


![image](assets/en/083.webp)


#### LND (gRPC)


O BTCPay expõe o serviço GRPC do LND para consumo externo; encontrará informações de ligação neste menu específico de definições; as carteiras compatíveis estão listadas aqui. O servidor BTCPay também fornece um código QR para a ligação, que pode ser digitalizado e aplicado num Wallet móvel.


Os administradores do servidor podem abrir mais pormenores para ver.



- Detalhes do anfitrião
- Utilização de SSL
- Macarrão
- AdminMacaroon
- FacturaMacaroon
- Apenas leituraMacaroon
- Conjunto de cifras GRPC SSL (GRPC_SSL_CIPHER_SUITES)


#### LND (REST)


A BTCPay expõe o serviço REST do LND para consumo externo; encontrará informações de ligação [aqui](https://docs.btcpayserver.org/FAQ/LightningNetwork/#how-to-find-node-info-and-open-a-direct-channel-with-a-store-using-btcpay); as carteiras compatíveis estão listadas [aqui](https://docs.btcpayserver.org/FAQ/Wallet/#can-i-use-a-hardware-wallet-with-btcpay-server). Entre as carteiras compatíveis estão Joule, Alby e ZeusLN. O servidor BTCPay fornece um código QR para ligação, que pode ser digitalizado e aplicado num Wallet compatível.



- URI REST
- Macarrão
- AdminMacaroon
- FacturaMacaroon
- Apenas leituraMacaroon


#### LND seed Cópia de segurança


O backup LND seed é útil para recuperar fundos do seu LND Wallet em caso de corrupção do servidor. Como o nó Lightning é um Hot-Wallet, pode encontrar as informações confidenciais do seed nesta página.


O LND documenta o processo de recuperação. Consulte https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md para obter a documentação.


#### Cavalgar o relâmpago


Ride the Lightning é uma ferramenta de gestão de nós Lightning construída como software de código aberto. O BTCPay Server usa RTL como o componente de gerenciamento de nó Lightning em sua pilha. Os administradores do BTCPay Server podem aceder à RTL através das definições do servidor - separador Serviços ou clicando no Lightning Wallet.


#### Full node P2P


Os administradores de servidores podem querer ligar o seu nó Bitcoin a um Wallet móvel. Esta página fornece informações sobre como se conectar remotamente ao seu Full node através do protocolo P2P. No momento da redação deste curso, o BTCPay Server lista as carteiras Blockstream Green e Wasabi como carteiras compatíveis. O BTCPay Server fornece um código QR para conexão, que pode ser escaneado e aplicado em um Wallet compatível.


#### Full node RPC


Esta página expõe informações para se ligar remotamente ao seu Full node através do protocolo RPC.


#### SSH


SSH é usado para fins de manutenção. BTCPay Server mostra o comando de conexão inicial para chegar ao seu servidor e as chaves públicas SSH autorizadas para se conectar ao seu servidor. Os administradores do servidor podem querer desativar as alterações SSH através do BTCPay Server UI.


#### DNS dinâmico


Dynamic DNS permite-lhe ter um nome DNS estável apontando para o seu servidor, mesmo que o seu IP Address mude regularmente. Isto é recomendado se está a hospedar o servidor BTCPay em casa e deseja ter um domínio limpo para aceder ao seu servidor.


Note que precisa de configurar corretamente o seu NAT e a instalação do servidor BTCPay para obter o certificado HTTPS.


### Tema


O BTCPay Server, como padrão, vem com dois temas: Modos claro e escuro. Estes podem ser alternados clicando em Conta no canto inferior esquerdo e alternando entre o tema Escuro e o tema Claro. Os administradores do BTCPay Server podem adicionar o seu próprio tema, fornecendo um tema CSS personalizado.


Os administradores podem alargar o tema Claro/Escuro adicionando as suas próprias CSS personalizadas ou definindo o seu tema personalizado como totalmente personalizado.


![image](assets/en/084.webp)


#### Marca do servidor


Os administradores do servidor podem alterar a marca do BTCPay Server, definindo uma marca de toda a sua empresa. Como o BTCPay Server é FOSS, os administradores do servidor podem colocar uma etiqueta branca no software e personalizar a aparência para se adequar ao seu negócio.


![image](assets/en/085.webp)


### Manutenção


Como administrador do servidor, os seus utilizadores esperam que cuide bem do servidor. No separador Maintenance (Manutenção) do BTCPay Server, o administrador pode fazer alguma manutenção essencial. Definir o nome de domínio para a instância do servidor BTCPay, reiniciar ou limpar o servidor. Possivelmente o mais importante, executar actualizações.


O BTCPay Server é um projeto Open Source e é atualizado frequentemente. Cada nova versão é anunciada pelas suas notificações do BTCPay Server ou nos canais oficiais através dos quais o BTCPay Server comunica.


![image](assets/en/086.webp)


#### Nome do domínio


Depois que o BTCPay Server é configurado, um administrador pode querer mudar o seu domínio original. No separador Maintenance (Manutenção), o administrador pode alterar o domínio. Depois de clicar em confirmar e configurar os registos DNS apropriados no domínio, BTCPay Server actualiza e reinicia para voltar ao novo domínio.


![image](assets/en/087.webp)


#### Reiniciar


Reinicie o servidor BTCPay e os serviços relacionados.


![image](assets/en/088.webp)


#### Limpo


O BTCPay Server é executado com componentes Docker; com as actualizações, pode haver restos de imagens Docker, ficheiros temporários, etc. Os administradores do servidor podem libertar espaço executando o script Clean.


![image](assets/en/089.webp)


#### Atualização


É a opção mais importante no separador Manutenção. O BTCPay Server é construído pela comunidade, e por isso, os seus ciclos de atualização são mais frequentes do que a maioria dos produtos de software. Quando o BTCPay Server tem uma nova versão, os administradores serão notificados no seu centro de notificações. Ao clicar no botão de atualização, o BTCPay Server irá verificar o GitHub para a versão mais recente, atualizar o servidor e reiniciar. Antes de atualizar, os administradores do servidor são sempre aconselhados a ler as notas de lançamento distribuídas através dos canais oficiais do BTCPay Server.


![image](assets/en/090.webp)


### Registos


Enfrentar um problema nunca é divertido. Este documento descreve o fluxo de trabalho e os passos mais comuns para identificar e resolver eficazmente o seu problema, de forma autónoma ou com a ajuda da comunidade.


A identificação do problema é crucial.


#### Replicar o problema


Antes de mais, tente determinar quando é que o problema ocorre. Tente reproduzir o problema. Tente atualizar e reiniciar o servidor para verificar se consegue reproduzir o problema. Se isso descrever melhor o seu problema, tire uma captura de ecrã.


##### Atualizar o servidor


Verifique se a sua versão do BTCPay Server é muito mais antiga do que a [última versão](https://github.com/btcpayserver/btcpayserver/releases) do BTCPay Server. A atualização do seu servidor pode resolver o problema.


##### Reiniciar o servidor


Reiniciar o seu servidor é uma maneira fácil de resolver muitos dos problemas mais comuns do servidor BTCPay. Pode ser necessário fazer SSH no seu servidor para o poder reiniciar.


##### Reiniciar um serviço


Pode ser necessário reiniciar apenas um serviço específico na sua implantação do BTCPay Server para alguns problemas, como reiniciar o contêiner letsencrypt para renovar o certificado SSL.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Use o docker ps para encontrar o nome de um serviço diferente que você gostaria de reiniciar.


#### Ver os registos


Os registos podem fornecer uma peça essencial de informação. Nos parágrafos seguintes, descreveremos como obter as informações de registo para várias partes do BTCPay.


##### Registos BTCPay


Desde a versão 1.0.3.8, pode aceder facilmente aos registos do servidor BTCPay a partir do front end. Se for um administrador do servidor, vá a Definições do servidor > Registos e abra o ficheiro de registos. Se não souber o que significa um determinado erro nos registos, mencione-o durante a resolução de problemas.


Se pretender registos mais detalhados e estiver a utilizar uma implementação Docker, pode ver os registos de contentores Docker específicos utilizando a linha de comandos. Veja estas [instruções para ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) em uma instância do BTCPay em execução em um VPS.


Na página seguinte, uma lista geral dos nomes dos contentores utilizados para o servidor BTCPay.


Execute os comandos abaixo para imprimir os registos por nome de contentor. Substitua o nome do contentor para ver os registos de outros contentores.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```


| Logs for     | Container Name                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


Existem algumas maneiras de acessar os logs do LND ao usar o Docker. Primeiro, faça login como root:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Em alternativa, pode imprimir rapidamente os registos utilizando o ID do contentor (apenas são necessários os primeiros caracteres de ID únicos, como os dois caracteres mais à esquerda):


```bash
docker logs 'add your container ID'
```


Se, por qualquer motivo, precisar de mais registos


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Verá algo como


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Para aceder aos logs descomprimidos desses logs, faça `cat LND.log` ou se quiser outro, use `cat LND.log.15`.


Para aceder a logs comprimidos em `.gzip`, utilize `gzip -d LND.log.16.gz` (neste caso, estamos a aceder a `LND.log.16.gz`). Isso deve dar um novo arquivo, onde você pode fazer `cat LND.log.16`. Caso o procedimento acima não funcione, pode ser necessário instalar o gzip primeiro com `sudo apt-get install gzip`.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Em alternativa, utilize isto:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Também é possível obter informações de registo com o comando c-lightning CLI.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Registos do nó Bitcoin


Para além de [ver os registos](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) do seu contentor bitcoind, também pode utilizar qualquer um dos [comandos bitcoin-cli](https://developer.Bitcoin.org/reference/RPC/index.html)


[(abre nova janela)](https://developer.Bitcoin.org/reference/RPC/index.html) para obter informações do seu nó Bitcoin. BTCPay inclui um script que lhe permite comunicar facilmente com o seu nó Bitcoin.


Dentro da pasta btcpayserver-docker, obtém a informação Blockchain utilizando o teu nó:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Ficheiros


O BTCPay Server possui um sistema de ficheiros local, que permite carregar os activos da loja (produto), logótipos e marca diretamente para o servidor. O sistema de ficheiros do servidor só é acessível pelos administradores do servidor; os proprietários de lojas podem carregar os seus logótipos ou marcas ao nível da loja.


Quando o administrador do Servidor está no separador Armazenamento de Ficheiros, é possível carregar diretamente para o seu Servidor ou alterar o fornecedor de armazenamento de ficheiros para um sistema de ficheiros Local ou Armazenamento de Blob do Azure.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Resumo das competências


Nesta secção, aprendeu o seguinte:



- A diferença entre as definições do Armazém e do Servidor, em particular no que diz respeito a Utilizadores, Funções e Emails
- Definir políticas a nível do servidor para a utilização e criação do Lightning ou Bitcoin Hot Wallet, registo de novos utilizadores e notificações por correio eletrónico.
- Como adicionar temas personalizados (em vez das simples opções claro/escuro fornecidas), bem como criar logótipos personalizados
- Executar tarefas simples de manutenção do servidor através da GUI fornecida
- Resolver problemas, incluindo a obtenção de detalhes para qualquer um dos contentores Docker ou do seu nó
- Gerir o armazenamento de ficheiros


### Avaliação dos conhecimentos


#### Revisão concetual da KA


Qual é a diferença entre as funções atribuídas através das definições do servidor e do armazenamento, e o que descreve uma potencial utilização de uma em detrimento da outra?


#### Revisão prática da KA


Descrever alguns casos de utilização possíveis activados no separador Políticas.


#### Revisão prática da KA


Descrever algumas acções que um administrador pode realizar rotineiramente no separador Manutenção.


## Servidor BTCPay - Pagamentos


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Um Invoice é um documento que o vendedor emite a um comprador para cobrar o pagamento.


No BTCPay Server, um Invoice representa um documento que deve ser pago dentro de um intervalo de tempo definido a uma taxa Exchange fixa. As facturas têm datas de expiração porque bloqueiam a taxa Exchange dentro de um período de tempo especificado, protegendo o recetor das flutuações de preços.


O núcleo do BTCPay Server é a capacidade de atuar como um sistema de gestão Bitcoin Invoice. Um Invoice é uma ferramenta essencial para o controlo e gestão dos pagamentos recebidos.


A menos que utilize um [Wallet](https://docs.btcpayserver.org/Wallet/) integrado para receber pagamentos manualmente, todos os pagamentos de uma loja serão apresentados na página Facturas. Esta página ordena cumulativamente os pagamentos por data e serve como um recurso central para a gestão e resolução de problemas de pagamentos.


![image](assets/en/093.webp)


### Geral


#### Status do Invoice


A tabela abaixo lista e descreve os estados padrão Invoice no BTCPay, juntamente com as acções comuns sugeridas. As acções são apenas recomendações. Cabe aos utilizadores definir o melhor curso de ação para o seu caso de utilização e negócio.


| Invoice Status             | Description                                                                                                                             | Action                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New                        | Not paid, invoice timer still has not expired                                                                                           | None                                                                                                                        |
| New (paidPartial)          | Paid, not in full, invoice timer still has not expired                                                                                  | None                                                                                                                        |
| Expired                    | Not paid, invoice timer expired                                                                                                         | None                                                                                                                        |
| Expired (paidPartial) \*\* | Paid, not in full amount, and expired                                                                                                   | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark the invoice as settled or invalid           |
| Expired (paidLate)         | Paid, in full amount, after the invoice timer has expired                                                                               | Contact buyer to arrange a refund or process order if late confirmations are acceptable.                                    |
| Settled (paidOver)         | Paid more than the invoice amount, settled, received sufficient amount of confirmations                                                 | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing                 | Paid in full, but has not received sufficient amount of confirmations specified in the store settings                                   | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing (paidOver)      | Paid more than the invoice amount, not received sufficient amount of confirmations                                                      | Wait to be settled, then contact the  buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                    | Paid, in full, received sufficient amount of confirmations in store                                                                     | Fulfil the order                                                                                                            |
| Settled (marked)           | Status was manually changed to settled from a processing or invalid status                                                             | Store admin has marked the payment as settled                                                                               |
| Invalid\*                  | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings                              | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |
| Invalid (marked)           | Status was manually changed to invalid from a settled or expired status                                                                 | Store admin has marked the payment as invalid                                                                               |
| Invalid (paidOver)         | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |

#### Detalhes do Invoice


A página de detalhes do Invoice contém todas as informações relacionadas com um Invoice.


As informações do Invoice são criadas automaticamente com base no estado do Invoice, na taxa do Exchange, etc. As informações sobre o produto são criadas automaticamente se o Invoice tiver sido criado com informações sobre o produto, como na aplicação Ponto de venda.


#### Filtragem Invoice


As facturas podem ser filtradas através dos filtros rápidos localizados junto ao botão de pesquisa ou dos filtros avançados, que podem ser alternados clicando na ligação (Ajuda) na parte superior. Os utilizadores podem filtrar as facturas por loja, ID da encomenda, ID do item, estado ou data.


#### Exportação Invoice


As facturas do servidor BTCPay podem ser exportadas em formato CSV ou JSON. Para mais informações sobre a exportação e contabilidade do Invoice.


#### Reembolso de um Invoice


Se, por qualquer motivo, pretender emitir um reembolso, pode criar facilmente um reembolso a partir da vista Invoice.


#### Arquivar facturas


Como resultado da caraterística de não reutilização Address do BTCPay Server, é comum ver muitas facturas expiradas na página Invoice da sua loja. Para as ocultar da sua vista, selecione-as na lista e marque-as como arquivadas. As facturas que foram marcadas como arquivadas não são eliminadas. O pagamento de um Invoice arquivado continuará a ser detectado pelo seu servidor BTCPay (estado paidLate). Pode ver as facturas arquivadas da loja em qualquer altura, selecionando facturas arquivadas no menu suspenso do filtro de pesquisa.


#### Moeda por defeito


Moeda predefinida da loja, que foi definida no assistente de criação da loja.


#### Permitir que qualquer pessoa crie um Invoice


Deve ativar esta opção se pretender permitir que o mundo exterior crie facturas na sua loja. Esta opção só é útil se estiver a utilizar o botão de pagamento ou se estiver a emitir facturas através da API ou de um site HTML de terceiros. A aplicação PdV é pré-autorizada e não requer que esta definição seja activada para que um visitante aleatório abra a sua loja PdV e crie um Invoice.


#### Acrescentar uma taxa adicional (taxa de rede) ao Invoice



- Apenas se o cliente efetuar mais do que um pagamento para o Invoice
- Em cada pagamento
- Nunca adicionar uma taxa de rede


#### O Invoice caduca se o montante total não tiver sido pago após ... Ata.


O temporizador do Invoice está definido para 15 minutos por defeito. O temporizador serve como um mecanismo de proteção contra a volatilidade, uma vez que bloqueia o montante de criptomoeda com base nas taxas de criptomoeda para Fiat. Se o cliente não pagar o Invoice dentro do período definido, o Invoice é considerado expirado. O Invoice é considerado "pago" assim que a transação é visível no Blockchain (com zero confirmações), e é considerado "completo" quando atinge o número de confirmações que o comerciante definiu (normalmente 1-6). O temporizador é personalizável.


#### Considerar o Invoice pago mesmo que o montante pago seja ..% inferior ao previsto.


No caso de um cliente utilizar um Exchange Wallet para pagar diretamente um Invoice, o Exchange cobra uma pequena taxa. Isto significa que esse Invoice não é considerado totalmente concluído. O Invoice é marcado como "pago parcialmente" Se um comerciante pretender aceitar facturas mal pagas, pode definir a taxa percentual aqui


### Pedidos


Os pedidos de pagamento são uma funcionalidade que permite aos proprietários de lojas BTCPay criar facturas de longa duração. Os fundos são pagos de acordo com o pedido de pagamento usando a taxa Exchange em vigor no momento do pagamento. Isto permite que os utilizadores façam pagamentos à sua conveniência sem terem de negociar ou verificar as taxas Exchange com o proprietário da loja no momento do pagamento.


Os utilizadores podem pagar os pedidos em pagamentos parciais. O pedido de pagamento permanecerá válido até ser pago na totalidade ou se o titular da loja exigir um prazo de validade. Os endereços nunca são reutilizados. É gerado um novo Address cada vez que o utilizador clica em pagar para criar um Invoice para o pedido de pagamento.


Os proprietários de lojas podem imprimir pedidos de pagamento (ou exportar dados Invoice) para manutenção de registos e contabilidade. O BTCPay rotula automaticamente as facturas como Pedidos de Pagamento na lista Invoice da sua loja.


#### Personalizar os seus pedidos de pagamento



- Montante Invoice - Definir o montante de pagamento solicitado
- Denominação - Mostrar o montante solicitado em moeda fiduciária ou criptomoeda
- Quantidade de pagamento - Permitir apenas pagamentos únicos ou pagamentos parciais
- Tempo de expiração - Permitir pagamentos até uma data ou sem expiração
- Descrição - Editor de texto, tabelas de dados, incorporação de fotos e vídeos
- Aparência - Cor e estilo com temas CSS


![image](assets/en/094.webp)


#### Criar um pedido de pagamento


No menu da esquerda, vá para Pedido de pagamento e clique em "Criar pedido de pagamento".


![image](assets/en/095.webp)


Forneça o nome do pedido, o montante, a denominação de exibição, a loja associada, a hora de expiração e a descrição (opcional)


Selecione a opção Permitir que o beneficiário crie facturas na sua denominação se pretender permitir pagamentos parciais.


Clique em Guardar e visualizar para rever o seu pedido de pagamento.


O BTCPay cria um URL para o pedido de pagamento. Partilhe este URL para ver o seu pedido de pagamento. Precisa de vários do mesmo pedido? Pode duplicar pedidos de pagamento utilizando a opção Clonar no menu principal.


![image](assets/en/096.webp)


**AVISO


Os pedidos de pagamento são dependentes da loja, o que significa que cada pedido de pagamento é associado a uma loja durante a criação. Certifique-se de que tem um Wallet ligado à sua loja à qual pertence o pedido de pagamento.


#### Pedido pago


O beneficiário e o requerente podem ver o estado do pedido de pagamento depois de o pagamento ter sido enviado. O status aparecerá como Liquidado se o pagamento tiver sido recebido na íntegra. Se tiverem sido efetuados apenas pagamentos parciais, o Valor devido exibirá o saldo restante.


![image](assets/en/097.webp)


#### Personalizar pedidos de pagamento


O conteúdo da descrição pode ser editado usando o editor de texto da ordem de pagamento. Ambas as opções estão disponíveis se pretender utilizar temas de cores adicionais ou estilos CSS personalizados.


Os utilizadores não técnicos podem utilizar um [tema bootstrap](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Pode ser efectuada uma personalização adicional fornecendo código CSS adicional, como se mostra abaixo.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Puxar pagamentos


Tradicionalmente, um recetor partilha o seu Bitcoin Address para efetuar um pagamento Bitcoin, e o remetente envia posteriormente dinheiro para este Address. Este sistema é designado por Push payment, uma vez que o remetente inicia o pagamento enquanto o destinatário pode não estar disponível, enviando o pagamento para o destinatário.


No entanto, que tal inverter o papel?


E se, em vez de um remetente empurrar o pagamento, o remetente permitir que o destinatário puxe o pagamento numa altura que o destinatário considere adequada? Este é o conceito de um pagamento Pull. Isto permite várias novas aplicações, tais como:



- Um serviço de subscrição (em que o subscritor permite que o serviço retire dinheiro de x em x tempo)
- Reembolsos (em que o comerciante permite que o cliente transfira o dinheiro do reembolso para o seu Wallet quando entender)
- Faturação com base no tempo para freelancers (em que a pessoa que contrata permite que o freelancer transfira dinheiro para o seu Wallet à medida que o tempo é registado)
- Mecenato (quando o mecenas permite que o beneficiário retire dinheiro todos os meses para continuar a apoiar o seu trabalho)
- Venda automática (quando um cliente de um Exchange permite que um Exchange retire dinheiro do seu Wallet para vender automaticamente todos os meses)
- Sistema de levantamento do saldo (quando um serviço de grande volume permite que os utilizadores solicitem levantamentos do seu saldo, o serviço pode então facilmente efetuar todos os pagamentos a muitos utilizadores em intervalos fixos)


### Pagamentos


A funcionalidade de pagamento está ligada à funcionalidade [Pull Payments](https://docs.btcpayserver.org/PullPayments/). Esta funcionalidade permite-lhe criar pagamentos dentro do seu BTCPay. Esta funcionalidade permite-lhe processar pagamentos pull (reembolsos, pagamentos de salários ou levantamentos).


#### Exemplo 1: Reembolso


Comecemos pelo exemplo do reembolso. O cliente comprou um artigo na sua loja, mas, infelizmente, tem de o devolver. Ele quer um reembolso. No BTCPay, você pode criar um [Refund](https://docs.btcpayserver.org/Refund/) e fornecer ao cliente o link para solicitar seus fundos. Assim que o cliente tiver fornecido o seu Address e reclamado os fundos, estes serão exibidos na secção Pagamentos.


O primeiro estado que tem é Aguardando aprovação. Os funcionários da loja podem verificar se existem vários em espera e, depois de fazer a seleção, utilizar o botão Acções.


Opções no botão de ação



- Aprovar pagamentos selecionados
- Aprovar e enviar pagamentos selecionados
- Cancelar pagamentos selecionados


O próximo passo é aprovar e enviar os pagamentos selecionados, uma vez que queremos reembolsar o cliente. Verificar o Address do cliente, que indica o montante e se pretendemos que as taxas sejam subtraídas do reembolso ou não. Uma vez concluídas as verificações, a assinatura da transação é o único passo que falta.


O cliente é agora atualizado na página de reclamação. O cliente pode seguir a transação, uma vez que lhe é fornecida uma ligação para um Block explorer e para a sua transação. Quando a transação é confirmada, o seu estado muda para "Concluída".


#### Exemplo 2: Salário


Passemos agora ao pagamento de salários, uma vez que este é efectuado a partir do interior da loja e não de acordo com o pedido do cliente. O conceito subjacente é o mesmo: utiliza pagamentos pull. Mas, em vez de criar um reembolso, faremos um [Pull Payment](https://docs.btcpayserver.org/PullPayments/).


Vá para o separador Pull Payments no seu servidor BTCPay. No canto superior direito, clique no botão Criar pagamento pull.


Agora estamos na criação do Pagamento, dê-lhe um nome e o valor desejado na moeda escolhida. Preencha a Descrição, para que o empregado saiba do que se trata. A parte seguinte é semelhante à dos reembolsos. O trabalhador preenche o Destino Address e o montante que pretende reclamar deste Pagamento. Ele pode decidir fazer dois pedidos separados, para endereços diferentes, ou até mesmo fazer um pedido parcial de reembolso.


Se existirem vários pagamentos em espera, pode agrupá-los para serem assinados e enviados. Uma vez assinados, os pagamentos são movidos para o separador Em curso e mostram a Transação. Quando aceite pela rede, o pagamento passa para o separador Concluído. O separador Concluído serve apenas para fins históricos. Contém os pagamentos processados e as transacções que lhe pertencem


### Puxar pagamentos


#### Conceito


Quando um remetente configura um pagamento Pull, pode configurar uma série de propriedades:



- Nome do pedido pull
- Um montante limite
- Uma unidade (por exemplo, BTC, SAT, USD)
- Métodos de pagamento
  - BTC On-Chain
  - BTC off-chain
- Descrição
- CSS personalizado
- Data final (facultativo para Lightning Network BOLT11)


Depois disso, o remetente pode partilhar o pagamento pull utilizando uma ligação com o destinatário, permitindo-lhe criar um pagamento. O destinatário escolherá o seu pagamento:



- Qual o método de pagamento a utilizar
- Para onde enviar o dinheiro


Uma vez criado um pagamento, este contará para o limite do pagamento pull para o período atual. O remetente aprovará então o pagamento, definindo a taxa à qual o pagamento será enviado, e procederá ao pagamento.


Para o remetente, fornecemos um método fácil de usar para agrupar vários pagamentos a partir do [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/).


#### API de raiz


O BTCPay Server fornece uma API completa tanto para o emissor como para o recetor que está documentada na página `/docs` da sua instância. (ou no site de documentação https://docs.btcpayserver.org)


Uma vez que a nossa API expõe toda a capacidade dos pagamentos pull, um remetente pode automatizar os pagamentos de acordo com as suas próprias necessidades.


### Resumo das competências


Nesta secção, aprendeu o seguinte:



- Conhecimento profundo dos estados Invoice do servidor BTCPay, bem como das acções que podem ser executadas sobre eles
- Personalizar e gerir mecanismos Invoice de vida prolongada conhecidos como Requests.
- As possibilidades de pagamento flexíveis adicionais abertas com a função Pull Payment exclusiva do BTCPay Server, particularmente no tratamento de reembolsos e pagamentos de salários.


### Avaliação dos conhecimentos


#### Revisão concetual da KA


Quais são algumas das diferenças entre facturas e pedidos de pagamento, e qual poderá ser uma boa razão para utilizar os últimos?


#### Revisão concetual da KA


De que forma é que os pagamentos pull expandem o que normalmente pode ser feito com o On-Chain? Descreva alguns casos de utilização que permitem.


## Plugins padrão do servidor BTCPay


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Plugins e aplicações predefinidos


O servidor BTCPay vem com um conjunto padrão de Plugins (Apps) que podem transformar o BTCPay Server num gateway de pagamento de comércio eletrónico. Com a adição de um ponto de venda, plataforma Crowdfund e um botão de pagamento fácil, o BTCPay Server torna-se uma solução fácil de implementar.


### Ponto de venda


Um dos plugins padrão do BTCPay Server é o Point of Sale (PoS). Com o plugin PoS, o proprietário de uma loja pode criar uma Webshop diretamente a partir do BTCPay Server; o proprietário da loja não precisa de soluções de comércio eletrónico de terceiros para executar uma Webshop. A aplicação PoS baseada na Web permite que os utilizadores com lojas físicas aceitem facilmente Bitcoin, sem taxas ou terceiros, diretamente no seu Wallet. O PoS pode ser facilmente apresentado em tablets ou outros dispositivos que suportem a navegação na Web. Os utilizadores podem criar facilmente um atalho no ecrã inicial para aceder rapidamente à aplicação Web.


#### Como criar um novo ponto de venda


O BTCPay Server permite que os proprietários de lojas criem rapidamente um Ponto de Venda em vários layouts. BTCPay Server reconhece que nem todas as lojas são de comércio eletrónico, e nem todas as lojas são bares ou restaurantes, e vem com várias configurações padrão para o seu PoS.


Quando o proprietário da loja clica em "Point of Sale" na sua barra de menu à esquerda, BTCPay Server pedirá um nome; este nome será visível na barra de menu à esquerda. Clique em Create para criar o PoS.


![image](assets/en/098.webp)


#### Atualizar o ponto de venda recentemente criado


Depois de criar um novo ponto de venda, o ecrã seguinte permite-lhe atualizar o seu ponto de venda e adicionar artigos à sua loja.


##### Nome da aplicação


O nome dado aqui ao seu ponto de venda será visível no menu principal do servidor BTCPay.


##### Exibir título


O público verá o título ou o nome da sua loja quando a visitar. O BTCPay Server, por defeito, nomeia a sua loja como "Tea shop" Substitua este nome pelo nome da sua loja.


![image](assets/en/099.webp)


#### Escolha o estilo do ponto de venda


O servidor BTCPay é capaz de apresentar o seu ponto de venda de várias formas.



- Lista de produtos
  - Uma vista de loja onde os clientes só podem comprar 1 produto de cada vez.
- Lista de produtos com um carrinho.
  - Uma vista de loja onde os clientes podem comprar vários artigos de uma só vez e obter uma visão geral do carrinho de compras à direita do ecrã.
- Apenas teclado
  - Sem lista de produtos, apenas um teclado para faturação direta.
- Ecrã de impressão (lista de produtos imprimível com QR)
  - Se não pode apresentar sempre a sua lista de produtos digitalmente, precisa de uma solução "offline" para os produtos; BTCPay Server tem um ecrã de impressão para funcionar como uma loja offline.


![image](assets/en/100.webp)


#### Point Of Sale Style - Lista de produtos


![image](assets/en/101.webp)


#### Estilo do ponto de venda - Lista de produtos + carrinho de compras


![image](assets/en/102.webp)


#### Estilo de ponto de venda - apenas teclado


![image](assets/en/103.webp)


#### Estilo de ponto de venda - expositor para impressão


![image](assets/en/104.webp)


#### Moeda


O proprietário da loja pode definir uma moeda diferente para o seu ponto de venda do que a moeda predefinida globalmente. A moeda predefinida da loja preencherá automaticamente este campo.


#### Descrição


Fale ao mundo sobre a sua loja; o que está a vender e por quanto? Tudo o que explica a sua loja está aqui.


![image](assets/en/105.webp)


#### Produtos


Quando um ponto de venda é criado, um servidor BTCPay padrão adiciona alguns itens à loja para referência. Clique no botão Editar em qualquer um dos itens padrão para entender melhor cada opção possível para um item.


A criação de um novo produto na sua loja consiste nos seguintes campos;



- Título
- Preço (fixo, mínimo ou personalizado)
- URL da imagem
- Descrição
- Inventário
- ID
- Comprar Button Text.
- Ativar/Desativar


Quando o lojista tiver preenchido todos os campos do novo produto, clique em guardar e verá que a secção Produtos no Ponto de venda está agora a ser preenchida. Guarde sempre no canto superior direito do seu ecrã para evitar que os lojistas percam o seu progresso ao adicionar produtos.


Os proprietários de lojas também podem utilizar o "Editor Raw" para configurar os seus produtos. O editor raw requer um conhecimento básico das estruturas JSON.


![image](assets/en/106.webp)


#### Finalizar a compra


O BTCPay Server permite uma pequena personalização do checkout específico do PoS. O proprietário da loja pode definir o texto "Comprar por x" ou solicitar dados específicos do cliente, adicionando-os aos formulários.


#### Dicas


Apenas algumas lojas necessitam da opção de Dicas sobre as suas vendas. Os proprietários das lojas podem ativar ou desativar esta opção conforme entenderem para a sua loja. Se a loja usa gorjetas activadas, o dono da loja pode definir o texto no campo para as gorjetas que quiser. As gorjetas do servidor BTCPay funcionam com base num valor percentual. Os proprietários de lojas podem adicionar várias percentagens, separadas por vírgulas.


#### Descontos


Como proprietário de uma loja, pode querer dar ao cliente um desconto personalizado na finalização da compra; o botão para Descontos fica disponível na finalização da compra da sua loja. No entanto, é fortemente desaconselhada a utilização de sistemas de auto-checkout.


#### Pagamentos personalizados


Quando a opção Pagamentos personalizados está activada, o cliente pode introduzir um preço definido igual ou superior ao Invoice original gerado pela loja.


#### Opções adicionais


Depois de configurar tudo para o seu ponto de venda, restam algumas opções extra. Os proprietários de lojas podem facilmente incorporar o seu PdV através de um Iframe ou incorporar um botão de pagamento ligado a um item específico da loja. Para estilizar a loja PdV recém-criada, os proprietários podem adicionar CSS personalizado na parte inferior das opções adicionais.


#### Eliminar esta aplicação


Se o proprietário da loja quiser apagar completamente o ponto de venda do seu servidor BTCPay, na parte inferior da atualização do PoS, os proprietários da loja podem clicar no botão Apagar esta aplicação para destruir completamente a sua aplicação PoS. Ao clicar em "Delete this app", o BTCPay Server pedirá confirmação digitando `DELETE` e confirmando clicando no botão Delete. Após a exclusão, o proprietário da loja retorna ao painel do BTCPay Server.


### Servidor BTCPay - Crowdfund


Ao lado do plugin de Ponto de Venda, o BTCPay Server tem a opção de criar um crowdfund. Tal como qualquer outra plataforma de Crowdfund, os proprietários de lojas podem definir um objetivo, criar vantagens para as contribuições e personalizá-lo de acordo com as suas necessidades.


#### Como criar um novo fundo de coleta


Clique no plugin Crowdfund através do menu principal à esquerda do seu BTCPay Server, abaixo da secção Plugin. BTCPay Server irá agora pedir um nome para o Crowdfund; este nome também será exibido na barra de menu à esquerda.


![image](assets/en/107.webp)


#### Atualizar o ponto de venda recentemente criado


Uma vez atribuído um nome à aplicação, o ecrã seguinte consiste em atualizar a aplicação para ter contexto.


#### Nome da aplicação


O nome dado ao seu Crowdfund será visível no menu principal do BTCPay Server.


#### Exibir título


O título é atribuído ao Crowdfund para o público.


#### Título


Dê ao crowdfund uma frase que reconheça o objetivo da angariação de fundos.


![image](assets/en/108.webp)


#### URL da imagem em destaque


Cada crowdfund tem a sua imagem principal, o banner que reconhece diretamente. Esta imagem pode ser armazenada no teu servidor se tiveres direitos administrativos. Os administradores podem fazer o upload nas configurações do servidor BTCPay - Arquivos. Se for proprietário de uma Loja, a imagem deve ser carregada na web através de um host de terceiros (por exemplo, Imgur).


#### Tornar público o financiamento coletivo


Esta opção faz com que o seu Crowdfund se torne público e, portanto, visível para o mundo exterior. Para efeitos de teste ou para verificar se o seu tema é aplicado corretamente, mantenha esta opção em OFF durante o período de construção do crowdfund.


#### Descrição


Fale ao mundo sobre o seu Crowdfund. Para que é que está a angariar fundos? Tudo o que explica o seu crowdfunding está aqui.


![image](assets/en/109.webp)


#### Objetivo do crowdfunding


Defina um objetivo para o montante que a angariação de fundos deve ganhar para o projeto e a moeda em que esse objetivo deve ser expresso. Se os seus objectivos forem definidos entre datas, inclua essas datas de objetivo e de fim em Objectivos no crowdfund.


![image](assets/en/110.webp)


#### Benefícios


Os benefícios podem melhorar significativamente os seus esforços de financiamento coletivo. Isto porque as vantagens dão às pessoas uma forma de participarem na sua campanha. Eles exploram tanto as motivações egoístas como as benevolentes. E permitem-lhe aceder aos gastos dos seus apoiantes, e não apenas à sua bolsa filantrópica - pode adivinhar o que é mais significativo.


A criação de uma nova vantagem consiste nos seguintes campos.



- Título
- Preço (fixo, mínimo ou personalizado)
- URL da imagem
- Descrição
- Inventário
- ID
- Comprar Button Text.
- Ativar/Desativar


Quando o proprietário da loja tiver preenchido todos os campos da nova vantagem, clique em guardar e verá que a secção Vantagens nos Crowdfunds está agora a ser preenchida.


![image](assets/en/111.webp)


### Servidor BTCPay - Ponto de venda


#### Contribuições


Os proprietários das lojas podem escolher como apresentar as Vantagens, como são ordenadas ou até classificá-las em relação a outras vantagens. No entanto, assim que os objectivos dos Crowdfunds forem atingidos, os proprietários da loja podem querer interromper os donativos para esta angariação de fundos. Por isso, ele pode ativar a opção "Não permitir contribuições adicionais depois de atingir o objetivo". Isto impedirá o Crowdfund de aceitar donativos.


##### Comportamento de crowdfunding


O padrão do Crowdfund apenas conta as facturas criadas com o Crowdfund para o objetivo. No entanto, pode haver casos em que o proprietário da loja queira que todas as facturas feitas nessa loja sejam contabilizadas para o crowdfund.


#### Opções adicionais para personalização


O BTCpay Server oferece um par de personalizações extra. Adicione sons, animações, ou até mesmo tópicos de discussão para o Crowdfund. Os proprietários de lojas também podem modificar a aparência do Crowdfund inserindo seu próprio CSS personalizado.


#### Eliminar esta aplicação


Se o proprietário da loja quiser apagar totalmente o Crowdfund do seu BTCPay Server, na parte inferior da atualização do Crowdfund, pode clicar no botão "Delete this app" para remover completamente a sua aplicação Crowdfund. Ao clicar em "Delete this app", o BTCPay Server pedirá confirmação digitando `DELETE` e confirmando clicando no botão Delete. Após a exclusão, o proprietário da loja retorna ao painel do BTCPay Server.


### Servidor BTCPay - Botão de pagamento


HTML facilmente incorporável e botões de pagamento altamente personalizáveis permitem que os proprietários de lojas recebam gorjetas e donativos. Na barra de menu esquerda do BTCPay Server, abaixo da secção Plugins, os proprietários de lojas podem clicar em "Pay Button" e clicar em Enable para criar um botão de pagamento.


#### Definições gerais


Nas Definições gerais do botão de pagamento, os proprietários de lojas podem definir



- Preço normal
- Moeda por defeito
- Método de pagamento por defeito
  - Utilizar a predefinição da loja
  - BTC On-Chain
  - BTC off-chain (Relâmpago)
  - BTC off-chain (LNURL-pay)
- Descrição do check-out
- ID da encomenda


#### Opções de visualização


O botão Pagar do BTCPay Server pode ser configurado para se adequar a diferentes estilos. Os botões podem ter uma quantia fixa ou personalizada, que é apresentada com uma barra deslizante ou com alternâncias de mais e menos.


#### Utilizar Modal


Ao criar o botão de pagamento, os proprietários de lojas podem escolher o seu comportamento quando um cliente clica nele e mostrá-lo num modal ou como uma nova página.


**!?Nota!?**


Aviso: O botão Pagamento só deve ser utilizado para gorjetas e donativos


A utilização do botão de pagamento para integrações de comércio eletrónico não é recomendada, uma vez que o utilizador pode modificar informações relevantes para a encomenda. Para o comércio eletrónico, deve utilizar a nossa API Greenfield. Se esta loja processar transacções comerciais, recomendamos a criação de uma loja separada antes de utilizar o botão de pagamento.


#### Personalizar o texto do botão Pagar


Por defeito, o botão de pagamento do BTCPay Server diz "Pay With BTCPay". Os proprietários de lojas podem definir este texto de acordo com o seu desejo e alterar o logótipo do BTCPay Server para o seu próprio. Defina o texto usando o "Texto do botão de pagamento" e cole o URL da imagem abaixo do "URL da imagem do botão de pagamento".


##### Tamanho da imagem


O tamanho da imagem no botão só pode ser definido para três predefinições.



- 146x40px
- 168x46px
- 209x57px


#### Tipo de botão


O servidor BTCPay conhece três estados para o botão de pagamento.



- Montante fixo
  - O preço definido anteriormente encontra-se nas definições gerais do botão.
- Montante personalizado
  - O botão Pagar do servidor BTCPay tem os botões + e - para definir um preço personalizado.
  - Ao usar o valor personalizado, o servidor BTCPay solicitará um Mínimo, Máximo e quão gradualmente ele deve aumentar.
  - Os botões podem ser definidos para "Utilizar estilo de entrada simples", o que elimina os botões +/-.
  - Ajustar o botão em linha onde o botão e os botões de alternância aparecem em linha.
- Controlo deslizante
  - Semelhante ao montante personalizado, no entanto, é visualmente diferente, uma vez que tem uma barra deslizante em vez dos botões +/-.
  - Ao usar o Slider, o servidor BTCPay solicitará um Mínimo, Máximo e quão gradualmente ele deve aumentar.


**!?Nota!?**


O botão Pagamento pode ser eliminado na parte superior da descrição do aviso.


#### Notificações de pagamento


O IPN (Instant Payment Notification) do servidor foi concebido para webhooks e pode ser configurado com um URL para dados pós-compra.


#### Notificações por correio eletrónico


Sempre que um pagamento é efectuado, o servidor BTCPay pode notificar o proprietário da loja.


#### Redireccionamento do navegador


Quando o cliente concluir a compra, será redireccionado para este link, se definido pelo proprietário da loja.


#### Opções avançadas do botão de pagamento


Especifique parâmetros adicionais da cadeia de consulta que devem ser anexados à página de checkout assim que o Invoice for criado. Por exemplo, `lang=da-DK` carregaria a página de checkout em dinamarquês por defeito.


#### Utilizar a aplicação como ponto final


Pode ligar diretamente o botão de pagamento a um artigo numa das aplicações PdS ou Crowdfund que já utilizou anteriormente.


Os proprietários de lojas podem clicar no menu pendente e selecionar a aplicação pretendida; uma vez selecionada a aplicação, o proprietário da loja pode adicionar o item que precisa de ser associado.


#### Código gerado


Como o botão de pagamento do BTCPay Server é um HTML facilmente incorporável, o BTCPay Server mostra o código gerado para copiar para um site na parte inferior após a configuração do botão de pagamento.


Os proprietários de lojas podem copiar o código gerado no seu site, e o botão de pagamento do servidor BTCPay fica diretamente ativo no seu site.


#### Notificações de pagamento


O IPN (Instant Payment Notification) do servidor foi concebido para webhooks e pode ser configurado com um URL para publicar dados de compra.


#### Notificações por correio eletrónico


Sempre que um pagamento é efectuado, o servidor BTCPay pode notificar o proprietário da loja.


#### Redireccionamento do navegador


Quando o cliente concluir a compra, será redireccionado para este link, se definido pelo proprietário da loja.


#### Opções avançadas do botão de pagamento


Especifique parâmetros de cadeia de consulta adicionais que devem ser anexados à página de checkout assim que o Invoice for criado. Por exemplo, `lang=da-DK` carregaria a página de checkout em dinamarquês por defeito.


#### Utilizar a aplicação como ponto final


Pode ligar diretamente o botão de pagamento a um artigo numa das aplicações PdS ou Crowdfund que já utilizou anteriormente. Os proprietários de lojas podem clicar no menu pendente e selecionar a aplicação pretendida. Uma vez selecionada a aplicação, o proprietário da loja pode adicionar o artigo que precisa de ser associado.


#### Código gerado


Como o botão de pagamento do BTCPay Server é um HTML facilmente incorporável, o BTCPay Server mostra o código gerado para copiar para um site na parte inferior após a configuração do botão de pagamento. Os proprietários de lojas podem copiar o código gerado para o seu site, e o botão de pagamento do BTCPay Server está diretamente ativo no seu site.


### Resumo das competências


Nesta secção, aprendeu:



- Como utilizar o plugin PoS integrado do BTCPay Server para criar facilmente uma loja personalizada
- Como utilizar o plugin Crowdfund integrado do BTCPay Server para criar facilmente uma aplicação de crowdfunding personalizada
- Geração de código para um botão de pagamento personalizado utilizando o plugin Pay Button


### Avaliação dos conhecimentos


#### Revisão da KA


Quais são os três plugins integrados que vêm de fábrica com o BTCPay Server? Em poucas palavras, descreva como cada um pode ser utilizado.


# Configurar o servidor BTCPay


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Conhecimento básico da instalação do BTCPay Server num ambiente LunaNode


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### Instalando o servidor BTCPay no ambiente hospedado (LunaNode)


Estas etapas fornecerão todas as informações necessárias para começar a usar o BTCPay Server no LunaNode. Existem muitas opções para implantar o software.

Pode encontrar todos os detalhes do servidor BTCPay em https://docs.btcpayserver.org.


#### Por onde começar?


Nesta parte, você vai se familiarizar com LunaNode como o provedor de hospedagem, aprender sobre os primeiros passos de usar o seu servidor BTCPay, e aprender a usar com Lightning Network. Depois de passarmos por todas as etapas, você pode executar uma loja virtual ou plataforma de crowdfund aceitando Bitcoin!


Esta é uma das muitas maneiras de implementar o BTCPay Server. Leia a nossa documentação para mais detalhes.


https://docs.btcpayserver.org.


### Servidor BTCPay - Implementação LunaNode


#### Implantação do LunaNode


Primeiro, aceda ao sítio Web do LunaNode.com, onde criaremos uma nova conta. Clique em Sign Up (Registar) no canto superior direito ou utilize o assistente Get Started (Começar) na página inicial.


![image](assets/en/112.webp)


Depois de ter criado a sua nova conta, o LunaNode envia um e-mail de verificação. Depois de verificar a conta, em comparação com Voltage, é-lhe imediatamente apresentada a opção de recarregar o saldo da sua conta. Este saldo é necessário para cobrir o espaço do servidor e os custos de alojamento.


![image](assets/en/113.webp)


#### Adicionar crédito à sua conta LunaNode


Depois de clicar em "Depositar crédito", você pode definir quanto deseja recarregar sua conta e como deseja pagar por isso. O LunaNode e o BTCPay Server custarão entre $ 10 e $ 20 por mês.

Em comparação com Voltage.cloud, obtém acesso total ao seu Servidor Privado Virtual (VPS), permitindo-lhe ter mais controlo sobre o seu servidor. Depois de ter criado a sua nova conta, o LunaNode envia um e-mail de verificação.

Uma vez verificada a conta, em comparação com Voltage, é-lhe imediatamente apresentada a opção de recarregar o saldo da sua conta. Este saldo é necessário para cobrir o espaço do servidor e os custos de alojamento.


#### Como implementar um novo servidor?


Neste guia, vamos guiá-lo através do processo de configuração, criando um conjunto de chaves API e usando o lançador BTCPay Server desenvolvido pela LunaNode.


No seu painel de controlo do LunaNode, clique em API no canto superior direito. Isso abre uma nova página. Nós só temos que definir um Nome para a chave da API. O resto será tratado pelo LunaNode e não será abordado neste guia. Clique no botão Criar credencial de API.

Depois de criar as credenciais da API, obtém uma longa sequência de letras e caracteres. Esta é a sua chave de API.


![image](assets/en/114.webp)


#### Como implementar um novo servidor?


Há duas partes nessas credenciais, chave da API e ID da API; precisaremos de ambas. Antes de passarmos ao passo seguinte, vamos abrir um segundo separador no browser e ir para https://launchbtcpay.lunanode.com/


Aqui ser-lhe-á pedido que forneça a sua chave API e o seu ID API. Isto serve para o informar de que foi o utilizador que forneceu este novo servidor. A chave da API ainda deve estar aberta no seu separador anterior; se percorrer a tabela abaixo, encontrará o ID da API.


Pode voltar à página com o Launcher, preencher os campos com a sua chave de API e ID e clicar em continuar.


![image](assets/en/115.webp)


No próximo passo, você pode fornecer um nome de domínio. Se você já possui um domínio e deseja usá-lo para o BTCPay Server, certifique-se de adicionar também o registro DNS (chamado de registro `A`) em seu domínio. Se você não possui um domínio, use o domínio fornecido pelo LunaNode (você pode mudar isso mais tarde nas configurações do BTCPay Server) e clique em Continue.


Leia mais sobre como definir ou alterar um registo DNS para o servidor BTCPay; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### Lançar o servidor BTCPay no LunaNode


Depois de seguir os passos anteriores, podemos definir todas as opções para o nosso novo servidor. Aqui, seleccionaremos Bitcoin (BTC) como a nossa moeda suportada. Também podemos definir um e-mail para receber notificações sobre certificados de encriptação para fins de renovação, o que é opcional.


Este guia tem como objetivo configurar um ambiente Mainnet (Bitcoin do mundo real); no entanto, o LunaNode também permite configurá-lo para Testnet ou Regtest para fins de desenvolvimento. Deixaremos a opção Mainnet para este guia.


Pode escolher a sua implementação Lightning. O LunaNode oferece duas implementações diferentes, LND e Core Lightning. Para este guia, usaremos o LND. Há poucas, mas verdadeiras diferenças em ambas as implementações; para saber mais sobre isso, recomendamos a leitura da extensa documentação: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


A LunaNode oferece vários planos de Máquina Virtual (VM). Eles diferem em termos de faixa de preço e especificações do servidor. Para este guia, um plano m2 será suficiente; no entanto, se tiver selecionado mais do que apenas o Bitcoin como moeda, considere utilizar pelo menos um m4.


Acelerar a sincronização inicial do Blockchain; isso é opcional e depende das suas necessidades. Existem opções avançadas, como definir um Alias do Lightning, apontar para uma versão específica do GitHub ou definir chaves SSH; nenhuma delas será abordada neste guia.


Depois de preencher o formulário, tem de clicar em Launch VM, e o Lunanode vai começar a criar a sua nova VM, incluindo o BTCPay Server instalado nela. Este processo leva alguns minutos; uma vez que o seu servidor está pronto, LunaNode dá-lhe o link para o seu novo servidor BTCPay.


Após o processo de criação, clique no link para o seu servidor BTCPay; aqui, ser-lhe-á pedido que crie uma conta de Administrador.


![image](assets/en/117.webp)


### Resumo das competências


Nesta secção, aprendeu:



- Criar e financiar uma conta no LunaNode
- Utilizar o BTCPay Server Launcher para criar o seu próprio servidor


### Avaliação dos conhecimentos


#### Revisão concetual da KA


Descreva algumas das diferenças entre executar uma instância do BTCPay Server em um VPS vs. criar uma conta em uma instância hospedada.


## Instalando o BTCPay Server num ambiente Voltage


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Você vai se familiarizar com Voltage.cloud como o provedor de hospedagem, aprender sobre os primeiros passos da utilização do seu servidor BTCPay, e aprender a usar o Lightning Network. Depois de termos passado por todas as etapas, você pode executar uma loja virtual ou plataforma de crowdfund aceitando Bitcoin!


Esta é uma das muitas maneiras de implementar o BTCPay Server. Leia a nossa documentação para mais detalhes.

https://docs.btcpayserver.org.


### Servidor BTCPay - Implantação Voltage.cloud


Em primeiro lugar, aceda ao sítio Web Voltage.cloud e registe-se para obter uma nova conta. Ao criar uma conta, pode inscrever-se para uma avaliação gratuita de 7 dias. Clique em Inscrever-se no canto superior direito ou utilize a opção "Experimente uma avaliação gratuita de 7 dias" na página inicial.


![image](assets/en/118.webp)


Depois de criar uma conta, clique no botão `NODES` no seu painel de controlo. Depois de seleccionarmos Nodes e criarmos um novo nó, são-nos apresentadas as possíveis ofertas Voltage do nó. Como este guia também cobrirá o Lightning Network, na Voltage, primeiro precisamos de escolher a nossa implementação Lightning antes de criar um servidor BTCPay. Clique em LightningNode.


![image](assets/en/119.webp)


Aqui, terá de selecionar o tipo de nó de iluminação que pretende. O Voltage tem uma variedade de opções para a sua configuração de iluminação. Isso é diferente quando a implantação é feita com, por exemplo, o LunaNode. Para a intenção deste guia, um Nó Lite será suficiente. Leia mais sobre as diferenças em Voltage.cloud.


![image](assets/en/120.webp)


Dê um nome ao seu nó, defina uma senha e proteja esta senha. Se esta palavra-passe se perder, perde o acesso às suas cópias de segurança e o Voltage não a pode recuperar. Crie o nó e o Voltage mostra-lhe o progresso. Voltage criou o seu Lightning Node. Podemos agora criar a instância do servidor BTCPay e aceder diretamente ao Lightning Network.


Clique em Nodes no canto superior esquerdo do seu painel de controlo. Aqui pode configurar a próxima parte da sua instância do servidor BTCPay. Clique em "criar novo" quando estiver na visão geral dos nós. Você obtém uma tela semelhante à anterior. Agora, em vez do Lightning Node, escolhemos o BTCPay Server.


Voltage mostra-lhe a geolocalização do seu servidor BTCPay, que está alojado na região Oeste dos EUA. Aqui também verá o custo de alojamento do servidor. Clique em Criar e dê um nome ao seu servidor BTCPay. Active o Lightning e o Voltage mostra-lhe o nó Lightning criado no passo anterior. Clique em Create (Criar) e Voltage criará uma instância do servidor BTCPay.


![image](assets/en/121.webp)


Depois de clicar em criar, Voltage apresenta-lhe o nome de utilizador e a palavra-passe predefinidos. Estes são semelhantes à sua palavra-passe anteriormente definida em Voltage. Clique no botão Login to Account para ser redireccionado para o seu servidor BTCPay.


Bem-vindo à sua nova instância do servidor BTCPay. Como já configurámos o Lightning no processo de criação, ele mostra que o Lightning já está ativado!


### Resumo das competências


Neste capítulo, aprendeu:



- Criar uma conta no Voltage.cloud
- Passos para colocar o servidor BTCPay a funcionar juntamente com um nó Lightning na conta


### Avaliação dos conhecimentos


#### Revisão concetual da KA


Quais são as principais diferenças entre as configurações do Voltage e do LunaNode?


## Instalando o servidor BTCPay em um nó Umbrel


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


No final destes passos, pode aceitar pagamentos lightning para a sua loja BTCPay na sua rede local. Este processo também se aplica se gerir um umbrel node num restaurante ou empresa. Se pretender ligar esta loja a um site público, siga o exercício Avançado para expor o seu umbrel node ao público.


https://umbrel.com/


![image](assets/en/122.webp)


### Servidor BTCPay - Implementação da Umbrel


Depois que seu nó Umbrel estiver totalmente sincronizado com o Bitcoin Blockchain, vá para a Umbrel App Store e procure por BTCPay Server em Apps.


![image](assets/en/123.webp)


Clique em BTCPay Server para ver os detalhes da aplicação. Quando os detalhes do BTCPay Server estão abertos, o canto inferior direito mostra os requisitos para que o aplicativo seja executado corretamente. Ele mostra que é necessário um Bitcoin e um nó Lightning. Se você não tiver instalado o Lightning Node no seu Umbrel, clique em Instalar. Esse processo pode levar alguns minutos.


![image](assets/en/124.webp)


Depois de instalar o seu Lightning Node:


1. Clique em abrir nos detalhes da aplicação ou na aplicação no painel de controlo da Umbrels.

2. Clique em configurar um novo nó; ser-lhe-ão mostradas 24 palavras para a recuperação do seu nó de iluminação.

3. Escreva-os.


![image](assets/en/125.webp)


A Umbrel pedirá a verificação das palavras que acabámos de escrever. Depois que o nó Lightning estiver configurado, volte para a Umbrel App Store e encontre o BTCPay Server. Clique no botão de instalação e a Umbrel mostrará se os componentes necessários estão instalados e que o BTCPay Server requer acesso a esses componentes. Após a instalação, clique em Abrir no canto superior direito dos detalhes da aplicação ou abra o BTCPay Server através do seu painel de controlo da Umbrel.


O guarda-chuva pedirá a verificação das palavras que acabou de escrever.


![image](assets/en/126.webp)


**!?Nota!?**


Certifique-se de que os guarda num local seguro, tal como aprendeu anteriormente quando guardou as chaves.


Depois que o nó Lightning estiver configurado, retorne à Umbrel App Store e encontre o BTCPay Server. Clique no botão de instalação, e a Umbrel mostrará se os componentes necessários estão instalados e se o BTCPay Server requer acesso a esses componentes.


![image](assets/en/127.webp)


Após a instalação, clique em Abrir no canto superior direito dos detalhes do aplicativo ou abra o BTCPay Server através do painel da Umbrels.


![image](assets/en/128.webp)


### Resumo das competências


Nesta secção, aprendeu:



- Passos para instalar o servidor BTCPay com a funcionalidade Lightning num nó Umbrel


### Avaliação dos conhecimentos


#### Revisão concetual da KA


Em que é que a configuração da Umbrel difere das duas opções de alojamento anteriores?


# Secção final


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Comentários e classificações

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Conclusão do curso


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>