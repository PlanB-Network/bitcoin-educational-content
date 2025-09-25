---
name: COLDCARD Q - Key Teleport
description: O que é o Teletransporte de Chaves e como o utilizo?
---

![cover](assets/cover.webp)




![video](https://www.youtube.com/watch?v=Bg0r0DQVcDg)




![video](https://www.youtube.com/watch?v=BRpBiK-F8VU)



Qual é a funcionalidade **Key Teleport** oferecida pela Coinkite com o seu dispositivo ColdCardQ de referência?



O **Key Teleport** permite-lhe transferir de forma segura dados confidenciais entre 2 ColdCardQs. O canal de transmissão nem sequer precisa de ser encriptado e pode ser público.



Isto pode ser utilizado para transferir:





- frases **gW-0** (o mestre seed de ColdCard Q ou os segredos guardados no [Cofre seed] de ColdCardQ(https://coldcard.com/docs/temporary-seeds/#seed-vault).
- **notas e palavras-passe confidenciais**: pode ser qualquer segredo ou todo o diretório [Secure Notes & Passwords](https://coldcard.com/docs/secure_notes/) no seu ColdCardQ.
- uma cópia de segurança de todo o seu **ColdCardQ**: o ColdCardQ que recebe esta cópia de segurança não deve ter um seed Master para que isto funcione.
- gW-3 (**Transacções Bitcoin parcialmente assinadas**) como parte de um sistema de assinaturas múltiplas.



Para tal, é necessário que tenha atualizado o [firmware do dispositivo para a versão v1.3.2Q](https://coldcard.com/docs/upgrade/) ou superior.



## Como é que utilizo o Teletransporte de Chaves?



### 1- Para transferir qualquer tipo de dados



Aqui, vamos analisar a transferência de frases seed, notas, palavras-passe ou uma transferência completa de uma cópia de segurança ColdCardQ. O caso das transferências PSBT para transacções com várias assinaturas será abordado mais tarde.



#### Preparar o dispositivo para receber os segredos



No menu **"Advanced / Tools**" do seu ColdCardQ, selecione **"Key Teleport (start) "**.


No ecrã seguinte, é proposta uma palavra-passe de 8 dígitos, neste caso "20420219". Terá de comunicar esta palavra-passe ao remetente. Utilize sms, por exemplo, para enviar esta palavra-passe, ou o seu sistema de mensagens seguro preferido, ou mesmo uma chamada de voz.



Em seguida, clique no botão **"Enter**" do seu ColdCardQ para passar à etapa seguinte.




![CCQ-key-teleport](assets/fr/01.webp)




É gerado um código QR no ecrã. Mais uma vez, terá de comunicar este código QR ao "remetente" do ColdCardQ. A forma mais fácil de o fazer é através de uma videochamada.



**NÃO ENVIAR ESTE CÓDIGO QR ATRAVÉS DO MESMO CANAL DE TRANSMISSÃO UTILIZADO PARA ENVIAR A ANTERIOR PALAVRA-PASSE DE 8 DÍGITOS**.



![CCQ-key-teleport](assets/fr/02.webp)



*Para aqueles que estão interessados, vamos tentar compreender o mecanismo subjacente que permite a transferência de segredos através de canais não seguros*



*O que estamos realmente a fazer aqui é iniciar uma transferência de segredos através do método Diffie-Hellman, abordado no curso BTC204 que incluí abaixo*



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

*Atualmente temos:*




- gerou um par de chaves efémeras (pública/privada, respetivamente Ka e ka com Ka=G.ka, sendo G o ponto gerador de ECDH) e uma palavra-passe de 8 dígitos.
- utilizou esta palavra-passe para encriptar a chave pública (Ka) através de AES-256-CTR, tendo depois transmitido esta palavra-passe através de um canal de comunicação A para o ColdCardQ "emissor".
- finalmente, transmitimos o pacote encriptado ao remetente através do código QR acima, utilizando um segundo canal de comunicação B diferente do 1.



#### Preparar o dispositivo que irá enviar os segredos



A partir do dispositivo de envio, clique no botão **"QR "** para digitalizar o código QR que lhe foi enviado pelo dispositivo de receção e, em seguida, introduza a palavra-passe de 8 dígitos que lhe foi comunicada na etapa anterior através de um canal separado. Estamos agora prontos para iniciar o envio de dados a partir do dispositivo "emissor".



**Não introduza incorretamente a palavra-passe de 8 dígitos, pois não será apresentada qualquer mensagem de erro e o processo continuará. No entanto, a transferência final de dados falhará e terá de começar de novo**.



![CCQ-key-teleport](assets/fr/03.webp)



*Para os mais curiosos, vejamos mais uma vez o que estamos a fazer em termos de criptografia e transferência de segredos:*




- importámos os dados encriptados através da leitura do código QR no dispositivo recetor.
- depois desencriptámo-los com a palavra-passe de 8 dígitos que nos foi transmitida por um canal secundário*.
- estamos, portanto, na posse da chave pública (Ka) gerada inicialmente pelo recetor
- De seguida, criamos um novo par de chaves efémeras (Kb/kb, com Kb=G.kb) no dispositivo de envio, que utilizamos para aplicar a ECDH a Ka. Efectuamos, portanto, a operação kb.Ka=Ks , em que Ks é designada por **"chave de sessão"**.




É-lhe agora pedido que escolha a natureza dos segredos a transmitir entre os 2 ColdCardQs (notas confidenciais, palavra-passe, cópia de segurança completa, sementes contidas no seu cofre, dispositivo mestre seed).



![CCQ-key-teleport](assets/fr/04.webp)



Aqui o nosso segredo será uma mensagem curta, selecionando **"Quick Text Message "**. Escreva a sua mensagem (para nós "PlanB Network rocks") e prima **"ENTER "**.


O dispositivo gera então uma nova palavra-passe aleatória denominada **"Palavra-passe de teletransporte "** , no exemplo "NE XG BT SK".



![CCQ-key-teleport](assets/fr/05.webp)



Prima **"ENTER "** e ser-lhe-á apresentado um novo código QR. Faça com que o dispositivo recetor o leia. E, num canal de comunicação diferente, transmita a **"Palavra-passe de teletransporte "** ao recetor.



![CCQ-key-teleport](assets/fr/06.webp)



*Mais uma vez, para os curiosos, durante esta fase:*




- depois de selecionar os segredos a transmitir, criamos uma nova palavra-passe aleatória chamada **"Teleport Password"**.
- encriptamos então os segredos através de AES-256-CTR utilizando a **"Session Key"**, "Ks", gerada no passo anterior.
- prefixamos o pacote já encriptado com a **"Chave de sessão "** com a nossa chave pública Kb, depois acrescentamos mais um Layer de encriptação AES-256-CTR com a **"Palavra-passe de teletransporte "**. Tudo isto é então codificado como um código QR




#### Finalizar a transferência de segredos para o dispositivo recetor



Premir o botão **"QR "** para digitalizar o código QR apresentado pelo dispositivo de envio através do canal visio. Ser-lhe-á pedido que introduza a sua **"Palavra-passe de teletransporte "** para nós "NE XG BT SK".



![CCQ-key-teleport](assets/fr/07.webp)





Os dados são então desencriptados e tornados inteligíveis para o dispositivo recetor. A mensagem recebida é de facto "PlanB Network rocks". E é tudo.



![CCQ-key-teleport](assets/fr/08.webp)



*O que é que aconteceu realmente durante esta última fase :*?




- desencriptámos os dados transmitidos pelo remetente utilizando a **"Palavra-passe de teletransporte "**
- temos, portanto, a chave pública Kb e a nossa mensagem secreta encriptada pela **"chave de sessão "**, "Ks". Mas como é que podemos fazer isto se, como recetor, não conhecemos Ks, que foi criada pelo emissor?
- Temos de aplicar a nossa chave privada "ka" do passo inicial **"Preparar o dispositivo que vai receber os dados"** à chave pública Kb.
- De facto, calculando ka.Kb = ka.kb.G=kb.ka.G=kb.Ka=Ks, encontramos Ks. Que é finalmente utilizado para decifrar a mensagem secreta



### 2- Para transferir o PSBT para o Multisig (avançado)



Isto pressupõe que o seu Wallet Multisig já tenha sido criado e que o seu dispositivo ColdCardQ já tenha sido pré-configurado para poder efetuar transacções com várias assinaturas. Se não for esse o caso, estão disponíveis explicações [aqui] (https://coldcard.com/docs/Multisig/) no sítio Web da Coinkite.



Uma breve recordação do que é um Wallet (Multisig) com várias assinaturas.



Normalmente, para gastar os seus fundos Wallet, apenas é necessária uma chave privada para desbloquear os UTXOs associados aos seus endereços.


No caso de um Wallet Multisig, podem ser necessárias até 15 chaves privadas e, por conseguinte, 15 assinaturas para gastar os fundos. Isto é conhecido como uma carteira "M de N", com N entre 1 e 15 e M o número de assinaturas necessárias para que os fundos possam ser gastos. Por exemplo, um Wallet Multisig 3 de 5 exigirá pelo menos 3 assinaturas de um total de 5 possíveis.



O desafio é então coordenar entre os signatários para assinarem um "PSBT" para o "Partially Signed Bitcoin Transaction". Neste contexto, o "**Key Teleport**" pode ser utilizado para transmitir o PSBT entre os co-signatários de uma forma simples e confidencial. Uma simples videochamada entre os co-signatários é suficiente.



Eis como se faz num Multisig 3 de 4.



**Signatário 1:**



O signatário 1 importa e assina o PSBT. Finalmente, clica em **"T "** para utilizar **"Key Teleport "** para transmitir o PSBT ao signatário 2.



![CCQ-key-teleport](assets/fr/09.webp)




Depois de selecionar o signatário 2 clicando em **"ENTER "**, é fornecida uma "SENHA DE TELEFONE" (aqui JJ YC AB 6A), que deve ser transmitida ao signatário 2 através de outro canal de comunicação. Por exemplo, um SMS ou uma chamada de voz, mas **não** uma chamada de vídeo.



Prima novamente **"ENTER "** e aparece um código QR que representa o PSBT assinado por 1 e encriptado pela "TELEPORT PASSWORD".



![CCQ-key-teleport](assets/fr/10.webp)



**Signatário 2:**



O signatário 2 lê o código QR que lhe é apresentado pelo signatário 1. De seguida, introduz a "PALAVRA-PASSE DO TELEPORTE" transmitida pelo canal de comunicação secundário para desencriptar os dados transmitidos.



O signatário 2 assina a transação e, em seguida, clica em **"T "** para transmitir o PSBT ao signatário 3 através do "Key Teleport".


É evidente que já foram efectuadas 2 assinaturas. Falta apenas a do signatário 3 para que a transação seja válida. Selecionar o signatário 3 clicando em **"ENTER "**.



![CCQ-key-teleport](assets/fr/11.webp)



E é criada uma nova "TELEPORT PASSWORD", seguida novamente de um código QR que codifica o PSBT assinado por 1 e 2 e depois encriptado por esta nova "TELEPORT PASSWORD" (GW YQ K3 LL).



![CCQ-key-teleport](assets/fr/12.webp)



**Signatário 3:**



Repetir o mesmo passo que o anterior.


O signatário 3 lê o código QR que lhe é apresentado pelo signatário 2. De seguida, introduz a "PASSWORD TELEPORT" transmitida pelo canal de comunicação secundário.



O signatário 3 assina a transação e, desta vez, como foram aplicadas 3 das 4 assinaturas, a transação é indicada como finalizada e está pronta para ser distribuída através de vários suportes (cartão SD, NFC, QR, etc.).



![CCQ-key-teleport](assets/fr/13.webp)



Se a função "Push Tx" do seu ColdCardQ estiver activada, basta fixar o seu ColdCardQ na parte de trás de qualquer dispositivo ligado à Internet com NFC (smartphone/tablet) para transmitir a transação através da rede Bitcoin.



![CCQ-key-teleport](assets/fr/14.webp)



*Para as transferências de PSBT de um signatário para outro, o "Teletransporte de Chaves" é simplesmente utilizado através de uma "Palavra-passe de Teletransporte" em cada fase, que encripta o PSBT à medida que é transferido de um signatário para outro. Como os dados transmitidos não podem ser utilizados para roubar fundos, não é necessário um Diffie-Hellman, como acontece quando se enviam segredos altamente confidenciais (seed, palavra-passe, etc...)*.



![CCQ-key-teleport](assets/fr/15.webp)



*Fonte: [Sítio Web oficial da ColdCard](https://coldcard.com/)*