---
name: Tox
description: Abrir conversas sem intermediários no protocolo descentralizado Tox
---
![cover](assets/cover.webp)



A encriptação de ponta a ponta é um serviço oferecido por muitas aplicações de mensagens, como o WhatsApp e o Telegram. Neste caso, a encriptação significa que, antes de ser enviada pelo remetente, a mensagem é protegida por uma fechadura criptográfica da qual apenas o destinatário dispõe da chave. Hoje vamos descobrir uma aplicação de mensagens encriptadas totalmente descentralizada e de ponta a ponta, baseada em princípios semelhantes aos do Blockchain, para oferecer uma comunicação segura, encriptada de ponta a ponta e sem intermediários: Tox Chat.



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
| **Tox**              | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = Encriptação de ponta a ponta*



## O que é Tox?



O Tox é um protocolo de comunicações livre (open source) e descentralizado que utiliza a tecnologia *Networking and Cryptography Library* (NaCl) e combinações de algoritmos de encriptação para garantir a segurança e a confidencialidade dos seus utilizadores. O Tox permite-lhe enviar mensagens de texto Exchange, fazer chamadas de áudio e vídeo, partilhar ficheiros e partilhar o seu ecrã com amigos de forma segura, descentralizada e sem intermediários.



A tecnologia que o protocolo Tox utiliza é semelhante à das redes peer-to-peer, como as cadeias de blocos, o que favorece a descentralização da infraestrutura do protocolo. Ao contrário das redes sociais e das aplicações de mensagens encriptadas de ponta a ponta, a aplicação Tox Chat baseia-se num protocolo descentralizado que não tem um servidor central. Todos os utilizadores comunicam numa rede peer-to-peer sem intermediários e resistente à censura. Para comunicar, cada utilizador é identificado por um ID único (ToxID) derivado da sua chave pública, que é armazenada numa tabela Hash distribuída.



## Aderir à Tox



