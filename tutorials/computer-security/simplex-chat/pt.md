---
name: SimpleX Chat
description: A primeira caixa de correio sem um ID de utilizador
---
![cover](assets/cover.webp)



Lançado em 2021, o SimpleX é uma aplicação gratuita de mensagens instantâneas com uma abordagem radicalmente diferente à privacidade. Ao contrário do WhatsApp, do Signal e de outros serviços de mensagens centralizados, o SimpleX distingue-se pela sua gestão de utilizadores: não existem identificadores de utilizadores, pseudónimos, números ou chaves públicas visíveis. Esta ausência total de identificadores torna praticamente impossível correlacionar os utilizadores, garantindo um elevado nível de privacidade.



Ao contrário da maioria das aplicações que requerem uma conta ou um número de telefone, o SimpleX permite-lhe iniciar conversas partilhando uma ligação ou um código QR efémero. Cada link cria um canal encriptado único, e os contactos não podem encontrar ou voltar a contactar o remetente sem um Exchange explícito. As mensagens são encriptadas de ponta a ponta e passam por servidores de retransmissão que as apagam após o envio, e não vêem nem o remetente nem o destinatário, nem as suas chaves.



![Image](assets/fr/01.webp)



A arquitetura da rede é totalmente descentralizada e não federada: os servidores não se conhecem uns aos outros, não mantêm um diretório global e não alojam quaisquer perfis de utilizador. Melhor ainda, cada utilizador pode implementar e utilizar o seu próprio servidor de retransmissão, mantendo-se interoperável com os servidores da rede pública.



O SimpleX é totalmente de código aberto (clientes, protocolos e servidores), disponível para Android, iOS, Linux, Windows e macOS. O seu armazenamento local é encriptado e portátil, pelo que é possível transferir um perfil de um dispositivo para outro sem depender de um servidor centralizado.



O SimpleX integra todas as funcionalidades clássicas das aplicações de mensagens. No entanto, a sua ergonomia continua a ser menos fluida do que a do WhatsApp ou do Signal. A sua utilização pode também ser mais restritiva, nomeadamente para adicionar contactos. Assim, na minha opinião, é uma alternativa pertinente ao WhatsApp ou ao Signal para os utilizadores que colocam a confidencialidade no centro das suas prioridades e que estão dispostos, por essa razão, a fazer algumas concessões no conforto quotidiano do utilizador.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| **SimpleX**          | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Encriptação de ponta a ponta*



## Instalar a aplicação SimpleX Chat



O SimpleX Chat está disponível em todas as plataformas. Pode descarregar a aplicação diretamente da loja de aplicações do seu telemóvel:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



