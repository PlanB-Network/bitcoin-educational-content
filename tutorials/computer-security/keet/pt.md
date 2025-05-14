---
name: Keet
description: Conversa entre pares
---
![cover](assets/cover.webp)



Keet é uma aplicação de mensagens instantâneas concebida para funcionar sem quaisquer servidores. Lançada em 2022 pela Holepunch (uma empresa financiada pela Tether e Bitfinex), a aplicação baseia-se inteiramente numa rede peer-to-peer e apresenta uma abordagem radicalmente descentralizada: mensagens, chamadas e ficheiros são trocados diretamente entre utilizadores, sem intermediários.



O Keet encripta todas as comunicações de ponta a ponta e não solicita dados pessoais. O registo é anónimo, não sendo necessário qualquer número de telefone ou e-mail. Para além da troca de mensagens de texto, o Keet oferece chamadas de vídeo de alta qualidade, bem como partilha ilimitada de ficheiros. A aplicação pode, portanto, ser utilizada de forma híbrida, tanto para uso pessoal como profissional.



![Image](assets/fr/01.webp)



Atualmente (abril de 2025), o Keet não é totalmente open-source. Parte do código-fonte está disponível no [repositório GitHub da Holepunch](https://github.com/holepunchto), nomeadamente os componentes criptográficos e de rede, mas o cliente Interface ainda não. A Holepunch anunciou, no entanto, a sua intenção de, eventualmente, tornar toda a aplicação open-source. Dependendo de quando você descobrir este tutorial, isso pode já ter sido feito.




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
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| **Keet**             | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Encriptação de ponta a ponta*



## Instalar o Keet



O Keet está disponível em todas as plataformas. Pode descarregar a aplicação diretamente da loja de aplicações do seu telemóvel:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



No Android, também é possível [instalar via APK] (https://github.com/holepunchto/keet-mobile-releases/releases).



Neste tutorial, vamos concentrar-nos na versão móvel, mas tenha em atenção que [as versões para computador também estão disponíveis](https://keet.io/) (MacOS, Linux e Windows). Também é possível sincronizar a sua conta em vários dispositivos.



## Criar uma conta no Keet



No primeiro arranque, pode ignorar os ecrãs de apresentação.



![Image](assets/fr/02.webp)



Clique no botão "*Sou um novo utilizador*".



![Image](assets/fr/03.webp)



Aceite as condições de utilização e, em seguida, clique em "*Configuração rápida*".



![Image](assets/fr/04.webp)



Escolha um nome ou alcunha e, em seguida, clique em "*Finalizar configuração*".



![Image](assets/fr/05.webp)



O seu perfil está agora criado. Clique novamente em "*Finalizar configuração*" para finalizar.



![Image](assets/fr/06.webp)



Pode personalizar o seu perfil em qualquer altura a partir do separador "*Perfil*".



## Guardar a sua conta Keet



A primeira coisa a fazer com a sua nova conta Keet é guardar a sua frase de recuperação. Esta é uma sequência de 24 palavras que lhe permitirá restaurar o acesso à sua conta em caso de perda ou mudança de dispositivo. Esta frase dá acesso total à sua conta a qualquer pessoa que a conheça, pelo que é importante fazer uma cópia de segurança fiável e nunca a divulgar.



Para o fazer, clique no separador "*Profile*" (Perfil) no canto inferior direito do Interface.



![Image](assets/fr/07.webp)



Em seguida, aceda ao menu "*Configurações*".



![Image](assets/fr/08.webp)



Selecionar "*Privacidade e segurança*".



![Image](assets/fr/09.webp)



Em seguida, clique em "*Frase de recuperação*".



![Image](assets/fr/10.webp)



Prima o botão "*Ver frase*" para visualizar a sua frase de recuperação. Copie-a cuidadosamente e guarde-a num local seguro.



![Image](assets/fr/11.webp)



## Enviar mensagens com o Keet



Para comunicar no Keet, é necessário criar "*Rooms*". Para o fazer, clique no ícone do lápis no canto superior direito do Interface.



![Image](assets/fr/12.webp)



Selecione "*Nova conversa de grupo*".



![Image](assets/fr/13.webp)



Escolha um nome e uma descrição para a sua "*Room*" e, em seguida, clique em "*Create group chat*".



![Image](assets/fr/14.webp)



A sua "*Room*" está agora criada. Clique no ícone "*+*" no canto superior direito para convidar participantes.



![Image](assets/fr/15.webp)



Defina os direitos que concede aos novos membros através da ligação de convite, bem como a duração da validade da ligação. Em seguida, clique em "*Convite generate*".



![Image](assets/fr/16.webp)



O Keet irá enviar ao generate um link para se juntar à sua "*Room*". Pode copiá-lo e partilhá-lo, ou fazer com que o seu código QR seja lido pelas pessoas que deseja convidar.



![Image](assets/fr/17.webp)



Pode agora começar a trocar mensagens e ficheiros multimédia. Para iniciar uma chamada, clique no ícone do telefone no canto superior direito.



![Image](assets/fr/18.webp)



A partir deste grupo, também pode enviar mensagens privadas a um membro específico. Clique na imagem de perfil do grupo e, em seguida, selecione o membro pretendido na secção "*Membros*".



![Image](assets/fr/19.webp)



Clique no botão "*Enviar pedido de DM*" e introduza a sua mensagem.



![Image](assets/fr/20.webp)



Quando o pedido de DM for aceite, encontrará este contacto na página inicial, onde poderá falar com ele em privado.



![Image](assets/fr/21.webp)



## Sincronizar a sua conta em vários dispositivos



Agora que já sabe como utilizar o Keet e tem uma conta, também pode sincronizá-la noutro dispositivo, como um computador. Para tal, abra a aplicação no seu telemóvel, clique em "*Perfil*" e aceda a "*Configurações*".



![Image](assets/fr/22.webp)



Em seguida, aceda ao menu "*Os meus dispositivos*".



![Image](assets/fr/23.webp)



Clique em "*Adicionar dispositivo*". O Keet apresentará um link para sincronizar um novo dispositivo. Copie esta ligação.



![Image](assets/fr/24.webp)



No seu segundo dispositivo, instale o Keet. No ecrã inicial, selecione a opção "*Sou um utilizador atual*".



![Image](assets/fr/25.webp)



Em seguida, clique em "*Ligar dispositivo*".



![Image](assets/fr/26.webp)



Cole a ligação fornecida pelo seu primeiro dispositivo e, em seguida, clique em "*Iniciar sincronização*".



![Image](assets/fr/27.webp)



No seu primeiro dispositivo, clique em "*Confirmar dispositivos de ligação*" para autorizar a ligação.



![Image](assets/fr/28.webp)



No segundo dispositivo, complete o processo clicando em "*Link devices*".



![Image](assets/fr/29.webp)



Agora pode aceder a todos os seus "*Room*" e conversas a partir deste novo dispositivo.



![Image](assets/fr/30.webp)



Parabéns, agora está a par da utilização do serviço de mensagens Keet, uma excelente alternativa ao WathsApp! Se achou este tutorial útil, ficaria muito grato se deixasse um polegar Green abaixo. Não hesite em partilhar este tutorial nas suas redes sociais. Muito obrigado!



Também recomendo este outro tutorial, no qual vos apresento o Proton Mail, uma alternativa muito mais amiga da privacidade ao Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2