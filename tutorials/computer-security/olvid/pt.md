---
name: Olvid
description: Mensagens privadas para todos
---
![cover](assets/cover.webp)



O Olvid é uma aplicação francesa de mensagens instantâneas lançada em 2019, concebida para oferecer um elevado nível de segurança, sem comprometer a privacidade. Ao contrário do WhatsApp ou do Signal, o Olvid não pede dados pessoais aquando do registo: nem número de telefone, nem e-mail, nada. A identificação entre utilizadores baseia-se num Exchange de chaves, sem servidor de diretório nem livro Address partilhado.



Todas as mensagens são encriptadas de ponta a ponta utilizando um protocolo criptográfico original, concebido para proteger também os metadados: ninguém sabe com quem está a falar, ou quando. O código do cliente é de código aberto, mas o servidor central utilizado para encaminhar as mensagens encriptadas continua a ser proprietário e está alojado na AWS.

O modelo de segurança do Olvid baseia-se num princípio essencial: a ausência total de terceiros de confiança no estabelecimento das identidades digitais. Ao contrário da maioria das aplicações de mensagens cifradas que dependem de um diretório centralizado para gerir as identidades dos utilizadores, o Olvid não depende de nenhuma infraestrutura centralizada para garantir a integridade das comunicações. Esta arquitetura elimina assim os riscos associados a uma eventual violação do diretório.

O Olvid utiliza, no entanto, um servidor central para a distribuição das mensagens, mas este tem um papel estritamente logístico: assegurar a transmissão assíncrona das mensagens cifradas. Este servidor não intervém em nenhuma etapa do processo de cifragem, não conhece a identidade real dos utilizadores, nem o conteúdo ou os metadados das mensagens (com exceção da chave pública do destinatário, necessária para o encaminhamento). Pode, por isso, ser considerado hostil por defeito sem comprometer a segurança global do sistema. Mesmo que fosse comprometido, não permitiria o acesso ao conteúdo das comunicações. O Olvid assume assim uma centralização da distribuição (por motivos de eficiência e qualidade de serviço), garantindo ao mesmo tempo uma segurança independente dessa infraestrutura.


O Olvid oferece uma versão gratuita e uma versão de subscrição a 4,99 euros por mês. A versão gratuita oferece todas as funcionalidades, com exceção da realização de chamadas de áudio e vídeo (embora seja possível recebê-las), e não permite a sincronização de contas em vários dispositivos. Assim, se pretende utilizar exclusivamente o seu smartphone e não precisa de fazer chamadas, o Olvid é uma excelente solução.



O Olvid é certificado pela ANSSI (autoridade francesa de cibersegurança). Esta aplicação é uma excelente alternativa aos serviços de mensagens tradicionais (WhatsApp, Facebook Messenger, WeChat...) para quem procura privacidade sem perder a simplicidade de utilização.


| Aplicativo           | E2EE 1:1      | E2EE grupos   | Registro anônimo | Licença cliente open-source | Licença servidor open-source | Servidor descentralizado | Ano de criação |
| -------------------- | ------------- | ------------- | ---------------- | --------------------------- | ---------------------------- | ------------------------ | -------------- |
| WhatsApp             | ✅             | ✅             | ❌                | ❌                           | ❌                            | ❌                        | 2009           |
| WeChat               | ❌             | ❌             | ❌                | ❌                           | ❌                            | ❌                        | 2011           |
| Facebook Messenger   | ✅             | 🟡 (opcional) | ❌                | ❌                           | ❌                            | ❌                        | 2011           |
| Telegram             | 🟡 (opcional) | ❌             | 🟡               | ✅                           | ❌                            | ❌                        | 2013           |
| LINE                 | ✅             | ✅             | ❌                | ❌                           | ❌                            | ❌                        | 2011           |
| Signal               | ✅             | ✅             | ❌                | ✅                           | ✅                            | ❌                        | 2014           |
| Threema              | ✅             | ✅             | ✅                | ✅                           | ❌                            | ❌                        | 2012           |
| Element (Matrix)     | ✅             | ✅             | ✅                | ✅                           | ✅                            | 🟡 (federado)            | 2016           |
| Delta Chat           | ✅             | ✅             | ✅                | ✅                           | N/A                          | 🟡 (via email)           | 2017           |
| Conversations (XMPP) | ✅             | ✅             | ✅                | ✅                           | ✅                            | 🟡 (federado)            | 2014           |
| Session              | ✅             | ✅             | ✅                | ✅                           | ✅                            | ✅                        | 2020           |
| SimpleX              | ✅             | ✅             | ✅                | ✅                           | ✅                            | ✅                        | 2021           |
| **Olvid**            | **✅**         | **✅**         | **✅**            | **✅**                       | **❌**                        | 🟡(sem diretório)        | **2019**       |
| Keet                 | ✅             | ✅             | ✅                | ❌                           | N/A                          | ✅                        | 2022           |
| Jami                 | ✅             | ✅             | ✅                | ✅                           | N/A                          | ✅                        | 2005           |
| Briar                | ✅             | ✅             | ✅                | ✅                           | N/A                          | ✅                        | 2018           |
| Tox                  | ✅             | ✅             | ✅                | ✅                           | N/A                          | ✅                        | 2013           |