No Android, também é possível [instalar via APK] (https://github.com/simplex-chat/simplex-chat/releases).



Neste tutorial, vamos concentrar-nos na versão móvel, mas tenha em atenção que também estão disponíveis [versões para computador](https://simplex.chat/downloads/) (MacOS, Linux e Windows). É possível ligar a versão para computador a um perfil de utilizador móvel existente, mas para que esta sincronização funcione, ambos os dispositivos têm de estar ligados à mesma rede local.



![Image](assets/fr/02.webp)



## Criar uma conta no SimpleX Chat



Quando abrir a aplicação pela primeira vez, clique no botão "*Criar o seu perfil*".



![Image](assets/fr/03.webp)



Escolha um nome de utilizador, que pode ser o seu nome verdadeiro ou um pseudónimo, e clique em "*Criar*".



![Image](assets/fr/04.webp)



Em seguida, defina a frequência com que a aplicação irá verificar se existem novas mensagens. Se a duração da bateria do seu telefone não for um problema, selecione "*Instantâneo*" para receber mensagens em tempo real. Se preferir poupar a bateria e evitar que a aplicação seja executada em segundo plano, selecione "*Quando a aplicação estiver a ser executada*": só receberá mensagens quando a aplicação estiver aberta. Um compromisso possível é optar por uma verificação periódica de 10 em 10 minutos.



Depois de ter feito a sua escolha, clique em "*Utilizar chat*".



![Image](assets/fr/05.webp)



Está agora ligado ao SimpleX Chat e pronto para começar a conversar.



![Image](assets/fr/06.webp)



## Configurar o SimpleX Chat



Em primeiro lugar, aceda às definições clicando na sua fotografia de perfil no canto inferior direito e, em seguida, em "*Definições*".



![Image](assets/fr/07.webp)



As predefinições são geralmente adequadas para a maioria dos utilizadores. No entanto, recomendo que aceda ao menu "*Database passphrase & export*". É aqui que pode exportar a sua base de dados de contas SimpleX para efeitos de cópia de segurança.



Também pode modificar o passphrase utilizado para encriptar esta base de dados. Por defeito, é gerado aleatoriamente e armazenado localmente no seu dispositivo. Se preferir, pode definir o seu próprio passphrase e eliminar a cópia de segurança do passphrase local: terá então de o introduzir manualmente sempre que abrir a aplicação, bem como quando migrar para outro dispositivo.



**Atenção**: se escolher esta opção, a perda do passphrase resultará na perda permanente de todos os seus perfis e mensagens SimpleX.



![Image](assets/fr/08.webp)



Também recomendo que vá ao menu "*Privacidade e segurança*", onde pode ativar a opção "*SimpleX Lock*". Esta opção protege o acesso à aplicação com um código de bloqueio.



![Image](assets/fr/09.webp)



Finalmente, os menus "*Notificações*" e "*Aparência*" permitem-lhe personalizar o SimpleX Chat de acordo com as suas preferências.



![Image](assets/fr/10.webp)



## Enviar mensagens com o SimpleX Chat



Para se ligar a outra pessoa no SimpleX, tem duas opções:




- Utilizar uma ligação de utilização única;
- Utilizar um Address estático reutilizável.



Um Address estático permite a qualquer pessoa que o conheça contactá-lo no SimpleX. É um Address persistente, que pode ser usado várias vezes, por pessoas diferentes, sem limite de tempo. É esta persistência que o torna mais vulnerável ao spam. No entanto, ao contrário de outras aplicações de mensagens, apagar o seu SimpleX Address é suficiente para parar todo o spam, sem afetar as conversas existentes. De facto, este Address só é utilizado para estabelecer a ligação inicial e deixa de ser necessário quando o Exchange tiver começado.



As ligações de utilização única, por outro lado, só podem ser utilizadas uma vez, por qualquer utilizador. Quando um contacto a utiliza, a ligação torna-se inválida. Terá de criar uma nova ligação generate para cada novo contacto.



### Com Address estático



Se desejar utilizar o Address, clique na sua imagem de perfil no canto inferior esquerdo do Interface e selecione "*Create SimpleX Address*". Em seguida, clique novamente em "*Criar SimpleX Address*".



![Image](assets/fr/11.webp)



O seu Address reutilizável foi criado. Pode partilhá-lo com pessoas que queiram entrar em contacto consigo, mostrando-lhes o código QR ou enviando-lhes a ligação.



![Image](assets/fr/12.webp)



Clique no botão "*Configurações do Address*". Aqui pode configurar as permissões associadas ao seu Address. A opção "*Partilhar com os contactos*" torna o seu Address visível no seu perfil SimpleX. Os seus contactos poderão então consultá-lo e reencaminhá-lo para outras pessoas que desejem contactá-lo.



A opção "*Auto-aceitação*" aceita automaticamente as ligações recebidas através do seu Address. Isto significa que qualquer pessoa com o seu Address poderá ver o seu perfil e enviar-lhe uma mensagem, a menos que active a opção "*Aceitar incógnito*". Esta opção oculta o seu nome e foto de perfil quando é estabelecida uma nova ligação, substituindo-os por um pseudónimo aleatório, distinto para cada interlocutor.



![Image](assets/fr/13.webp)



### Com ligação reutilizável



A segunda forma de estabelecer uma ligação com uma pessoa é criar uma ligação única. Para tal, clique no ícone do lápis no canto inferior direito do Interface e, em seguida, selecione "*Criar uma ligação única*".



Se o seu contacto lhe enviou uma ligação, clique em "*Digitalizar / Colar ligação*" para a digitalizar ou colar.



![Image](assets/fr/14.webp)



O SimpleX gera então uma ligação de utilização única. Pode reencaminhá-lo para o seu contacto por qualquer meio: Exchange físico, outras mensagens, etc.



![Image](assets/fr/15.webp)



Também pode escolher o perfil a associar a esta ligação de convite. Para o fazer, clique no seu perfil logo abaixo do código QR. Poderá então :




- selecione um dos seus perfis existentes (veremos como criar vários perfis na secção seguinte);
- ou escolher o modo "*Incógnito*", que oculta o seu nome e fotografia de perfil com um pseudónimo gerado aleatoriamente para o seu correspondente.



Aqui, escolho o modo "*Incognito*".



![Image](assets/fr/16.webp)



O meu contacto utilizou a ligação. Por seu lado, não activou o modo "*Incognito*", razão pela qual vejo o seu nome de perfil, "*Bob*". Por outro lado, o Bob não vê o meu nome verdadeiro "*Loïc Morel*", mas sim um pseudónimo aleatório, neste caso "*RealSynergy*".



![Image](assets/fr/17.webp)



Poderia começar a conversar imediatamente, mas primeiro gostaria de verificar se estou a falar com o Bob e não com uma pessoa mal-intencionada que possa ter intercetado a ligação ou efectuado um ataque MITM.



Para o fazer, vamos verificar a nossa ligação de segurança **fora da aplicação**. Isto é importante, porque no caso de um ataque MITM, a verificação interna seria comprometida. Por isso, utilize outro sistema de mensagens seguro ou, melhor ainda, verifique os códigos pessoalmente.



No chat, clica na fotografia do Bob e depois em "*Verificar código de segurança*". O Bob tem de fazer o mesmo do seu lado.



![Image](assets/fr/18.webp)



Se estiver a trabalhar remotamente, compare os códigos noutro sistema de mensagens seguro (têm de ser idênticos). Ou, melhor ainda, se puderem encontrar-se pessoalmente, digitalize o código QR do seu contacto clicando em "*Digitalizar código*".



![Image](assets/fr/19.webp)



Se a verificação for bem sucedida, aparecerá um ícone de escudo com uma marca de verificação junto ao nome do seu contacto. Esta é a sua garantia de que está a trocar mensagens com o Bob. Se a verificação não for bem sucedida, aparecerá um alerta "*Código de segurança incorreto!*".



![Image](assets/fr/20.webp)



Agora, pode enviar livremente mensagens, chamadas e ficheiros do Exchange para o Bob, dependendo das permissões que definiu para esta conversa.



## Personalize seus perfis do SimpleX Chat



Uma das caraterísticas mais poderosas do SimpleX é a capacidade de gerir vários perfis de utilizador completamente separados, todos acessíveis a partir da mesma conta local. Isto permite-lhe separar as suas diferentes identidades, sem complicar a gestão de mensagens.



Por exemplo, pode criar um ficheiro :




- Um perfil com o seu nome verdadeiro e uma fotografia verdadeira para as suas trocas profissionais;
- Um perfil com o seu nome verdadeiro e uma fotografia engraçada para os seus intercâmbios familiares;
- Um perfil com uma fotografia falsa e um pseudónimo para as suas conversas pessoais;
- Outro perfil pseudónimo para conversar com estranhos.



É isso que vamos fazer aqui. Começo por configurar o meu perfil principal, o que está ligado à minha identidade real. Para tal, clico na minha fotografia de perfil no canto inferior direito e, em seguida, no meu nome de utilizador.



![Image](assets/fr/21.webp)



Depois, clico na minha fotografia de perfil para a alterar e adicionar uma nova.



![Image](assets/fr/22.webp)



Para adicionar outros perfis, clique no menu "*Os seus perfis de conversação*".



![Image](assets/fr/23.webp)



Aqui verá todos os seus perfis. Clique em "*Adicionar perfil*" para criar um novo perfil.



![Image](assets/fr/24.webp)



Em seguida, escolha as informações para o seu novo perfil: nome, fotografia, etc. Aqui, utilizo um pseudónimo e uma imagem diferente para ocultar a minha identidade real em certas trocas de mensagens.



![Image](assets/fr/25.webp)



Se mantiver o dedo premido sobre um perfil, pode ocultá-lo. Isto torná-lo-á invisível na aplicação, juntamente com todas as conversas associadas. Também pode optar por "*Mudo*" para deixar de receber notificações.



![Image](assets/fr/26.webp)



Depois de ter criado os seus perfis, pode geri-los de forma independente. Na página inicial, basta selecionar o perfil ativo a apresentar.



![Image](assets/fr/27.webp)



Quando crias um link de convite ou um Address estático, podes agora escolher o perfil a associar ao mesmo. Por exemplo, se eu selecionar o perfil "*Satoshi Nakamoto*" para criar um link generate e o enviar à Alice, ela só verá a minha identidade pseudónima "*Satoshi Nakamoto*", sem nunca conhecer a minha identidade real "*Loïc Morel*". Por outro lado, se eu lhe fornecer um link do meu perfil real, ela não terá forma de se ligar ao meu perfil pseudónimo.



![Image](assets/fr/28.webp)



Parabéns, já está a par do SimpleX messaging, uma excelente alternativa à WathsApp!



Recomendo também este outro tutorial, no qual apresento o Threema, outra alternativa interessante para a sua aplicação de mensagens:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74