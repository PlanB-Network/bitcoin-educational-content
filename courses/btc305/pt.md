---
name: Bitcoin e BTCPay Server
goal: Instalar o BTCPay Server para o seu negócio
objectives:
  - Entender o que é o btcpayserver.
  - Auto hospedar e configurar o BTCPay Server.
  - Usar o btcpayserver no seu dia a dia empresarial.
---

# Bitcoin e BTCPay Server

Este é um curso introdutório sobre Operador do BTCPay Server escrito por Alekos e Bas, que foi adaptado no Formato de Curso Plan ₿ por melontwist e asi0.

UMA HISTÓRIA INACABADA

"Isso É Mentira, Minha Confiança Em Você Está Quebrada, Eu Vou Tornar Você Obsoleto".

Produzido pela Fundação BTCPay Server

+++

# Introdução

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Elogios críticos para o Bitcoin e BTCPay Server dos Autores

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

Vamos começar com o que é o BTCPay Server e de onde ele veio. Valorizamos a transparência e certos padrões para formar confiança no espaço Bitcoin.
Um projeto neste espaço quebrou esses valores. O desenvolvedor líder do BTCPay Server, Nicolas Dorier, levou isso para o lado pessoal e fez a promessa de torná-los obsoletos. Aqui estamos nós, muitos anos depois, trabalhando em direção a este futuro, totalmente de código aberto, todos os dias.

> Isso é mentira, minha confiança em você está quebrada, eu vou tornar você obsoleto.
> Nicolas Dorier

Após as palavras de Nicolas, era hora de começar a construir. Muito trabalho foi investido no que agora chamamos de BTCPay Server. Mais pessoas quiseram ajudar com esse impulso. Os mais reconhecíveis são r0ckstardev, MrKukks, Pavlenex e o primeiro comerciante a usar o software, astupidmoose.

O que significa código aberto, e o que entra em um projeto desse tipo?

FOSS significa Software Livre e de Código Aberto. O primeiro termo refere-se a condições que permitem a qualquer um copiar, modificar e até distribuir versões (mesmo com fins lucrativos) do software. O último refere-se a compartilhar abertamente o código-fonte, incentivando o público a contribuir e melhorá-lo.
Isso atrai usuários experientes entusiasmados em contribuir para o software que já usam e do qual derivam valor, provando ao longo do tempo ser mais adotado do que o software proprietário. Isso está de acordo com o ethos do Bitcoin de que "a informação deseja ser livre". Reúne pessoas apaixonadas que formam uma comunidade e é simplesmente mais divertido. Como o Bitcoin, FOSS é inevitável.

### Antes de começarmos

Este curso consiste em várias partes. Muitas serão tratadas pelo seu professor da sala de aula, ambientes de demonstração aos quais você terá acesso, um servidor hospedado para você mesmo e possivelmente um nome de domínio. Se você completar este curso de forma independente, esteja ciente de que os ambientes rotulados como DEMO não estarão disponíveis para você.
NB. Se você seguir este curso por sala de aula, os nomes dos servidores podem diferir dependendo da configuração da sua sala de aula. Variáveis nos nomes dos servidores podem ser diferentes devido a isso.

### Estrutura do Curso

Cada capítulo tem objetivos e avaliações de conhecimento. Neste curso, vamos cobrir cada um deles e ter um resumo das características-chave em cada bloco de lição (ou seja, capítulo). Ilustrações são apresentadas para fornecer feedback visual e reforçar conceitos-chave de forma visual. Os objetivos são definidos no início de cada bloco de lição. Esses objetivos vão além de uma lista de verificação. Eles fornecem um guia para um novo conjunto de habilidades. As Avaliações de Conhecimento se tornam progressivamente mais desafiadoras na configuração do seu BTCPay Server.

### O que os alunos recebem com o curso?

Com o Curso do BTCPay Server, um estudante pode entender os princípios básicos, técnicos e não técnicos do Bitcoin. O treinamento extensivo no uso do Bitcoin através do BTCPay Server permitirá aos estudantes operar sua própria infraestrutura Bitcoin.

### Endereços Web importantes ou Oportunidades de Contato

A Fundação BTCPay Server, que permitiu a Alekos e Bas escrever este curso, está em Tóquio, Japão. A Fundação BTCPay Server pode ser contatada através do site listado;

- https://foundation.btcpayserver.org
- junte-se aos canais oficiais de chat: https://chat.btcpayserver.org

## Introdução ao Bitcoin

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Entendendo o Bitcoin por meio de exercício em sala de aula

Este é um exercício em sala de aula, então, se você fizer este curso por conta própria, não poderá realizá-lo, mas ainda pode passar por este exercício. Para completar esta tarefa, o número mínimo de pessoas é entre 9 e 11.

O exercício começa após assistir à introdução "Como o Bitcoin e o blockchain funcionam" pela BBC.