*E2EE = Encriptação de ponta a ponta*



## Instalar a aplicação Olvid



O Olvid está disponível em todas as plataformas. Pode descarregar a aplicação diretamente da loja de aplicações do seu telemóvel:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);



No Android, também é possível [instalar via APK] (https://www.olvid.io/download/).



Neste tutorial, vamos concentrar-nos na versão móvel, mas tenha em atenção que também estão disponíveis [versões para computador](https://www.olvid.io/download/) (MacOS, Linux e Windows). Se escolher a versão paga, poderá sincronizar a sua conta em vários dispositivos.



![Image](assets/fr/01.webp)



## Criar uma conta no Olvid



Quando abrir a aplicação pela primeira vez, clique no botão "*Sou um novo utilizador*".



![Image](assets/fr/02.webp)



Escolha uma alcunha ou introduza o seu primeiro e último nome.



![Image](assets/fr/03.webp)



Adicionar uma fotografia de perfil.



![Image](assets/fr/04.webp)



A sua conta está agora criada.



![Image](assets/fr/05.webp)



Para evitar qualquer perda de acesso à sua conta Olvid, recomendamos a criação de cópias de segurança automáticas. Para tal, abra as definições clicando nos três pontos no canto superior direito do Interface e selecione "*Definições*".

⚠️ **Atenção**: desde a versão 3.7 do Olvid, o procedimento para fazer backup dos seus perfis e contatos foi substituído por um novo. Este tutorial ainda apresenta a versão antiga. Você pode descobrir a nova versão em suas FAQ: [💾 Fazer backup dos seus perfis](https://www.olvid.io/faq/sauvegarder-vos-profils/)

![Image](assets/fr/06.webp)



Aceder ao menu "*Guardar chaves e contactos*".



![Image](assets/fr/07.webp)



Em seguida, clique em "*generate a backup key*". Esta chave irá encriptar as suas cópias de segurança. Se precisar de recuperar a sua conta noutro dispositivo e já não tiver acesso à mesma, precisará de uma cópia de segurança e desta chave para a desencriptar.



![Image](assets/fr/08.webp)



Guarde esta chave num local seguro. Também pode fazer uma cópia em papel.



![Image](assets/fr/09.webp)



Pode então optar por criar uma cópia de segurança local ou uma cópia de segurança automática num serviço de nuvem. Esta segunda opção é altamente recomendada para garantir o acesso à sua conta Olvid em todas as circunstâncias, mesmo que perca o seu telemóvel.



![Image](assets/fr/10.webp)



Certifique-se de que a opção "*Ativar cópia de segurança automática*" está selecionada.



![Image](assets/fr/11.webp)



Também pode explorar as outras definições disponíveis para personalizar a aplicação de acordo com as suas necessidades.



![Image](assets/fr/12.webp)



## Enviar mensagens com o Olvid



Para poder enviar mensagens, tem de começar por adicionar contactos. Na página inicial, clique no botão azul "*+*".



![Image](assets/fr/13.webp)



Olvid apresenta então o seu ID de utilizador. Pode então transmiti-lo às pessoas com quem deseja comunicar, para que estas o possam adicionar como contacto.



Para adicionar uma pessoa, digitalize a respectiva identificação com a sua câmara ou cole-a manualmente clicando nos três pequenos pontos no canto superior direito.



![Image](assets/fr/14.webp)



Após a leitura do ID, pode pedir ao seu contacto que leia o código QR apresentado ou enviar-lhe um pedido de ligação remota clicando em "*Contacto remoto*".



![Image](assets/fr/15.webp)



A ligação está agora estabelecida.



![Image](assets/fr/16.webp)



Pode agora começar a trocar mensagens e outros conteúdos com o seu correspondente!



![Image](assets/fr/17.webp)



A partir da página inicial, encontra todas as suas conversas.



![Image](assets/fr/18.webp)



O segundo separador contém todos os seus contactos.



![Image](assets/fr/19.webp)



Também pode criar debates em grupo.



![Image](assets/fr/20.webp)



Parabéns, agora estás a par da utilização do Olvid messaging, uma excelente alternativa ao WathsApp! Se achou este tutorial útil, ficar-lhe-ia muito grato se deixasse um polegar Green abaixo. Não hesite em partilhar este tutorial nas suas redes sociais. Muito obrigado!



Também recomendo este outro tutorial, no qual vos apresento o Proton Mail, uma alternativa muito mais amiga da privacidade ao Gmail:



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2