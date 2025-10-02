---
name: Session
description: Enviar mensagens encriptadas, não metadados
---
![cover](assets/cover.webp)



A Session é uma aplicação de mensagens encriptadas criada em 2020, concebida para oferecer um nível de confidencialidade mais elevado do que as mensagens tradicionais. Foi inicialmente desenvolvida pela *Oxen Privacy Tech Foundation* e depois pela *Session Technology Foundation*.



A Session possui algumas caraterísticas técnicas interessantes: encriptação de ponta a ponta das mensagens, uma rede descentralizada organizada para garantir a disponibilidade e a redundância, e o encaminhamento onion inspirado no Tor. Além disso, ao contrário da WathsApp ou da Signal, que exigem um número de telefone para o registo, a Session não pede qualquer informação pessoal (nem número, nem e-mail, apenas um par de chaves criptográficas).



A sessão permite-lhe enviar mensagens, ficheiros, mensagens de voz, chamadas de áudio, bem como grupos até 100 membros (e comunidades para além disso), minimizando as fugas de metadados.



![Image](assets/fr/01.webp)



A Session destina-se sobretudo aos utilizadores que colocam a confidencialidade no centro das suas prioridades. Este serviço de mensagens representa uma alternativa séria ao WhatsApp, com uma arquitetura concebida para resistir aos modelos de vigilância modernos.



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
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Encriptação de ponta a ponta*



## Instalar a aplicação Session



A sessão está disponível em todas as plataformas. Pode descarregar a aplicação diretamente da loja de aplicações do seu telemóvel:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



