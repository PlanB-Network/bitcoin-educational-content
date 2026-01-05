---
name: White Noise
description: Uma aplicação de mensagens privada e descentralizada baseada nos protocolos Nostr e MLS
---

![cover](assets/cover.webp)




## Introdução



"No meio da dificuldade está a oportunidade". Esta citação de Albert Einstein lembra-nos que os problemas não são definitivos, mas que contêm em si as sementes de soluções novas e inovadoras.



As motivações subjacentes ao lançamento da solução que apresentamos neste tutorial ilustram-no perfeitamente. Trata-se do **White Noise**, nascido da necessidade.



Nas palavras do seu fundador, Max Hillebrand, relatadas pela *Bitcoin Magazine*: "Lançámos este projeto por falta de alternativas" Ele explica que "as aplicações de encriptação existentes são ineficientes em grande escala: adicionar 100 pessoas a uma conversa de grupo torna a encriptação consideravelmente mais lenta. As plataformas descentralizadas, por sua vez, não oferecem mensagens privadas. Finalmente, a rede de retransmissão aberta do Nostr permite que todos divulguem ideias, mas a proteção das mensagens diretas continua a ser dramaticamente inadequada. Percebemos que, para proteger a liberdade, tínhamos de fundir estes sistemas"



## O que é o White Noise?



O White Noise é uma aplicação de mensagens de código aberto desenvolvida por uma equipa sem fins lucrativos. A aplicação promove a segurança, a privacidade e a descentralização. Ao contrário das aplicações convencionais, não requer nem um número de telefone nem um endereço de correio eletrónico.


O White Noise distingue-se pela integração de dois protocolos fundamentais - Nostr e MLS - que constituem a sua base técnica.



O Nostr (Notes and Other Stuff Transmitted by Relays) é um protocolo descentralizado e de código aberto concebido para resistir à censura.  O protocolo usa relés, pares de chaves e clientes.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

Com o Ruído branco, pode até escolher as suas próprias definições de retransmissão para maximizar a privacidade.



O MLS (Messaging Layer Security), por outro lado, é um protocolo de segurança que permite a cifragem de ponta a ponta das mensagens. Por outras palavras, as mensagens são acessíveis apenas nos pontos finais, ou seja, o remetente e o destinatário da mensagem. Isto significa que os retransmissores envolvidos no encaminhamento de mensagens não podem aceder ao seu conteúdo.



Eis uma comparação rápida entre o White Noise e algumas das aplicações de mensagens mais conhecidas.



| Points de comparaisons      | White Noise | Telegram   | Whatsapp (Meta) | Bitchat | iMessage | Messenger (Meta) | Signal |
| --------------------------- | ----------- | ---------- | --------------- | ------- | -------- | ---------------- | ------ |
| Chiffrement E2EE / 1:1      | ✅ Oui       | Facultatif | ✅ Oui           | ✅ Oui   | ✅ Oui    | ✅ Oui            | ✅ Oui  |
| Chiffrement de groupe E2EE  | ✅ Oui       | ❌ Non      | ✅ Oui           | ✅ Oui   | ✅ Oui    | Facultatif       | ✅ Oui  |
| Anonymisation de l'identité | ✅ Oui       | Facultatif | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Serveur open source         | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Client open source          | ✅ Oui       | ✅ Oui      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ✅ Oui  |
| Serveur décentralisé        | ✅ Oui       | ❌ Non      | ❌ Non           | ✅ Oui   | ❌ Non    | ❌ Non            | ❌ Non  |
| Année de création           | 2025        | 2013       | 2009            | 2025    | 2011     | 2011             | 2014   |


## Começar a utilizar o White Noise



### Instalação do White Noise



