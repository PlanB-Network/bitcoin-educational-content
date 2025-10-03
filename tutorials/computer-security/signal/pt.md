---
name: Signal
description: Exprimir-se livremente
---
![cover](assets/cover.webp)



O Signal é uma aplicação de mensagens encriptadas de ponta a ponta, concebida para oferecer uma boa confidencialidade por defeito. Todas as mensagens, chamadas e ficheiros são protegidos pelo protocolo Signal, reconhecido como um dos protocolos de mensagens mais robustos. É reutilizado por muitas outras aplicações, incluindo o WathsApp, o Facebook Messenger, o Skype e o Google Messages para comunicações RCS.



O Signal foi lançado em 2014 por Moxie Marlinspike (pseudónimo) e desenvolvido desde 2018 pela Signal Foundation, uma organização sem fins lucrativos criada com o apoio de Brian Acton (cofundador do WhatsApp).



![Image](assets/fr/01.webp)



Em comparação com o WhatsApp, o Signal distingue-se pela sua transparência: o código da aplicação, tanto do lado do cliente como do lado do servidor, é totalmente open source. Isto permite que qualquer pessoa o possa auditar e, em particular, verificar se a encriptação é aplicada como anunciado.



No entanto, a Signal baseia-se na utilização de um número de telefone, o que constitui o seu principal ponto fraco em termos de anonimato em comparação com outras soluções. Apesar disso, a aplicação é, na minha opinião, uma das mais fiáveis em termos de segurança e confidencialidade, graças à sua arquitetura totalmente aberta e a um protocolo de encriptação amplamente adotado, e portanto testado e auditado, ao contrário de outras aplicações mais marginais.



| Aplicativo           | E2EE 1:1       | E2EE grupos    | Registro anônimo    | Licença cliente open-source | Licença servidor open-source | Servidor descentralizado | Ano de criação    |
| -------------------- | -------------- | -------------- | ------------------- | --------------------------- | ---------------------------- | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                           | ❌                            | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                           | ❌                            | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opcional)  | ❌                   | ❌                           | ❌                            | ❌                        | 2011              |
| Telegram             | 🟡 (opcional)  | ❌              | 🟡                  | ✅                           | ❌                            | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                           | ❌                            | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                           | ✅                            | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                           | ❌                            | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                           | ✅                            | 🟡 (federado)           | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                           | N/A                          | 🟡 (via email)          | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                           | ✅                            | 🟡 (federado)           | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                           | ✅                            | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                           | ✅                            | ✅                        | 2021              |
| Olvid                | ✅              | ✅              | ✅                   | ✅                           | ❌                            | 🟡(sem diretório)       | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                           | N/A                          | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                           | N/A                          | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                           | N/A                          | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                           | N/A                          | ✅                        | 2013              |

*E2EE = Encriptação de ponta a ponta*




## Instalar a aplicação Signal



O Signal está disponível em todas as plataformas. Pode descarregar a aplicação diretamente da loja de aplicações do seu telemóvel:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669);