No Android, também é possível [instalar via APK] (https://github.com/session-foundation/session-android/releases).



Neste tutorial, vamos concentrar-nos na versão móvel, mas tenha em atenção que [as versões para computador também estão disponíveis](https://getsession.org/download) (MacOS, Linux e Windows). Mais adiante, veremos como sincronizar uma conta em vários dispositivos.



## Criar uma conta na sessão



No primeiro lançamento, clique em "*Criar conta*".



![Image](assets/fr/02.webp)



Escolha um nome de apresentação para o seu perfil. Pode ser um pseudónimo ou o seu nome verdadeiro.



![Image](assets/fr/03.webp)



Terá então de escolher entre dois modos de gestão de notificações:





- Modo rápido (**Firebase Cloud Messaging/Apple Push Notification Service**): permite-lhe receber notificações de mensagens quase em tempo real, graças aos serviços de notificação fornecidos pela Google ou pela Apple (consoante o seu sistema). Para que isto funcione, o seu IP Address e um ID de notificação único são transmitidos à Google ou à Apple, e o ID da conta de sessão é também registado num servidor STF (via Tor). Este modo envolve a exposição (reconhecidamente mínima) de metadados, mas não compromete o conteúdo das mensagens ou os contactos e não permite que a sua atividade real seja rastreada. Este modo é, portanto, mais eficiente em termos de capacidade de resposta, mas depende de uma infraestrutura centralizada e é ligeiramente menos eficaz em termos de confidencialidade.





- Modo lento (**background polling**): a aplicação Session permanece ativa em segundo plano, sondando periodicamente a rede em busca de novas mensagens. Esta abordagem garante uma maior confidencialidade do que a primeira, uma vez que nenhum dado é transmitido a servidores de terceiros; nem os servidores da Google, da Apple ou do STF recebem qualquer informação. Por outro lado, este modo tem dois inconvenientes: as notificações podem ser atrasadas (até vários minutos) e o consumo de energia é geralmente mais elevado devido à atividade da aplicação em segundo plano.



![Image](assets/fr/04.webp)



Está agora ligado à aplicação Session e pode começar a trocar mensagens.



![Image](assets/fr/05.webp)



## Guardar a sua conta de sessão



A primeira coisa a fazer antes de começar a utilizar a Session é guardar a sua conta para a poder restaurar se perder o seu dispositivo. Para o fazer, clique no botão "*Continuar*" junto a "*Guardar a sua palavra-passe de recuperação*".



![Image](assets/fr/06.webp)



A sessão apresentará uma frase Mnemonic. Copie-a cuidadosamente e guarde-a num local seguro. Esta frase fornece acesso total à sua conta Session, pelo que é importante não a divulgar. Necessitará dela para aceder à sua conta noutro dispositivo, especialmente se o seu telemóvel atual se perder ou for substituído.



![Image](assets/fr/07.webp)



Esta frase funciona de forma semelhante às frases Mnemonic utilizadas nos portefólios Bitcoin. Por isso, recomendo que consulte este outro tutorial, no qual explico as melhores práticas para guardar uma frase Mnemonic:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Atenção**: Ao contrário das frases Mnemonic utilizadas nos portefólios Bitcoin, na Sessão, **deve absolutamente guardar cada palavra na sua totalidade**. As primeiras 4 letras não são suficientes!



## Configurar a aplicação Session



Para aceder às definições da aplicação, clique na sua fotografia de perfil no canto superior esquerdo do Interface. É aqui que pode adicionar uma fotografia de perfil.



![Image](assets/fr/08.webp)



No menu "*Privacidade*", pode ativar ou desativar várias funcionalidades (atenção, algumas podem expor o seu IP Address). Também recomendo ativar a opção "*Lock App*", que requer autenticação para aceder à aplicação.



![Image](assets/fr/09.webp)



No menu "*Notificação*", pode escolher entre "*Modo rápido*" e "*Modo lento*" (ver partes anteriores do tutorial). Também pode personalizar as notificações de acordo com as suas preferências.



![Image](assets/fr/10.webp)



Finalmente, aceda ao menu "*Appearance*" para adaptar o Interface ao seu gosto. O menu "*Senha de recuperação*" permite-lhe recuperar a sua frase Mnemonic se desejar fazer uma nova cópia de segurança.



![Image](assets/fr/11.webp)



## Enviar mensagens com a sessão



Para contactar outras pessoas, clique no botão "*+*" na página inicial.



![Image](assets/fr/12.webp)



Estão disponíveis várias opções. Se pretender criar ou aderir a um grupo, selecione "*Criar grupo*" ou "*Juntar à comunidade*".



![Image](assets/fr/13.webp)



Se quiser que alguém o adicione como contacto, pode pedir-lhe que digitalize o seu ID de sessão como um código QR.



![Image](assets/fr/14.webp)



Para enviar o seu início de sessão remotamente, clique em "*Convidar um amigo*". Pode então copiar o seu ID de sessão e enviá-lo através de outro canal de comunicação. Também pode obter estas informações clicando na sua fotografia de perfil a partir da página inicial.



![Image](assets/fr/15.webp)



Se tiver o ID de sessão de outra pessoa e pretender adicioná-lo, clique em "*Nova mensagem*".



![Image](assets/fr/16.webp)



Pode então colar o seu identificador no texto ou digitalizá-lo diretamente se o tiver como código QR.



![Image](assets/fr/17.webp)



Em seguida, envie uma mensagem inicial a essa pessoa.



![Image](assets/fr/18.webp)



Assim que a pessoa aceitar o seu pedido, verá o seu nome de utilizador aparecer e poderá conversar livremente com ela.



![Image](assets/fr/19.webp)



## Software Synchronize Desktop



Para sincronizar a sua conta no seu computador, tem de instalar o software. [Descarregue-o a partir do sítio Web oficial](https://getsession.org/download). Aconselho-o a verificar a sua autenticidade e integridade antes de o instalar.



![Image](assets/fr/20.webp)



No primeiro lançamento, clique em "*Tenho uma conta*".



![Image](assets/fr/21.webp)



Introduza a sua frase Mnemonic, certificando-se de que deixa um espaço entre cada palavra.



![Image](assets/fr/22.webp)



Pode agora aceder às suas conversas a partir do seu computador.



![Image](assets/fr/23.webp)



Parabéns, já sabe como utilizar o serviço de mensagens Session, uma excelente alternativa à WathsApp!



Recomendo também este outro tutorial, no qual apresento o Threema, outra alternativa interessante para a sua aplicação de mensagens:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74