![como o bitcoin e o blockchain funcionam](https://youtu.be/mhE_vvwAiRc)

Este exercício requer pelo menos nove pessoas para participar. Este exercício tem como objetivo obter fisicamente uma ideia de como o Bitcoin funciona. Ao desempenhar cada papel na rede, você terá uma maneira interativa e divertida de aprender. Este exercício não envolve a Lightning Network.

### Exemplo; Requer 9 / 11 pessoas

Os papéis são:

- 1 Cliente
- 1 Comerciante
- 7 a 9 nós Bitcoin

**A configuração é a seguinte:**

Clientes compram um produto da loja com Bitcoin.

**Cenário 1 - Sistema Bancário Tradicional**

- Configuração:
  - Veja diagramas/explicador no Figjam anexado - [Esquema da Atividade](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Obtenha três voluntários estudantes para desempenhar os papéis de Cliente (Alice), Comerciante (Bob) e Banco.
- Atue a sequência de eventos:
  - Cliente- navegando pela loja online e encontra um item por $25 que deseja, e informa ao Comerciante que gostaria de comprar
  - Comerciante- pede pagamento.
  - Cliente- envia informações do cartão ao Comerciante
  - Comerciante- encaminha informações ao Banco (identificando tanto a própria identidade quanto a informação) solicitando pagamento de
  - Banco coleta informações sobre o Cliente e o Comerciante (Alice e Bob) e verifica se o saldo do cliente é suficiente.
  - Deduz \$25 da conta de Alice, adiciona \$24 à conta de Bob, leva \$1 pelo serviço
  - O Comerciante recebe sinal verde do Banco e envia o item ao cliente.
- Comentários:
  - Bob e Alice devem ter um relacionamento com um banco.
  - Banco coleta informações identificáveis sobre Bob e Alice.
  - Banco leva uma comissão.
  - Banco deve ser confiável para custodiar o dinheiro de cada participante o tempo todo.

**Cenário 2 - Sistema Bitcoin**

- Configuração:
  - Veja diagramas/explicador no Figjam anexado - [Esquema da Atividade](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
- Substitua o Banco por nove estudantes que desempenharão o papel de um Computador (Nós/Mineradores de Bitcoin) em uma rede para substituir o Banco.
- Cada um dos 9 Computadores possui um registro histórico completo de todas as transações passadas já realizadas (portanto, saldos precisos sem falsificações), bem como um conjunto de regras:
  - Verificar se a transação está devidamente assinada (achaveencaixanafechadura)
  - Transmitir e receber transações válidas para os pares na rede, descartar as inválidas (incluindo qualquer tentativa de gastar os mesmos fundos duas vezes)
- Atualizar/Adicionar registros periodicamente com novas transações recebidas de um computador "aleatório", desde que todo o conteúdo seja válido (nota: estamos ignorando, por enquanto, o componente Prova de Trabalho (Proof of Work) de tudo isso, para simplicidade), caso contrário, rejeitar essas e continuar como antes até que o próximo computador "aleatório" envie uma atualização
  - A quantidade apropriada foi recompensada se o conteúdo fosse válido.
- Encenar a sequência de eventos:
  - Cliente- navegando pela loja online e encontra um item por $25 que deseja, e informa ao Comerciante que gostaria de comprar
  - Comerciante- pede pagamento enviando ao cliente uma fatura/endereço de sua carteira.
  - Cliente- constrói uma transação (enviando $25 em BTC para um endereço fornecido pelo Comerciante) e a transmite para a Rede Bitcoin.
- Computadores- recebem a transação e verificam:
  - Há pelo menos $25 de BTC no endereço de envio
  - A transação está devidamente assinada (“desbloqueada” pelo cliente)
  - Se não for o caso, então a transação não será propagada pela rede, e se for, então ela se propaga e fica em espera.
  - Comerciantes podem verificar que a transação está pendente e esperando.
- Um computador é "aleatoriamente" escolhido para propor a finalização da transação proposta, transmitindo "um bloco" contendo-a; se tudo estiver correto, eles receberão uma recompensa em BTC.
  - OPCIONAL/AVANÇADO - em vez de selecionar aleatoriamente um Computador, simular a mineração fazendo com que os Computadores joguem dados até que algum resultado predeterminado ocorra (por exemplo, o primeiro a tirar dois seis é selecionado)
  - Também pode simular o que aconteceria se dois Computadores ganhassem aproximadamente ao mesmo tempo, resultando em uma divisão da cadeia.
  - Computadores verificam a validade, atualizam/adicionam registros aos seus livros-razão se as regras forem cumpridas e transmitem o bloco aos pares.
  - O computador escolhido aleatoriamente recebe uma recompensa por propor um bloco válido.
  - Comerciante verifica que a transação foi finalizada; assim, os fundos foram recebidos, e o item foi enviado ao cliente.
- Comentários:
  - Note que não foi necessário um relacionamento bancário pré-existente.
  - Nenhuma terceira parte precisou facilitar; substituída por código/incentivos.
  - Nenhuma coleta de dados por alguém fora da troca direta e apenas a quantidade necessária deve ser trocada entre os participantes (por exemplo, endereço de envio).
  - Não é necessário confiança entre as pessoas (além do Comerciante enviar o item), de muitas maneiras, como uma compra em dinheiro.
  - O dinheiro é de propriedade direta dos indivíduos.
  - O livro-razão do Bitcoin é representado em dólares para simplicidade, mas na realidade, é em BTC.
  - Simulamos uma única transação sendo transmitida, mas na realidade, várias transações estão pendentes na rede, e os blocos incluem milhares de transações de uma vez. Os nós também verificam se não há transações de duplo gasto pendentes (eu descartaria todas, exceto uma, se fosse o caso).
- Cenários de trapaça:
  - E se o cliente não tivesse $25 em BTC?
    - Eles não seriam capazes de criar a transação porque “desbloquear” e “propriedade” são a mesma coisa, e os computadores verificam se a transação está devidamente assinada; caso contrário, eles a rejeitam.
- E se o computador escolhido aleatoriamente tentar "alterar o livro-razão"?
  - O bloco seria rejeitado, pois todos os outros computadores têm um histórico completo e notariam a mudança, violando uma de suas regras.
  - O Computador Aleatório não receberia uma recompensa, e nenhuma transação do seu bloco seria finalizada.

## Avaliação de Conhecimento

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### Discussão em Sala de Aula KA

Discuta algumas simplificações feitas no exercício em sala de aula sob o segundo cenário e descreva o que o sistema Bitcoin faz de forma mais detalhada.

### Revisão de Vocabulário KA

Defina os seguintes termos-chave introduzidos na seção anterior:

- Nó
- Mempool
- Alvo de Dificuldade
- Bloco

**Discuta o significado de alguns termos adicionais em grupo:**

Blockchain, Transação, Gasto Duplo, Problema dos Generais Bizantinos, Mineração, Prova de Trabalho (PoW), Função de Hash, Recompensa de Bloco, Blockchain, Cadeia Mais Longa, Ataque de 51%, Saída, Bloqueio de Saída, Mudança, Satoshis, Chave Pública/Privada, Endereço, Criptografia de Chave Pública, Assinatura Digital, Carteira

# Introdução ao BTCPay Server

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## Entendendo a tela de login do BTCPay Server

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Trabalhando com o BTCPay Server

O objetivo deste bloco do curso será ter um entendimento geral do software BTCPay Server. Em um ambiente compartilhado, é recomendado seguir a demonstração do instrutor e acompanhar com o Livro do Curso BTCPay Server para seguir o professor. Você aprenderá a criar uma carteira por meio de vários métodos. Exemplos incluem configurações de carteira quente e carteiras de hardware conectadas através do BTCPay Server Vault. Esses objetivos ocorrem no ambiente de demonstração, exibido e dado acesso pelo seu instrutor do curso.

Se você seguir este curso por conta própria, pode encontrar uma lista de hosts de terceiros para fins de demonstração em https://directory.btcpayserver.org/filter/hosts. Aconselhamos fortemente contra o uso dessas opções de terceiros como ambientes de produção, mas eles servem aos propósitos certos para uma introdução ao uso do Bitcoin e do BTCPay Server.

Como um aprendiz de estrela do BTCPay Server, você pode ter experiência prévia na configuração de um nó Bitcoin. Este curso falará especificamente adaptado para o stack de software do BTCPay Server.

Muitas das opções no BTCPay Server existem de alguma forma ou de outra em outros softwares relacionados à carteira Bitcoin.

### Tela de Login do BTCPay Server

Ao ser recebido no ambiente de demonstração, você é solicitado a 'Entrar' ou 'Criar sua conta'. Administradores de servidor podem desativar o recurso de criar novas contas por razões de segurança. Logos e cores de botão do BTCPay Server podem ser alterados porque o BTCPay Server é um Software de Código Aberto. Um host de terceiros pode personalizar o software e mudar toda a aparência.

![image](assets/en/0.webp)

### Janela de Criar uma Conta

Criar contas no BTCPay Server requer strings de endereço de Email válidas; exemplo@email.com seria uma string válida para Email.

A senha precisa ter pelo menos 8 caracteres, incluindo letras, números e caracteres. Após definir a senha uma vez, você terá que verificar a senha digitada para garantir que está correta em relação ao que foi digitado no primeiro campo de senha.
Quando os campos de Email e Senha estiverem devidamente preenchidos, clique no botão ‘Criar Conta’. Isso salvará o Email e a senha na instância do BTCPay Server do instrutor.
![image](assets/en/1.webp)

**!Nota!**

Se você seguir este curso por conta própria, criar esta conta seria algo que você poderia fazer em um host de terceiros; portanto, novamente, mencionamos para nunca usar esses ambientes como ambientes de produção, mas apenas para fins de treinamento.

### Criação de Conta pelo Administrador do BTCPay Server

O Administrador da Instância do BTCPay Server também pode criar contas para o BTCPay Server. O Administrador da instância do BTCPay Server pode clicar em ‘Configurações do Servidor’ (1), clicar na aba ‘Usuários’ (2) e clicar no botão “+ Adicionar Usuário” (3) no topo direito da aba de Usuários. No Objetivo (4.3), você aprenderá mais sobre o controle do administrador de Contas.

![image](assets/en/2.webp)

Como administrador, você precisará do endereço de Email do usuário e definir uma senha padrão. É aconselhável como Administrador informar ao usuário que ele deve alterar esta senha antes de usar a conta por razões de segurança. Se o Administrador NÃO definir uma Senha e o SMTP estiver configurado no servidor, o usuário receberá um email com um link de convite para criar sua conta e definir a senha por si mesmo.

### Exemplo

Ao seguir o curso com um instrutor, siga o link fornecido pelo instrutor e crie sua conta no ambiente de Demonstração fornecido. Certifique-se de que seu endereço de email e senha estejam salvos de forma segura; você precisará dessas credenciais de login para o restante dos objetivos de demonstração neste curso.

Seu instrutor pode ter coletado o endereço de email antecipadamente e enviado um link de convite antes deste exercício. Se instruído, verifique seu Email.

Ao fazer o curso sem um instrutor, crie sua conta usando o ambiente de demonstração do BTCPay Server; acesse

https://mainnet.demo.btcpayserver.org/login.

Esta conta deve ser usada apenas para fins de demonstração/treinamento e nunca para negócios.

### Resumo de Habilidades

Nesta seção, você aprendeu o seguinte:

- Como criar uma conta em um servidor hospedado através da interface.
- Como um administrador de servidor pode adicionar manualmente usuários nas configurações do servidor.

### Avaliação de Conhecimento

#### Revisão Conceitual de KA

Dê razões pelas quais usar um Servidor de Demonstração é uma má ideia para fins de produção.

## Gerenciamento de conta(s) de usuário

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Gerenciamento de Conta no BTCPay Server

Após um proprietário de loja criar sua conta, ele pode gerenciá-la na Parte Inferior Esquerda da UI do BTCPay Server. Abaixo do botão Conta, existem várias configurações de nível superior.

- Modo Escuro/Claro.
- Alternar Ocultar Informações Sensíveis.
- Gerenciar Conta.

![image](assets/en/3.webp)

### Modo Escuro e Claro

Os usuários do BTCPay Server podem escolher entre uma versão do UI em Modo Escuro ou Claro. As páginas voltadas para o cliente não mudarão. Elas usam as configurações preferidas do cliente em relação ao modo escuro ou claro.

### Alternar Ocultar Informações Sensíveis

O botão de ocultar informações sensíveis traz uma camada rápida e simples de segurança. Sempre que você precisar operar seu BTCPay Server, mas pode haver pessoas espiando por cima do seu ombro em um espaço público, ative Ocultar Informações Sensíveis, e todos os valores no BTCPay Server serão ocultados. Alguém pode ser capaz de olhar por cima do seu ombro, mas não poderá mais ver os valores com os quais você está lidando.

### Gerenciar Conta

Uma vez que a conta do usuário tenha sido criada, aqui é onde gerenciar senhas, autenticação de dois fatores ou chaves API.

### Gerenciar Conta - Conta

Atualize opcionalmente sua conta com um endereço de Email diferente. Para garantir que seu endereço de email esteja correto, o BTCPay Server permite que você envie um email de verificação. Clique em salvar se o usuário definir um novo endereço de email e confirmar que a verificação funcionou. O nome de usuário permanece o mesmo que o Email anterior.

Um usuário pode decidir excluir toda a sua conta. Isso pode ser feito clicando no botão de excluir na aba da Conta.

![image](assets/en/4.webp)

**!Nota!**

Após mudar o Email, o nome de usuário para a conta não mudará. O endereço de Email anteriormente fornecido permanecerá como o nome de Login.

### Gerenciar Conta - Senha

Um estudante pode querer mudar sua senha. Ele pode fazer isso indo até a aba Senha. Aqui ele precisa digitar sua senha antiga e pode mudá-la para uma nova.

![image](assets/en/5.webp)

### Autenticação de Dois Fatores (2fa)

Para limitar as consequências de uma senha roubada, você pode usar a autenticação de dois fatores (2fa), um método de segurança relativamente novo. Você pode ativar a autenticação de dois fatores via Gerenciar conta e a aba para autenticação de dois fatores. Você deve completar um segundo passo após fazer login com seu nome de usuário e senha.

O BTCPay Server permite duas maneiras de habilitar o 2FA, 2FA baseado em App (Authy, Google, Microsoft authenticators) ou através de Dispositivos de Segurança (FIDO2 ou LNURL Auth).

### Autenticação de Dois Fatores - Baseada em App

Baseado no Sistema Operacional do seu celular (Android ou iOS), os usuários podem escolher entre os seguintes apps;

1. Baixe um autenticador de dois fatores;
   - Authy para [Android](https://play.google.com/store/apps/details?id=com.authy.authy) ou [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator para [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) ou [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator para [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) ou [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. Após baixar e instalar o App Autenticador.
   - Escaneie o QR Code fornecido pelo BTCPay Server
   - Ou insira a chave gerada pelo BTCPay Server manualmente no seu app Autenticador.
3. O app Autenticador fornecerá um código único. Insira o código único no BTCPay Server para verificar a configuração e clique em verificar para completar o processo.

![image](assets/en/6.webp)

### Resumo de Habilidades

Nesta seção, você aprendeu o seguinte:

- Opções de gerenciamento de conta e as várias maneiras de gerenciar uma conta em uma instância do BTCPay Server.
- Como configurar o 2FA baseado em app.

### Avaliação de Conhecimento

#### Revisão Conceitual do KA

Descreva como o 2FA baseado em app ajuda a proteger sua conta

## Criando uma nova loja

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>

### Crie seu assistente de loja

Quando um novo usuário faz login no BTCPay Server, o ambiente está vazio e precisa de uma primeira loja. O assistente de introdução do BTCPay Server dará ao usuário a opção de ‘Criar sua loja’ (1). Uma Loja pode ser vista como um Lar para suas necessidades com Bitcoin. Um novo Nó do BTCPay Server começará com a Sincronização da Blockchain do Bitcoin (2). Dependendo da infraestrutura em que você executa o BTCPay Server, isso pode variar de algumas horas a alguns dias. A versão atual da instância é mostrada no canto inferior direito da sua UI do BTCPay Server. Isso é útil para referência quando estiver resolvendo problemas.
![imagem](assets/en/7.webp)

### Assistente de criação da sua loja

Seguir este curso começará com uma tela ligeiramente diferente da página anterior. Como seu instrutor preparou o ambiente de Demonstração, a blockchain do Bitcoin foi sincronizada previamente, e, portanto, você não verá o status de sincronização dos nós.

Um usuário pode decidir deletar toda a sua conta. Isso pode ser feito clicando no botão de deletar na aba de Conta.

![imagem](assets/en/8.webp)

**!Nota!**

Contas do BTCPay Server podem criar quantidades ilimitadas de lojas. Cada loja é uma carteira ou “lar”.

### Exemplo

Comece clicando em "Criar sua loja".

![imagem](assets/en/9.webp)

Isso criará seu primeiro Lar e painel para usar o servidor BTCPay.

(1) Após clicar em "Criar sua loja", o BTCPay Server exigirá que você nomeie a loja; isso pode ser qualquer coisa útil para você.

![imagem](assets/en/10.webp)

(2) Em seguida, deve-se definir uma moeda padrão para a loja, seja uma moeda fiduciária ou denominada em um padrão Bitcoin / Sats. Para o ambiente de demonstração, definiremos como USD.

![imagem](assets/en/11.webp)

(3) Como último parâmetro na configuração da loja, o BTCPay Server exige que você defina uma "Fonte de preço preferencial" para comparar o preço do Bitcoin contra o preço fiduciário atual, para que sua loja exiba a taxa de câmbio correta entre Bitcoin e a moeda fiduciária definida para a loja. Vamos manter o padrão no exemplo de Demonstração e definir isso para a exchange Kraken. O BTCPay Server usa a API da Kraken para verificar as taxas de câmbio.

![imagem](assets/en/12.webp)

(4) Agora que esses parâmetros da loja foram definidos, clique no botão Criar, e o BTCPay Server criará o painel da sua primeira loja, onde o assistente continuará.

![imagem](assets/en/13.webp)

Parabéns, você criou sua primeira loja, e isso conclui este exercício.

![imagem](assets/en/14.webp)

### Resumo de Habilidades

Nesta seção, você aprendeu:

- Criação de loja e configuração de uma moeda padrão combinada com preferências de fonte de preço.
- Cada "Loja" é um novo lar separado das outras lojas nesta instalação do BTCPay Server.

# Introdução à Segurança das Chaves do Bitcoin

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Entendendo a Geração de Chaves do Bitcoin

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### O que envolve a geração de chaves bitcoin?

Carteiras de bitcoin, quando criadas, geram o chamado "seed". No último objetivo, você criou um "seed". A série de palavras geradas antes também é conhecida como frases mnemônicas. O seed é usado para derivar Chaves Bitcoin individuais e usado para enviar ou receber Bitcoin. Frases-seed nunca devem ser compartilhadas com terceiros ou pares não confiáveis.
A geração de sementes é realizada de acordo com o padrão da indústria conhecido como o framework "Hierarchical Deterministic" (HD).
![image](assets/en/15.webp)

### Endereços

O BTCPay Server foi construído para gerar um novo Endereço. Isso alivia o problema do reuso de chave pública ou Endereço. Usar a mesma chave pública torna muito fácil rastrear todo o seu histórico de pagamentos. Pensar nas chaves como vouchers de uso único melhoraria significativamente sua privacidade. Também usamos Endereços Bitcoin, não os confunda com chaves públicas.

Um Endereço é derivado da chave pública por meio de um “algoritmo de hash”. No entanto, a maioria das carteiras e transações exibirá Endereços em vez dessas chaves públicas. Endereços são, em geral, mais curtos do que chaves públicas e geralmente começam com `1`, `3`, ou `bc1`, enquanto chaves públicas começam com `02`, `03`, ou `04`.

- Endereços que começam com `1.....` ainda são endereços muito comuns. Como mencionado no capítulo Criando uma nova loja, esses são endereços legados. Esse tipo de endereço é destinado a transações P2PKH. P2Pkh usa codificação Base58, o que torna o endereço sensível a maiúsculas e minúsculas. Sua estrutura é baseada na chave pública com um dígito adicional como identificador.

- Endereços que começam com `bc1...` estão lentamente se tornando endereços muito comuns. Estes são conhecidos como Endereços SegWit (nativos). Estes oferecem uma melhor estrutura de taxas do que os outros Endereços mencionados. Endereços SegWit Nativos usam codificação Bech32 e permitem apenas letras minúsculas.

- Endereços que começam com `3...` ainda são comumente usados por exchanges para endereços de depósito. Esses endereços são mencionados no capítulo Criando uma nova loja, endereços SegWit embrulhados ou aninhados. No entanto, eles também podem funcionar como um "Endereço Multisig". Quando usado como um endereço SegWit, há algumas economias nas taxas de transação novamente, embora menos do que SegWit Nativo. Endereços P2SH usam codificação Base58. Isso os torna sensíveis a maiúsculas e minúsculas, como o endereço legado.

- Endereços que começam com `2...` são endereços de Testnet. Eles são destinados a receber bitcoin de testnet (tBTC). Você nunca deve confundir isso e enviar Bitcoin para esses endereços. Para fins de desenvolvimento, você pode gerar uma carteira de testnet. Existem várias torneiras online para obter Bitcoin de testnet. Nunca compre Bitcoin de testnet. Bitcoin de testnet é minerado. Isso pode ser uma razão para um desenvolvedor usar Regtest em vez disso. Este é um ambiente de playground para desenvolvedores, faltando certos componentes de rede. Bitcoin é, no entanto, muito útil para fins de desenvolvimento.

### Chaves Públicas

Chaves públicas são menos usadas na prática hoje em dia. Com o tempo, os usuários de bitcoin têm substituído-as por Endereços. Elas ainda existem e ocasionalmente são usadas. Chaves públicas são, em geral, sequências muito mais longas do que endereços. Assim como com os endereços, elas começam com um identificador específico.

- Primeiro, `02...` e `03...` são identificadores de chave pública muito padrão codificados no formato SEC. Estes podem ser processados e transformados em endereços para recebimento, usados para criar endereços multi-assinatura ou para verificar uma assinatura. Transações Bitcoin dos primeiros dias usavam chaves públicas como parte das transações P2PK.

- Carteiras HD, no entanto, usam uma estrutura diferente. `xpub...`, `ypub...` ou `zpub...` são chamadas de chaves públicas estendidas, ou xpubs. Essas chaves são usadas para derivar muitas chaves públicas, pois fazem parte da carteira HD. Como seu xpub contém os registros de todo o seu histórico, significando transações passadas e futuras, nunca compartilhe estas com partes não confiáveis.

### Resumo das Habilidades

Nesta seção, você aprendeu o seguinte:

- As diferenças entre endereços e tipos de dados de chave pública e os benefícios de usar endereços em vez de chaves públicas.

### Avaliação de Conhecimento

Descreva o benefício de usar endereços novos para cada transação em comparação com a reutilização de endereços ou métodos de chave pública

## Protegendo chaves com carteira de hardware

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Armazenando Chaves Bitcoin

Após gerar uma frase-semente, a lista de 12 - 24 palavras geradas neste livro requer backups adequados e segurança, pois essas palavras são a única maneira de recuperar o acesso a uma carteira. A estrutura das carteiras HD e como ela gera endereços de forma determinística usando essa única semente, todos os seus endereços criados serão respaldados usando esta única lista de palavras mnemônicas representando sua frase ou frase de recuperação.

Mantenha sua frase de recuperação segura. Se acessada por alguém, especificamente com intenção maliciosa, eles podem mover seus fundos. Manter a semente segura e protegida, mas também lembrá-la é mútuo entre si. Existem vários métodos para armazenar chaves privadas Bitcoin, cada um com benefícios e desvantagens, seja em segurança, privacidade, conveniência ou meios físicos. Devido à importância das chaves privadas, os usuários de bitcoin tendem a armazenar e manter essas chaves de forma segura em "autocustódia" em vez de usar serviços "custodiais" como bancos. Dependendo do usuário, ele deve usar uma solução de Armazenamento a Frio ou uma Carteira Quente.

### Armazenamento Quente e Frio de chaves bitcoin

Geralmente, as carteiras bitcoin são denominadas em Carteira Quente ou Carteira Fria. A maioria dos compromissos está na conveniência, facilidade de uso e riscos de segurança. Cada um desses métodos também pode ser visto em uma solução de custódia. No entanto, os compromissos aqui são principalmente baseados em segurança e privacidade e vão além do escopo deste curso.

### Carteira Quente

Carteiras quentes são a maneira mais conveniente de interagir com o Bitcoin por meio de software móvel, web ou desktop. A carteira está sempre conectada à internet, permitindo aos usuários enviar ou receber Bitcoin. Isso, no entanto, também é sua fraqueza, a carteira, como está sempre online, agora está mais vulnerável a ataques de hackers ou malware em seu dispositivo. No BTCPay Server, carteiras quentes armazenam as chaves privadas na instância. Qualquer pessoa que acessar sua loja BTCPay Server poderia roubar fundos deste endereço se mal-intencionada. Quando o BTCPay Server é executado em um ambiente hospedado, você sempre deve considerar isso em seu perfil de segurança e preferencialmente não usar uma Carteira Quente nesse caso. Quando o BTCPay Server é instalado em hardware próprio, seguro e confiável por você, o perfil de risco diminui significativamente, mas nunca desaparece!

### Carteira Fria

Indivíduos movem seus Bitcoin para uma carteira fria porque ela pode isolar as chaves privadas da internet. Remover a conexão com a internet da equação reduz o risco de malware, spyware e trocas de SIM. Acredita-se que o armazenamento frio seja superior ao armazenamento quente em termos de segurança e autonomia, contanto que precauções adequadas sejam tomadas para evitar a perda das chaves privadas Bitcoin. O armazenamento frio é mais adequado para grandes quantidades de Bitcoin, que não se destinam a ser gastas frequentemente devido à complexidade da configuração da carteira.

Existem vários métodos de como armazenar chaves Bitcoin em armazenamento frio, desde carteiras de papel até carteiras cerebrais, carteiras de hardware ou, desde o início, um arquivo de carteira. A maioria das carteiras usa o BIP 39 para gerar a frase-semente. No entanto, dentro do software Bitcoin Core, ainda não foi alcançado um consenso sobre o uso dele. O software Bitcoin Core ainda gerará um arquivo Wallet.dat que você precisa armazenar em um local seguro offline.

### Resumo de Habilidades

Nesta seção, você aprendeu:

- As diferenças entre carteiras quentes e frias em termos de funcionalidade e seus compromissos.

### Avaliação de Conhecimento Revisão Conceitual

- O que é uma carteira?
- Qual a diferença entre carteiras quentes e frias?

- Descreva o que significa "gerar uma carteira"?

## Usando suas chaves Bitcoin

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### Carteira BTCPay Server

O BTCPay Server consiste nas seguintes características padrão de carteira:

- Transações
- Enviar
- Receber
- Reescanear
- Pagamentos Pull
- Pagamentos
- PSBT
- Configurações Gerais

### Transações

Os administradores podem ver as transações de entrada e saída para a carteira on-chain conectada a esta loja específica na visualização de transações. Cada transação tem uma distinção entre recebidas e enviadas. As recebidas serão verdes e as transações de saída serão vermelhas. Na visualização de transações do BTCPay Server, os administradores também verão um conjunto de etiquetas padrão.

| Tipo de Transação | Descrição                                                      |
| ----------------- | -------------------------------------------------------------- |
| App               | Pagamento foi recebido através de uma fatura de app            |
| invoice           | Pagamento foi recebido através de uma fatura                   |
| payjoin           | Não pago, o temporizador da fatura ainda não expirou           |
| payjoin-exposed   | UTXO foi exposto através de uma proposta de payjoin de fatura  |
| payment-request   | Pagamento foi recebido através de uma solicitação de pagamento |
| payout            | Pagamento foi enviado através de um pagamento ou reembolso     |

### Como Enviar

A função de envio do servidor BTCPay envia transações da sua carteira on-chain do BTCPay Server. O BTCPay Server permite várias maneiras de assinar suas transações para gastar fundos. Uma transação pode ser assinada com;

- Carteira de Hardware
- Carteiras que suportam PSBT
- Chave privada HD ou sementes de recuperação.
- Carteira Quente

#### Carteira de hardware

O BTCPay Server possui suporte integrado para carteira de hardware, permitindo que você use sua carteira de hardware com o BTCPay Vault sem vazar informações para aplicativos ou servidores de terceiros. A integração da carteira de hardware dentro do BTCPay Server permite que você importe sua carteira de hardware e gaste os fundos recebidos com uma simples confirmação no seu dispositivo. Suas chaves privadas nunca deixam o dispositivo, e todos os fundos são validados contra seu nó completo, então não há vazamento de dados.

#### Assinando com uma carteira que suporta PSBT

PSBT (Transações Bitcoin Parcialmente Assinadas) é um formato de intercâmbio para transações Bitcoin que ainda precisam ser totalmente assinadas. PSBT é suportado no BTCPay Server e pode ser assinado com carteiras de hardware e software compatíveis.

A construção de uma transação Bitcoin totalmente assinada passa pelas seguintes etapas:

- Um PSBT é construído com entradas e saídas específicas, mas sem assinaturas
- O PSBT exportado pode ser importado por uma carteira que suporta este formato
- Os dados da transação podem ser inspecionados e assinados usando a carteira
- O arquivo PSBT assinado é exportado da carteira e importado com o BTCPay Server
- O BTCPay Server produz a transação Bitcoin final
- Você verifica o resultado e o transmite para a rede

#### Assinando com Chave Privada HD ou semente mnemônica

Se você criou uma carteira antes usando o BTCPay Server, você pode gastar os fundos inserindo sua chave privada em um campo apropriado. Defina um "AccountKeyPath" adequado em configurações da carteira; caso contrário, você não poderá gastar.

#### Assinando com uma carteira quente

Se você criou uma nova carteira ao configurar sua loja e a ativou como uma carteira quente, ela usará automaticamente a semente armazenada em um servidor para assinar.

### RBF (Substituir-Por-Taxa)

Replace-By-Fee (RBF) é uma funcionalidade do protocolo Bitcoin que permite substituir uma transação previamente transmitida (enquanto ainda não confirmada). Isso permite randomizar a impressão digital da transação da sua carteira ou substituí-la por uma taxa de comissão mais alta para mover a transação para uma posição mais alta na fila de prioridade de confirmação (mineração). Isso efetivamente substituirá a transação original, pois a taxa de comissão mais alta será priorizada e, uma vez confirmada, invalidará a original (sem duplo gasto).
Pressione o botão "Configurações Avançadas" para visualizar as opções de RBF;

![imagem](assets/en/16.webp)

- Randomizar para maior privacidade, permite que a transação seja substituída automaticamente para randomização da impressão digital da transação.
- Sim, Marcar transação para RBF e ser substituída explicitamente (Não substituída por padrão, apenas por entrada)
- Não, Não permitir que a transação seja substituída.

### Seleção de Moedas

A seleção de moedas é uma funcionalidade avançada que aumenta a privacidade, permitindo selecionar as moedas que deseja gastar ao criar uma transação. Por exemplo, pagar com moedas que são recentes de uma mistura de conjoin.

A seleção de moedas funciona nativamente com a funcionalidade de etiquetas da carteira. Isso permite etiquetar fundos recebidos para um gerenciamento e gasto de UTXO mais suave.

O BTCPay Server também suporta o BIP-329 para gerenciamento de etiquetas. BIP-329 permite etiquetas em; se você transferir de uma carteira que suporta este BIP específico e definir etiquetas, o BTCPay Server reconhecerá estas e as importará. Ao migrar servidores, esta informação também pode ser exportada e importada para o novo ambiente.

### Como Receber

Ao clicar no botão de receber no BTCPay Server, ele gera um endereço não utilizado que pode ser usado para receber pagamentos. Os administradores também podem gerar um novo endereço ao gerar uma nova “Fatura”.

O BTCPay Server sempre pedirá para gerar o próximo endereço disponível para evitar a reutilização de endereço. Após clicar em “Gerar próximo endereço BTC disponível”, o BTCPay Server gerou um novo endereço e QR. Ele também permite definir diretamente uma Etiqueta para o endereço para melhor gerenciamento dos seus endereços.

![imagem](assets/en/17.webp)

![imagem](assets/en/18.webp)

#### Re-escanear

A funcionalidade de Re-escanear depende do “Scantxoutset” do Bitcoin Core 0.17.0 para escanear o estado atual da blockchain (chamado Conjunto UTXO) em busca de moedas pertencentes ao esquema de derivação configurado. A re-escanear da carteira resolve dois problemas que os usuários do BTCPay Server enfrentam.

1. Problema do limite de gap - A maioria das carteiras de terceiros são carteiras leves que compartilham um nó entre muitos usuários. Carteiras dependentes de nó leve e completo limitam a quantidade (tipicamente 20) de endereços sem saldo que rastreiam na blockchain para prevenir problemas de desempenho. O BTCPay Server gera um novo endereço para cada fatura. Com isso em mente, após o BTCPay Server gerar 20 faturas consecutivas não pagas, a carteira externa para de buscar as transações, assumindo que não ocorreram novas transações. Sua carteira externa não as mostrará uma vez que as faturas sejam pagas na 21ª, 22ª, etc. Por outro lado, internamente, a carteira do BTCPay Server rastreia qualquer endereço que gera junto com um limite de gap muito maior. Ela não depende de terceiros e sempre pode mostrar um saldo correto.
2. A solução do limite de lacuna - Se a sua [carteira externa/existente](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) permite a configuração de limite de lacuna, a solução fácil é aumentá-lo. No entanto, a maioria das carteiras não permite isso. As únicas carteiras que conhecemos que permitem a configuração de limite de lacuna são Electrum, Wasabi e Sparrow Wallet. Infelizmente, é provável que você encontre um problema com muitas outras carteiras. Para a melhor experiência do usuário e privacidade, considere abandonar as carteiras externas e usar a carteira interna do BTCPay Server.

#### BTCPay Server usa “mempoolfullrbf=1”

O BTCPay Server utiliza “mempoolfullrbf=1”; adicionamos isso como padrão na sua configuração do BTCPay Server. No entanto, também fizemos disso um fragmento que você pode desativar por conta própria. Sem “mempoolfullrbf=1”, se um cliente gastar duas vezes um pagamento com uma transação que não sinaliza RBF, o Comerciante só saberia após a confirmação.

Um administrador pode querer optar por não usar essa configuração. Pela seguinte string, você pode alterar o padrão definido.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### Configurações da Carteira do BTCPay Server

As configurações da carteira dentro do BTCPay Server oferecem uma visão clara e rápida das configurações gerais da sua carteira. Todas essas configurações são preenchidas previamente se a carteira foi criada com o BTCPay Server.

![image](assets/en/19.webp)

As configurações da carteira dentro do BTCPay Server oferecem uma visão clara e rápida das configurações gerais da sua carteira. Todas essas configurações são preenchidas previamente se a carteira foi criada com o BTCPay Server. As configurações da carteira do BTCPay Server começam com o status da carteira. É uma carteira Somente Visualização ou uma Hot Wallet? Dependendo do tipo de carteira, as ações podem variar desde rescannear a carteira por transações perdidas, Podar transações antigas do histórico, registrar a carteira para links de pagamento, ou substituir e deletar a carteira atual anexada à loja. Nas configurações da carteira do BTCPay Server, os administradores podem definir um Rótulo para a carteira para melhor gerenciamento da mesma. Aqui, o Administrador também poderá ver o Esquema de Derivação, chave da conta (xpub), Impressão Digital e Caminho da Chave. Pagamentos nas configurações da carteira só têm 2 configurações principais. O pagamento é inválido se a transação falhar em confirmar em (minutos definidos) após a expiração da fatura. Considera-se a fatura confirmada quando a transação de pagamento tem X quantidade de confirmações. Os administradores também podem definir um interruptor para mostrar as taxas recomendadas nos pagamentos ou definir um alvo de confirmação manual no número de blocos.

![image](assets/en/20.webp)

**!Nota!**

Se você seguir este curso por conta própria, criar esta conta seria algo que você poderia fazer em um host de terceiros, portanto, novamente mencionamos para nunca usar esses como ambientes de produção, mas apenas para fins de treinamento.

### Exemplo

#### Configurar uma Carteira Bitcoin no BTCPay Server

O BTCPay Server permite duas maneiras de configuração de carteira. Uma maneira é importar uma carteira Bitcoin já existente. A importação pode ser feita Conectando uma carteira de hardware, importando um arquivo de carteira, inserindo uma Chave pública estendida, Escaneando o código QR de uma carteira, ou o menos favorável, inserindo uma semente de recuperação de carteira previamente criada manualmente. No BTCPay Server, também é possível criar uma nova carteira. Existem duas maneiras possíveis de configurar o BTCPay Server ao gerar uma nova carteira.
A opção de carteira quente (hot wallet) no BTCPay Server permite recursos como 'Payjoin' ou 'Liquid'. No entanto, há uma desvantagem: a semente de recuperação gerada para esta Carteira será armazenada no servidor, onde qualquer pessoa que tenha controle de Admin pode obter a semente de recuperação. Como sua chave privada é derivada da sua semente de recuperação, um ator malicioso poderia ganhar acesso aos seus fundos atuais e futuros!
Para mitigar tal risco no BTCPay Server, um Admin pode definir em Configurações do Servidor > Políticas > "Permitir que não-admins criem carteiras quentes para suas lojas" para não, como é por padrão. Para aumentar a segurança dessas carteiras quentes, o administrador do servidor deve habilitar a autenticação 2FA em contas autorizadas a ter carteiras quentes. Armazenar chaves privadas em um servidor público é perigoso e vem com riscos. Alguns são semelhantes aos riscos da Rede Lightning (veja o próximo capítulo para riscos da Rede Lightning).

A segunda opção que o BTCPay Server oferece na geração de uma nova carteira é criando uma carteira Somente-Leitura (Watch-Only wallet). O BTCPay Server irá gerar suas chaves privadas uma vez. Após o usuário confirmar que escreveu sua Frase Semente, o BTCPay Server irá apagar as chaves privadas do servidor. Como resultado, sua loja agora tem uma carteira Somente-Leitura conectada a ela. Para gastar os fundos recebidos em sua carteira Somente-Leitura, veja o capítulo Como Enviar, seja usando o BTCPay Server Vault, PSBT (transação bitcoin parcialmente assinada), ou, menos recomendado, fornecendo manualmente sua frase semente.

Você criou uma nova 'Loja' na última parte. O assistente de instalação continuará perguntando para "Configurar uma carteira" ou "Configurar um nó Lightning". Neste exemplo, você seguirá o processo do assistente "Configurar uma carteira" (1).

![image](assets/en/21.webp)

Após clicar em "Configurar uma carteira", o assistente continuará solicitando como você deseja prosseguir; o BTCPay Server agora oferece a opção de conectar uma carteira Bitcoin existente à sua nova loja. Se você não tem uma carteira, o BTCPay Server propõe criar uma nova. Este exemplo seguirá os passos para “criar uma nova carteira” (2). Siga os passos para aprender como "Conectar uma carteira existente (1).

![image](assets/en/22.webp)

**!Nota!**

Se você tomar este curso em uma sala de aula, o exemplo atual e a semente que geramos é apenas para fins educacionais. Nunca deve haver qualquer quantia substancial além do necessário durante os exercícios nessas endereços.

(1) Continue o assistente de “Nova carteira” clicando no botão "Criar uma nova carteira".

![image](assets/en/23.webp)

(2) Após clicar em “Criar uma nova carteira”, a próxima janela no assistente dará as opções “Carteira Quente” e “Carteira Somente-Leitura”. Se você estiver acompanhando um instrutor, seu ambiente é uma Demonstração compartilhada, e você só pode criar uma Carteira Somente-Leitura. Observe a diferença entre as duas figuras abaixo. Como você está no ambiente de Demonstração acompanhando o instrutor, crie uma "Carteira Somente-Leitura" e continue com o assistente de "Nova Carteira".

![image](assets/en/24.webp)

![image](assets/en/25.webp)

(3) Continuando o assistente de nova carteira, você está agora na seção Criar carteira BTC Somente-Leitura. Aqui temos a opção de definir o tipo de endereço da carteira. O BTCPay Server permite que você escolha seu tipo de endereço preferido; até o momento da escrita deste curso, ainda é recomendado usar endereços bech32. Aprenda mais em detalhes sobre endereços no primeiro capítulo desta parte.

- Segwit (bech32)
- Native SegWit são endereços que começam com `bc1q`. - Exemplo: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Endereços Legacy são endereços que começam com o número `1`.
  - Exemplo: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (Para usuários avançados)
  - Endereços Taproot começam com `bc1p`.
  - Exemplo: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- Segwit embrulhado
  - Endereços Segwit embrulhados são endereços que começam com `3`.
  - Exemplo: `37BBXXXXXXXXXXXXXXX`

Escolha segwit (recomendado) como o tipo de endereço de carteira preferencial.

![imagem](assets/en/26.webp)

(4) Ao definir o parâmetro para a Carteira, o BTCPay Server permite que os usuários definam uma passphrase opcional através do BIP39, certifique-se de confirmar sua senha.

![imagem](assets/en/27.webp)

(5) Após definir o tipo de endereço da Carteira e possivelmente definir algumas opções avançadas, clique em Criar, e o BTCPay Server irá gerar sua nova Carteira. Note que este é o último passo antes de gerar sua frase-semente. Certifique-se de fazer isso em um ambiente onde outros não possam roubar a frase-semente olhando para sua tela.

![imagem](assets/en/28.webp)

(6) Na tela seguinte do assistente, o BTCPay Server mostra a frase-semente de recuperação para sua Carteira recém-gerada; estas são as chaves para recuperar sua Carteira e assinar transações. O BTCPay Server gera uma frase-semente de 12 palavras. Estas palavras serão apagadas do servidor após esta tela de configuração. Esta Carteira é especificamente uma carteira Somente-Visualização. É aconselhado não armazenar esta frase-semente digitalmente ou por imagem fotográfica. Os usuários podem prosseguir no assistente apenas se reconhecerem ativamente que anotaram sua frase-semente.

![imagem](assets/en/29.webp)

(7) Após clicar em Concluído e garantir a nova frase-semente de Bitcoin gerada, o BTCPay Server atualizará sua loja com a nova Carteira anexada e estará pronto para receber pagamentos. Na Interface do Usuário, no menu de navegação à esquerda, observe como o Bitcoin agora está destacado e ativado em Carteira.

![imagem](assets/en/30.webp)

### Exemplo: Anotando uma frase-semente

Este é um momento muito particular e seguro para usar Bitcoin. Como mencionado antes, apenas você deve ter acesso ou conhecimento sobre sua frase-semente. Ao seguir junto com um instrutor e sala de aula, a frase-semente gerada deve ser usada apenas neste curso. Muitos fatores, olhares curiosos dos colegas de classe, sistemas inseguros e muitos outros tornam essas chaves apenas educacionais e não confiáveis. No entanto, as chaves geradas ainda devem ser armazenadas para exemplos do curso.

O primeiro método que usaremos na situação atual, também o menos seguro, é anotar a frase-semente na ordem correta. Um cartão de frase-semente está no material do curso fornecido ao aluno ou encontrado no GitHub do BTCPay Server. Usaremos este cartão para anotar as palavras geradas no passo anterior. Certifique-se de escrevê-las na ordem correta. Depois de tê-las anotado, confira-as contra o que foi dado pelo software para garantir que você as escreveu na ordem correta. Depois de tê-las escrito, marque a caixa indicando que você anotou sua frase-semente corretamente.

### Exemplo: Armazenando uma frase-semente em uma Carteira de Hardware

Neste curso, abordamos o armazenamento de uma frase-semente em uma carteira de hardware. Seguir este curso por um instrutor pode nem sempre incluir tal dispositivo. No guia do curso, materiais escritos têm uma lista de carteiras de hardware fornecidas que se adequariam a este exercício.
Neste exemplo, utilizaremos o cofre do BTCPay Server e uma carteira de hardware Blockstream Jade.
Você também pode acompanhar por vídeo para referência sobre como conectar uma carteira de hardware.
![BTCPay Server - Como conectar sua carteira de hardware com o BTCPay Vault.](https://youtu.be/s4qbGxef43A)

Baixe o BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Certifique-se de baixar os arquivos corretos para o seu sistema. Usuários do Windows devem baixar o pacote [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), usuários de Mac baixam o [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), e usuários de Linux devem baixar [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

Após instalar o BTCPay Server Vault, inicie o software clicando no ícone na sua Área de Trabalho. Quando o BTCPay Server Vault for instalado corretamente e iniciado pela primeira vez, ele pedirá permissão para ser usado com Aplicações Web. Ele solicitará a concessão de acesso ao BTCPay Server específico com o qual você trabalha. Aceite estas condições. O BTCPay Server Vault agora procurará pelo dispositivo de hardware. Uma vez encontrado o dispositivo, o BTCPay Server reconhecerá que o Vault está em execução e capturou seu dispositivo.

**!Nota!**

Não forneça suas chaves SSH ou conta de administrador do servidor para mais ninguém, exceto administradores, ao usar uma carteira quente (hot wallet). Qualquer pessoa com acesso a essas contas terá acesso aos fundos na Carteira Quente.

### Resumo de Habilidades

Nesta seção, você aprendeu o seguinte:

- A visualização de transação da carteira Bitcoin e suas várias categorizações.
- As várias opções disponíveis ao enviar de uma carteira Bitcoin, de hardware a carteiras quentes.
- O problema do limite de lacuna enfrentado ao usar a maioria das carteiras e como corrigi-lo.
- Como gerar uma nova carteira Bitcoin dentro do BTCPay Server, incluindo armazenar as chaves em uma carteira de hardware e fazer backup da frase de recuperação.

Neste objetivo, você aprendeu como gerar uma nova carteira Bitcoin dentro do BTCPay Server. Ainda não entramos em como proteger ou usar essas chaves. Em uma visão geral rápida deste objetivo, você aprendeu como configurar a primeira loja. Você aprendeu como gerar uma frase de Recuperação de Semente Bitcoin.

### Avaliação de Conhecimento Revisão Prática

Descreva um método para gerar chaves e um esquema para protegê-las, junto com os trade-offs/risco do esquema de segurança.

## Carteira Lightning do BTCPay Server

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Quando um administrador de servidor provisiona uma nova instância do BTCPay Server, ele pode configurar uma implementação da rede Lightning, LND, Core Lightning ou Eclair; veja a Parte Configurando o BTCPay Server para instruções de instalação mais detalhadas.
Se seguido por uma sala de aula, conectar um nó Lightning ao seu BTCPay Server funciona através de um nó personalizado. Um usuário que não seja um administrador do servidor no BTCPay Server não poderá usar o nó Lightning interno por padrão. Isso é para proteger o proprietário do servidor de perder seus fundos. Os administradores do servidor podem instalar um Plugin para dar acesso ao seu nó Lightning através do LNBank; isso está fora do escopo deste livro; leia mais sobre o LNBank na página oficial do plugin.

### Conectar nó interno (administrador do servidor)

O Administrador do Servidor pode usar o Nó Lightning interno do BTCPay Server. Independentemente da implementação do Lightning, a conexão com o nó Lightning interno é a mesma.

Vá para uma loja configurada anteriormente e clique na carteira "Lightning" no menu à esquerda. O BTCPay Server oferece duas possibilidades de configuração, Usando o nó interno (apenas para o admin do servidor por padrão) ou um nó personalizado (conexão externa). Os administradores do servidor podem clicar na opção "Usar nó interno". Não é necessária mais configuração. Clique no botão "salvar" e observe a notificação dizendo, "Nó Lightning BTC atualizado". A loja agora obteve com sucesso capacidades da rede Lightning.

### Conectar nó externo (usuário da loja/proprietário da loja)

Como os proprietários de lojas, por padrão, não têm permissão para usar o Nó Lightning do administrador do servidor. A conexão precisa ser feita a um nó externo, seja um nó de propriedade do proprietário da loja antes de uma configuração do BTCPay Server, um plugin LNBank se disponibilizado pelo administrador do servidor, ou uma solução de custódia como Alby.

Vá para uma loja configurada anteriormente e clique em "Lightning" abaixo de carteiras no menu à esquerda. Como os proprietários de lojas não têm permissão para usar o nó interno por padrão, esta opção está esmaecida. Usar um nó personalizado é a única opção disponível por padrão para os proprietários de lojas.

O BTCPay Server precisa de informações de conexão; a solução feita anteriormente (ou de custódia) fornecerá essas informações específicas para uma implementação Lightning. Dentro do BTCPay Server, os proprietários de lojas podem usar as seguintes conexões;

- C-lightning via conexão TCP ou Unix domain socket.
- Lightning Charge via HTTPS
- Eclair via HTTPS
- LND via o proxy REST
- LNDhub via a API REST

![imagem](assets/en/31.webp)

Clique em "testar conexão" para garantir que você inseriu corretamente os detalhes da conexão. Após a confirmação de que a conexão está boa, clique em salvar, e o BTCPay Server mostra que a loja foi atualizada com um Nó Lightning.

### Gerenciando nó Lightning interno LND (Administrador do servidor)

Após conectar o Nó Lightning interno, os administradores do servidor notarão novos blocos no Dashboard especificamente para informações do Lightning.

- Saldo Lightning
- BTC em canais
  - BTC abrindo canais
  - Saldo local BTC
  - Saldo remoto BTC
  - BTC fechando canais
- BTC On-chain
  - BTC confirmado
  - BTC não confirmado
  - BTC reservado
- Serviços Lightning
  - Ride the Lightning (RTL).

Clicando tanto no Logo do Ride the Lightning no bloco "Serviços Lightning" quanto em "Lightning" abaixo de carteiras no menu à esquerda, os administradores do servidor podem acessar o RTL para gerenciamento do nó Lightning.

**Nota!**

Se a conexão com o Nó Lightning interno falhar - Se a conexão interna falhar, confirme:

1. O nó Bitcoin on-chain está totalmente sincronizado
2. O nó Lightning interno está "Habilitado" em "Lightning" > "Configurações" > "Configurações do BTC Lightning"
   Se você não consegue conectar ao seu nó Lightning, tente reiniciar seu servidor ou leia mais detalhes na documentação oficial do BTCPay Server; https://docs.btcpayserver.org/Troubleshooting/ . Você não pode aceitar pagamentos via Lightning em sua loja até que seu nó Lightning apareça como "Online". Tente testar sua conexão Lightning clicando no link "Informações do Nó Público"

### Carteira Lightning

Na opção de carteira Lightning na barra de menu à esquerda, os administradores do servidor encontrarão fácil acesso ao RTL, suas Informações do Nó Público e configurações específicas de Lightning para sua loja BTCPay Server.

#### Informações internas do nó

Os administradores do servidor podem clicar nas informações internas do nó e verificar o status do seu servidor (Online/Offline) e a string de conexão para Clearnet ou Tor.

![imagem](assets/en/32.webp)

#### Alterar conexão

Se o proprietário da loja decidir usar alterações nas Configurações de Lightning - Alterar conexão.
Ao lado das informações do Nó Público da loja, os proprietários podem encontrar esta opção. Isso retornará à configuração inicial para a conexão do nó lightning externo, preencha as novas informações do nó Lightning, clique em salvar e atualize a loja com as novas informações do nó.

![imagem](assets/en/33.webp)

#### Serviços

Se o administrador do servidor decidir instalar múltiplos serviços para a implementação Lightning, eles serão listados aqui. Com uma implementação padrão de LND, os administradores terão o Ride The Lightning (RTL) como uma ferramenta padrão para gerenciamento do nó.

#### Configurações da carteira BTC Lightning

Após adicionar o nó Lightning à loja em uma etapa anterior, dentro das configurações da carteira Lightning, os proprietários da loja ainda podem escolher desativá-la para sua loja usando o Toggle no topo das configurações de Lightning.

![imagem](assets/en/34.webp)

#### Opções de pagamento Lightning

Os proprietários da loja podem definir parâmetros para melhorar a experiência Lightning para seus clientes.

- Exibir quantias de pagamento Lightning em Satoshis.
- Adicionar dicas de salto para canais privados à fatura Lightning.
- Unificar URLs/códigos QR de pagamento on-chain e Lightning no checkout.
- Definir um modelo de descrição para faturas Lightning.

#### LNURL

Os proprietários da loja podem escolher usar ou não o LNURL. Uma URL da Rede Lightning, ou LNURL, é um padrão proposto para interações entre o pagador e o recebedor Lightning. Resumidamente, um LNURL é uma url codificada em bech32 prefixada com lnurl. Espera-se que a carteira Lightning decodifique a URL, contate a URL e aguarde um objeto JSON com mais instruções, mais notavelmente uma tag definindo o comportamento do lnurl.

- Habilitar LNURL
- Modo Clássico LNURL
  - Para compatibilidade de carteira, Bech32 codificado (clássico) vs URL em texto claro (próximo)
- Permitir que o recebedor passe um comentário.

### Exemplo 1

#### Conectar ao Lightning com o nó interno (Administrador)

Esta opção só está disponível se você for o Administrador desta instância ou se o Administrador alterou as configurações padrão onde os usuários podem usar o nó lightning interno.

Como administrador, clique na Carteira Lightning na barra de menu à esquerda. O BTCPay Server pedirá para usar uma das duas opções para conectar um Nó Lightning, um nó Interno ou um nó externo personalizado. Clique em Usar nó interno e clique em salvar.

#### Gerenciando seu nó Lightning (RTL)

Após conectar ao nó lightning interno, o BTCPay Server será atualizado e mostrará uma notificação "Nó Lightning BTC atualizado", confirmando que você agora conectou Lightning à sua loja.

Gerenciar o nó lightning é uma tarefa para o Administrador do servidor. Isso envolve.

- Gerenciar transação
- Gerenciar liquidez
  - Liquidez de entrada
  - Liquidez de saída
- Gerenciar pares e canais
  - Pares conectados
  - Taxas do canal
  - Status do canal
- Fazer backups frequentes dos estados do canal.
- Verificar relatórios de roteamento
- Alternativamente, usar serviços como o Loop.

Todo gerenciamento de nó Lightning é feito como padrão com RTL (assumindo que você está executando uma implementação LND). Os administradores podem clicar na sua Lightning Wallet no BTCPay Server e encontrar um botão para abrir o RTL. O principal Dashboard do BTCPay Server agora está atualizado com os Tiles da Lightning Network, incluindo acesso rápido ao RTL.

### Exemplo 2

#### Conectar ao lightning com Alby

Ao conectar com um custodiante como o Alby, os proprietários de loja devem primeiro criar uma conta, visite: https://getalby.com/

![imagem](assets/en/35.webp)

Após criar a conta Alby, vá para a sua loja BTCPay Server.

Passo 1: Clique em 'Configurar um nó Lightning' no Dashboard ou 'Lightning' abaixo de carteiras.

![imagem](assets/en/36.webp)

Passo 2: Insira suas credenciais de conexão da carteira fornecidas pelo Alby. No Dashboard do Alby, clique em Carteira. Aqui você encontrará "Credenciais de Conexão da Carteira". Copie essas credenciais. Cole as credenciais do Alby no campo de configuração de Conexão no BTCPay Server.

![imagem](assets/en/37.webp)

Passo 3: Após fornecer ao BTCPay Server os detalhes da Conexão, clique no botão "Testar Conexão" para garantir que a conexão está funcionando corretamente. Observe a mensagem "Conexão ao nó lightning bem-sucedida" no topo da sua tela. Isso confirma que tudo está em ordem.

![imagem](assets/en/38.webp)

Passo 4: Clique em salvar, e sua loja agora está conectada com um nó lightning pelo Alby.

![imagem](assets/en/39.webp)

**!Nota!**

Nunca confie em uma solução Lightning custodiante com mais valor do que você está disposto a perder.

### Resumo de Habilidades

Nesta seção você aprendeu:

- Como conectar um nó Lightning interno ou externo
- Os conteúdos e função de diversos Tiles relacionados ao Lightning no Dashboard
- Como configurar a carteira Lightning usando Voltage Surge ou Alby

### Avaliação de Conhecimento Revisão Prática

Descreva algumas das várias opções para conectar uma carteira Lightning à sua loja.

# Interface do BTCPay Server

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Visão geral do Dashboard

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

O BTCPay Server é um pacote de software modular. No entanto, existem padrões que todo BTCPay Server terá e o Administrador/usuários interagirão com. Começando pelo Dashboard. O principal ponto de entrada de todo BTCPay Server após fazer login. O Dashboard oferece uma visão geral de como sua loja está se saindo, o saldo atual da carteira e as últimas transações nos últimos 7 dias. Como é uma visão modular, Plugins podem utilizar esta visão para seu benefício e criar seus próprios tiles no Dashboard. Para este livro de curso, falaremos apenas sobre plugins/apps padrão e suas respectivas visões ao longo do BTCPay Server.

### Tiles do Dashboard

Dentro da visão principal do dashboard do BTCPay Server, há alguns tiles padrão disponíveis. Esses tiles são destinados para o Proprietário da loja ou Administrador gerenciar sua loja em uma visão geral rapidamente.

- Saldo da carteira
- Atividade de transação
- Saldo Lightning (se Lightning está habilitado na loja)
- Serviços Lightning (se Lightning está habilitado na loja)
- Transações recentes.
- Faturas recentes
- Crowdfunds ativos atuais
- Desempenho da loja / itens mais vendidos.

### Saldo da carteira

O bloco de Saldo da Carteira oferece uma visão rápida dos fundos e do desempenho da sua carteira. Pode ser visualizado em BTC ou em moeda Fiat em um gráfico semanal, mensal ou anual.
![image](assets/en/40.webp)

### Atividade de Transação

Ao lado do bloco de Saldo da Carteira, o BTCPay Server mostra uma visão rápida dos Pagamentos pendentes, a quantidade de Transações nos últimos 7 dias e se a sua loja emitiu algum reembolso. Clicar no botão Gerenciar leva você ao gerenciamento de pagamentos pendentes (saiba mais sobre pagamentos no BTCPay Server - capítulo de Pagamentos).

![image](assets/en/41.webp)

### Saldo Lightning

Isso só é visível quando o Lightning está ativado.

Quando o Administrador permite o acesso à rede Lightning, o painel do BTCPay Server agora tem um novo bloco com informações do seu nó Lightning. Quanto de BTC está nos canais, como isso está balanceado local ou remotamente (liquidez de entrada ou saída), se os canais estão fechando ou abrindo e quanto de bitcoin é mantido on-chain no nó lightning.

![image](assets/en/42.webp)

### Serviços Lightning

Isso só é visível quando o lightning está ativo.

Ao lado de ver seu saldo Lightning no painel do BTCPay Server, os administradores também verão o bloco para Serviços Lightning. Aqui, os administradores podem encontrar botões rápidos para ferramentas que usam para gerenciar seu nó Lightning; por exemplo, Ride the Lightning é uma das ferramentas padrão com o BTCPay Server para gerenciamento de nó Lightning.

![image](assets/en/43.webp)

### Transações Recentes

O bloco de transações recentes mostrará as transações mais recentes da sua loja. Com um clique, o Administrador da instância do BTCPay Server pode agora ver a última transação e verificar se é necessário dar atenção a ela.

![image](assets/en/44.webp)

### Faturas Recentes

O bloco de faturas recentes mostra as 6 últimas faturas geradas pelo seu BTCPay Server, incluindo Status e valor da fatura. O bloco também inclui um botão "Ver todos" para acessar facilmente a visão geral completa da Fatura.

![image](assets/en/45.webp)

### Ponto de Venda e Financiamentos Coletivos

Como o BTCPay Server oferece um conjunto de plugins ou aplicativos padrão, Ponto de Venda e Financiamento Coletivo são os dois principais plugins do BTCPay Server. Com cada loja e carteira, um usuário do BTCPay Server pode gerar tantos Pontos de Venda ou Financiamentos Coletivos quanto desejar. Cada um criará um novo bloco no painel mostrando o desempenho dos plugins.

![image](assets/en/46.webp)

Note a pequena diferença entre um bloco de Ponto de Venda e de Financiamento Coletivo. O Administrador vê os itens mais vendidos no bloco de Ponto de Venda. No bloco de Financiamento Coletivo, isso se torna Principais Vantagens. Ambos os blocos têm botões rápidos para gerenciar o aplicativo respectivo e visualizar faturas recentes criadas pelos itens mais vendidos ou principais vantagens.

![image](assets/en/47.webp)

**!?Nota!?**

Gráficos de saldo e transações recentes estão disponíveis apenas para um método de pagamento on-chain. Informações sobre saldos e transações da Rede Lightning estão na lista de tarefas. A partir da Versão 1.6.0 do BTCPay Server, saldos básicos da Rede Lightning estão disponíveis.

### Resumo de Habilidades

Nesta seção, você aprendeu o seguinte:

- O layout principal dos blocos na página inicial é conhecido como Dashboard.
- Um entendimento básico do conteúdo de cada bloco.

### Revisão da Avaliação de Conhecimento

Liste tantos blocos quanto puder lembrar do Dashboard.

## BTCPay Server - Configurações da Loja

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>
No software BTCPay Server, conhecemos 2 tipos de configurações. Configurações específicas da loja BTCPay Server, o botão de configurações encontrado na barra de menu à esquerda abaixo do Dashboard, e configurações do BTCPay Server, encontradas na parte inferior da barra de menu logo acima de Conta. As configurações específicas do servidor BTCPay Server só podem ser visualizadas pelos administradores do servidor.
As configurações da loja consistem em várias abas para categorizar cada conjunto de configurações.

- Geral
- Taxas
- Aparência do Checkout
- Tokens de Acesso
- Usuários
- Funções
- Webhooks
- Processadores de Pagamento
- Emails
- Formulários

### Geral

Na aba de Configurações Gerais, os proprietários da loja definem sua marca e os padrões de pagamento. Na configuração inicial da loja, um nome para a loja foi dado; isso será refletido nas configurações Gerais sob Nome da Loja. Aqui, o proprietário da loja também pode definir seu site para corresponder à marca e um ID da Loja para o Administrador reconhecer no banco de dados.

#### Branding

Como o BTCPay Server é FOSS, um proprietário de loja pode fazer a personalização da marca para corresponder à sua loja. Defina a cor da marca, armazene os logotipos da sua marca e adicione CSS personalizado para páginas voltadas para o público/cliente (Faturas, Pedidos de Pagamento, Pagamentos Pull)

#### Pagamento

Nas configurações de pagamentos, os proprietários da loja definem a moeda padrão da loja (seja em Bitcoin ou em qualquer moeda fiduciária).

#### Permitir que qualquer um crie faturas

Esta configuração é destinada a desenvolvedores ou construtores em cima do BTCPay Server. Com essa configuração ativada para sua loja, ela permite que o mundo externo crie faturas na sua instância do BTCPay Server.

#### Adicionar taxa adicional (taxa de rede) às faturas

Uma funcionalidade dentro do BTCPay para proteger os comerciantes de ataques de dust ou clientes que geram um alto custo em taxas mais tarde, quando o comerciante precisa mover uma grande quantidade de bitcoin de uma só vez. Por exemplo, o cliente criou uma fatura de 20$ e pagou parcialmente, pagando 1$ 20 vezes até que a fatura fosse totalmente paga. O comerciante agora tem uma transação maior, aumentando o custo de mineração caso o comerciante decida mover esses fundos mais tarde. Por padrão, o BTCPay aplica um custo de rede adicional ao valor total da fatura para cobrir essa despesa para o comerciante quando a fatura é paga em várias transações. O BTCPay oferece várias opções para personalizar esse recurso de proteção. Você pode aplicar uma taxa de rede:

- Apenas se o cliente fizer mais de um pagamento para a fatura (No exemplo acima, se o cliente criou uma fatura de 20\$ e pagou 1\$, o total devido da fatura é agora de 19\$ + a taxa de rede. A taxa de rede é aplicada após o primeiro pagamento)
- Em cada pagamento (incluindo o primeiro pagamento, no nosso exemplo, o total será de 20\$ + taxa de rede imediatamente, mesmo no primeiro pagamento)
- Nunca adicionar taxa de rede (desativa completamente a taxa de rede)

Embora proteja contra transações dust, isso também pode refletir negativamente nos negócios se não for comunicado adequadamente. Os clientes podem ter perguntas adicionais e pensar que estão sendo cobrados a mais.

#### A fatura expira se o valor total não for pago após?

O temporizador da fatura é definido para 15 minutos por padrão. O temporizador é um mecanismo de proteção contra a volatilidade, pois bloqueia a quantidade de Bitcoin de acordo com as taxas de Bitcoin para fiat. Se o cliente não pagar a fatura dentro do período definido, a fatura é considerada expirada. A fatura é considerada "paga" assim que a transação é visível na blockchain (0-confirmações) mas considerada "completa" quando atinge o número de confirmações definido pelo comerciante (geralmente, 1-6). O temporizador é personalizável por minutos.

#### Considerar a fatura paga mesmo se o valor pago for X% menor do que o esperado?

Quando um cliente usa uma carteira de câmbio para pagar diretamente por uma fatura, a bolsa de valores cobra uma pequena taxa. Isso significa que tal fatura não é considerada totalmente concluída. A fatura recebe o status de "paga parcialmente". Você pode definir a taxa percentual aqui se um comerciante deseja aceitar faturas subpagas.

### Taxas

No BTCPay Server, quando uma fatura é gerada, ela sempre precisa do preço mais atualizado e preciso de Bitcoin para fiat. Ao criar uma nova loja no BTCPay Server, os administradores são solicitados a definir sua fonte de preço preferida; após a configuração da loja, os proprietários da loja podem sempre alterar sua fonte de preço nesta aba.

#### Regras avançadas de taxas de script

Principalmente usado por usuários avançados. Se ativado, os proprietários de lojas podem criar scripts sobre o comportamento de preço e como cobrar de seus clientes.

#### Testes

Um local rápido para testar seus pares de moedas preferidos. Isso também inclui um recurso para verificar pares de moedas padrão via consulta REST.

### Aparência do Checkout

A aba de Aparência do Checkout começa com configurações específicas da fatura e um método de pagamento padrão e habilita métodos de pagamento específicos quando os requisitos definidos são atendidos.

#### Configurações da fatura

Métodos de pagamento padrão. O BTCPay Server, em uma configuração padrão, tem três opções.

- BTC (on-chain)
- BTC (LNURL-pay)
- BTC (Off-chain & Lightning)

Podemos definir parâmetros para nossa loja, onde um cliente só interagirá com Lightning quando o preço for menor que X quantidade e vice-versa para transações On-chain quando X for maior que Y sempre apresentar a opção de pagamento On-chain.

![imagem](assets/en/48.webp)

#### Checkout

A partir do lançamento do BTCPay Server 1.7, foi introduzida uma nova interface de Checkout, Checkout V2, como é chamada. Desde o lançamento 1.9 foi padronizado, administradores e proprietários de lojas ainda podem definir o checkout para o lançamento anterior. Usando a alternância "Use o checkout clássico", um proprietário de loja pode retornar a loja para a experiência de checkout anterior. O BTCPay Server também tem um conjunto selecionado de predefinições para comércio online ou uma experiência na loja.

![imagem](assets/en/49.webp)

Quando um cliente interage com a loja e gera uma fatura, há um tempo de expiração para a fatura. Por padrão, o BTCPay Server define isso para 5 minutos, e o Administrador pode definir isso conforme achar adequado. A página de checkout pode ser ainda mais personalizada verificando os seguintes parâmetros:

- Celebrar o pagamento mostrando confete
- Mostrar o cabeçalho da loja (Nome e logo)
- Mostrar o botão "Pagar na carteira"
- Unificar URLs/Códigos QR de pagamentos on-chain e off-chain
- Exibir quantias de pagamento Lightning em Satoshis
- Auto-detectar idioma no checkout

![imagem](assets/en/50.webp)

Quando a detecção automática de idioma não está configurada, o BTCPay Server, por padrão, exibirá em inglês. Um proprietário de loja pode alterar esse padrão para o idioma de sua preferência.

![imagem](assets/en/51.webp)

Clique no menu suspenso e os proprietários da loja podem definir um título HTML personalizado para ser exibido na página de checkout.

![imagem](assets/en/52.webp)

Para garantir que o cliente conheça seu método de pagamento, um proprietário de loja pode definir explicitamente seu checkout para sempre exigir que os usuários escolham seu método de pagamento preferido. Quando a fatura é paga, o BTCPay Server permite que o cliente retorne à loja online. Os proprietários da loja podem configurar esse redirecionamento após o cliente ter pago automaticamente.

![imagem](assets/en/53.webp)

#### Recibo público

Dentro das configurações de recibo público, um proprietário de loja pode definir as páginas de recibo para o público e mostrar a lista de pagamentos na página de recibo e o código QR do recibo para que o cliente possa acessá-lo digitalmente com facilidade.

### Tokens de Acesso

Tokens de acesso são utilizados para pareamento com certas integrações de e-commerce ou integrações personalizadas.

### Usuários

Usuários da loja é onde o proprietário da loja pode gerenciar seus membros da equipe, suas contas e acesso à loja. Após os membros da equipe criarem suas contas, o proprietário da loja pode adicionar usuários específicos à loja como Usuários Convidados ou proprietários. Para definir ainda mais o papel do membro da equipe, consulte a próxima seção sobre "Configurações da Loja no BTCPay Server - Funções."

### Funções

Um proprietário de loja pode não encontrar as funções padrão dos usuários suficientemente significativas. Nas configurações de funções personalizadas, um proprietário de loja pode definir as necessidades exatas para cada função em seu negócio.

(1) Para criar uma nova função, clique no botão "+ Adicionar função".

(2) Insira um nome para a Função, por exemplo, "Caixa".

(3) Configure as permissões individuais para a função.

- Modificar suas lojas.
- Gerenciar contas de câmbio vinculadas às suas lojas.
  - Visualizar contas de câmbio vinculadas às suas lojas.
- Gerenciar seus pagamentos recorrentes.
- Criar pagamentos recorrentes.
  - Criar pagamentos recorrentes não aprovados.
- Modificar faturas.
  - Visualizar faturas.
  - Criar uma fatura.
  - Criar faturas a partir dos nós lightning associados às suas lojas.
- Visualizar suas lojas.
  - Visualizar faturas.
  - Visualizar seus pedidos de pagamento.
  - Modificar webhooks das lojas.
- Modificar seus pedidos de pagamento.
  - Visualizar seus pedidos de pagamento.
- Usar os nós lightning associados às suas lojas.
  - Visualizar as faturas lightning associadas às suas lojas.
  - Criar faturas a partir dos nós lightning associados às suas lojas.
- Depositar fundos em contas de câmbio vinculadas às suas lojas.
- Retirar fundos de contas de câmbio para sua loja.
- Negociar fundos nas contas de câmbio da sua loja.

Quando a função é criada, o nome é fixado e não pode ser alterado depois no modo de edição.

### Webhooks

Dentro do BTCPay Server, é relativamente fácil fazer um novo "Webhook". Nas configurações da Loja BTCPay Server - aba Webhooks, um proprietário de loja pode facilmente criar um novo webhook clicando em "+ Criar Webhook". Webhooks permitem que o BTCPay Server envie eventos HTTP relacionados à sua loja para outros servidores ou integrações de e-commerce.

Você está agora na visualização para criar um Webhook. Certifique-se de conhecer seu URL de Payload e cole isso no seu BTCPay Server. Enquanto você cola o URL do payload, abaixo dele mostra o segredo do webhook. Copie o segredo do webhook e forneça-o no endpoint. Quando tudo estiver configurado, você pode alternar no BTCPay Server para Redelivery Automático. Tentaremos redeliver qualquer entrega falhada após 10 segundos, 1 minuto e até 6 vezes após 10 minutos. Você pode alternar entre cada evento ou especificar os eventos de acordo com suas necessidades. Certifique-se de habilitar o webhook e clique em Adicionar webhook para salvá-lo.

Webhooks não são feitos para ser compatíveis com a API Bitpay. Existem dois IPNs separados (nos termos da BitPay: "Notificações de Pagamento Instantâneo") no BTCPay Server.

- Webhook
- Notificações

Use apenas URL de Notificação quando você criar faturas através da api Bitpay.

### Processadores de Pagamento

Processadores de pagamento trabalham em conjunto com o conceito de Pagamentos no BTCPay Server. Um agregador de pagamentos para agrupar múltiplas transações e enviá-las de uma vez. Com processadores de pagamento, um proprietário de loja pode automatizar os pagamentos agrupados. O BTCPay Server oferece dois métodos de pagamentos automatizados, On-chain e Off-chain (LN).
O proprietário da loja pode clicar e configurar ambos os processadores de pagamento separadamente. Um proprietário de loja pode querer executar o processador on-chain apenas uma vez a cada X horas, enquanto o off-chain pode ser executado a cada poucos minutos. Para On-chain, você também pode definir um alvo para qual bloco ele deve ser incluído. Por padrão, isso é definido como 1 (ou o próximo bloco disponível). Note que configurar o processador de pagamento Off-chain só tem o temporizador de intervalo e nenhum alvo de bloco. Os pagamentos da rede Lightning são instantâneos.

![imagem](assets/en/62.webp)
![imagem](assets/en/63.webp)

Proprietários de loja só podem configurar o processador on-chain se tiverem uma Hot-wallet conectada à sua loja.

![imagem](assets/en/64.webp)

Após configurar um Processador de Pagamento, você pode rapidamente remover ou modificá-lo retornando à aba de Processador de Pagamento nas configurações da Loja no BTCPay Server.

**!?Nota!?**

Processador de pagamento on-chain - O processador de pagamentos on-chain só pode funcionar em uma loja configurada com uma Hot wallet conectada. Se não houver uma hot wallet conectada, o BTCPay Server não possui as chaves da carteira e não será capaz de processar os pagamentos automaticamente.

### Emails

O BTCPay Server pode usar Emails para Notificações ou, quando configurado corretamente, para recuperar contas que foram criadas na instância, já que o BTCPay Server padrão não envia um email quando a senha é perdida, por exemplo.

![imagem](assets/en/65.webp)

Antes de um proprietário de loja poder configurar regras de Email para disparar em eventos específicos de sua loja, precisamos configurar algumas configurações básicas de email. O BTCPay Server precisa dessas configurações para enviar emails para eventos baseados em sua loja ou para redefinições de senha.

O BTCPay Server facilitou o preenchimento dessas informações usando a opção "Preenchimento Rápido":

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

Usando a opção de preenchimento rápido, o BTCPay Server preencherá previamente os campos para o servidor SMTP e porta; agora, o proprietário da loja só precisa preencher suas credenciais em um endereço de Email, Login (que geralmente é igual ao seu endereço de email) e sua senha. A opção avançada que o BTCPay Server oferece nas configurações de email é Desativar verificações de segurança do Certificado TLS; por padrão, isso está Ativado.

![imagem](assets/en/66.webp)

Com regras de Email, um proprietário de loja pode definir eventos específicos para disparar emails para endereços de email específicos.

- Fatura Criada
- Fatura Recebeu Pagamento
- Fatura em Processamento
- Fatura Expirada
- Fatura Resolvida
- Fatura Inválida
- Pagamento da Fatura Resolvido

Se o cliente forneceu um endereço de Email, esses gatilhos também podem enviar as informações para o cliente. Proprietários de loja podem preencher previamente a linha de Assunto para deixar claro por que este Email aconteceu e qual gatilho o causou.

![imagem](assets/en/67.webp)

### Formulários

Como o BTCPay Server não coleta nenhum dado, um proprietário de loja pode querer adicionar um formulário personalizado à sua experiência de checkout; desta forma, o proprietário da loja pode coletar informações adicionais de seu cliente. O construtor de Formulários do BTCPay Server consiste em duas partes, uma visual e uma visão mais avançada em código dos formulários.
Ao criar um novo formulário, o BTCPay Server abre uma nova janela solicitando informações básicas sobre o que você deseja que seu novo formulário solicite. Inicialmente, o proprietário da loja precisa dar um nome claro ao seu novo formulário, este nome NÃO pode ser alterado após a definição.

![image](assets/en/68.webp)

Após o proprietário da loja dar um nome ao formulário, você também pode ativar a opção "Permitir formulário para uso público" para LIGADO, e ela se torna verde. Isso é para que o formulário seja usado em todos os lugares voltados para o cliente. Por exemplo, se um proprietário de loja cria uma fatura separada não através do seu Ponto de Venda, ele ainda pode querer coletar as informações do cliente; essa opção para LIGADO permite que essas informações sejam coletadas.

![image](assets/en/69.webp)

Todo formulário começa com pelo menos 1 novo campo de formulário. Um proprietário de loja pode escolher qual o tipo de campo deve ser;

- Texto
- Número
- Senha
- Email
- URL
- Números de telefone
- Data
- Campos ocultos
- Conjunto de campos
- Uma área de texto para comentários abertos.
- Seletor de opção

Cada tipo vem com seus parâmetros para preencher. O proprietário da loja pode configurá-lo ao seu gosto. Abaixo do primeiro campo criado, os proprietários de lojas podem continuar adicionando novos campos a este único formulário.

![image](assets/en/70.webp)

#### Formulários personalizados avançados

O BTCPay Server também permite que você construa Formulários em código. JSON, em particular. Em vez de olhar para o editor, os proprietários de lojas podem clicar no botão CÓDIGO ao lado do editor e entrar no código de seus Formulários. Em uma definição de campo, apenas os seguintes campos podem ser definidos; os valores dos campos são armazenados nos metadados da fatura:

| Campo                 | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | Se verdadeiro, o .value deve ser definido na definição do formulário, e o usuário não poderá alterar o valor do campo. (exemplo: a versão da definição do formulário)                                                                                                                                                                                                                                                                                                                            |
| .fields.type          | O tipo de entrada HTML texto, rádio, caixa de seleção, senha, oculto, botão, cor, data, data-hora-local, mês, semana, tempo, email, número, intervalo, pesquisa, url, seleção, tel                                                                                                                                                                                                                                                                                                               |
| .fields.options       | Se .fields.type for seleção, a lista de valores selecionáveis                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.options.text  | O texto exibido para esta opção                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.options.value | O valor do campo se esta opção for selecionada                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| .fields.type=fieldset | Cria um conjunto de campos HTML ao redor dos .fields.fields (veja abaixo)                                                                                                                                                                                                                                                                                                                                                                                                                        |
| .fields.name          | O nome da propriedade JSON do campo conforme aparecerá nos metadados da fatura                                                                                                                                                                                                                                                                                                                                                                                                                   |
| .fields.value         | O valor padrão do campo                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| .fields.required      | Se verdadeiro, o campo será obrigatório                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| .fields.label         | A etiqueta do campo                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.helpText      | Texto adicional para fornecer uma explicação para o campo.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| .fields.fields        | Você pode organizar seus campos em uma hierarquia, permitindo que campos filhos sejam aninhados dentro dos metadados da fatura. Esta estrutura pode ajudá-lo a organizar e gerenciar melhor as informações coletadas, tornando-as mais fáceis de acessar e interpretar. Por exemplo, se você tem um formulário que coleta informações do cliente, você pode agrupar os campos sob um campo pai chamado cliente. Dentro deste campo pai, você pode ter campos filhos como nome, Email e endereço. |

O nome do campo representa o nome da propriedade JSON que armazena o valor fornecido pelo usuário nos metadados da fatura. Alguns nomes bem conhecidos podem ser interpretados e modificar as configurações da fatura.

| Nome do campo    | Descrição         |
| ---------------- | ----------------- |
| invoice_amount   | O valor da fatura |
| invoice_currency | A moeda da fatura |

Você pode preencher previamente os campos de uma fatura automaticamente adicionando strings de consulta à URL do formulário, como "?your_field=value".

Aqui estão alguns casos de uso para esta funcionalidade:

- Auxiliando a entrada do usuário: Preencher previamente os campos com informações conhecidas do cliente para facilitar o preenchimento do formulário. Por exemplo, se você já conhece o endereço de email de um cliente, você pode preencher previamente o campo de email para economizar tempo dele.
- Personalização: Personalizar o formulário com base nas preferências do cliente ou segmentação. Por exemplo, se você tem diferentes níveis de clientes, você pode preencher previamente o formulário com dados relevantes, como seu nível de associação ou ofertas específicas.
- Rastreamento: Rastrear a origem das visitas dos clientes usando campos ocultos e valores preenchidos previamente. Por exemplo, você pode criar links com valores utm_media preenchidos previamente para cada canal de marketing (por exemplo, Twitter, Facebook, Email). Isso ajuda a analisar a eficácia dos seus esforços de marketing.
- Testes A/B: Preencher previamente os campos com diferentes valores para testar diferentes versões do formulário, permitindo otimizar a experiência do usuário e as taxas de conversão.

### Resumo de Habilidades

Nesta seção, você aprendeu o seguinte:

- O layout e as funções das abas nas Configurações da Loja
- Uma infinidade de opções para ajustar o tratamento de taxas de câmbio subjacentes, pagamentos parciais, pequenos pagamentos insuficientes e mais.
- Personalizar a aparência do checkout, incluindo habilitação da cadeia principal dependente do preço vs. Lightning em faturas.
- Gerenciar níveis de acesso à loja e permissões entre papéis.
- Configurar emails automáticos e seus gatilhos
- Criar formulários personalizados para coletar informações adicionais do cliente no checkout.

### Avaliações de Conhecimento

#### Revisão de KA

Qual é a diferença entre Configurações da Loja e Configurações do Servidor?

#### Hipotético de KA

Descreva algumas opções que você pode selecionar em Aparência do Checkout > Configurações da Fatura, e por quê.

## BTCPay Server - Configurações do Servidor

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

O BTCPay Server consiste em duas diferentes visões de configurações. Uma é dedicada às Configurações da Loja e outra para as Configurações do Servidor. A última só está disponível se você for um administrador do Servidor e não para os proprietários da loja. Os administradores do servidor podem adicionar usuários, criar papéis personalizados, configurar o servidor de email, definir políticas, executar tarefas de manutenção, verificar todos os serviços anexados ao BTCPay Server, fazer upload de arquivos para o servidor ou verificar Logs.

### Usuários

Como mencionado na parte anterior, os Administradores do Servidor podem convidar usuários para o seu servidor, adicionando-os à aba Usuários.

### Papéis customizados em todo o Servidor

O BTCPay Server conhece dois tipos de papéis customizados, os papéis customizados específicos da loja e os Papéis Customizados em todo o Servidor nas configurações do BTCPay Server. Ambos possuem um conjunto similar de permissões; no entanto, se definido através da aba Configurações do BTCPay Server - Papéis, o papel aplicado será em todo o servidor e aplicará a múltiplas lojas. Observe uma etiqueta "Em todo o servidor" nos papéis customizados nas configurações do Servidor.

### Funções Personalizadas em Todo o Servidor

Conjunto de permissões para funções personalizadas em todo o servidor:

- Modificar suas lojas.
- Gerenciar contas de câmbio vinculadas às suas lojas.
  - Visualizar contas de câmbio vinculadas às suas lojas.
- Gerenciar seus pagamentos programados.
- Criar pagamentos programados.
  - Criar pagamentos programados não aprovados.
- Modificar faturas.
  - Visualizar faturas.
  - Criar uma fatura.
  - Criar faturas a partir dos nós lightning associados às suas lojas.
- Visualizar suas lojas.
  - Visualizar faturas.
  - Visualizar seus pedidos de pagamento.
  - Modificar webhooks das lojas.
- Modificar seus pedidos de pagamento.
  - Visualizar seus pedidos de pagamento.
- Usar os nós lightning associados às suas lojas.
  - Visualizar as faturas lightning associadas às suas lojas.
  - Criar faturas a partir dos nós lightning associados às suas lojas.
- Depositar fundos em contas de câmbio vinculadas às suas lojas.
- Retirar fundos de contas de câmbio para sua loja.
- Negociar fundos nas contas de câmbio da sua loja.

**!?Nota!?**

Quando a função é criada, o nome é fixado e não pode ser alterado depois no modo de edição.

### Email

As configurações de Email em Todo o Servidor são semelhantes às configurações de Email Específicas da Loja. No entanto, esta configuração não trata apenas de disparadores para lojas ou registros de administrador. Esta configuração de Email também disponibiliza a recuperação de senha no BTCPay Server no Login. Funciona de maneira semelhante às configurações Específicas da Loja; os administradores podem preencher rapidamente seus parâmetros de Email e inserir suas credenciais de email, e o servidor agora pode enviar emails.

### Políticas

Os administradores de políticas do BTCPay Server podem definir algumas configurações sobre tópicos como Configurações de Usuários Existentes, Configurações de Novos Usuários, Configurações de Notificações e Configurações de Manutenção. Estas são destinadas para registrar novos usuários como administradores ou usuários normais ou até mesmo ocultar o BTCPay Server dos motores de busca adicionando ao cabeçalho do seu servidor.

#### Configurações de Usuários Existentes

As opções disponíveis aqui são separadas das funções personalizadas. Estas permissões extras podem tornar uma loja ou proprietário de loja vulneráveis a ataques. Políticas que podem ser adicionadas a usuários existentes:

- Permitir que não-administradores usem o nó Lightning interno em suas lojas.
  - Isso permitiria que os proprietários de lojas usassem o nó Lightning do administrador do servidor e, portanto, seus fundos! Cuidado, isso não é uma solução para dar acesso ao Lightning.
- Permitir que não-administradores criem carteiras quentes para suas lojas.
  - Isso permitiria que qualquer pessoa com uma conta na sua instância do BTCPay Server criasse carteiras quentes e armazenasse sua semente de recuperação no servidor do Administrador. Isso pode tornar o Administrador responsável por guardar fundos de terceiros!
- Permitir que não-administradores importem carteiras quentes para suas lojas.
  - Semelhante ao tópico anterior sobre criar carteiras quentes, esta política permite importar uma carteira quente, com os mesmos perigos mencionados na seção de criação de carteiras quentes.

#### Configurações de Novos Usuários

Podemos definir algumas configurações importantes para gerenciar novos usuários que chegam ao servidor. Podemos definir um email de confirmação para novos registros, Desativar a criação de novos usuários através da tela de login e restringir o acesso de não-administradores à criação de usuários através da API.

- Exigir um email de confirmação para registro.
  - O administrador do servidor deve ter configurado um servidor de Email!
- Desativar o registro de novos usuários no servidor
- Desativar o acesso de não-administradores ao endpoint de criação de usuários da API.

Por padrão, o BTCPay Server ativou a Desativação de registro de novos usuários e desativou o acesso de não-administradores ao endpoint de criação de usuários da API. Isso é por uma questão de segurança, onde nenhuma pessoa aleatória que possa ter encontrado o Login do BTCPay do seu servidor pode começar a criar contas.

#### Configurações de Notificação

![image](assets/en/76.webp)

#### Configurações de Manutenção

O BTCPay Server é um projeto Open Source que vive no GitHub. Sempre que o BTCPay Server lança uma nova versão do software, os Administradores podem ser notificados de que uma nova versão está disponível. Os administradores também podem querer desencorajar motores de busca (google, yahoo, duckduckgo) de indexar o domínio do BTCPay Server. Como o BTCPay Server é FOSS, desenvolvedores ao redor do mundo podem querer criar novas funcionalidades; o BTCPay Server tem uma funcionalidade experimental que, quando ativada, permite que um administrador use funcionalidades ainda não destinadas à produção, puramente para fins de teste.

- Verificar lançamentos no GitHub e notificar quando uma nova versão do BTCPay Server estiver disponível.
- Desencorajar motores de busca de indexar este site
- Habilitar funcionalidades experimentais.

![image](assets/en/77.webp)

#### Plugins

O BTCPay Server pode adicionar Plugins e expandir seu conjunto de funcionalidades. Os plugins, por padrão, são carregados do repositório plugin-builder do BTCPay Server. No entanto, um administrador pode escolher ver plugins em estado de Pré-lançamento, e se o desenvolvedor do plugin permitir, o administrador do servidor agora pode instalar versões beta dos plugins.

![image](assets/en/78.webp)

##### Configurações de Personalização

Uma implantação padrão do BTCPay Server será acessível através do domínio configurado para ele na instalação. No entanto, um administrador do servidor pode remapear o domínio raiz e exibir um dos aplicativos criados de uma loja específica. O Administrador do Servidor também pode mapear domínios específicos para aplicativos específicos.

- Exibir o aplicativo na raiz do site
  - Mostra lista de possíveis aplicativos para exibir no domínio raiz.

![image](assets/en/79.webp)

- Mapear domínios específicos para aplicativos específicos.
  - Quando você clica para configurar um domínio específico para aplicativos específicos, o Administrador pode configurar tantos domínios apontados para aplicativos específicos quanto necessário.

![image](assets/en/80.webp)

#### Exploradores de Blocos

O BTCPay Server, como padrão, vem com mempool.space como seu explorador de blocos para transações. Quando o BTCPay Server gera uma nova fatura, e há uma transação vinculada a ela, o proprietário da loja pode clicar para abrir a transação; o BTCPay Server apontará padrão para mempool.space como um explorador de blocos; um administrador do servidor pode alterar isso conforme sua preferência.

![image](assets/en/81.webp)

### Serviços

A aba de configurações do BTCPay Server: Serviços é uma visão geral dos componentes que seu BTCPay Server utiliza. Os serviços que seu BTCPay Server expõe podem variar dependendo do método de implantação.

Um Administrador do BTCPay Server pode clicar em “Ver informações” atrás de cada serviço para abri-lo e configurar as definições específicas.

![image](assets/en/82.webp)

#### LND (gRPC)

O BTCPay expõe o serviço gRPC do LND para consumo externo; você encontrará informações de conexão neste menu de configurações específico; carteiras compatíveis estão listadas aqui. O BTCPay Server também fornece um código QR para conexão para escanear e aplicar na carteira móvel.

Os administradores do servidor podem abrir mais detalhes para ver;

- Detalhes do Host
- Uso de SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- Conjunto de cifras SSL GRPC (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

O BTCPay expõe o serviço REST do LND para consumo externo; você encontrará informações de conexão aqui; carteiras compatíveis estão listadas aqui. Entre as carteiras compatíveis estão Joule, Alby e ZeusLN. O BTCPay Server fornece um código QR para conexão, escaneie e aplique na carteira compatível.

- URI REST
- Macaroon
- AdminMacaroon - InvoiceMacaroon
- ReadonlyMacaroon

#### Backup da Semente LND

O backup da semente LND é útil para recuperar fundos da sua carteira LND em caso de corrupção do seu Servidor. Como o nó Lightning é uma Hot-wallet, você pode encontrar as informações confidenciais da semente nesta página.

LND documenta o processo de recuperação. Veja https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md para documentação.

#### Ride The Lightning

Ride the Lightning é uma ferramenta de gerenciamento de nó Lightning construída como software de Código Aberto. O BTCPay Server utiliza o RTL como componente de gerenciamento de nó Lightning em sua pilha. Administradores do BTCPay Server podem acessar o RTL através das configurações do Servidor - aba Serviços ou clicando na carteira Lightning.

#### Nó completo P2P

Administradores de servidor podem querer conectar seu nó Bitcoin a uma carteira móvel. Esta página expõe informações para conectar remotamente ao seu nó completo via protocolo P2P. Até a escrita deste livro, o BTCPay Server lista as carteiras Blockstream Green e Wasabi como compatíveis. O BTCPay Server fornece um código QR para conexão, escaneie e aplique na carteira compatível.

#### Nó completo RPC

Esta página expõe informações para conectar remotamente ao seu nó completo via protocolo RPC.

#### SSH

SSH é usado para fins de manutenção. O BTCPay Server mostra o comando inicial de conexão para alcançar seu Servidor e as chaves públicas SSH autorizadas a se conectar ao seu Servidor. Administradores de Servidor podem querer desativar alterações SSH através da UI do BTCPay Server.

#### DNS Dinâmico

O DNS Dinâmico permite que você tenha um nome DNS estável apontando para o seu Servidor, mesmo se o seu endereço IP mudar regularmente. Isso é recomendado se você está hospedando o BTCPay Server em casa e deseja ter um domínio clearnet para acessar seu Servidor.

Note que você precisa configurar corretamente seu NAT e a instalação do BTCPay Server para obter o certificado HTTPS.

### Tema

O BTCPay Server, como padrão, vem com dois temas: Modos Claro e Escuro. Estes podem ser alternados clicando em Conta no canto inferior esquerdo e alternando entre tema Escuro ou tema Claro. Administradores do BTCPay Server podem adicionar seu próprio tema fornecendo um tema CSS personalizado.

Administradores podem estender o tema Claro/Escuro adicionando seu próprio CSS personalizado ou definindo seu tema personalizado como completo.

![imagem](assets/en/83.webp)

#### Branding do Servidor

Administradores de servidor podem mudar o branding do BTCPay Server configurando um branding abrangente do servidor para sua empresa. Como o BTCPay Server é FOSS, administradores de servidor podem personalizar o software e mudar a aparência para se adequar ao seu negócio.

![imagem](assets/en/84.webp)

### Manutenção

Como administrador de servidor, seus usuários esperam que você cuide bem do Servidor. Na aba de Manutenção do BTCPay Server, o administrador pode fazer algumas manutenções essenciais. Definir o nome de domínio para a instância do BTCPay Server, Reiniciar ou limpar o Servidor. Possivelmente o mais importante, executar atualizações.

O BTCPay Server é um projeto de Código Aberto e atualiza frequentemente. Cada novo lançamento é anunciado ou pelas Notificações do seu BTCPay Server ou pelos canais oficiais de comunicação do BTCPay Server.

![imagem](assets/en/85.webp)

#### Nome de domínio

Após a configuração do BTCPay Server, um administrador pode querer mudar de seu Domínio original. Na aba de Manutenção, o administrador pode mudar o Domínio. Após clicar em confirmar e configurar os registros DNS adequados no Domínio, o BTCPay Server atualiza e reinicia para retornar ao novo Domínio.

![imagem](assets/en/86.webp)

#### Reiniciar

Reinicie o BTCPay Server e serviços relacionados.

![imagem](assets/en/87.webp)

#### Limpar

O BTCPay Server opera com componentes Docker; com atualizações, podem sobrar imagens Docker, arquivos temporários, etc. Os Administradores de Servidor podem limpar isso e recuperar espaço em seu ambiente executando o script de Limpeza.
![imagem](assets/en/88.webp)

#### Atualização

Possivelmente a opção mais importante na aba de Manutenção. O BTCPay Server é construído pela comunidade e, portanto, seus ciclos de atualização são mais frequentes do que a maioria dos produtos de software. Quando o BTCPay Server tem um novo lançamento, os administradores serão notificados em seu centro de notificações. Ao clicar no botão de atualização, o BTCPay Server verificará o GitHub para obter o lançamento mais recente, atualizará o Servidor e o reiniciará. Antes de atualizar, sempre é aconselhável que os administradores do servidor leiam as notas de lançamento distribuídas pelos canais oficiais do BTCPay Server.

![imagem](assets/en/89.webp)

### Logs

Enfrentar um problema nunca é divertido. Este documento explica o fluxo de trabalho mais comum e as etapas para identificar eficientemente seu problema e resolvê-lo por conta própria ou com a ajuda da comunidade.

Identificar o problema é crucial.

#### Replicando o problema

Primeiro e acima de tudo, tente determinar quando o problema acontece. Tente replicar o problema. Tente atualizar e reiniciar seu Servidor para verificar se você pode reproduzir seu problema. Se isso descreve melhor o seu problema, tire uma captura de tela.

##### Atualizando o servidor

Verifique a versão do seu BTCPay Server se ela for muito mais antiga do que a [versão mais recente](https://github.com/btcpayserver/btcpayserver/releases) do BTCPay Server. Atualizar seu Servidor pode resolver o problema.

##### Reiniciando o servidor

Reiniciar seu Servidor é uma maneira fácil de resolver muitos dos problemas mais comuns do BTCPay Server. Você pode precisar usar SSH para entrar no seu Servidor e reiniciá-lo.

##### Reiniciando um serviço

Para alguns problemas, você pode precisar reiniciar apenas um serviço específico na sua implantação do BTCPay Server. Como, por exemplo, reiniciar o container do lets encrypt para renovar o certificado SSL.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Use docker ps para encontrar o nome de um serviço diferente que você gostaria de reiniciar.

#### Analisando os logs

Os logs podem fornecer uma peça essencial de informação. Nos parágrafos seguintes, descreveremos como obter as informações de log para várias partes do BTCPay.

##### Logs do BTCPay

Desde a versão v1.0.3.8, você pode acessar facilmente os logs do BTCPay Server pela interface. Se você é um administrador do servidor, vá para Configurações do Servidor > Logs e abra o arquivo de logs. Se você não sabe o que um erro particular nos logs significa, mencione-o ao solucionar problemas.

Se você deseja logs mais detalhados e está usando uma implantação Docker, você pode visualizar logs de containers Docker específicos usando a linha de comando. Veja estas [instruções para usar ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) em uma instância do BTCPay executando em um VPS.

Na próxima página, uma lista geral dos nomes dos containers usados para o BTCPay Server.

Execute os comandos abaixo para imprimir logs pelo nome do container. Substitua o nome do container para visualizar outros logs de containers.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Logs para    | Nome do Container                 |
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

Existem algumas maneiras de acessar seus logs do LND quando usando Docker. Primeiro, faça login como root:

```bash
sudo su -
Navegue até o diretório correto:
cd btcpayserver-docker
# Encontre o nome do container:
docker ps
Imprima os logs pelo nome do container:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

Alternativamente, você pode imprimir rapidamente os logs usando o ID do container (apenas os primeiros caracteres únicos do ID são necessários, como os dois caracteres mais à esquerda):

```bash
docker logs 'adicione seu ID do container'
```

Se por algum motivo você precisar de mais logs

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/bitcoin/mainnet/
ls
```

Você verá algo como

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

Para acessar logs descomprimidos desses logs faça `cat lnd.log` ou se quiser outro, use `cat lnd.log.15`.

Para acessar logs comprimidos em `.gzip` use `gzip -d lnd.log.16.gz` (neste caso estamos acessando `lnd.log.16.gz`). Isso deve gerar um novo arquivo, onde você pode fazer `cat lnd.log.16`. Caso o acima não funcione, talvez seja necessário instalar o gzip primeiro com `sudo apt-get install gzip`.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Encontre o ID do container c-lightning.
docker logs 'adicione seu ID do container aqui'
```

alternativamente, use isso

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

Você também pode obter informações de log com o comando cli do c-lightning.

```bash
bitcoin-lightning-cli.sh getlog
```

#### Logs do Nó Bitcoin

Além de [olhar os logs](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) do seu container Bitcoind, você também pode usar qualquer um dos [comandos bitcoin-cli](https://developer.bitcoin.org/reference/rpc/index.html)

[(abre nova janela)](https://developer.bitcoin.org/reference/rpc/index.html) para obter informações do seu nó bitcoin. O BTCPay inclui um script para permitir que você se comunique com seu nó Bitcoin facilmente.

Dentro da pasta btcpayserver-docker, obtenha a informação da blockchain usando seu nó:

```bash
bitcoin-cli.sh getblockchaininfo
```

O BTCPay Server possui um sistema de arquivos local e faz upload de ativos de Loja (produtos), Logotipos e branding diretamente para o Servidor. O sistema de arquivos do Servidor é acessível apenas pelos Administradores do Servidor; os proprietários de lojas podem fazer upload de seus logotipos/branding no nível da loja.
Quando o administrador do Servidor está na aba de Armazenamento de Arquivos, é possível fazer upload diretamente para o seu Servidor ou alterar o provedor de armazenamento de arquivos para um sistema de arquivos Local ou Azure Blob Storage.

![imagem](assets/en/90.webp)

![imagem](assets/en/91.webp)

### Resumo de Habilidades

Nesta seção, você aprendeu o seguinte:

- A diferença entre as configurações de Loja e Servidor, em particular no que diz respeito a Usuários, Funções e Emails
- Definir políticas em todo o servidor para o uso e criação de carteiras quentes de Lightning ou Bitcoin, registro de novos usuários e notificações por email.
- Como adicionar temas personalizados (em vez das simples opções de claro/escuro fornecidas) bem como criar logotipos personalizados
- Realizar tarefas simples de manutenção do servidor via GUI fornecida
- Solucionar problemas, incluindo buscar detalhes para qualquer um dos contêineres Docker ou seu nó
- Gerenciar o armazenamento de arquivos

### Avaliação de Conhecimento

#### Revisão Conceitual KA

Qual é a diferença nas Funções atribuídas através das Configurações do Servidor vs Configurações da Loja, e descreva um uso potencial para uma em detrimento da outra?

#### Revisão Prática KA

Descreva alguns possíveis casos de uso habilitados na aba de Políticas.

#### Revisão Prática KA

Descreva algumas ações que um administrador pode fazer rotineiramente na aba de Manutenção.

## BTCPay Server - Pagamentos

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Uma fatura é um documento que o vendedor emite para um comprador para coletar pagamento.

No BTCPay Server, uma fatura representa um documento que deve ser pago dentro de um intervalo de tempo definido a uma taxa de câmbio fixa. As faturas têm validade porque bloqueiam a taxa de câmbio dentro de um prazo especificado para proteger o receptor de flutuações de preço.

O núcleo do BTCPay Server é a capacidade de atuar como um sistema de gerenciamento de faturas Bitcoin. Uma fatura é uma ferramenta essencial para rastrear e gerenciar um pagamento recebido.

A menos que você use uma [Carteira](https://docs.btcpayserver.org/Wallet/) integrada para receber pagamentos manualmente, todos os pagamentos dentro de uma loja serão mostrados na página de Faturas. Esta página classifica os pagamentos por data de forma cumulativa e é uma peça central para o gerenciamento de faturas e solução de problemas de pagamento.

![imagem](assets/en/92.webp)

### Geral

#### Status de faturas

A tabela abaixo lista e descreve os status padrão de faturas no BTCPay e sugere ações comuns. As ações são apenas recomendações. Cabe aos usuários definir o melhor curso de ação para seu caso de uso e negócio.

| Status da Fatura                | Descrição                                                                                                                                               | Ação                                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nova                            | Não paga, o temporizador da fatura ainda não expirou                                                                                                    | Nenhuma                                                                                                                                                        |
| Nova (pagamentoParcial)         | Paga, não integralmente, o temporizador da fatura ainda não expirou                                                                                     | Nenhuma                                                                                                                                                        |
| Expirada                        | Não paga, o temporizador da fatura expirou                                                                                                              | Nenhuma                                                                                                                                                        |
| Expirada (pagamentoParcial)\*\* | Paga, não no valor integral, e expirada                                                                                                                 | Contatar o comprador para organizar um reembolso ou pedir para completarem o pagamento. Opcionalmente marcar a fatura como resolvida ou inválida               |
| Expirada (pagamentoTardio)      | Paga, no valor integral, após o temporizador da fatura ter expirado                                                                                     | Contatar o comprador para organizar um reembolso ou processar o pedido se confirmações tardias forem aceitáveis.                                               |
| Liquidado (paidOver)            | Pagou mais do que o valor da fatura, liquidado, recebeu quantidade suficiente de confirmações                                                           | Contate o comprador para organizar um reembolso pelo valor extra, ou opcionalmente espere que o comprador entre em contato com você                            |
| Processando                     | Pago integralmente, mas não recebeu quantidade suficiente de confirmações especificadas nas configurações da loja                                       | Contate o comprador para organizar um reembolso pelo valor extra, ou opcionalmente espere que o comprador entre em contato com você                            |
| Processando (paidOver)          | Pagou mais do que o valor da fatura, não recebeu quantidade suficiente de confirmações                                                                  | Espere ser liquidado então contate o comprador para organizar um reembolso pelo valor extra, ou opcionalmente espere que o comprador entre em contato com você |
| Liquidado                       | Pago, integralmente, recebeu quantidade suficiente de confirmações na loja                                                                              | Cumpra o pedido                                                                                                                                                |
| Liquidado (marcado)             | O status foi manualmente alterado para liquidado de um status em processamento ou inválido                                                              | O administrador da loja marcou o pagamento como liquidado                                                                                                      |
| Inválido\*                      | Pago, mas falhou em receber quantidade suficiente de confirmações dentro do tempo especificado nas configurações da loja                                | Verifique a transação em um explorador de blockchain, se recebeu confirmações suficientes, marque como liquidado                                               |
| Inválido (marcado)              | O status foi manualmente alterado para inválido de um status liquidado ou expirado                                                                      | O administrador da loja marcou o pagamento como inválido                                                                                                       |
| Inválido (paidOver)             | Pagou mais do que o valor da fatura, mas falhou em receber quantidade suficiente de confirmações dentro do tempo especificado nas configurações da loja | Verifique a transação em um explorador de blockchain, se recebeu confirmações suficientes, marque como liquidado                                               |

#### Detalhes da fatura

A página de detalhes da fatura contém todas as informações relacionadas a uma fatura.

As informações da fatura são criadas automaticamente com base no status da fatura, taxa de câmbio, etc. As informações do produto são criadas automaticamente se a fatura foi criada com informações do produto, como no aplicativo Ponto de Venda.

#### Filtragem de faturas

As faturas podem ser filtradas através dos filtros rápidos localizados ao lado do botão de pesquisa ou dos filtros avançados, que podem ser ativados clicando no link (Ajuda) no topo. Os usuários podem filtrar faturas por loja, ID do pedido, ID do item, status ou data.

#### Exportação de faturas

As faturas do BTCPay Server podem ser exportadas em formato CSV ou JSON. Para mais informações sobre exportação de faturas e contabilidade.

#### Reembolsando uma fatura

Se, por qualquer motivo, você desejar emitir um reembolso, você pode facilmente criar um reembolso a partir da visualização da fatura.

#### Arquivando faturas

Como resultado da funcionalidade de não reutilização de endereços do BTCPay Server, é comum ver muitas faturas expiradas na página de faturas da sua loja. Para ocultá-las da sua visualização, selecione-as na lista e marque-as como arquivadas. As faturas que foram marcadas como arquivadas não são deletadas. Pagamentos para uma fatura arquivada ainda serão detectados pelo seu BTCPay Server (status paidLate). Você pode visualizar as faturas arquivadas da loja a qualquer momento selecionando faturas arquivadas no dropdown de filtro de pesquisa.

#### Moeda Padrão

Moeda padrão da loja, isso foi definido no assistente de criação da loja

#### Permitir que qualquer um crie fatura

Você deve habilitar esta opção se quiser permitir que o mundo externo crie faturas na sua loja. Esta opção só é útil se você estiver usando o botão de pagamento ou se estiver emitindo faturas via API ou site HTML de terceiros. O aplicativo PoS é pré-autorizado e não precisa disso habilitado para que um visitante aleatório abra sua loja PoS e crie uma fatura.

#### Adicionar taxa adicional (taxa de rede) à fatura

- Apenas se o cliente fizer mais de um pagamento para a fatura
- Em cada pagamento
- Nunca adicionar taxa de rede

#### A fatura expira se o valor total não for pago após .. Minutos.

O temporizador da fatura é definido para 15 minutos por padrão. O temporizador é um mecanismo de proteção contra a volatilidade, pois bloqueia a quantidade de criptomoeda de acordo com as taxas de câmbio cripto para fiat. Se o cliente não pagar a fatura dentro do período definido, a fatura é considerada expirada. A fatura é considerada "paga" assim que a transação é visível na blockchain (o-confirmações), mas considerada "completa" quando atinge o número de confirmações definido pelo comerciante (geralmente, 1-6). O temporizador é personalizável.

#### Considere a fatura paga mesmo se o valor pago for ..% menor do que o esperado.

Em uma situação em que um cliente usa uma carteira de câmbio para pagar diretamente uma fatura, a bolsa de valores retira uma pequena taxa. Isso significa que tal fatura não é considerada totalmente completa. A fatura recebe o status de "paga parcialmente". Se um comerciante deseja aceitar faturas pagas parcialmente, você pode definir a taxa percentual aqui.

### Solicitações

Solicitações de Pagamento são um recurso que permite aos proprietários de lojas BTCPay criar faturas de longa duração. Os fundos são pagos a uma solicitação de pagamento usando a taxa de câmbio no momento do pagamento. Isso permite que os usuários façam pagamentos conforme sua conveniência, sem negociar ou verificar as taxas de câmbio com o proprietário da loja no momento do pagamento.

Os usuários podem pagar as solicitações em pagamentos parciais. A solicitação de pagamento permanecerá válida até que seja totalmente paga ou se o proprietário da loja exigir um tempo de expiração. Os endereços nunca são reutilizados. Um novo endereço é gerado cada vez que o usuário clica em pagar para criar uma fatura para a solicitação de pagamento.

Os proprietários de lojas podem imprimir solicitações de pagamento (ou exportar dados de fatura) para fins de registro e contabilidade. O BTCPay rotula automaticamente as faturas como Solicitações de Pagamento na lista de faturas da sua loja.

#### Personalize Suas Solicitações de Pagamento

- Valor da Fatura - Definir Valor de Pagamento Solicitado
- Denominação - Mostrar Valor Solicitado em Fiat ou Criptomoeda
- Quantidade de Pagamento - Permitir apenas pagamentos únicos ou pagamentos parciais
- Tempo de Expiração - Permitir pagamentos até uma data ou sem expiração
- Descrição - Editor de Texto, Tabelas de Dados, Incorporar Fotos & Vídeos
- Aparência - Cor e Estilo com Temas CSS

![image](assets/en/93.webp)

#### Criar uma Solicitação de Pagamento

No menu à esquerda, vá para Solicitação de Pagamento e clique em "Criar Solicitação de Pagamento".

![image](assets/en/94.webp)

Forneça o Nome da Solicitação, Valor, Denominação de Exibição, Loja Associada, Tempo de Expiração & Descrição (Opcional)

Selecione a opção Permitir que o pagador crie faturas em sua denominação se desejar permitir pagamentos parciais.

Clique em Salvar & Visualizar para revisar sua solicitação de pagamento.

O BTCPay cria uma URL para a solicitação de pagamento. Compartilhe esta URL para visualizar sua solicitação de pagamento. Precisa de várias da mesma solicitação? Você pode duplicar solicitações de pagamento usando a opção Clonar no menu principal.

![image](assets/en/95.webp)

**AVISO**

As solicitações de pagamento são dependentes da loja, o que significa que cada solicitação de pagamento está associada a uma loja durante a criação. Certifique-se de ter uma carteira conectada à sua loja à qual a solicitação de pagamento pertence.

#### Solicitação Paga

O pagador e o solicitante podem visualizar o status da solicitação de pagamento após o envio do pagamento. O status aparecerá como Liquidado se o pagamento for recebido integralmente. Se apenas pagamentos parciais foram feitos, o Valor Devido mostrará o saldo devedor.

![image](assets/en/96.webp)

#### Personalizar Solicitações de Pagamento

O conteúdo da descrição pode ser editado usando o editor de texto da solicitação de pagamento. Ambas as opções estão disponíveis se você deseja usar temas de cores adicionais ou estilização CSS personalizada.
Usuários não técnicos podem usar um [tema bootstrap](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Personalizações adicionais podem ser feitas fornecendo código CSS adicional, como mostrado abaixo.

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

### Pagamentos por Solicitação

Tradicionalmente, um receptor compartilha seu endereço Bitcoin para fazer um pagamento Bitcoin, e o remetente envia dinheiro para este endereço mais tarde. Esse sistema é chamado de Pagamento por Envio, pois o remetente inicia o pagamento enquanto o receptor pode estar indisponível, empurrando o pagamento para o receptor.

Mas, e se invertêssemos o papel?

E se, em vez de um remetente empurrar o pagamento, o remetente permitisse que o receptor puxasse o pagamento no momento que achasse conveniente? Esse é o conceito de um Pagamento por Solicitação. Isso permite várias novas aplicações, como:

- Um serviço de assinatura (onde o assinante permite que o serviço retire dinheiro a cada x quantidade de tempo)
- Reembolsos (onde o comerciante permite que o cliente retire o dinheiro do reembolso para sua carteira quando achar conveniente)
- Cobrança baseada em tempo para freelancers (onde a pessoa que contrata permite que o freelancer retire dinheiro para sua carteira conforme o tempo é reportado)
- Patronato (onde o patrono permite que o beneficiário retire dinheiro todo mês para continuar apoiando seu trabalho)
- Venda automática (onde um cliente de uma exchange permitiria que a exchange retirasse dinheiro de sua carteira para vender automaticamente todo mês)
- Sistema de retirada de saldo (onde um serviço de alto volume permite que os usuários solicitem retiradas de seu saldo, o serviço pode então facilmente agrupar todos os pagamentos para muitos usuários em intervalos fixos)

### Pagamentos

A funcionalidade de pagamento está integrada aos [Pagamentos por Solicitação](https://docs.btcpayserver.org/PullPayments/). Esta característica permite que você crie pagamentos dentro do seu BTCPay. Esta funcionalidade permite que você processe pagamento por solicitação (reembolsos, pagamentos de salários ou retiradas).

#### Exemplo 1: Reembolso

Vamos começar com o exemplo de reembolso. O cliente comprou um item em sua loja, mas infelizmente precisa devolver o item. Eles querem um reembolso. Dentro do BTCPay, você pode criar um [Reembolso](https://docs.btcpayserver.org/Refund/) e fornecer ao cliente o link para reivindicar seus fundos. Sempre que o cliente fornecer seu endereço e reivindicar os fundos, isso será mostrado nos Pagamentos.

O primeiro status é Aguardando Aprovação. Os atendentes da loja podem verificar se há múltiplos esperando, e após fazer a seleção, você usa o botão Ações.

Opções no botão de ações

- Aprovar pagamentos selecionados
- Aprovar e enviar pagamentos selecionados
- Cancelar pagamentos selecionados

O próximo passo é Aprovar e enviar pagamentos selecionados, pois queremos reembolsar o cliente. Verifique o Endereço do Cliente, mostra o valor e se queremos que as taxas sejam subtraídas do reembolso ou não. Uma vez feitas as verificações, só resta assinar a transação.
O cliente agora é atualizado na página de Reivindicações. Ele pode acompanhar a transação, pois é fornecido com um link para um explorador de blocos e sua transação. Uma vez que a transação tenha sido confirmada, e o status muda para Concluído.

#### Exemplo 2: Salário

Agora, vamos falar sobre pagamento de salários, já que isso é gerenciado internamente pela loja e não a pedido do Cliente. A base é a mesma; utiliza os Pagamentos por Solicitação. Mas, em vez de criar um reembolso, vamos fazer um [Pagamento por Solicitação](https://docs.btcpayserver.org/PullPayments/).

Vá até a aba de Pagamentos por Solicitação no seu servidor BTCPay. No canto superior direito, clique no botão Criar Pagamento por Solicitação.

Agora estamos na criação do Pagamento, dê um nome e o valor desejado na moeda desejada, preencha a Descrição, para que o funcionário saiba do que se trata. A próxima parte é semelhante aos reembolsos. O funcionário preenche o Endereço de Destino e o valor que deseja reivindicar deste Pagamento. Ele pode decidir fazer 2 reivindicações separadas, para endereços diferentes, ou até mesmo reivindicar parcialmente via lightning.

Se houver múltiplos Pagamentos pendentes, você pode agrupá-los para serem assinados e enviados. Uma vez assinados, os pagamentos passam para a aba Em progresso e mostram a Transação. Quando aceitos pela rede, o pagamento passa para a aba Concluído. A aba Concluído é puramente para fins históricos. Ela contém os Pagamentos processados e a transação que pertence a ele

### Pagamentos por Solicitação

#### Conceito

Quando um remetente configura um Pagamento por Solicitação, ele pode configurar uma série de propriedades:

- Nome do Pedido de Pagamento
- Um valor limite
- Uma Unidade (como BTC, SAT, USD)
- Métodos de Pagamento
  - BTC On-chain
  - BTC Off-chain
- Descrição
- CSS Personalizado
- Data de término (opcional para Lightning Network BOLT11)

Após isso, o remetente pode compartilhar o pagamento por solicitação usando um link com o receptor, permitindo que o receptor crie um pagamento. O receptor escolherá seu pagamento:

- Qual método de pagamento usar
- Para onde enviar o dinheiro

Uma vez criado um pagamento, ele contará para o limite do pagamento por solicitação para o período atual. O remetente então aprovará o pagamento definindo a taxa na qual o pagamento será enviado e procederá com o pagamento.

Para o remetente, fornecemos uma maneira fácil de usar para agrupar o pagamento de vários pagamentos a partir da [Carteira Interna BTCPay](https://docs.btcpayserver.org/Wallet/).

#### API Greenfield

O Servidor BTCPay fornece uma API completa tanto para o remetente quanto para o receptor que está documentada na página `/docs` da sua instância. (ou no site de documentações https://docs.btcpayserver.org)

Como nossa API expõe a capacidade completa dos pagamentos por solicitação, um remetente pode automatizar pagamentos de acordo com suas próprias necessidades.

### Resumo de Habilidades

Nesta seção, você aprendeu o seguinte:

- Compreensão profunda dos status de faturas do Servidor BTCPay, bem como ações que podem ser realizadas nelas
- Personalizar e gerenciar mecanismos de fatura de vida estendida conhecidos como Pedidos.
- As possibilidades de pagamento flexíveis adicionais abertas com a característica única de Pagamento por Solicitação do Servidor BTCPay, particularmente como lidar com reembolsos e pagamentos de salários.

### Avaliação de Conhecimento

#### Revisão Conceitual KA

Quais são algumas diferenças entre faturas e pedidos de pagamento, e qual pode ser um bom motivo para usar este último?

#### Revisão Conceitual KA

Como os pagamentos por solicitação expandem o que tipicamente pode ser feito on-chain? Descreva alguns casos de uso que eles possibilitam.

## Plugins Padrão do Servidor BTCPay

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Plugins e Aplicativos Padrão

O servidor BTCPay vem com um conjunto padrão de Plugins (Apps) que podem transformar o BTCPay Server em um gateway de pagamento para e-commerce. Com as adições de um Ponto de Venda, plataforma de Financiamento Coletivo e um botão de Pagamento Fácil, o BTCPay Server torna-se uma solução fácil de ser implementada.

### Ponto de Venda

Um dos Plugins padrão do BTCPay Server é o Ponto de Venda (PoS). Com o plugin PoS, um proprietário de loja pode criar um Webshop diretamente do BTCPay Server, sem a necessidade de soluções de e-commerce de terceiros para executar um Webshop. O aplicativo PoS baseado na web permite que usuários com lojas físicas aceitem Bitcoin facilmente, sem taxas ou um terceiro, diretamente em sua carteira. O PoS pode ser facilmente exibido em tablets ou outros dispositivos que suportam navegação na web. Os usuários podem facilmente criar um atalho na tela inicial para acessar o aplicativo web rapidamente.

#### Como criar um novo Ponto de Venda

O BTCPay Server permite que os proprietários de lojas criem um Ponto de Venda em múltiplos layouts rapidamente. O BTCPay Server reconhece que nem toda loja é de e-commerce, e nem toda loja é um bar ou restaurante, e vem com múltiplas configurações padrão para o seu PoS.

Quando o proprietário da loja clica em "Ponto de Venda" em sua barra de menu à esquerda, o BTCPay Server agora pedirá um nome; este nome será visível na barra de menu à esquerda. Clique em Criar para criar o PoS.

![image](assets/en/97.webp)

#### Atualizar o Ponto de Venda recém-criado

Após criar um novo PoS, a próxima tela será para atualizar seu Ponto de Venda e adicionar itens para sua loja.

##### Nome do Aplicativo

O nome dado aqui ao seu Ponto de Venda será visível no menu principal do BTCPay Server.

##### Título de Exibição

O público verá o título público ou nome ao visitar sua loja. O BTCPay Server como padrão nomeia sua loja “Loja de Chá” Substitua isso pelo nome da sua loja.

![image](assets/en/98.webp)

#### Escolher Estilo do Ponto de Venda

O BTCPay Server é capaz de exibir seu Ponto de Venda de várias maneiras.

- Lista de produtos
  - Uma visão de loja onde os clientes podem comprar apenas 1 produto por vez.
- Lista de produtos com carrinho.
  - Uma visão de loja onde os clientes podem comprar múltiplos itens de uma vez e obter uma visão geral do carrinho de compras à direita da tela.
- Apenas teclado
  - Sem lista de produtos, apenas um teclado para faturamento direto.
- Exibição para impressão (Lista de produtos imprimível com QR)
  - Se você não pode sempre exibir sua lista de produtos digitalmente, você precisa de uma solução "offline" para produtos; o BTCPay Server tem uma exibição para impressão para funcionar como uma loja Offline.

![image](assets/en/99.webp)

#### Estilo do Ponto de Venda - Lista de produtos

![image](assets/en/100.webp)

#### Estilo do Ponto de Venda - Lista de produtos + Carrinho

![image](assets/en/101.webp)

#### Estilo do Ponto de Venda - Apenas teclado

![image](assets/en/102.webp)

#### Estilo do Ponto de Venda - Exibição para impressão

![image](assets/en/103.webp)

#### Moeda

O proprietário da loja pode definir uma moeda diferente para seu Ponto de Venda do que sua moeda padrão definida. A moeda padrão da loja preencherá automaticamente este campo.

#### Descrição

Conte ao mundo sobre sua loja; o que você está vendendo e por quanto? Tudo explicando sua loja vai aqui.

#### Produtos

Quando um Ponto de Venda é criado, um BTCPay Server padrão adiciona alguns itens à loja para referência. Clique no botão Editar em qualquer um dos itens padrão para entender melhor cada opção possível para um item.

Criar um novo produto na sua loja consiste nos seguintes campos;

- Título
- Preço (fixo, mínimo ou personalizado)
- URL da Imagem
- Descrição
- Estoque
- ID
- Texto do Botão de Compra.
- Habilitar/Desabilitar

Uma vez que o proprietário da loja preencheu todos os campos do novo produto, clique em salvar, e você notará que a seção Produtos no Ponto de Venda está agora sendo preenchida. Sempre certifique-se de salvar no canto superior direito da sua tela para evitar que os proprietários da loja possam perder seu progresso ao adicionar produtos.

Os proprietários de loja também podem usar o "Editor Bruto" para configurar seus produtos. O editor bruto requer um entendimento básico das estruturas JSON.

#### Checkout

O BTCPay Server permite uma pequena personalização específica de checkout para PoS. O proprietário da loja pode definir o texto "Comprar por x" ou solicitar dados específicos do cliente adicionando formulários.

#### Gorjetas

Nem todas as lojas precisam da opção de Gorjetas em suas vendas. Os proprietários de lojas podem ativar ou desativar isso conforme acharem adequado para sua loja. Se a loja usar gorjetas ativadas, o proprietário da loja pode definir o texto no campo para gorjetas que desejar. As gorjetas do BTCPay Server funcionam com base em um valor percentual. Os proprietários de lojas podem adicionar várias porcentagens com separação por vírgulas.

#### Descontos

Como proprietário de uma loja, você pode querer oferecer ao cliente um desconto personalizado no checkout; a opção para Descontos fica disponível no checkout da sua loja. No entanto, isso é muito desaconselhado para sistemas de autoatendimento.

#### Pagamentos Personalizados

Quando a opção de Pagamentos Personalizados é ativada, o cliente pode inserir o preço definido por ele, igual ou superior à fatura original gerada pela loja.

#### Opções Adicionais

Após configurar tudo para o seu Ponto de Venda, restam algumas opções extras. Os proprietários de lojas podem facilmente Incorporar seu PoS por meio de um Iframe ou incorporar um botão de pagamento vinculado a um item específico da loja. Para estilizar a loja PoS recém-criada, os proprietários podem adicionar CSS personalizado na parte inferior das opções adicionais.

#### Excluir este aplicativo

Se o proprietário da loja quiser excluir completamente o Ponto de Venda do seu BTCPay Server, na parte inferior da atualização do PoS, os proprietários da loja podem clicar no botão Excluir este aplicativo para destruir completamente seu aplicativo PoS. Ao clicar em "Excluir este aplicativo", o BTCPay Server pedirá confirmação digitando `DELETE` e confirmando clicando no botão Excluir. Após a exclusão, o proprietário da loja retorna ao painel do BTCPay Server.

### BTCPay Server - Crowdfund

Ao lado do plugin Ponto de Venda, o BTCPay Server oferece a opção de criar um financiamento coletivo. Assim como qualquer outra plataforma de Crowdfund, os proprietários de lojas podem definir uma meta, criar recompensas para contribuições e personalizá-la conforme suas necessidades.

#### Como configurar um novo financiamento coletivo

Clique no plugin Crowdfund através do menu principal à esquerda do seu BTCPay Server, abaixo da seção Plugin. O BTCPay Server agora solicitará um nome para o Crowdfund; este nome também será exibido na barra de menu à esquerda.

#### Atualizar o Ponto de Venda recém-criado

Uma vez que o aplicativo recebe um nome, a próxima tela será para atualizar o Aplicativo para ter contexto.

#### Nome do Aplicativo

O nome dado ao seu Crowdfund será visível no menu principal do BTCPay Server.

#### Título de Exibição

O título é dado ao Financiamento Coletivo para o público.

#### Tagline

Dê ao financiamento coletivo uma frase de efeito para reconhecer sobre o que é a arrecadação de fundos.

![image](assets/en/107.webp)

#### URL da Imagem Destacada

Todo financiamento coletivo tem sua imagem principal, o banner que você reconhece diretamente. Esta imagem pode ser armazenada no seu servidor se você tiver direitos Administrativos, Admins podem fazer upload em Configurações do Servidor - Arquivos no BTCPay Server. Quando você é um proprietário de loja, a imagem deve ser enviada para a web através de um host de terceiros (por exemplo, imgur)

#### Tornar o Financiamento Coletivo Público

Este interruptor torna seu Financiamento Coletivo público e, portanto, visível para o mundo exterior. Para fins de teste ou para ver se seu tema foi aplicado corretamente, pode-se querer manter isso definido como DESLIGADO durante o período de construção do financiamento coletivo.

#### Descrição

Conte ao mundo sobre seu Financiamento Coletivo, para que você está arrecadando? Tudo explicando seu financiamento coletivo vai aqui.

![image](assets/en/108.webp)

#### Meta do Financiamento Coletivo

Defina uma meta de objetivo para o que a arrecadação de fundos deve ganhar para o projeto e em que moeda o objetivo deve ser denominado. Certifique-se de que, se seus objetivos são definidos entre datas, inclua estas datas de início e fim abaixo de Metas no financiamento coletivo.

![image](assets/en/109.webp)

#### Benefícios

Benefícios ajudam muito com seu financiamento coletivo. Isso porque os benefícios dão às pessoas uma maneira de participar da sua campanha. Eles exploram motivações egoístas, bem como motivações benevolentes. E eles permitem que você acesse os gastos de seus apoiadores, não apenas sua bolsa filantrópica -- você pode adivinhar qual é mais significativo.

Criar um novo benefício consiste nos seguintes campos;

- Título
- Preço (fixo, mínimo ou personalizado)
- URL da Imagem
- Descrição
- Estoque
- ID
- Texto do Botão de Compra.
- Habilitar/Desabilitar

Uma vez que o proprietário da loja tenha preenchido todos os campos do novo benefício a ser criado, clique em salvar, e você notará que a seção de Benefícios nos financiamentos coletivos está agora sendo preenchida.

![image](assets/en/110.webp)

### BTCPay Server - Ponto de Venda

#### Contribuições

Os proprietários de lojas podem escolher como exibir os Benefícios, como eles são ordenados, ou até mesmo classificados em relação aos outros benefícios. No entanto, uma vez que as metas do Financiamento Coletivo são alcançadas, os proprietários de lojas podem querer parar o fluxo de doações para esta arrecadação de fundos. Portanto, ele pode ativar "Não permitir contribuições adicionais após alcançar o alvo". Isso impedirá o Financiamento Coletivo de aceitar doações.

##### Comportamento do Financiamento Coletivo

O padrão do Financiamento Coletivo só conta as faturas criadas com o Financiamento Coletivo em direção ao objetivo. No entanto, pode haver casos em que o Proprietário da loja queira que todas as faturas feitas nesta loja contem para o financiamento coletivo.

#### Opções Adicionais para personalização

O BTCPay Server oferece algumas personalizações extras. Adicione sons, animações ou até mesmo tópicos de discussão ao Financiamento Coletivo. Os proprietários de lojas também podem mudar a aparência do Financiamento Coletivo inserindo seu próprio CSS personalizado.

#### Excluir este aplicativo

Se o proprietário da loja quiser excluir completamente o Financiamento Coletivo do seu BTCPay Server, na parte inferior de atualizar o Financiamento Coletivo, os proprietários da loja podem clicar no botão “Excluir este aplicativo” para destruir completamente seu aplicativo de Financiamento Coletivo. Ao clicar em "Excluir este aplicativo", o BTCPay Server pedirá confirmação digitando `DELETE` e confirmando clicando no botão Excluir. Após excluir, o proprietário da loja retorna ao painel do BTCPay Server.

### BTCPay Server - Botão de Pagamento

Botões de pagamento HTML facilmente incorporáveis e altamente personalizáveis permitem que os proprietários de lojas recebam gorjetas e doações. Na barra de menu à esquerda do BTCPay Server, abaixo da seção Plugins, os proprietários de lojas podem clicar em "Pay Button" e clicar em Ativar para criar um botão de Pagamento.

#### Configurações Gerais

Dentro das Configurações Gerais para o Botão de Pagamento, os proprietários de lojas podem definir

- Preço padrão
- Moeda padrão
- Método de pagamento padrão
  - Usar padrão da loja
  - BTC on-chain
  - BTC Off-chain (Lightning)
  - BTC Off-chain (LNURL-pay)
- Descrição do checkout
- ID do pedido

#### Opções de Exibição

O botão de Pagamento do BTCPay Server pode ser configurado para se adequar a diferentes estilos. Os botões podem ter um valor fixo ou personalizado, exibido com um deslizador ou com botões de mais e menos.

#### Usar Modal

Ao criar o botão de pagamento, os proprietários de lojas podem escolher seu comportamento quando um cliente clica nele e mostrá-lo em um modal ou como uma nova página.

**!?Nota!?**

Aviso: O botão de pagamento deve ser usado apenas para gorjetas e doações

Usar o botão de pagamento para integrações de comércio eletrônico não é recomendado, pois informações relevantes do pedido podem ser modificadas pelo usuário. Para comércio eletrônico, você deve usar nossa API Greenfield. Se esta loja processa transações comerciais, aconselhamos a criar uma loja separada antes de usar o botão de pagamento.

#### Personalizar Texto do Botão de Pagamento

Por padrão, o botão de pagamento do BTCPay Server indica "Pagar com BTCPay". Os proprietários de lojas podem definir este texto conforme desejarem e mudar o logo do BTCPay Server pelo seu próprio. Defina o texto usando "Pay Button Text" e cole a URL da imagem abaixo de "Pay Button Image URL".

##### Tamanho da Imagem

O tamanho da imagem no botão só pode ser definido para três padrões.

- 146x40px
- 168x46px
- 209x57px

#### Tipo de Botão

O BTCPay Server conhece três estados para o Botão de Pagamento.

- Quantia Fixa
  - O preço previamente definido está nas configurações gerais do botão.
- Quantia Personalizada
  - O botão de Pagamento do BTCPay Server tem botões de + e - para definir um preço personalizado.
  - Ao usar a quantia personalizada, o BTCPay Server solicitará um Min, Max e como deve aumentar gradualmente.
  - Os botões podem ser configurados para "Usar estilo de entrada simples". Isso remove os botões de +/-.
  - Encaixar botão na linha onde o botão e os botões de alternância aparecem na linha.
- Deslizador
  - Semelhante à quantia personalizada, porém, visualmente diferente, pois possui um deslizador em vez dos botões de +/-.
  - Ao usar o Deslizador, o BTCPay Server solicitará um Min, Max e como deve aumentar gradualmente.

**!?Nota!?**

Excluir o Botão de Pagamento pode ser feito no topo na descrição de aviso.

#### Notificações de Pagamento

O IPN do Servidor (Notificação Instantânea de Pagamento) é destinado a webhooks e pode ser preenchido por uma URL para postar dados de compra.

#### Notificações por Email

Sempre que um pagamento for realizado, o BTCPay Server pode notificar o proprietário da loja.

#### Redirecionamento do Navegador

Quando o cliente completa a compra, ele será redirecionado para este link, se definido pelo proprietário da loja.

#### Opções Avançadas do Botão de Pagamento

Especifique parâmetros adicionais de string de consulta que devem ser anexados à página de checkout assim que a fatura for criada. Por exemplo, `lang=da-DK` carregaria a página de checkout em dinamarquês por padrão.

#### Usar Aplicativo como Endpoint

Vincule diretamente o botão de pagamento a um item em um dos aplicativos PoS ou Crowdfund antes.
Os proprietários de lojas podem clicar no menu suspenso e selecionar o App desejado; uma vez que o App é selecionado, o proprietário da loja pode adicionar o item que precisa ser vinculado.

#### Código Gerado

Como o botão de Pagamento do BTCPay Server é HTML facilmente incorporável, o BTCPay Server mostra o código gerado para copiar em um site na parte inferior após configurar o botão de Pagamento.

Os proprietários de lojas podem copiar o código gerado em seu site, e o botão de Pagamento do BTCPay Server fica diretamente ativo em seu site.

#### Notificações de Pagamento

O IPN do Servidor (Notificação Instantânea de Pagamento) destina-se a webhooks e pode ser preenchido por uma URL para postar dados de compra.

#### Notificações por Email

Sempre que um pagamento é realizado, o BTCPay Server pode notificar o proprietário da loja.

#### Redirecionamento do Navegador

Quando o cliente completa a compra, ele será redirecionado para este link, se definido pelo proprietário da loja.

#### Opções Avançadas do Botão de Pagamento

Especifique parâmetros adicionais de string de consulta que devem ser anexados à página de checkout assim que a fatura for criada. Por exemplo, `lang=da-DK` carregaria a página de checkout em dinamarquês por padrão.

#### Usar App como Endpoint

Vincule diretamente o botão de pagamento a um item em um dos apps PoS ou Crowdfund antes. Os proprietários de lojas podem clicar no menu suspenso e selecionar o app desejado, uma vez que o app é selecionado, o proprietário da loja pode adicionar o item que precisa ser vinculado.

#### Código Gerado

Como o botão de Pagamento do BTCPay Server é HTML facilmente incorporável, o BTCPay Server mostra o código gerado para copiar em um site na parte inferior após configurar o botão de Pagamento. Os proprietários de lojas podem copiar o código gerado em seu site e o botão de Pagamento do BTCPay Server fica diretamente ativo em seu site.

### Resumo de Habilidades

Nesta seção, você aprendeu:

- Como usar o plugin integrado PoS do BTCPay Server para criar facilmente uma loja personalizada
- Como usar o plugin integrado Crowdfund do BTCPay Server para criar facilmente um app de financiamento coletivo personalizado
- Gerando código para um botão de pagamento personalizado usando o plugin do Botão de Pagamento

### Avaliação de Conhecimento

#### Revisão da KA

Quais são os três plugins integrados que vêm como padrão com o BTCPay Server? Em poucas palavras, descreva como cada um pode ser usado.

# Configurando o BTCPay Server

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Entendimento Básico da Instalação do BTCPay Server em um Ambiente LunaNode

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### Instalando o BTCPay Server em Amb. Hospedado (LunaNode)

Estas etapas fornecerão todas as informações necessárias para começar a usar o BTCPay Server no LunaNode. Existem muitas opções sobre como implantar o software.
Você pode encontrar todos os detalhes do BTCPay Server em https://docs.btcpayserver.org.

#### Por onde começamos?

Nesta parte, você se familiarizará com o LunaNode como o provedor de hospedagem, aprenderá sobre os primeiros passos de usar seu BTCPay Server e aprenderá como proceder com a Lightning Network. Depois de passarmos por todas as etapas, você pode executar uma loja virtual ou plataforma de financiamento coletivo aceitando Bitcoin!

Esta é uma das muitas maneiras de implantar o BTCPay Server. Leia nossa documentação para mais detalhes,

https://docs.btcpayserver.org.

### BTCPay Server - Implantação LunaNode

#### Implantação LunaNode

Primeiro, acesse o site LunaNode.com, onde criaremos uma nova conta. Clique em Sign Up no canto superior direito ou use o assistente Get Started na página inicial.
![image](assets/en/111.webp)

Depois de criar sua nova conta, a LunaNode envia um e-mail de verificação. Uma vez que você verifique a conta, em comparação com a Voltage, você é imediatamente apresentado à opção de adicionar saldo à sua conta. Esse saldo é necessário para pagar pelo espaço no servidor e pelos custos de hospedagem.

![image](assets/en/112.webp)

#### Adicione crédito à sua conta LunaNode

Uma vez que você clicou em "Deposit credit", você pode definir quanto deseja adicionar de saldo à sua conta e como deseja pagar por isso. LunaNode e BTCPay Server custarão entre 10$USD e 20$USD por mês.
Comparado com Voltage.cloud, você obtém acesso completo ao seu Servidor Privado Virtual (VPS daqui para frente) e, portanto, tem mais controle sobre seu servidor. Depois de criar sua nova conta, a LunaNode envia um e-mail de verificação.
Uma vez que você verifique a conta, em comparação com a Voltage, agora você é imediatamente apresentado à opção de adicionar saldo à sua conta. Esse saldo é necessário para pagar pelo espaço no servidor e pelos custos de hospedagem.

#### Como implantar um novo servidor?

Neste guia, passaremos pela configuração criando um conjunto de chaves API e usando o lançador do BTCPay Server feito pela LunaNode.

No seu painel de controle LunaNode, clique em API no canto superior direito. Isso abre uma nova página. Só precisamos definir um Nome para a chave API. O resto será cuidado pela LunaNode e não será coberto neste guia. Clique no botão Create API Credential.
Após criar as credenciais da API, você recebe uma longa sequência de letras e caracteres. Esta é a sua chave API.

![image](assets/en/113.webp)

#### Como implantar um novo servidor?

Há 2 partes nessas credenciais, chave API e ID da API; precisaremos de ambas. Antes de irmos para o próximo passo, vamos abrir uma segunda aba no navegador e acessar https://launchbtcpay.lunanode.com/

Aqui você será solicitado a fornecer sua chave API e ID da API. Isso é para verificar que é você quem provisiona este novo servidor. A chave API ainda deve estar aberta na sua aba anterior; se você rolar para baixo na tabela abaixo, encontrará o ID da API.

Volte para a página com o Launcher, preencha os campos com sua chave API e ID, e clique em continuar.

![image](assets/en/114.webp)

No próximo passo, você pode fornecer um nome de domínio. Se você já possui um domínio e deseja usá-lo para o BTCPay Server, certifique-se de também adicionar o registro DNS (Chamado de registro `A`) no seu domínio. Se você não possui um domínio, use o domínio fornecido pela LunaNode (você pode alterar isso mais tarde nas configurações do BTCPay Server) e clique em Continuar.

Leia mais sobre como configurar ou alterar um registro DNS para o BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Lançar o BTCPay Server na LunaNode

Após seguir os passos anteriores, podemos definir todas as opções para nosso novo servidor. Aqui selecionaremos Bitcoin (BTC) como nossa moeda suportada; podemos definir um e-mail para ser notificado sobre a renovação de certificados de criptografia; isso não é obrigatório.
Este guia tem como objetivo configurar um ambiente Mainnet (Bitcoin do mundo real); no entanto, a LunaNode também permite que você configure isso para Testnet ou Regtest para fins de desenvolvimento. Deixaremos a opção Mainnet para este guia.
Escolha sua implementação do Lightning. A LunaNode oferece duas implementações diferentes, LND e Core Lightning. Para este guia, escolheremos LND. Existem pequenas, mas verdadeiras diferenças entre ambas as implementações; para mais informações sobre isso, recomendamos a leitura da extensa documentação; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![imagem](assets/en/115.webp)

A LunaNode oferece múltiplos planos de Máquina Virtual (VM). Estes variam em faixas de preço e especificações do servidor. Para este guia, um plano m2 será suficiente; no entanto, se você selecionou mais do que apenas Bitcoin como moeda, considere usar pelo menos m4.

Acelere a sincronização inicial da blockchain; isso é opcional e depende de suas necessidades. Existem opções avançadas como definir um Alias Lightning, apontar para um lançamento específico do GitHub, ou configurar chaves SSH; nenhuma destas será abordada neste guia.

Após preencher o formulário, você deve clicar em Launch VM, e a Lunanode começará a criar sua nova VM, incluindo o BTCPay Server instalado nela. Este processo leva alguns minutos; uma vez que seu servidor estiver pronto, a LunaNode lhe dará o link para o seu novo BTCPay Server.

Após o processo de criação, clique no link para o seu BTCPay Server; aqui, você será solicitado a criar uma conta de Administrador.

![imagem](assets/en/116.webp)

### Resumo de Habilidades

Nesta seção você aprendeu:

- Criar e financiar uma conta na LunaNode
- Usar o BTCPay Server Launcher para criar seu próprio servidor

### Avaliação de Conhecimento

#### Revisão Conceitual do KA

Descreva algumas das diferenças entre executar uma instância do BTCPay Server em um VPS versus criar uma conta em uma instância hospedada.

## Instalando o BTCPay Server em um ambiente Voltage

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Você se familiarizará com Voltage.cloud como provedor de hospedagem, aprenderá sobre os primeiros passos de usar seu BTCPay Server e aprenderá como proceder com a Lightning Network. Depois de passarmos por todos os passos, você poderá executar uma loja virtual ou plataforma de financiamento coletivo aceitando Bitcoin!

Esta é uma das muitas maneiras de implantar o BTCPay Server. Leia nossa documentação para mais detalhes,
https://docs.btcpayserver.org.

### Implantação do BTCPay Server - Voltage.cloud

Primeiro, vá ao site Voltage.cloud e inscreva-se para uma nova conta. Ao criar uma conta, você pode se inscrever para um teste gratuito de 7 dias. Clique em Sign Up no topo direito ou use o "Try a free 7 day trial" na página inicial.

![imagem](assets/en/117.webp)

Depois de criar uma conta, clique no botão `NODES` no seu painel. Uma vez que selecionamos Nodes e criamos um novo nó, nos é apresentado os possíveis nós que a Voltage oferece. Como este guia também abordará a LightningNetwork, na Voltage, primeiro temos que escolher nossa implementação do Lightning antes de criarmos um BTCPay Server. Clique em LightningNode.

![imagem](assets/en/118.webp)
Aqui você terá que selecionar qual tipo de nó Lightning você deseja. A Voltage oferece uma variedade de opções para a sua configuração de iluminação. Isso é diferente quando se faz a implantação com, por exemplo, a LunaNode. Para a intenção deste guia, um Lite Node será suficiente. Leia mais sobre as diferenças em Voltage.cloud.
![image](assets/en/119.webp)

Dê um Nome ao seu nó, defina uma senha e proteja esta senha. Se esta senha for perdida, você perde acesso aos seus backups, e a Voltage não pode recuperá-la. Crie o nó, e a Voltage mostra o progresso. A Voltage criou seu Lightning Node. Agora podemos criar a instância do BTCPay Server e acessar diretamente a Lightning Network.

Clique em Nodes no canto superior esquerdo do seu painel. Aqui você pode configurar a próxima parte da sua instância do BTCPay Server. Clique em "create new" uma vez que você estiver na visão geral dos nós. Você terá uma tela similar à anterior. Agora, em vez de Lightning Node, escolhemos BTCPay Server.

A Voltage mostra a geolocalização do seu BTCPay Server, a voltage hospeda na região Oeste dos EUA. Aqui você também verá o custo de hospedar o servidor. Clique em Create e dê um nome ao seu BTCPay Server. Habilite Lightning e a Voltage mostra o nó Lightning criado na etapa anterior. Clique em Create, e a Voltage criará uma instância do BTCPay Server.

![image](assets/en/120.webp)

Após você clicar em create, a Voltage apresenta o nome de usuário e senha padrões. Estes são similares à senha que você definiu anteriormente na Voltage. Clique no botão Login to Account para ser redirecionado ao seu BTCPay Server.

Bem-vindo à sua nova instância do BTCPay Server. Como já configuramos Lightning no processo de criação, ele mostra que Lightning já está habilitado!

### Resumo de Habilidades

Neste capítulo você aprendeu:

- Criar uma conta em Voltage.cloud
- Passos para colocar o BTCPay Server para funcionar junto com um nó Lightning na conta

### Avaliação de Conhecimento

#### Revisão Conceitual do KA

Quais são algumas diferenças-chave entre as configurações da Voltage e da LunaNode?

## Instalando o BTCPay Server em um nó Umbrel

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

Ao final destes passos, você pode aceitar pagamentos lightning na sua loja BTCPay na sua rede local. Este processo também se aplica se você executar um nó umbrel em um restaurante ou negócio. Se você quiser conectar esta loja a um site público, siga o exercício Avançado para expor seu nó umbrel ao público.

https://umbrel.com/

![image](assets/en/121.webp)

### BTCPay Server - Implantação Umbrel

Após seu nó Umbrel ter sincronizado completamente com a blockchain do Bitcoin, vá até a Umbrel App Store e procure por BTCPay Server em Apps.

![image](assets/en/122.webp)

Clique em BTCPay Server para ver os detalhes do App. Quando os detalhes estiverem abertos para o BTCPay Server, o canto inferior direito mostra os requisitos para o App funcionar corretamente. Mostra que é necessário ter o Bitcoin e o nó Lightning. Se você ainda não instalou o nó Lightning no seu Umbrel, clique em Install. Este processo pode levar alguns minutos.

![image](assets/en/123.webp)

Após instalar seu nó Lightning:

1. Clique em open nos detalhes do app ou no App no painel do Umbrel.
2. Clique em setup a new node; serão mostradas 24 palavras para a recuperação do seu nó lightning.
3. Anote-as.

![image](assets/en/124.webp)
Umbrel solicitará a verificação das palavras recém-anotadas. Após a configuração do nó Lightning, retorne à Loja de Aplicativos Umbrel e encontre o BTCPay Server. Clique no botão de instalação, e o Umbrel mostrará se os componentes necessários estão instalados e que o BTCPay Server requer acesso a esses componentes. Após a instalação, clique em Abrir no topo direito dos detalhes do aplicativo ou abra o BTCPay Server através do painel de controle do seu Umbrel.

Umbrel solicitará a verificação das palavras recém-anotadas.

![imagem](assets/en/125.webp)

**!?Nota!?**

Certifique-se de armazenar estas em um local adequado, como aprendido anteriormente com o armazenamento de chaves.

Após a configuração do nó Lightning, retorne à Loja de Aplicativos Umbrel e encontre o BTCPay Server. Clique no botão de instalação, e o Umbrel mostrará se os componentes necessários estão instalados e que o BTCPay Server requer acesso a esses componentes.

![imagem](assets/en/126.webp)

Após a instalação, clique em Abrir no topo direito dos detalhes do aplicativo ou abra o BTCPay Server através do painel de controle do seu Umbrel.

![imagem](assets/en/127.webp)

### Resumo da Habilidade

Nesta seção, você aprendeu:

- Passos para instalar o BTCPay Server com funcionalidade Lightning em um nó Umbrel

### Avaliação de Conhecimento

#### Revisão Conceitual do KA

Como a configuração no Umbrel difere das duas opções hospedadas anteriormente?

# Conclusão

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>



## Avalie o curso
<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>
<isCourseReview>true</isCourseReview>

## Conclusão do Curso

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![imagem](assets/en/128.webp)

Você também deve ter uma compreensão geral do que é o Bitcoin, como funciona e como pode escalar com camadas secundárias como a Lightning Network. Neste curso, cobrimos extensivamente como qualquer pessoa pode usar o BTCPay Server, desde a instalação inicial até a criação de lojas e o gerenciamento complexo de faturas, para se tornar um indivíduo ou comerciante financeiramente autossuficiente.

Parabéns por completar este curso. Esperamos que você tenha gostado do conteúdo e continue a usar e explorar o BTCPay Server, e esteja tão empolgado com o futuro promissor que o Bitcoin e a crescente comunidade de construtores e participantes trarão como nós estamos.

> **O FOSS é inevitável.**

### Glossário

| Termo                                          | Definição                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ataque de 51%                                  | Ato de construir intencionalmente uma nova cadeia de blocos mais longa para substituir blocos na blockchain. Isso permite substituir transações que foram mineradas na blockchain. Esse tipo de ataque é mais fácil de realizar quando se tem a maioria do poder de mineração, razão pela qual é referido como "Ataque da Maioria" ou "Ataque de 51%".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AccountKey                                     | A chave da conta para rebase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| AccountKeyPath                                 | O caminho da raiz até a chave da conta é prefixado pela impressão digital da chave pública mestra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Endereço                                       | Os endereços Bitcoin codificam de forma compacta as informações necessárias para pagar um receptor. Um endereço moderno consiste em uma sequência de letras e números que começa com bc1 e se parece com bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4. Um endereço é uma forma abreviada do script de bloqueio do receptor, que pode ser usado pelo remetente para assinar a transferência de fundos para o receptor. A maioria dos endereços representa a chave pública do receptor ou algum tipo de script que define condições de gasto mais complexas. O exemplo anterior é um endereço bech32 codificando um programa de testemunha que bloqueia fundos para o hash de uma chave pública (Veja Pagamento-para-Testemunha-Chave-Pública-Hash). Também existem formatos de endereço mais antigos que começam com 1 ou 3 que usam a codificação de endereço Base58Check para representar hashes de chave pública ou hashes de script.           |
| Tipo de Endereço                               | Um endereço pode representar vários scripts diferentes. Os endereços são codificados e prefixados para transmitir seu tipo de script. Endereços legados usam Base58, e quando um endereço legado é o hash de uma chave pública, um endereço P2PKH, ele começa com um ‘1’. Menos frequentemente, um endereço legado é um hash de um script, caso em que começará com um ‘3’. Atualmente, todos os endereços SegWit são codificados em Bech32 e começam com o prefixo ‘bc1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| App                                            | O BTCPay Server possui plugins que podem funcionar como uma aplicação por si só.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| BIP 329                                        | Exportar/importar etiquetas de carteira                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| BIP49                                          | Define o esquema de derivação para carteiras HD usando o formato de serialização P2WPKH-aninhado-em-P2SH (BIP 141) para transações de testemunha segregada.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Endereço Bitcoin                               | String alfanumérica para onde você envia seu bitcoin, então ele “vive” lá agora É um identificador, que consiste em uma sequência de cerca de 33 letras e números combinados. Em uma versão atual do protocolo, um endereço começa com 1, 3 ou b. Ter o endereço do destinatário é uma parte necessária para iniciar uma transação bitcoin. Os endereços Bitcoin são gerados a partir de chaves públicas e vários endereços podem ser gerados a partir de um conjunto de chaves públicas para melhorar a privacidade. Os endereços Bitcoin funcionam como um endereço de e-mail, se você quer enviar uma mensagem você precisa saber para onde ela está indo, o mesmo acontece com o bitcoin. Antes de enviar uma transação bitcoin, você precisa garantir que o endereço do destinatário esteja correto, já que as transações bitcoin são irreversíveis e você pode estar enviando bitcoins para um endereço que não pertence ao destinatário. |
| bitcoin versus Bitcoin                         | Bitcoin é a rede monetária, e bitcoin (minúsculo) é uma unidade monetária na rede Bitcoin. Você usa a moeda bitcoin ou um token para transacionar na rede Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Bloco                                          | Um bloco é uma estrutura de dados na blockchain do Bitcoin que consiste em um cabeçalho e um corpo de transações Bitcoin. O bloco é marcado com um carimbo de data/hora e compromete-se com um bloco predecessor (pai) específico. Quando hashado, o cabeçalho do bloco fornece a prova de trabalho que torna a blockchain probabilisticamente imutável. Os blocos devem aderir às regras impostas pelo consenso da rede para estender a blockchain. Quando um bloco é anexado à blockchain, as transações incluídas são consideradas como tendo sua primeira confirmação.                                                                                                                                                                                                                                                                                                                                                                      |
| Explorador de Blocos                           | Uma ferramenta online que permite pesquisar por informações em tempo real e históricas sobre uma blockchain, incluindo dados relacionados a blocos, transações, endereços e mais.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Hash do Bloco                                  | Um hash do bloco é o hash SHA-256 dos dados do bloco, geralmente representado em formato hexadecimal. Um hash do bloco pode ser interpretado como um número muito grande. Para satisfazer o requisito de Prova de Trabalho, um hash do bloco deve estar abaixo de um certo limite. Assim, todos os hashes de blocos começam com uma série de zeros seguidos por uma string alfanumérica. Alguns blocos têm até vinte zeros iniciais, enquanto os blocos mais antigos têm tão poucos quanto oito. O número de zeros necessários demonstra aproximadamente a dificuldade de mineração no momento em que o bloco foi publicado.                                                                                                                                                                                                                                                                                                                    |
| Altura do Bloco                                | Cada bloco é numerado em ordem ascendente, começando do zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Recompensa do Bloco                            | Consiste na subvenção do bloco (bitcoin recém-criado) e na soma de todas as taxas de transação das transações incluídas no bloco.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Tamanho do Bloco                               | Cada bloco tem uma quantidade limitada de dados que pode conter. Os dados que não couberam em um determinado bloco serão registrados em um dos blocos seguintes. No que diz respeito aos blocos de bitcoin, costumava ter um tamanho de bloco de 1mb, no entanto, após um soft fork, o tamanho do bloco pode tecnicamente conter até 4mb de dados.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Subsídio do Bloco                              | A quantidade de novo bitcoin cunhado em cada bloco. Cada bloco que é produzido e adicionado à blockchain permite ao criador do bloco cunhar uma certa quantidade de novo bitcoin. O subsídio começou em 50 BTC por bloco e é reduzido pela metade a cada 210.000 blocos ou aproximadamente 4 anos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Blockchain                                     | Um log distribuído, ou banco de dados, de todas as transações Bitcoin. As transações são agrupadas em atualizações discretas chamadas blocos, limitadas até 4 milhões de unidades de peso. Os blocos são produzidos aproximadamente a cada 10 minutos por meio de um processo estocástico chamado mineração. Cada bloco inclui uma "prova de trabalho" computacionalmente intensiva. O requisito de prova de trabalho é usado para regular os intervalos de blocos e proteger a blockchain contra ataques para reescrever a história: um atacante precisaria superar a prova de trabalho existente para substituir blocos já publicados, tornando cada bloco probabilisticamente imutável à medida que é enterrado sob blocos subsequentes.                                                                                                                                                                                                     |
| BTCPay Server Vault                            | Para um equilíbrio ótimo entre facilidade de uso, segurança e privacidade, é recomendado usar a Carteira BTCPay Server com uma carteira de hardware. BTCPay Vault é construído para fazer a ponte entre a Carteira de Hardware e o BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Problema dos Generais Bizantinos               | Um problema de teoria dos jogos que descreve a dificuldade que as partes descentralizadas têm em chegar a um consenso sem depender de uma parte central confiável. O nome vem do cenário de vários generais cercando Bizâncio. Eles cercaram a cidade, mas devem decidir coletivamente quando atacar. Se todos os generais atacarem ao mesmo tempo, eles vencerão, mas se atacarem em momentos diferentes, perderão. Os generais não têm canais de comunicação seguros entre si porque qualquer mensagem que enviem ou recebam pode ter sido interceptada ou enviada de forma enganosa pelos defensores de Bizâncio. Como os generais podem se organizar para atacar ao mesmo tempo?                                                                                                                                                                                                                                                            |
| Censura                                        | Controle sobre quais informações podem ser transmitidas às massas. Quando se trata de bitcoin, censura é sobre a capacidade de parar a transação por terceiros.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Troco                                          | A porção de UTXOs retornada à carteira do remetente, geralmente por meio de um endereço diferente. Corresponde à soma das entradas menos o valor gasto e a taxa de transação.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Child Pays For Parent (CPFP)                   | Uma técnica de aumento de taxa onde um usuário gasta uma saída de uma transação não confirmada com taxa baixa em uma transação filha com taxa alta, a fim de incentivar os mineradores a incluir ambas as transações em um bloco.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Coinbase Transaction                           | A primeira transação em cada bloco que distribui a recompensa do bloco e as taxas de transação para quem minerou o bloco.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Coincidence of Wants                           | Um fenômeno econômico onde duas partes possuem um item que a outra deseja, então eles trocam esses itens diretamente sem qualquer meio monetário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Cold Storage                                   | Uma maneira de gerenciar dados sem estar conectado à internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Cold Wallet                                    | Um tipo de carteira bitcoin que armazena suas chaves privadas offline, geralmente em um dispositivo físico. Também conhecida como carteira de hardware, protege seu bitcoin digital de hackers online usando um dispositivo semelhante a um pen drive que não está conectado à internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Command Line Interface (CLI)                   | Interação com um dispositivo ou programa de computador com comandos de um usuário ou cliente, e respostas do dispositivo ou programa, na forma de linhas de texto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Commitment Transaction                         | Uma transação de compromisso é uma transação Bitcoin, assinada por ambos os parceiros do canal, que codifica o saldo mais recente de um canal. Toda vez que um novo pagamento é feito ou encaminhado usando o canal, o saldo do canal será atualizado, e uma nova transação de compromisso será assinada por ambas as partes. Importante, em um canal entre Alice e Bob, tanto Alice quanto Bob mantêm sua própria versão da transação de compromisso, que também é assinada pela outra parte. Em qualquer momento, o canal pode ser fechado por Alice ou Bob se eles submeterem sua transação de compromisso para o blockchain Bitcoin. Submeter uma transação de compromisso mais antiga (desatualizada) é considerado trapaça (ou seja, uma violação do protocolo) na Lightning Network e pode ser penalizado pela outra parte, reivindicando todos os fundos no canal para si mesmo, via uma transação de penalidade.                       |
| Confirmation                                   | Uma vez que uma transação é incluída em um bloco, ela tem uma confirmação. Assim que outro bloco é minerado no blockchain, a transação tem duas confirmações, e assim por diante. Seis ou mais confirmações são consideradas prova suficiente de que uma transação não pode ser revertida.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Crowdfund (CF)                                 | Um plugin padrão do BTCPay Server que permite ao proprietário de uma loja criar facilmente um site de financiamento coletivo típico. Eles podem definir facilmente um objetivo, criar recompensas para contribuições e personalizá-lo de acordo com suas necessidades.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Cryptography                                   | Um sistema especial, onde a mensagem original é alterada para que apenas os destinatários pretendidos possam recebê-la.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Dashboard                                      | A página central de destino do BTCPay Server. Fornece uma visão geral de toda a atividade de uma loja, exibida em uma série de blocos de resumo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Demo                                           | Refere-se ao ambiente virtual em que as demonstrações de software ocorrem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Deployment                                     | O deployment de software é todas as atividades que tornam um sistema de software disponível para uso. O processo geral de deployment consiste em várias atividades inter-relacionadas com possíveis transições entre elas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Caminho de Derivação                           | Um dado que informa a uma carteira Hierárquica Determinística (HD) como derivar uma chave específica dentro de uma árvore de chaves. Os caminhos de derivação são usados como um padrão Bitcoin e foram introduzidos com as carteiras HD como parte do BIP 32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Ajuste de Dificuldade                          | Ajuste no alvo de dificuldade, a cada 2016 blocos (aproximadamente duas semanas) para tentar garantir que os blocos sejam minerados uma vez a cada 10 minutos, em média. Isso cria um tempo consistente entre os blocos e uma emissão consistente de novos bitcoins na rede (via recompensa do bloco).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Alvo de Dificuldade                            | Usado na mineração, é um número que o hash de um bloco deve estar abaixo para que o bloco seja adicionado à blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Assinatura Digital                             | Uma assinatura digital é um esquema matemático para verificar a autenticidade e integridade de mensagens ou documentos digitais. Pode ser visto como um compromisso criptográfico no qual a mensagem não é ocultada.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Divisível                                      | A propriedade de um bem que pode ser dividido em quantidades menores sem perder valor. Como as transações econômicas frequentemente ocorrem em quantidades variadas, uma moeda deve ser divisível para ser amplamente utilizada em uma economia.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Docker                                         | Software que empacota software em unidades padronizadas chamadas contêineres que possuem tudo o que o software precisa para funcionar, incluindo bibliotecas, ferramentas do sistema, código e tempo de execução.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Gasto Duplo                                    | O resultado de gastar o mesmo dinheiro mais de uma vez. O Bitcoin protege contra o gasto duplo verificando que cada transação adicionada à blockchain adere às regras de consenso; isso significa verificar que as entradas para a transação não foram previamente gastas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Durável                                        | Propriedade do dinheiro, na qual a moeda pode manter seu estado original ao longo do tempo e suportar uso repetido. Uma moeda durável deve ser capaz de sobreviver a danos potenciais.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Electrum                                       | Electrum é uma das carteiras Bitcoin mais populares, criada em 2011.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Chave pública estendida (Xpub)                 | Chave pública estendida, também conhecida como Xpub, uma chave pública que funciona como pai para chaves derivadas do xpub como uma característica da Carteira HD. Este Xpub é um padrão introduzido no BIP 32. As carteiras usam isso nos bastidores para derivar chaves públicas. Não é aconselhado compartilhar o Xpub, seus fundos não estarão em risco direto de serem movidos, o xpub não pode derivar chaves privadas. O benefício de compartilhar um xpub pode ser para fins de financiamento coletivo no BTCPay Server. O xpub é compartilhado por meios online, enquanto as chaves privadas permanecem offline em um HWW.                                                                                                                                                                                                                                                                                                             |
| F.U.D.                                         | Abreviação para Medo, incerteza e dúvida; geralmente evocado intencionalmente para colocar um concorrente em desvantagem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Taxa                                           | No contexto da Lightning Network, os nós cobrarão taxas de roteamento para encaminhar os pagamentos de outros usuários. Os nós individuais podem definir suas próprias políticas de taxas, que serão calculadas como a soma de uma taxa_base fixa e uma taxa_rate que depende do valor do pagamento. No contexto do Bitcoin, o remetente de uma transação paga uma taxa de transação aos mineradores para incluir a transação em um bloco. As taxas de transação do Bitcoin não incluem uma taxa base e dependem linearmente do peso da transação, mas não do valor.                                                                                                                                                                                                                                                                                                                                                                            |
| Fiat                                           | Moeda emitida pelo governo que não é respaldada por uma commodity como ouro.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Finite                                         | Refere-se ao fornecimento limitado do Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Fork                                           | Uma mudança em um protocolo ou em um pedaço de código. Forks geralmente são introduzidos para atualizar um projeto. Na comunidade de código aberto, forks existem porque muitos indivíduos escolhem baixar e executar o mesmo software em momentos diferentes e nem sempre atualizam. Se dois usuários baixam e executam a versão 1 de um software, e apenas um usuário atualiza quando a versão 2 é lançada, o usuário que atualizou está executando um fork da versão 1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Funding Transaction                            | Transação usada para abrir um canal de pagamento. O valor (em bitcoin) da transação de financiamento é exatamente a capacidade do canal de pagamento. A saída da transação de financiamento é um script de assinatura múltipla 2-de-2 (multisig) onde cada parceiro do canal controla uma chave. Devido à sua natureza multisig, ela só pode ser gasta por acordo mútuo entre os parceiros do canal. Eventualmente, será gasta por uma das transações de compromisso ou pela transação de fechamento.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Fungible                                       | Ser algo (como dinheiro ou uma commodity) de tal natureza que uma parte ou quantidade pode ser substituída por outra parte ou quantidade igual em pagamento de uma dívida ou liquidação de uma conta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Gap Limit                                      | Refere-se ao número padrão de endereços públicos que são verificados por transações na blockchain a fim de calcular o saldo de uma conta. Transações recebidas em um endereço além do limite de gap de endereço não são detectadas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Genesis Block                                  | Primeiro bloco na blockchain do Bitcoin. Satoshi Nakamoto, o criador do Bitcoin, minerou o bloco Gênesis em 3 de janeiro de 2009 e incluiu a manchete do Financial Times daquele dia, “Chancellor on brink of second bailout for banks” (Chanceler à beira do segundo resgate para os bancos).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Github                                         | Uma plataforma e serviço baseado na nuvem para desenvolvimento de software e controle de versão usando Git, permitindo que desenvolvedores armazenem e gerenciem seu código.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Gossip Protocol                                | Nós da LN enviam e recebem informações sobre a topologia da Lightning Network através de mensagens de fofoca que são trocadas com seus pares. O protocolo de fofoca é principalmente definido no BOLT #7 e define o formato das mensagens de node_announcement, channel_announcement e channel_update. Para prevenir spam, mensagens de anúncio de nós só serão encaminhadas se o nó já tiver um canal, e mensagens de anúncio de canal só serão encaminhadas se a transação de financiamento do canal tiver sido confirmada pela rede Bitcoin. Geralmente, nós da Lightning se conectam com seus parceiros de canal, mas é aceitável conectar com qualquer outro nó da Lightning para processar mensagens de fofoca.                                                                                                                                                                                                                           |
| Gresham's Law                                  | Lei que afirma que “o dinheiro ruim expulsa o bom”. Em outras palavras, em uma economia onde duas moedas estão em uso, os indivíduos gastarão o dinheiro ruim, que está constantemente desvalorizando, e guardarão o dinheiro bom, que retém seu valor. Assim, o dinheiro ruim dominará em termos de circulação e uso em transações diárias, enquanto o dinheiro bom dominará em termos de poupança e investimento a longo prazo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Halving                                        | Um evento que reduz a taxa de emissão de bitcoin pela metade a cada 210.000 blocos (aproximadamente quatro anos).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Hard Fork                                      | Uma mudança de consenso que não é compatível com versões anteriores. A incompatibilidade com versões anteriores ocorre quando um comportamento anteriormente inválido é tornado válido. Para manter o consenso após um hard fork, todos os nós são obrigados a atualizar. Caso contrário, os nós antigos rejeitarão transações ou blocos como inválidos sob as regras antigas, enquanto os nós atualizados os aceitarão como válidos. Por essa razão, os hard forks são evitados a todo custo no Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Hardware Wallet (HWW)                          | Um tipo especial de carteira Bitcoin que armazena as chaves privadas do usuário em um dispositivo de hardware seguro.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Hash Function                                  | Uma função de hash criptográfica é um algoritmo matemático que mapeia dados de tamanho arbitrário para uma cadeia de bits de tamanho fixo (um hash) e é projetada para ser uma função unidirecional, ou seja, uma função que é inviável de inverter. A única maneira de recriar os dados de entrada a partir da saída de uma função de hash criptográfica ideal é tentar uma busca de força bruta de entradas possíveis para ver se elas produzem uma correspondência.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Hash Rate                                      | Uma medida de quantos hashes os mineradores produzem cumulativamente por segundo na rede Bitcoin. Um único hash é uma tentativa de criar uma Prova de Trabalho para um bloco.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Hot Wallet                                     | Um dispositivo com conexões externas, especialmente com a internet. Uma hot wallet é uma carteira Bitcoin que se conecta à internet. Essas carteiras são mais convenientes para gastos do dia a dia, mas não são tão seguras quanto as opções de armazenamento a frio porque interagem com a internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Initial Block Download (IBD)                   | O processo de construir a blockchain completa do Bitcoin do zero. Quando um novo nó é configurado e se junta à rede, ele se conecta a outros nós e pede por blocos. O novo nó processa esses blocos e constrói a blockchain até que tenha alcançado e esteja sincronizado com a rede.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Invoice                                        | Um documento comercial emitido por um vendedor para um comprador relacionado a uma transação de venda e indicando os produtos, quantidades e preços acordados para produtos ou serviços que o vendedor forneceu ao comprador.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Know Your Customer (KYC)                       | Leis destinadas a prevenir que instituições financeiras sejam usadas para transferências de dinheiro ilícitas, exigindo que todas as contas financeiras sejam identificáveis a indivíduos ou organizações.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Layer 2                                        | Uma rede construída em cima de uma blockchain, por exemplo, a Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Legacy Address                                 | Endereços legacy usam Base58, e quando um endereço legacy é o hash de uma chave pública, um endereço P2PKH, ele começa com um ‘1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Lightning Network                              | Um protocolo em cima do Bitcoin. Ele cria uma rede de canais de pagamento que permite o encaminhamento sem confiança de pagamentos através da rede com a ajuda de HTLCs e roteamento onion. Outros componentes da Lightning Network são o protocolo de fofoca, a camada de transporte e as solicitações de pagamento.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Liquidity                                      | Medida de várias características do livro de ordens de um determinado ativo dentro de um dado mercado. Liquidez é um indicador de quanto impacto no mercado uma grande ordem terá sobre o preço de um ativo. Um ativo com mais liquidez tem maior profundidade no livro de ordens. Isso significa que ele será capaz de absorver mais ordens com menores movimentos de preço.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Cadeia Mais Longa                              | A cadeia de blocos que exigiu mais esforço para ser construída. Nomeada desta forma pois, intuitivamente, uma blockchain com mais blocos terá exigido mais energia para ser construída do que uma cadeia com menos blocos, mas de forma mais precisa, é a cadeia que exigiu mais trabalho para ser produzida, então um nome melhor poderia ter sido "cadeia mais pesada".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Cadeia Principal                               | No contexto da Lightning Network, refere-se à Rede Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Meio de Troca                                  | Um tipo de bem que facilita a troca de outros bens e serviços dentro de uma economia. Historicamente, itens como conchas, contas e ouro foram usados como meio de troca.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Mempool                                        | Abreviação de "pool de memória", é um armazenamento temporário para transações que foram recebidas por um nó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Minerador                                      | Um nó envolvido no processo de construção da blockchain, adicionando novos blocos por meio do processo de hashing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Mineração                                      | Processo de construir um bloco a partir de transações recentes do Bitcoin e, em seguida, resolver um problema computacional exigido como prova de trabalho. É o processo pelo qual o livro-razão compartilhado do bitcoin (ou seja, a blockchain do Bitcoin) é atualizado e pelo qual novas transações são incluídas no livro-razão. Também é o processo pelo qual novos bitcoins são emitidos. Toda vez que um novo bloco é criado, o nó de mineração receberá novos bitcoins criados dentro da transação coinbase desse bloco.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Multisignature (multisig)                      | Um script que requer mais de uma assinatura para autorizar gastos. Canais de pagamento são sempre codificados como endereços multisig, exigindo uma assinatura de cada parceiro do canal de pagamento. No caso padrão de um canal de pagamento de duas partes, um endereço multisig 2-de-2 é usado.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Nó                                             | Um computador participando de uma rede. Em particular, as redes Bitcoin ou Lightning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Saída                                          | Pacote de bitcoins criado em uma transação bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Bloqueio de Saída                              | Um conjunto de requisitos colocados em uma saída. Esses requisitos devem ser atendidos para poder usar a saída em uma transação. O exemplo mais comum é uma simples exigência de possuir a chave privada.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Endereço P2SH                                  | Os endereços P2SH são codificações Base58Check do hash de 20 bytes de um script. Endereços P2SH começam com um "3". Endereços P2SH escondem toda a complexidade, de modo que o remetente de um pagamento não vê o script.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Endereço P2WPKH                                | O formato de endereço "SegWit nativo v0", endereços P2WPKH são codificados em bech32 e começam com "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Endereço P2WSH                                 | O formato de endereço de script "SegWit nativo v0", endereços P2WSH são codificados em bech32 e começam com "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Transação Bitcoin Parcialmente Assinada (PSBT) | Um padrão Bitcoin que facilita a portabilidade de transações não assinadas, o que permite que várias partes assinem facilmente a mesma transação. Isso é mais útil quando várias partes desejam adicionar entradas à mesma transação. PSBT foi introduzido pelo BIP 174 e permite que os usuários assinem transações mais facilmente em um dispositivo de armazenamento a frio e, em seguida, transmitam a transação assinada de um dispositivo conectado à internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pathfinding                                    | O processo de encontrar um caminho para pagamento de uma fonte até um destino na Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pay-to-Public-Key-Hash (P2PKH)                 | P2PKH é um tipo de saída que bloqueia bitcoin ao hash de uma chave pública. Uma saída bloqueada por um script P2PKH pode ser desbloqueada (gasta) apresentando a chave pública correspondente ao hash e uma assinatura digital criada pela chave privada correspondente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Pay-to-Script-Hash (P2SH)                      | P2SH é um tipo versátil de saída que permite o uso de Scripts Bitcoin complexos. Com P2SH, o script complexo que detalha as condições para gastar a saída (script de resgate) não é apresentado no script de bloqueio. Em vez disso, o valor é bloqueado ao hash de um script, que deve ser apresentado e cumprido para gastar a saída.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Pay-to-Taproot (P2TR)                          | Ativado em novembro de 2021, Taproot é um novo tipo de saída que bloqueia bitcoin a uma árvore de condições de gasto, ou uma única condição raiz.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Pay-to-Witness-Public-Key-Hash (P2WPKH)        | P2WPKH é o equivalente SegWit de P2PKH, usando uma testemunha segregada. A assinatura para gastar uma saída P2WPKH é colocada na árvore de testemunhas em vez do campo ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Pay-to-Witness-Script-Hash (P2WSH)             | P2WSH é o equivalente SegWit de P2SH, usando uma testemunha segregada. A assinatura e o script para gastar uma saída P2WSH são colocados na árvore de testemunhas em vez do campo ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Payjoin                                        | Um tipo especial de transação Bitcoin onde tanto o remetente quanto o receptor contribuem com entradas a fim de quebrar a heurística de posse de entrada comum, uma suposição usada para retirar a privacidade dos usuários do bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Payment Channel                                | Uma relação financeira entre dois nós na Lightning Network, criada usando uma transação bitcoin que paga a um endereço de assinatura múltipla. Os parceiros do canal podem usar o canal para enviar bitcoin de um para o outro sem registrar todas as transações na blockchain do Bitcoin. Em um canal de pagamento típico, apenas duas transações, a transação de financiamento e a transação de compromisso, são adicionadas à blockchain. Pagamentos enviados através do canal não são registrados na blockchain e diz-se que ocorrem "fora da cadeia".                                                                                                                                                                                                                                                                                                                                                                                      |
| Payment Request                                | Uma funcionalidade que permite aos proprietários de lojas BTCPay criar faturas de longa duração. Fundos pagos a um pedido de pagamento usam a taxa de câmbio no momento do pagamento. Isso permite que os usuários façam pagamentos quando lhes convier, sem ter que negociar ou verificar taxas de câmbio com o proprietário da loja no momento do pagamento.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Payout                                         | A funcionalidade de pagamento está ligada aos Pagamentos por Solicitação. Esta característica permite processar pagamento por solicitação (reembolsos, pagamentos de salários ou saques).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Plugin                                         | Um complemento de software que é instalado em um programa, melhorando suas capacidades.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Point Of Sale (PoS)                            | Um plugin padrão do BTCPay Server que permite a um proprietário de loja criar uma loja virtual diretamente do BTCPay Server. O proprietário da loja não precisa de soluções de comércio eletrônico de terceiros para executar uma loja virtual.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Portabilidade                                  | Capacidade de um bem ser transportado facilmente pelo espaço. A portabilidade é uma característica importante do dinheiro sólido; para que um dinheiro seja amplamente adotado, e, portanto, utilizável, ele deve ser capaz de se mover através de fronteiras, entre indivíduos e por longas distâncias com relativa facilidade.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Prova de Trabalho (PoW)                        | Dados que requerem significativa computação para serem encontrados, e podem ser facilmente verificados por qualquer pessoa para provar a quantidade de trabalho que foi necessária para produzi-los. No Bitcoin, os mineradores devem encontrar uma solução numérica para o algoritmo SHA-256 que atenda a um alvo definido pela rede, chamado de alvo de dificuldade.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Pseudônimo                                     | Um nome falso usado por indivíduos para proteger sua identidade ou construir uma reputação separada de sua identidade real. Chaves públicas são usadas para permitir que usuários de Bitcoin recebam bitcoin enquanto permanecem pseudônimos em relação ao blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Criptografia de Chave Pública                  | Envolve um par de chaves conhecido como chave pública e chave privada, que estão associadas a uma entidade que precisa autenticar sua identidade eletronicamente ou para assinar ou criptografar dados. A chave pública é publicada e a chave privada correspondente é mantida em segredo. Dados que são criptografados com a chave pública só podem ser descriptografados com a chave privada correspondente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Chave Pública/Privada                          | Par de chaves usado em criptografia de chave pública. A chave pública é compartilhada com outros abertamente, e pode ser considerada como um número de conta, enquanto a chave privada é mantida em segredo e pode ser considerada como uma senha.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Pagamento por Solicitação                      | Tradicionalmente, para fazer um pagamento em Bitcoin, um receptor compartilha seu endereço de bitcoin e o remetente posteriormente envia dinheiro para este endereço. Esse sistema é chamado de pagamento por envio, pois o remetente inicia o pagamento enquanto o receptor pode estar indisponível, efetivamente empurrando o pagamento para o receptor. Em vez do cenário típico de um remetente "empurrando" o pagamento, o remetente permite que o receptor solicite o pagamento no momento que achar conveniente.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Buraco do Coelho                               | Uma referência a Alice no País das Maravilhas, onde a heroína embarca em uma aventura entrando em um buraco de coelho. Dentro do Bitcoin, refere-se aos tópicos aparentemente intermináveis que alguém explora e vê sob uma nova luz, uma vez que começou a entender o Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Receber                                        | O processo de ter bitcoin enviado para um endereço fornecido.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Registrar                                      | O processo de criar uma conta ou inscrever-se para um serviço, geralmente feito escolhendo um nome de usuário e senha.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Substituir por Taxa (RBF)                      | Uma transação de Bitcoin pode ser designada como RBF para permitir que o remetente substitua esta transação por outra semelhante que pague uma taxa maior. Esse mecanismo existe para permitir que os usuários respondam se a rede se tornar congestionada e as taxas aumentarem inesperadamente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Repositório                                    | Em sistemas de controle de versão, um repositório é uma estrutura de dados que armazena metadados para um conjunto de arquivos ou estrutura de diretório. Dependendo se o sistema de controle de versão em uso é distribuído, como Git ou Mercurial, ou centralizado, como Subversion, CVS ou Perforce, todo o conjunto de informações no repositório pode ser duplicado em cada sistema do usuário ou pode ser mantido em um único servidor. Alguns dos metadados que um repositório contém incluem, entre outras coisas, um registro histórico de mudanças no repositório, um conjunto de objetos de commit e um conjunto de referências a objetos de commit, chamados cabeças.                                                                                                                                                                                                                                                               |
| Rescan                                         | Processo de escanear o estado atual do conjunto UTXO para moedas pertencentes a um esquema de derivação previamente configurado.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Revokation Key                                 | Cada Contrato de Maturidade de Sequência Revogável (RSMC) contém duas chaves de revogação. Cada parceiro do canal conhece uma chave de revogação. Conhecendo ambas as chaves de revogação, a saída do RSMC pode ser gasta dentro do timelock pré-definido. Ao negociar um novo estado do canal, as antigas chaves de revogação são compartilhadas, assim "revogando" o estado antigo. Chaves de revogação são usadas para desencorajar parceiros do canal de transmitir um estado antigo do canal.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Routing                                        | O processo de usar o caminho da Lightning Network para fazer pagamento.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Routing Fees                                   | Na Lightning Network, taxas cobradas por encaminhar pagamentos de outros usuários. Nós individuais podem definir suas próprias políticas de taxas, que serão calculadas como a soma de uma base_fee fixa e uma fee_rate que depende do valor do pagamento.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Salability                                     | A facilidade com que um bem pode ser vendido no mercado sempre que seu detentor desejar, com a menor perda no seu preço.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Satoshi (sat)                                  | Um satoshi é a menor unidade (denominação) de bitcoin que pode ser registrada na blockchain. Um satoshi é 1/100 milionésimo (0.00000001) de um bitcoin e é nomeado após o criador do Bitcoin, Satoshi Nakamoto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Satoshi Nakamoto                               | O nome usado pela pessoa ou grupo de pessoas que projetou o Bitcoin e criou sua implementação de referência original. Como parte da implementação, eles também conceberam o primeiro banco de dados blockchain. No processo, foram os primeiros a resolver o problema do gasto duplo para moeda digital. Sua verdadeira identidade permanece desconhecida.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Satoshi Per Byte                               | Uma unidade para medir a prioridade da transação, definida pela taxa da transação em satoshi dividida pelo tamanho da transação em bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Satoshi Per Verabyte                           | Conceito semelhante ao Satoshi Per Byte, mas para endereços mais novos que usam Segwit. Igual ao tamanho da transação em unidades de Peso dividido por 4. Unidades de Peso são calculadas pegando o tamanho da transação (sem a testemunha) vezes 3, adicionado ao tamanho da transação incluindo testemunha.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Scarcity                                       | Propriedade de um bem que não pode ser replicado sem custos. A escassez não depende do número de unidades existentes de um bem, mas sim do custo de produzir mais unidades.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Script                                         | O Bitcoin usa um sistema de script para transações chamado Bitcoin Script. Assemelhando-se à linguagem de programação Forth, é simples, baseado em pilha e processado da esquerda para a direita. É propositalmente Turing-incompleto, sem loops ou recursão.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Seed Phrase                                    | Uma lista de palavras que armazena todas as informações necessárias para recuperar fundos Bitcoin na cadeia. O software de carteira geralmente gera uma frase-semente e instrui o usuário a escrevê-la em papel. Se o computador do usuário quebrar ou seu disco rígido se tornar corrompido, eles podem baixar o mesmo software de carteira novamente e usar o backup em papel para recuperar seus bitcoins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Segregated Witness (SegWit)                    | Segregated Witness (SegWit) é uma atualização do protocolo Bitcoin introduzida em 2017 que adiciona um novo campo de testemunha para assinaturas e outras provas de autorização de transações. Esse novo campo de testemunha é isento do cálculo do ID da transação, o que resolve a maioria das classes de maleabilidade de transação por terceiros. Segregated Witness foi implementado como um soft fork e é uma mudança que tecnicamente torna as regras do protocolo Bitcoin mais restritivas.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Self-Sovereignty                               | Um modelo para gerenciar identidades digitais no qual indivíduos ou empresas têm a propriedade exclusiva sobre a capacidade de controlar suas contas e dados pessoais.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Send                                           | O processo de enviar bitcoin para um endereço.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Sensitivity Mode                               | Ativado por meio de um interruptor nas configurações da loja, a ativação resulta em valores numéricos (por exemplo, quantidade de bitcoin) sendo obscurecidos em todas as visualizações.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Server Settings                                | Configurações dentro do BTCPay Server que se aplicam a todo o servidor (em contraposição às Configurações da Loja, que são limitadas em escopo a uma única loja).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| SHA-256                                        | Uma função de hash criptográfica. Membro de uma família de funções de hash chamada Funções de Hashing Seguro (SHA).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Shopify                                        | Uma empresa multinacional de comércio eletrônico canadense com sede em Ottawa, Ontário. Shopify é o nome de sua plataforma proprietária de comércio eletrônico para lojas online e sistemas de ponto de venda.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SMTP                                           | Simple Mail Transfer Protocol é um padrão de protocolo de comunicação da Internet para transmissão de correio eletrônico.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Soft Fork                                      | Uma atualização de protocolo que é compatível para frente e para trás, permitindo que tanto os nós antigos quanto os novos continuem usando a mesma cadeia.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Software Stack                                 | Em computação, um stack de soluções ou stack de software é um conjunto de subsistemas ou componentes de software necessários para criar uma plataforma completa de tal forma que nenhum software adicional seja necessário para suportar aplicações.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Store                                          | Uma loja dentro do BTCPay Server pode ser vista como um "Lar" para uma carteira bitcoin específica, estendendo com todas as funcionalidades do BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Store Settings                                 | Configurações dentro do BTCPay Server específicas para uma loja.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Taproot                                        | Atualização do Bitcoin que introduziria várias novas funcionalidades. A atualização é descrita nos BIPs 340, 341 e 342, e introduz o esquema de assinatura Schnorr, Taproot e Tapscript. Juntas, essas atualizações introduzem novas maneiras mais eficientes, flexíveis e privadas de transferir bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Thier's Law                                    | Lei que afirma que o bom dinheiro expulsará o mau dinheiro.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Third-Party Host                               | Quando um site de um indivíduo ou empresa é executado em servidores de propriedade e gerenciados por outra empresa. A alternativa é ter seu site hospedado em seus próprios servidores em seu data center.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Timelock                                       | Um timelock é um tipo de ônus que restringe a despesa de alguns bitcoins até um tempo futuro especificado ou altura de bloco. Timelocks são proeminentes em muitos contratos Bitcoin, incluindo canais de pagamento e HTLCs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Topologia                                      | A topologia da Lightning Network descreve a forma da Lightning Network como um gráfico matemático. Os nós do gráfico são os nós da Lightning (participantes da rede/pares). As arestas do gráfico são os canais de pagamento. A topologia da Lightning Network é publicamente transmitida com a ajuda do protocolo de fofoca, com exceção dos canais não anunciados. Isso significa que a Lightning Network pode ser significativamente maior do que o número anunciado de canais e nós. Conhecer a topologia é de interesse particular no processo de roteamento baseado na origem dos pagamentos, no qual o remetente descobre uma rota.                                                                                                                                                                                                                                                                                                      |
| Transação                                      | Transações são estruturas de dados usadas pelo Bitcoin para transferir bitcoin de um endereço para outro. Várias milhares de transações são agregadas em um bloco, que é então registrado (minerado) na blockchain. A primeira transação em cada bloco, chamada de transação coinbase, gera novos bitcoins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ID da Transação                                | Uma sequência de letras e números que identifica uma transação específica na blockchain. A sequência é simplesmente o hash duplo SHA-256 de uma transação. Esse hash pode ser usado para procurar uma transação em um nó ou explorador de blocos.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Autenticação de Dois Fatores (2FA)             | Um método de segurança de gerenciamento de identidade e acesso que requer duas formas de identificação para acessar recursos e dados, muitas vezes com um dispositivo secundário além da senha de login padrão.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Incensurável                                   | Propriedade de que nenhuma entidade tem a capacidade de reverter uma transação Bitcoin ou colocar na lista negra uma carteira ou endereço.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Inconfiscável                                  | Propriedade de que nenhuma entidade pode tomar bitcoin de uma entidade contra a sua vontade.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Saídas de Transação Não Gastas (UTXO)          | Saídas ainda não gastas, portanto disponíveis para serem usadas em novas transações.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Experiência do Usuário (UX)                    | Como um usuário interage com e vivencia um produto, sistema ou serviço. Inclui as percepções de uma pessoa sobre utilidade, facilidade de uso e eficiência.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Interface do Usuário (UI)                      | O ponto de interação e comunicação humano-computador em um dispositivo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Verificável                                    | Propriedade de um bem que pode ser facilmente diferenciado de impostores e falsificações.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Virtual                                        | Existindo ou simulado em um computador ou rede de computadores.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Máquina Virtual (VM)                           | Em computação, uma máquina virtual é a virtualização ou emulação de um sistema de computador. Máquinas virtuais são baseadas em arquiteturas de computadores e fornecem a funcionalidade de um computador físico. Suas implementações podem envolver hardware especializado, software ou uma combinação dos dois.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Servidor Privado Virtual                       | Um servidor privado virtual é uma máquina virtual vendida como um serviço por um serviço de hospedagem na Internet. O termo "servidor dedicado virtual" também tem um significado semelhante. Um servidor privado virtual executa sua própria cópia de um sistema operacional, e os clientes podem ter acesso de nível de superusuário a essa instância do sistema operacional, para que possam instalar quase qualquer software que funcione nesse SO                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Volatilidade                                   | Medida do grau de variação no preço de um ativo ao longo do tempo. Ativos que experimentam grandes mudanças de preço regularmente são mais voláteis, enquanto ativos que têm um preço mais estável são menos voláteis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Carteira                                       | As carteiras Bitcoin armazenam as chaves de um usuário, permitindo que os usuários recebam bitcoin, assinem transações e verifiquem o saldo de suas contas. As chaves privadas e públicas contidas em uma carteira Bitcoin desempenham duas funções distintas, mas são vinculadas na criação. Carteiras Bitcoin contêm as chaves de um usuário, não seus bitcoins de fato. Conceitualmente, uma carteira é como um chaveiro no sentido de que ela contém muitos pares de chaves privadas e públicas. Essas chaves são usadas para assinar transações, permitindo que um usuário prove que possui saídas de transações na blockchain, ou seja, seus bitcoins. Todos os bitcoins são registrados na blockchain na forma de saídas de transações.                                                                                                                                                                                                  |
| Wasabi Wallet                                  | Uma carteira Bitcoin de código aberto, não custodial e focada em privacidade para Desktop que implementa CoinJoin sem necessidade de confiança.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Carteira Somente-Leitura                       | Carteiras Bitcoin que permitem acompanhar seus bitcoins em armazenamento frio enquanto desabilitam a capacidade de gastar fundos. Isso ocorre porque carteiras somente-leitura não armazenam ou usam chaves privadas, e, portanto, são incapazes de autorizar qualquer gasto em nome do usuário.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Baleia                                         | No contexto do Bitcoin, uma baleia é alguém que possui uma grande quantidade de bitcoins.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| White-Label                                    | Um produto white-label é um produto ou serviço produzido por uma empresa que outras empresas rebrandizam para fazer parecer que foram elas que o criaram.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Whitepaper                                     | Apresenta uma nova ideia ou tópico para discussão. O whitepaper do Bitcoin introduziu o Bitcoin como um "Sistema de dinheiro eletrônico peer-to-peer" que "não requeria partes terceiras confiáveis". Satoshi Nakamoto lançou o whitepaper em 31 de outubro de 2008 para uma lista de e-mails de criptógrafos e cypherpunks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Wrapped Segwit                                 | Uma implementação de design incluída na atualização SegWit destinada a permitir que carteiras e outros softwares Bitcoin suportem mais facilmente o SegWit. Para alcançar isso, os dois scripts nativos SegWit, P2WPKH e P2WSH, são usados como o "redeemScript" de uma transação P2SH, resultando nos tipos de script SegWit embrulhados P2SH-P2WPKH e P2SH-P2WSH, respectivamente.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

![imagem](assets/en/129.webp)