No Android, também é possível [instalar via APK] (https://github.com/signalapp/Signal-Android/releases).



Neste tutorial, vamos concentrar-nos na versão móvel, mas tenha em atenção que também estão disponíveis [versões para computador](https://signal.org/fr/download/) (MacOS, Linux e Windows). No entanto, terá de configurar primeiro a aplicação móvel, antes de poder sincronizar a sua conta com a versão para computador.



## Criar uma conta no Signal



Quando lançar a aplicação pela primeira vez, clique no botão "*Continuar*".



![Image](assets/fr/02.webp)



Introduza o seu número de telefone e clique em "*Próximo*".



![Image](assets/fr/03.webp)



Ser-lhe-á enviado um código de verificação por SMS. Introduza este código na aplicação Signal.



![Image](assets/fr/04.webp)



Escolha um código PIN para proteger a sua conta Signal. Este código encripta os seus dados e pode ser utilizado para restaurar o acesso à sua conta em caso de perda do dispositivo. Por isso, é importante escolher um código PIN robusto, que seja o mais longo e aleatório possível, e manter um registo fiável do mesmo.



![Image](assets/fr/05.webp)



Confirme este código PIN uma segunda vez.



![Image](assets/fr/06.webp)



Pode agora personalizar o seu perfil de utilizador. Escolha uma fotografia, introduza o seu nome ou uma alcunha. Nesta fase, também pode definir quem o pode encontrar no Signal através do seu número. Selecione "*Todos*" se pretender estar visível ou "*Ninguém*" para não ser detectado através do número de telefone (só pode ser adicionado com o seu "*Nome de utilizador*"). Depois de ter feito as suas selecções, clique em "*Próximo*".



![Image](assets/fr/07.webp)



Está agora ligado ao Signal e pronto para receber mensagens Exchange.



![Image](assets/fr/08.webp)



## Configurar a sua conta Signal



Clique na sua fotografia de perfil no canto superior esquerdo para aceder às definições da aplicação.



![Image](assets/fr/09.webp)



O menu "*Conta*" permite-lhe gerir as definições do seu perfil. Aconselho-o a manter as predefinições. Também pode ativar a opção "*Bloqueio de registo*", que protege a sua conta contra certos tipos de ataques. Este menu também contém as opções necessárias para transferir a sua conta para um novo dispositivo.



![Image](assets/fr/10.webp)



Clicando novamente na sua imagem de perfil nas definições, acederá às opções de personalização do seu perfil. Recomendo que defina um "*Nome de utilizador*": isto permitir-lhe-á entrar em contacto com outras pessoas sem expor o seu número de telefone.



![Image](assets/fr/11.webp)



Ao selecionar "*Código QR ou link*", obterá a informação necessária para partilhar com alguém que o queira adicionar ao Signal.



![Image](assets/fr/12.webp)



O menu "*Privacidade*" é particularmente importante. Aqui encontrará opções para controlar a visibilidade do seu número, a gestão das suas mensagens com os seus contactos, bem como várias autorizações concedidas na aplicação.



![Image](assets/fr/13.webp)



E sinta-se à vontade para explorar os menus "*Appearance*", "*Chats*" e "*Notifications*" para adaptar o Interface e o funcionamento da aplicação às suas necessidades pessoais.



## Ligar a aplicação de ambiente de trabalho



Para ligar a aplicação de ambiente de trabalho, comece por instalar o software no seu computador (consulte a primeira parte deste tutorial). Em seguida, no telemóvel, vá a Definições e abra a secção "*Dispositivos ligados*".



![Image](assets/fr/14.webp)



Clique no botão "*Ligar um novo dispositivo*".



![Image](assets/fr/15.webp)



No seu computador, inicie o software e, em seguida, digitalize o código QR apresentado no ecrã utilizando o seu telemóvel. Se pretender importar as suas conversas, selecione a opção "*Transferir histórico de mensagens*".



![Image](assets/fr/16.webp)



Os seus dispositivos estão agora totalmente sincronizados.



![Image](assets/fr/17.webp)



## Enviar mensagens com o Signal



Para comunicar com alguém no Signal, primeiro tem de o adicionar como contacto. Existem várias opções: pode adicioná-la através do seu número de telefone (se a pessoa tiver ativado a opção de ser encontrada por este meio), ou utilizar a sua ID Signal.



Clique no ícone do lápis no canto inferior direito do Interface.



![Image](assets/fr/18.webp)



No meu caso, quero adicionar a pessoa pelo nome de utilizador. Por isso, clico em "*Encontrar por nome de utilizador*".



![Image](assets/fr/19.webp)



Pode então colar o seu login ou digitalizar o seu código QR.



![Image](assets/fr/20.webp)



Envie-lhe uma mensagem para estabelecer contacto.



![Image](assets/fr/21.webp)



A conversa será então apresentada na página inicial. Se a pessoa aceitar o seu pedido de contacto, verá o seu nome e a sua fotografia de perfil.



![Image](assets/fr/22.webp)



Parabéns, agora está a par da utilização do serviço de mensagens Signal, uma excelente alternativa ao WathsApp! Se achou este tutorial útil, ficaria muito grato se deixasse um polegar Green abaixo. Não hesite em partilhar este tutorial nas suas redes sociais. Muito obrigado!



Também recomendo este outro tutorial, no qual vos apresento o Proton Mail, uma alternativa muito mais amiga da privacidade ao Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2