---
name: Threema
description: Mensagens instantâneas seguras e anónimas
---
![cover](assets/cover.webp)



Fundado em 2012 na Suíça, o Threema é uma aplicação de mensagens instantâneas concebida para garantir a privacidade e a segurança. Ao contrário do WhatsApp, Telegram ou Signal, o Threema não requer um número de telefone ou e-mail Address para criar uma conta. Cada utilizador tem um identificador único, o que permite um registo completamente anónimo.



Do ponto de vista técnico, as comunicações através do Threema são encriptadas de ponta a ponta. O código da aplicação móvel é de fonte aberta desde 2020, mas a infraestrutura do servidor continua a ser proprietária e centralizada. Os servidores estão alojados exclusivamente na Suíça (um país conhecido pelo seu quadro jurídico para a proteção de dados).



![Image](assets/fr/01.webp)



O Threema tem clientes básicos para Android e iOS. Existe também uma aplicação web, bem como software disponível para Windows, Linux e macOS. No entanto, para os utilizar, é necessário registar-se primeiro num dispositivo móvel.



A aplicação Threema não é gratuita. Funciona com base num modelo de compra única: 5,99 euros para utilizar a aplicação para sempre (ou 4,99 euros se a comprar diretamente). Para utilizar realmente o Threema de forma anónima, o pagamento também tem de ser anónimo. É por isso que pode comprar uma chave de ativação em bitcoins ou em dinheiro na "*Threema Shop*" para ativar a versão Android. No iOS, por outro lado, a compra deve ser feita através da App Store, devido às restrições da Apple sobre a monetização de aplicações.



Existe também uma versão dedicada a empresas chamada "*Threema Work*". Neste tutorial, vamos concentrar-nos na versão doméstica.



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



## Instalar a aplicação Threema



O Threema está disponível em todas as plataformas. Pode descarregar a aplicação diretamente da loja de aplicações do seu telemóvel:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