Aceda ao [sítio Web do White Noise] (https://www.whitenoise.chat/) e, em seguida, clique em **Download**.



![screen](assets/fr/03.webp)



Atualmente, o White Noise só está disponível em dispositivos móveis.


Na nova interface que aparece, prima :





- o botão **Zapstore** ou **Android APK** se quiser descarregá-lo no Android ;
- no botão **iOS TestFlight** se estiver a utilizar um iPhone.



![screen](assets/fr/04.webp)



Para efeitos deste tutorial, vamos efetuar uma transferência para Android.


Se optar pela transferência através da **Zapstore**, será redireccionado para a mesma. Uma vez na Zapstore, escreva **White Noise** na barra de pesquisa. Em seguida, proceda à transferência clicando em **Instalar**.



![screen](assets/fr/05.webp)



![screen](assets/fr/06.webp)



Se optar por descarregar o ficheiro APK, será redireccionado para o repositório GitHub do White Noise para escolher a versão adequada ao seu smartphone.



Os ficheiros APK disponíveis são :





- whitenoise-0.2.1-arm64-v8a.apk** (57,7 MB), adequado para telemóveis recentes com processadores de 64 bits;
- whitenoise-0.2.1-armeabi-v7a.apk** (47,5 MB) adequado para telemóveis mais antigos com processadores de 32 bits.



Também tem ficheiros **.sha256**, que são apenas somas de verificação para verificar a integridade da transferência.



![screen](assets/fr/07.webp)



Quando a transferência estiver concluída, instale e abra a aplicação.



![screen](assets/fr/08.webp)



### Configuração inicial da conta de utilizador



Para a sua primeira ligação ao White Noise, prima o botão **Registar**.



![screen](assets/fr/09.webp)



Em seguida, configure o seu perfil escolhendo uma fotografia de perfil, um nome e acrescentando uma breve descrição de si próprio. Não é necessário preencher a sua identidade real (nome e fotografia).


Note que o White Noise escolhe automaticamente um nome (pseudónimo) para si, que pode manter ou alterar. Por fim, prima o botão **End**.



![screen](assets/fr/10.webp)



Será redireccionado para o **ecrã inicial** do White Noise, onde as suas conversas serão listadas. A sua conta está agora configurada e pronta a ser utilizada. Pode partilhar o seu perfil ou procurar amigos para iniciar uma conversa.



![screen](assets/fr/11.webp)




### Descobrir interfaces White Noise



Na interface principal, na parte superior do ecrã, verá :



No canto superior esquerdo, o ícone do perfil é uma miniatura da sua fotografia de perfil ou a primeira letra do seu nome de perfil. Clique nele para aceder às definições da sua conta.



![screen](assets/fr/12.webp)



![screen](assets/fr/13.webp)



No canto superior direito, encontra o ícone para iniciar uma nova conversa.



![screen](assets/fr/14.webp)



![screen](assets/fr/15.webp)




## Definições da conta de utilizador



Prima o ícone do perfil no canto superior esquerdo para aceder às definições.



![screen](assets/fr/16.webp)



Na parte superior da interface **Configurações**, encontrará a sua fotografia e o nome do seu perfil, seguidos da sua chave pública, que pode partilhar utilizando o código QR ao lado.



![screen](assets/fr/17.webp)



Logo abaixo, encontrará o botão **Alterar conta**, que lhe permite ligar-se a outro perfil dentro da aplicação.



![screen](assets/fr/18.webp)



Em seguida, tem uma primeira secção com quatro (4) submenus, tais como :





- Modificar o perfil**



Neste submenu, pode modificar o nome do perfil, o endereço Nostr (NIP-05)... Não se esqueça de clicar em **Guardar** para guardar as suas alterações.



![screen](assets/fr/19.webp)





- Chaves de perfil**



Aqui tem acesso às suas chaves públicas e privadas (secretas). Como o White Noise recorda, a sua chave privada não deve ser divulgada em circunstância alguma.



![screen](assets/fr/20.webp)





- Relé de rede



Neste submenu, é possível adicionar ou remover **relés gerais** (relés definidos para serem utilizados em todas as aplicações do Nostr), **relés de caixa** e **relés de pacote de chaves**.



Para o fazer, toque no ícone **lixo** à frente de uma retransmissão para a apagar ou toque no ícone **+** (mais) para adicionar uma nova retransmissão.



![screen](assets/fr/21.webp)





- Desligar**



Clique neste submenu para desligar a sua conta da aplicação. Mas certifique-se de que guardou as suas chaves privadas offline, caso contrário não poderá iniciar sessão novamente mais tarde.



![screen](assets/fr/22.webp)




Uma segunda secção oferece sub-menus:





- Definições da aplicação



Aqui pode definir o aspeto (tema e língua de apresentação) da aplicação e até apagar dados se considerar que foram comprometidos ou se se sentir em risco.



![screen](assets/fr/23.webp)





- Doar para o White Noise



Pode apoiar a equipa do White Noise (uma organização sem fins lucrativos) com donativos através do seu endereço Lightning ou do seu endereço de pagamento silencioso Bitcoin.



![screen](assets/fr/24.webp)



Por fim, na parte inferior, encontram-se as **configurações do programador**.



![screen](assets/fr/25.webp)




## Iniciar uma conversa



Vejamos agora como iniciar uma conversa. No momento em que escrevo, o White Noise oferece três opções de comunicação. Por sua vez, vamos explorar as **Conversas privadas** (**Chat 1:1**), ou seja, entre si e uma outra pessoa, as **Conversas de grupo** e o **Envio de ficheiros multimédia**.




### Gato 1:1



Na interface principal, para adicionar um novo correspondente, clique no ícone para iniciar uma nova conversa.


Em seguida, digitalize o código QR da chave pública (1) ou cole a chave pública (2) do seu novo correspondente na barra de pesquisa para o encontrar.



![screen](assets/fr/26.webp)



Em seguida, toque no botão **Iniciar conversa** para iniciar uma conversa com o seu correspondente. Também pode **Seguir** o seu correspondente ou convidá-lo para uma conversa de grupo premindo o botão **Adicionar ao grupo**.



![screen](assets/fr/27.webp)



A sua primeira mensagem para um novo correspondente é semelhante a um pedido de convite. Este pedido tem de ser aceite pelo seu correspondente antes de poder comunicar com ele. Se ele recusar, bem, não há conversa possível.



![screen](assets/fr/28.webp)



Além disso, enquanto não aceitarem o seu convite, não poderão ler o conteúdo da sua mensagem inicial.



Depois de aceitar o seu convite, ele pode responder-lhe e os dois podem comunicar sem problemas e de forma segura.



![screen](assets/fr/29.webp)



Além disso, numa discussão, tem funcionalidades adicionais.



Pode premir longamente uma mensagem específica para visualizar opções como :




- reagir à mensagem com um emoji (1) ;
- fazer uma **citação direta** para responder à mensagem premindo **Reply** (2) ;
- copiar a mensagem premindo **Copiar** (3).



![screen](assets/fr/30.webp)





- só pode apagar uma mensagem com o botão **Apagar** se for da sua autoria.



![screen](assets/fr/31.webp)



Pode pesquisar dentro de uma conversa.



Clique no avatar do correspondente na parte superior do ecrã para aceder às "informações da conversa" e toque no botão **Pesquisar na conversa**.



![screen](assets/fr/32.webp)



![screen](assets/fr/33.webp)



Na barra de pesquisa que aparece, escreva a palavra que pretende procurar e inicie a pesquisa. Verá então as suas palavras de pesquisa destacadas em **negrito**.



![screen](assets/fr/34.webp)




### Conversas em grupo



Os grupos de conversação podem ser criados no White Noise.



Para o fazer, toque no ícone na interface de início de uma nova conversa e, em seguida, clique em **Nova conversa de grupo**. Em seguida, na barra de pesquisa, introduza a chave pública do primeiro membro que pretende adicionar ao seu grupo.



![screen](assets/fr/35.webp)



![screen](assets/fr/36.webp)



Eventualmente, se esta opção não funcionar, a partir da interface **Iniciar uma nova conversa**, introduza a chave pública do primeiro membro que pretende adicionar ao grupo na barra de pesquisa. Também pode digitalizar o código QR associado à sua chave pública.



Desta vez, em vez de tocar no botão **Iniciar conversa**, clique no botão **Adicionar ao grupo**.



![screen](assets/fr/37.webp)



No menu pop-up que aparece, toque em **Nova conversa de grupo**.



![screen](assets/fr/38.webp)



Em seguida, prima **Continuar** (não é necessário introduzir novamente a sua chave pública).



![screen](assets/fr/39.webp)



Como criador do grupo, é automaticamente o seu administrador. Preencha os detalhes do grupo, tais como **nome e descrição do grupo** e, em seguida, clique no botão **Criar grupo**.



![screen](assets/fr/40.webp)



O utilizador que adicionar como primeiro membro, e quaisquer outros que adicione posteriormente, recebem uma notificação a convidá-los a juntarem-se ao grupo. Têm de aceitar clicando em **Aceitar** para se juntarem ao grupo.



![screen](assets/fr/41.webp)



Também é possível adicionar um novo membro com quem já está a conversar a um grupo existente. Para o fazer, clique no avatar do correspondente na parte superior do ecrã para aceder às "informações da conversa" e toque no botão **Adicionar ao grupo**.



![screen](assets/fr/42.webp)



Na nova interface que aparece, **marque** o grupo ao qual pretende adicioná-lo e toque em **Adicionar ao grupo**. Só falta esperar que ele aceite juntar-se ao grupo.



![screen](assets/fr/43.webp)



Tenha em atenção que apenas um administrador de grupo pode modificar as informações do grupo e adicionar ou expulsar membros. Além disso, a rotação de chaves impede que os membros banidos desencriptem mensagens futuras.



Para remover um membro, na interface principal do grupo, toque no ícone do grupo na parte superior para aceder à interface de informações do grupo.



![screen](assets/fr/44.webp)



![screen](assets/fr/45.webp)



Em seguida, clique no nome do membro e em **Remover do grupo**. A partir desta interface, pode também enviar-lhe uma mensagem, segui-lo ou adicioná-lo a outro grupo.



![screen](assets/fr/46.webp)



### Envio de ficheiros multimédia



De momento, só é possível partilhar fotografias entre utilizadores no White Noise. Quer se trate de uma conversa privada ou de um chat de grupo, para o fazer, é necessário :





- prima o símbolo **mais (+)** no lado esquerdo do campo de introdução de mensagens de texto.



![screen](assets/fr/47.webp)





- e, em seguida, clique na caixa **Fotos** na parte inferior para aceder à sua galeria.



![screen](assets/fr/48.webp)





- selecionar a(s) fotografia(s) a enviar.



![screen](assets/fr/49.webp)



![screen](assets/fr/50.webp)



![screen](assets/fr/51.webp)





## Pontos-chave a reter



O White Noise oferece um bom nível de confidencialidade e uma segurança superior. Por outro lado, trata-se de uma aplicação muito recente, pouco difundida e ainda em fase de arranque. Por conseguinte, é ainda muito cedo para tirar conclusões concretas. É possível que se verifiquem alguns problemas de funcionamento durante a utilização.



Atualmente, carece de certas funcionalidades (ausência de chamadas áudio ou vídeo, ausência de envio de ficheiros multimédia áudio ou vídeo) em comparação com as aplicações de mensagens populares.



No entanto, o White Noise continua a ser uma opção interessante para conversas em que a confidencialidade é primordial (por exemplo, com a família, amigos próximos ou activistas de uma causa comum), mesmo que exija um pouco de esforço para instalar (através de lojas de aplicações alternativas ou ficheiros APK) e aprender (dominando um pouco o conceito de pares de chaves, clientes e relés com o protocolo Nostr).



Agora já sabe como utilizar o White Noise para comunicar em segurança com os seus amigos e familiares. Por favor, dê-nos um polegar para cima se achar este tutorial útil.



Recomendamos o nosso tutorial sobre o Tox Chat, uma aplicação que lhe permite conversar sem intermediários através do protocolo descentralizado Tox.



https://planb.academy/tutorials/computer-security/communication/tox-027bc897-8c98-4265-b85b-e78b7ab607f3