Pode utilizar o protocolo Tox através de um cliente de mensagens instantâneas que pode ser descarregado a partir do [sítio Tox Chat] (https://tox.chat).



![download](assets/fr/01.webp)



Dependendo do seu sistema operativo, pode descarregar e instalar um cliente Tox que corresponda ao :





- aTox: [aTox](https://github.com/evilcorpltd/aTox), um cliente Tox escrito em Kotlin disponível apenas no Android



![aTox](assets/fr/02.webp)





- qTox: Um cliente Tox de [open source](https://github.com/TokTok/qTox) baseado no Qt Framework (C++) disponível em Windows, Linux, MacOs.



![qTox](assets/fr/03.webp)





- Toxic: [Toxic](https://github.com/JFreegman/toxic) é um cliente Tox escrito em C e executado em sistemas com interfaces de linha de comando.



![Toxic](assets/fr/04.webp)



Neste tutorial, utilizaremos clientes qTox no Windows e aTox para comunicar.



## Introdução ao qTox



Uma vez descarregado, instale o seu cliente Tox e crie o seu perfil.



![qTox-acount](assets/fr/05.webp)



Parabéns, acaba de aderir ao protocolo Tox. No software qTox, pode encontrar as informações do seu perfil clicando no seu nome de utilizador.



![profil](assets/fr/06.webp)



Em particular, encontrará o seu Tox ID, que pode guardar como um código QR e partilhar com pessoas que queiram entrar em contacto consigo.



Exporte o seu ficheiro de perfil Tox para ter uma cópia de segurança do seu perfil e das informações de contacto que pode utilizar para restaurar. Clique no botão **Exportar** e, em seguida, escolha o caminho para o seu ficheiro de cópia de segurança.



![export](assets/fr/07.webp)



No menu **Mais**, adicione amigos, importe contactos e gira os pedidos de amizade que recebe.



![friends](assets/fr/08.webp)



Pode contactar-me através deste ID Tox, por exemplo: EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C3C16BE3DC2CA6D9F



Depois de o pedido de amizade ter sido enviado, o destinatário terá de aceitar ou rejeitar o seu pedido antes de o poder contactar.



![request](assets/fr/09.webp)



O seu cliente Tox inclui todas as opções oferecidas pelas aplicações de mensagens instantâneas:





- Chamadas de vídeo





- Chamadas de voz





- Partilha de ficheiros





- emojis



![chat](assets/fr/10.webp)



### Grupos peer-to-peer



Os seus clientes Tox também lhe permitem comunicar com um grupo de pessoas de uma forma completamente descentralizada: são as chamadas conferências. No menu **Grupos**, crie uma nova conferência ou consulte a lista de convites para participar em conferências que recebeu.



![conferences](assets/fr/11.webp)



Depois de a conferência ter sido criada, pode convidar os seus amigos a juntarem-se à conferência no seu cliente Tox. Na sua lista de amigos, clique com o botão direito do rato no nome de utilizador do amigo que pretende convidar. Clique na opção **Convidar para conferência** e, em seguida, selecione o nome da conferência que criou. Também pode convidar um amigo criando implicitamente uma conferência com a opção **Criar uma nova conferência**.



⚠️ Os clientes Tox ainda estão em desenvolvimento, pelo que poderá encontrar erros ao interagir com o software. As funcionalidades de conferência e videochamada ainda não estão disponíveis no cliente Tox para Android (aTox).



![invite](assets/fr/12.webp)



### Transferências de ficheiros



No menu **Transferências de ficheiros**, encontra um histórico dos ficheiros que enviou e dos que recebeu dos seus contactos.



![files](assets/fr/13.webp)



Também pode personalizar as configurações de partilha de ficheiros para cada discussão que tiver. Clique com o botão direito do rato no nome de utilizador do destinatário e selecione "Mostrar mais detalhes".



![details](assets/fr/14.webp)



A partir dos detalhes do Interface, pode gerir as autorizações que concede ao seu destinatário para :





- Aceitação automática de convites para conferências.





- Aceitação automática de ficheiros.





- Caminhos de cópia de segurança para os seus ficheiros de discussão.



![permissions](assets/fr/15.webp)



### Mais parâmetros



No menu **Configurações**, pode personalizar as definições do seu cliente Tox.





- Na secção **Geral**, altere o idioma básico do seu cliente Tox, defina os caminhos de cópia de segurança dos ficheiros e o tamanho máximo dos ficheiros a aceitar automaticamente.



![general](assets/fr/16.webp)





- Na secção **Interface user**, modifique as fontes e os tamanhos das suas mensagens. Também pode alterar o tema do seu cliente Tox.



![ui](assets/fr/17.webp)





- O separador **Privacidade** permite-lhe definir mensagens efémeras, desmarcando a caixa "Manter histórico da conversa". Também pode alterar o seu código Nospam quando notar que está a ser alvo de spam de pedidos de amizade, clicando no botão "generate código NoSpam aleatório".



![privacy](assets/fr/18.webp)



### O que garante a confidencialidade no Tox?



O protocolo Tox utiliza a Tabela Distribuída Hash para criar uma rede de nós descentralizados. Cada cliente Tox faz parte da rede DHT e armazena informações sobre outros nós. No caso do Tox, a DHT armazena endereços IP como valores associados às chaves públicas do Tox (Tox ID). Isto facilita a procura de um dispositivo cliente Tox sem ter de consultar um servidor central.



Imaginemos que escrevemos para o nosso utilizador `EBC5604D9386E594CCC32943A03F96A96687FBD46788F1CD4F3337EB703C16BE3DC2CA6D9F` a quem chamaremos **utilizador B**. O seu cliente Tox localizará este identificador na tabela Hash Distributed e obterá o IP Address associado. Assim que o IP Address for encontrado, o seu cliente Tox criará um canal de comunicação direto e encriptado com a máquina do **utilizador B**, ou usará outros nós como relés para chegar ao **utilizador B**. Os algoritmos de encriptação garantem que, independentemente do canal de comunicação, apenas **Utilizador B** poderá ler o conteúdo da sua mensagem.



Se gostou de descobrir o Tox e conseguiu perceber como é útil para reforçar a sua privacidade, sinta-se à vontade para dar um "polegar para cima" a este tutorial. Recomendamos também o nosso tutorial sobre o Simple Login, uma ferramenta que lhe permite receber e enviar e-mails anonimamente.



https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41