No Android, também é possível [instalar via APK] (https://shop.threema.ch/en/download).



Existem também [versões para computador](https://threema.ch/download) (MacOS, Linux e Windows). Este tutorial mostra-lhe como sincronizá-las.



## Comprar licença Threema



Depois de instalar a aplicação, se a tiver feito diretamente através de uma loja de aplicações, já pagou a licença e deverá ter acesso imediato à mesma. Se foi através do F-Droid ou do APK, tem agora de comprar uma licença no sítio Web oficial.



[Ir para a "*Threema Shop*" (https://shop.threema.ch/) e clicar no botão "*Buy Threema for Android*".



![Image](assets/fr/02.webp)



Selecione o número de licenças que pretende adquirir (apenas uma, se for só para si), escolha a moeda e selecione o método de entrega da licença. Pode optar por receber a licença por correio eletrónico ou diretamente no sítio, caso pretenda manter o anonimato. Em seguida, clique em "*Proceder ao pagamento*".



![Image](assets/fr/03.webp)



Escolha o seu método de pagamento. No meu caso, vou pagar em bitcoins, o que também recomendo que faça, pois permite-lhe manter o anonimato (desde que utilize o Bitcoin de forma adequada) e é muito mais conveniente do que um pagamento em dinheiro à distância. De seguida, clique em "*Next*".



![Image](assets/fr/04.webp)



Se não precisar de um Invoice, clique novamente em "*Next*" sem introduzir quaisquer informações pessoais.



Em seguida, confirme a sua compra clicando em "*Confirmar pagamento*".



![Image](assets/fr/05.webp)



De seguida, terá de enviar o montante indicado para o Bitcoin Address fornecido (infelizmente, o Lightning ainda não é suportado). Quando a transação tiver sido confirmada no Blockchain, clique em "*Fechar*" junto ao Invoice.



Terá então acesso à sua chave de licença. Atenção: se não tiver introduzido um e-mail Address, esta chave só será apresentada aqui. Não se esqueça de guardar o URL da página para poder aceder-lhe mais tarde, se necessário.



![Image](assets/fr/06.webp)



## Criar uma conta no Threema



Agora que tem a sua chave de licença, pode finalmente lançar a aplicação. No primeiro lançamento, se não tiver adquirido o Threema através de uma loja de aplicações, ser-lhe-á pedido que introduza a sua chave de licença, adquirida no sítio.



![Image](assets/fr/07.webp)



Em seguida, clique no botão "*Configurar agora*".



![Image](assets/fr/08.webp)



Move o teu dedo pelo ecrã para generate uma fonte de entropia, necessária para criar o teu "*Threema ID*".



![Image](assets/fr/09.webp)



O seu "*Threema ID*" será então apresentado. Permite-lhe contactar outros utilizadores. Clique em "*Próximo*".



![Image](assets/fr/10.webp)



Escolha uma palavra-passe. Esta permitir-lhe-á restabelecer o acesso à sua conta em caso de necessidade. A palavra-passe deve ser tão longa e aleatória quanto possível e deve ser guardada numa cópia segura, por exemplo, num gestor de palavras-passe.



![Image](assets/fr/11.webp)



Em seguida, escolha um nome de utilizador, que pode ser o seu nome verdadeiro ou um pseudónimo.



![Image](assets/fr/12.webp)



Pode então associar a sua ID Threema ao seu número de telefone. Isto facilita a pesquisa nos seus contactos, mas se utiliza o Threema, é também para preservar o seu anonimato: por isso, é melhor não o associar. Clique em "*Próximo*".



![Image](assets/fr/13.webp)



Uma vez concluída esta etapa, clique em "*Finalizar*".



![Image](assets/fr/14.webp)



Está agora ligado ao Threema e pode começar a comunicar.



![Image](assets/fr/15.webp)



## Configurar o Threema



Em primeiro lugar, aceda às definições clicando nos três pequenos pontos no canto superior direito e, em seguida, selecione "*Definições*".



![Image](assets/fr/16.webp)



No separador "*Privacidade*", encontrará várias opções para ajustar às suas necessidades:




- Sincronizar os contactos do seu telefone ;
- Aceitar mensagens de pessoas desconhecidas;
- Código de escrita durante a introdução de dados ;
- Aviso de receção de mensagens...



![Image](assets/fr/17.webp)



No separador "*Segurança*", recomendo a ativação da opção "*Mecanismo de bloqueio*" para proteger o acesso à aplicação. Também é aconselhável ativar a opção passphrase para proteger as suas cópias de segurança locais.



![Image](assets/fr/18.webp)



Pode explorar as outras secções das definições para personalizar a aplicação de acordo com as suas preferências.



![Image](assets/fr/19.webp)



## Fazer uma cópia de segurança da sua conta Threema



Antes de começar a trocar mensagens, é importante planear uma forma de recuperar a sua conta, especialmente se o seu telemóvel for trocado ou perdido. Para o fazer, clique nos três pontos no canto superior direito do Interface e aceda ao menu "*Backups*".



![Image](assets/fr/20.webp)



Aqui encontra duas opções para fazer cópias de segurança dos seus dados:




- "*Threema Safe*";
- "*Cópia de segurança dos dados*".



"O Threema Safe* guarda todas as informações da sua conta, exceto as suas conversas, nos servidores do Threema. Estes dados são encriptados com a palavra-passe que escolheu quando criou a sua conta, garantindo que o Threema não tem acesso a eles. Os backups são feitos automaticamente e regularmente.



Com o "*Threema Safe*", para recuperar a sua conta num novo dispositivo, basta introduzir o seu "*Threema ID*" e a sua palavra-passe. Se uma destas duas informações estiver em falta, será impossível restaurar a sua conta.



Esta opção apenas lhe permite recuperar a sua ID, perfil, contactos, grupos e determinadas definições, mas **não o seu histórico de conversações**.



Para ativar o "*Threema Safe*", basta marcar a opção no menu "*Backups*".



![Image](assets/fr/21.webp)



Se também quiser fazer uma cópia de segurança e restaurar o seu histórico de conversações, terá de utilizar a opção "*Cópia de segurança de dados*". Esta opção gera uma cópia de segurança completa da sua conta, armazenada localmente no seu telemóvel. Terá de transferir esta cópia de segurança para o seu novo dispositivo e utilizar a sua palavra-passe (e possivelmente o seu passphrase) para restaurar toda a sua conta.



Uma vez que esta cópia de segurança é apenas local, tem de ser copiada regularmente para um suporte externo. Caso contrário, se o seu dispositivo se perder, a recuperação será impossível. Por conseguinte, este método é mais adequado para uma transferência planeada de um dispositivo para outro do que para situações de emergência.



Nota: a "*Cópia de segurança de dados*" só funciona se estiver a utilizar o mesmo sistema operativo. Não poderá utilizá-la, por exemplo, para migrar de um Samsung para um iPhone.



## Personalizar o seu perfil Threema



No canto superior esquerdo do Interface, clique na sua imagem de perfil e, em seguida, selecione "*O meu perfil*".



![Image](assets/fr/22.webp)



Aqui pode personalizar o seu perfil: adicionar uma fotografia, escolher quem o pode ver ou ver o seu login Threema.



![Image](assets/fr/23.webp)



## Sincronizar o software do PC



Se quiser aceder às suas conversas no seu PC, pode sincronizar a sua conta Threema com o software dedicado. Descarregue o software para o seu sistema operativo [a partir do sítio Web oficial] (https://threema.ch/en/download).



![Image](assets/fr/24.webp)



No seu telemóvel, clique nos três pontos no canto superior direito e, em seguida, abra o menu "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Clique em "*Adicionar dispositivo*" e, em seguida, utilize o seu telemóvel para digitalizar o código QR apresentado pelo software no seu computador.



![Image](assets/fr/26.webp)



Para confirmar a sincronização, clique no grupo de emojis apresentado no software.



![Image](assets/fr/27.webp)



No seu computador, inicie sessão com a sua palavra-passe.



![Image](assets/fr/28.webp)



Para além da aplicação móvel, pode agora aceder à sua conta Threema diretamente a partir do seu computador.



![Image](assets/fr/29.webp)



## Enviar mensagens com o Threema



Agora que tudo está configurado corretamente, pode começar a comunicar. Clique no botão "*Iniciar conversação*".



![Image](assets/fr/30.webp)



Selecione "*Novo contacto*".



![Image](assets/fr/31.webp)



Introduza ou digitalize o "*Threema ID*" do seu correspondente.



![Image](assets/fr/32.webp)



Clique no ícone de mensagem.



![Image](assets/fr/33.webp)



Envie uma primeira mensagem ao seu correspondente.



![Image](assets/fr/34.webp)



Quando o seu correspondente responder, a ligação será estabelecida e poderá ver o seu nome e a sua fotografia de perfil. Pode então enviar mensagens Exchange, ficheiros multimédia e até fazer chamadas.



![Image](assets/fr/35.webp)



Parabéns, agora você está pronto para usar o serviço de mensagens Threema, uma ótima alternativa ao WathsApp! Se achou este tutorial útil, ficaria muito grato se deixasse um polegar Green abaixo. Não hesite em partilhar este tutorial nas suas redes sociais. Muito obrigado!



Também recomendo este outro tutorial, no qual vos apresento o Proton Mail, uma alternativa muito mais amiga da privacidade ao Gmail :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2