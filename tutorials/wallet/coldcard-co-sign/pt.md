---
name: COLDCARD - Co-Sign
description: Descubra a funcionalidade Co-Sign e utilize-a no seu COLDCARD
---

![cover](assets/cover.webp)


*NB: Este tutorial destina-se a pessoas que já têm alguma experiência com carteiras com várias assinaturas, dispositivos Coinkite e software como o Sparrow wallet ou o Nunchuk.*



![video](https://youtu.be/MjMPDUWWegw)




**Porquê o ColdCard Co-Sign?



Esta funcionalidade permite-lhe adicionar **condições de despesa** ao seu dispositivo ColdCard (Q ou Mk4), à semelhança de um módulo de segurança de hardware (HSM), para proteger os seus fundos, mantendo uma flexibilidade e um controlo consideráveis sobre os mesmos.



As condições de despesa podem ser, por exemplo:





- Limites de magnitude**: limitar o montante de bitcoins que pode gastar numa única transação.
- Limites de velocidade:** decidir quantas transacções pode efetuar por unidade de tempo (por hora, dia, semana, etc.), exigindo um número mínimo de blocos entre elas.
- Endereços pré-aprovados:** Permitir apenas o envio de bitcoins para endereços pré-aprovados.
- Autenticação de dois factores:** Requer a confirmação de uma aplicação móvel 2FA de terceiros (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) num smartphone/tablet com NFC e acesso à Internet.



**Como funciona



Adicionando um segundo seed ao seu ColdCard Mk4 ou Q, chamado "Spending Policy Key" (chave de política de despesas), que chamaremos de "chave C" ao longo deste tutorial.


Para além deste seed adicional, ser-lhe-á pedido que Supply pelo menos uma chave adicional (XPUB), a que chamaremos "Backup Key", para criar um Wallet Multisig 2-on-N.



Em resumo, vamos criar um Wallet Multisig, e o seu dispositivo ColdCard conterá 2 das chaves privadas necessárias para gastar os fundos, o seed master do dispositivo e a "Spending Policy Key".



Sempre que a "Chave C" for solicitada a assinar, aplicar-se-ão as condições de despesa especificadas e o ColdCard só assinará se a transação estiver em conformidade com as mesmas.



Se o utilizador desejar renunciar a estas condições de despesa, pode fazê-lo:




- assinando com uma das chaves de reserva e a mão seed, ou 2 chaves de reserva dependendo do tamanho do seu Multisig.
- introduzindo a "Chave de política de despesas" ou a "Chave C" no menu "Co-assinatura". **Esta última não pode ser consultada diretamente no dispositivo, caso contrário qualquer pessoa poderia anular as condições de despesa configuradas




## Configuração do ColdCard Co-Sign



![video](https://youtu.be/MjMPDUWWegw)



### 1- Ativar a funcionalidade



Antes de mais, certifique-se de que o seu dispositivo tem, pelo menos, a versão mais recente do firmware:




- Mk4: v5.4.2
- Q: v1.3.2Q




No seu Mk4 ou ColdCardQ, aceda a *Ferramentas avançadas > Co-assinatura de ColdCard*.



![Co-Sign](assets/fr/01.webp)



*No tutorial que se segue, as imagens de ecrã serão tiradas num ColdCardQ por conveniência, mas os passos e menus são idênticos entre o Mk4 e o Q.*



É apresentado um resumo da funcionalidade.


A terminologia utilizada para designar as chaves, que iremos utilizar novamente no Wallet multi-assinaturas 2 contra 3 que estamos prestes a criar, é



Chave A = Coldcard master seed


Tecla B = Tecla de reserva


Chave C = Chave da política de despesas



Clicar em **"ENTER "**.



![Co-Sign](assets/fr/02.webp)



O passo seguinte é decidir qual a chave privada que actuará como "Chave da política de despesas" ou "Chave C".



Podemos ver que temos várias opções à nossa disposição:





- Ou prima **"ENTER "** para generate uma nova frase seed de 12 palavras.





- Clicar em **"(1) "** para importar um seed de 12 palavras existente, ou selecionar **"(2) "** para importar um seed de 24 palavras existente.





- Ou prima **"(6) "** para importar um seed do cofre do seu dispositivo.



Para efeitos deste tutorial, decidimos importar um seed de 12 palavras existente, premindo **"(1) "**. Pode ser qualquer seed BIP39 que já possua e para o qual tenha obviamente uma cópia de segurança.



Utilize o seu teclado para introduzir as 12 palavras do seu seed. Para este exemplo, vamos escolher a frase válida seed beef x 12. Em seguida, prima **"ENTER "**.


*NB: se não tiver uma cópia de segurança deste seed, deixará de poder modificar as definições de "Co-Sign" no seu dispositivo, a fim de alterar as suas condições de despesa*



A funcionalidade "Co-Sign" está agora activada no dispositivo. De seguida, temos de escolher as nossas condições de despesa e concluir a criação do Wallet com várias assinaturas.



![Co-Sign](assets/fr/03.webp)



### 2- Escolher as condições de despesa ou "*políticas de despesa*"



Aqui especificamos as condições de despesas que devem ser cumpridas quando a **"Chave C "** ou **"Chave da política de despesas**" assina uma transação.



No menu **"Co-assinatura "**, clicar em **"Política de despesas**".



Pode então escolher a magnitude máxima, ou seja, o número máximo de satoshis que pode ser gasto numa única transação.



Para este exemplo, vamos escolher uma magnitude máxima de **21212** satoshis. Clique em **"ENTER "** para confirmar.




![Co-Sign](assets/fr/04.webp)



Em seguida, optamos por definir a velocidade máxima, ou seja, o número de transacções que o dispositivo será capaz de assinar por unidade de tempo. Para este tutorial, vamos escolher a velocidade ilimitada, ou seja, sem limite para o número de transacções.




![Co-Sign](assets/fr/05.webp)



### 3- Criar Wallet Multisig 2 em N



Temos ainda de escolher a terceira chave para o nosso Wallet Multisig, ou seja, a **"Backup Key "** (Chave B), para além da **master seed** do dispositivo (Chave A) e da **"Spending Policy Key "** (Chave C).



A nossa "chave B" terá de ser importada através de um cartão SD ou através de um código QR, no caso do ColdCardQ.


Para o fazer, precisamos de um segundo dispositivo ColdCard Mk4 ou Q, no qual é utilizada a nossa "Chave B".



Neste segundo dispositivo que contém a sua **"Backup Key "**, digamos um ColdCard Mk4 para este exemplo, vá do menu principal para **"Settings "**, depois, **"Multisig Wallet"**, e finalmente **"Export Xpub "**.


(Se o seu segundo dispositivo for um ColdCardQ, terá a opção de exportar o seu Xpub através de um código QR, como é óbvio).





![Co-Sign](assets/fr/06.webp)





No ecrã seguinte, inserir um cartão SD e clicar no botão **"validar "** no canto inferior direito. Em seguida, clicar em **"(1) "** para guardar o ficheiro no cartão SD.



O ficheiro conterá a impressão digital da chave pública (*fingerprint*) no seu nome, e terá a forma `ccxp-0F056943.json`.




![Co-Sign](assets/fr/07.webp)



Em seguida, insira o cartão SD no ColdCardQ "inicial" para importar a nossa "Backup Key" (chave B).


No menu "ColdCard Co-Signing", escolher "Build 2-of-N" e, no ecrã seguinte, clicar em **"ENTER "** e, em seguida, novamente em **"ENTER "** para importar a "Backup Key" do cartão SD.



![Co-Sign](assets/fr/08.webp)



No ecrã seguinte, deixe "Account Number" em branco (a menos que saiba exatamente o que está a fazer) e clique novamente em **"ENTER "**.



![Co-Sign](assets/fr/09.webp)



Finalmente, estamos prontos para usar o nosso novo Wallet Multisig 2-sur-3, composto da seguinte forma:



Chave A= Coldcard Q master seed


Chave B= Chave de backup (acabou de ser importada de um segundo dispositivo Coldcard)


Chave C= Chave da política de despesas (se utilizada para assinar, impõe condições de despesas predefinidas)



## Assinatura conjunta com o Sparrow wallet



Se necessário, consulte os tutoriais abaixo para se familiarizar com o software Sparrow wallet:



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Exportação Wallet Multisig 2-sur-3 para Sparrow wallet



Agora precisamos de exportar o nosso Wallet Multisig para o Sparrow para que possamos colocar aí os nossos primeiros satoshis.



No menu principal do seu ColdCardQ, selecione **"Definições "** e, em seguida, **"Carteiras Multisig"**.


O conjunto de carteiras Multisig conhecidas pelo seu ColdCard é agora apresentado, com o número de chaves aqui envolvidas "2/3" (2-sur3). Escolha o Multisig **"ColdCard Co-Sign "** que acabámos de criar e clique em **"ColdCard Export "**.



![Co-Sign](assets/fr/10.webp)




Por fim, escolhe o método que te permitirá exportar o Wallet para o Sparrow. No nosso caso, escolhemos o cartão SD e clicamos em **"(1) "** depois de inserir um cartão SD na ranhura A do dispositivo.



![Co-Sign](assets/fr/11.webp)



Em seguida, no Sparrow wallet, selecione "Importar Wallet".



![Co-Sign](assets/fr/12.webp)



Em seguida, clicar em **"Importar ficheiro "**. Em seguida, escolha o ficheiro **"export-Coldcard_Co-sign.txt "** no seu cartão SD.



![Co-Sign](assets/fr/13.webp)



Dê ao seu Wallet um nome como aparecerá no Sparrow e escolha uma palavra-passe para encriptar o seu Wallet (ou não).



![Co-Sign](assets/fr/14.webp)



![Co-Sign](assets/fr/15.webp)



Estamos agora prontos para receber os nossos primeiros satoshis e testar as condições de despesa que aplicámos ao nosso Wallet.



![Co-Sign](assets/fr/16.webp)



### 2- Teste de políticas de despesas predefinidas



Para relembrar, tínhamos decidido um valor máximo de 21212 satoshis para o nosso Wallet Multisig. Isto significa que cada vez que a Chave de Política de Gastos (Chave C) assinasse uma transação, esta só seria válida se o montante gasto fosse inferior ou igual a 21212 satoshis.



Vamos testá-lo.


Primeiro, vamos clicar no separador "Receive" (Receber) no Sparrow e colocar alguns Satss no Wallet, que utilizaremos ao longo deste tutorial.



![Co-Sign](assets/fr/17.webp)



![Co-Sign](assets/fr/18.webp)



Em seguida, vamos tentar gastar mais do que os 21212 satoshis permitidos, simulando uma transação de 50.000 Sats.



![Co-Sign](assets/fr/19.webp)



![Co-Sign](assets/fr/20.webp)



![Co-Sign](assets/fr/21.webp)



![Co-Sign](assets/fr/22.webp)



Depois de digitalizar o código QR que representa a transação *não assinada* com o nosso ColdCardQ para importar a transação, eis o que nos é mostrado no ecrã. Uma mensagem de aviso indica-nos que as condições de despesa não foram cumpridas. Se assinarmos a transação na mesma, apenas uma das 2 chaves (a chave principal seed no dispositivo, mas não a "chave C") assinará.




![Co-Sign](assets/fr/23.webp)



Aqui, depois de importar a nossa transação para o Sparrow, podemos ver que apenas uma das assinaturas foi aplicada à transação.



![Co-Sign](assets/fr/24.webp)




Agora vamos repetir a experiência, mas para uma transação de 21.000 satoshis, ou seja, menos do que a magnitude máxima (21212 Sats) que definimos para este Wallet.




![Co-Sign](assets/fr/25.webp)



![Co-Sign](assets/fr/26.webp)



![Co-Sign](assets/fr/27.webp)



![Co-Sign](assets/fr/28.webp)



Vamos tentar assinar esta transação com o nosso ColdCardQ.



Desta vez não há problema, não aparece qualquer mensagem de aviso e, quando importamos a transação assinada para o Sparrow wallet, desta vez as duas assinaturas foram aplicadas, tornando a transação válida e pronta para distribuição.




![Co-Sign](assets/fr/29.webp)




![Co-Sign](assets/fr/30.webp)






## Co-assinar com o Nunchuk



https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Endereços Web 2FA e de lista branca



Neste parágrafo, utilizaremos o nosso Co-Sign Wallet Multisig com a matraca e aproveitaremos a oportunidade para aplicar novas condições de despesa para ver como corre.



Aceda a *Ferramentas avançadas > Assinatura conjunta ColdCard*.


É-nos pedido que introduzamos a nossa "Chave de Política de Despesas", para aceder ao menu que nos permite alterar as condições de despesa. No nosso caso, introduzimos 12 x "carne de vaca".



Decidimos manter uma magnitude de 21212 Sats e uma "Velocidade Limite" máxima por razões práticas relacionadas com este tutorial. Por outro lado, vamos utilizar o menu **"Whitelist Addresses "** para impor os endereços nos quais os nossos fundos podem ser gastos.




![Co-Sign](assets/fr/31.webp)




Digitalize os códigos QR associados aos endereços (vamos escolher 2) que pretende adicionar à sua lista branca e, em seguida, clique em **"ENTER "**. Após ter validado os seus endereços premindo sucessivamente **"ENTER "**, verificamos que foram aplicados limites aos endereços Magnitude e beneficiários.



![Co-Sign](assets/fr/32.webp)



Por último, para ter uma visão completa das possibilidades oferecidas pela "Co-Sign", activemos a opção "Web 2FA".


Esta funcionalidade permite-lhe utilizar uma aplicação compatível com TOTP RFC-6238, como o Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / ou Aegis Authenticator, para adicionar um Layer extra de segurança.



https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

Em termos concretos, antes de assinar uma transação, terá de aproximar o seu dispositivo com NFC e ligado à Internet do seu Coldcard. Isto levá-lo-á automaticamente para uma página Web coldcard.com, onde lhe será pedido que introduza o código de 6 dígitos da sua aplicação. Se introduzir o código correto, a página Web mostrar-lhe-á um código QR para digitalizar para o ColdCardQ, ou um código de 8 dígitos para introduzir no seu Mk4, para autorizar o seu dispositivo a assinar.





![Co-Sign](assets/fr/33.webp)



Depois de digitalizar o código QR apresentado na sua aplicação de dupla autenticação e de adicionar a sua conta ColdCard Co-Sign (CCC), ser-lhe-á pedido que verifique se tudo está em ordem, introduzindo o seu código 2FA.



Introduza o seu ColdCard na parte de trás do seu dispositivo NFC.



![Co-Sign](assets/fr/34.webp)



Na página web que se abre, introduza o código 2FA da sua aplicação favorita. Em seguida, digitalize o código QR apresentado com o seu ColdCardQ (ou introduza o código de 8 dígitos apresentado no seu Mk4).



![Co-Sign](assets/fr/35.webp)




Impusemos agora um limite de magnitude (21212 Sats), endereços de destino e dupla autenticação.



![Co-Sign](assets/fr/36.webp)



### 2- Exportar Wallet Multisig 2 contra 3 para o matraca



Vamos exportar o Wallet Multisig 2 contra 3 para o Nunchuk desta vez, como fizemos com o Sparrow anteriormente.


Aceda a *Definições > Carteiras Multisig > 2/3: Co-assinatura de ColdCard > Exportação de ColdCard*.



![Co-Sign](assets/fr/10.webp)



Desta vez, selecionar a opção NFC para exportação, clicando no botão ColdcardQ com o mesmo nome **"NFC "**.



![Co-Sign](assets/fr/37.webp)



No Nunchuk, se estiveres a abrir a aplicação pela primeira vez, clica em **"Recover existing Wallet"**.



![Co-Sign](assets/fr/38.webp)



Se já tiver um Wallet na aplicação, clique em **"+"** no canto superior direito e depois em **"Recover existing Wallet"**.



![Co-Sign](assets/fr/39.webp)




Em seguida, selecione **"Recover Wallet from COLDCARD "** e depois **"Multisig Wallet"**.



![Co-Sign](assets/fr/40.webp)



Por fim, toque com a parte de trás do seu smartphone no ecrã do seu ColdCardQ para importar o Wallet através de NFC.



![Co-Sign](assets/fr/41.webp)



A nossa conta e os satoshis anteriormente depositados através do Sparrow wallet estão de volta.



![Co-Sign](assets/fr/42.webp)



### 3- Teste de políticas de despesas predefinidas



Vamos agora tentar fazer uma transação que viole as 2 condições de despesa que definimos. **Vamos tentar gastar mais de 21212 Sats num Address que não foi aprovado.** Vamos tentar enviar 22 222 Sats para um Address aleatório.



![Co-Sign](assets/fr/43.webp)



Depois de a transação ter sido criada, clique nos três pequenos pontos no canto superior direito para a exportar para o seu ColdCard.



![Co-Sign](assets/fr/44.webp)



Em seguida, selecione **"Exportar via BBQR "** e digitalize o código QR apresentado com o seu ColdCardQ.



![Co-Sign](assets/fr/45.webp)



O ColdcardQ apresenta então um aviso que, à medida que se desloca para o fundo do ecrã, esclarece que a transação viola as condições de despesas, como esperado.



**Note-se que o dispositivo não nos diz quais são as condições de despesa envolvidas, para evitar que um potencial atacante tente contornar as restrições




![Co-Sign](assets/fr/46.webp)



Se continuar a validar premindo **"ENTER "**, aparece o código QR que representa a transação assinada. Se o importar no Nunchuk, pode ver que só foi aplicada uma assinatura.



![Co-Sign](assets/fr/47.webp)



![Co-Sign](assets/fr/48.webp)






Vamos realizar exatamente a mesma operação, mas desta vez com uma transação que respeita o limite de magnitude (21212 Sats), e gasta os satoshis num dos 2 endereços que pré-configurámos.



Enviamos o Nunchuk 12121 Sats para um dos nossos 2 endereços. Em seguida, exportamos a transação para o nosso ColdCard, como fizemos anteriormente.



![Co-Sign](assets/fr/49.webp)




Depois de importar a transação não assinada para o nosso ColdCardQ, vejamos o que nos é mostrado desta vez.



Um aviso está sempre presente, mas desta vez, passando para a parte inferior do ecrã, vemos que se trata de validar a transação através de 2FA. O dispositivo pede-nos que aproximemos o nosso ColdcardQ do nosso terminal NFC ligado à Internet (smartphone ou tablet), o que fazemos.



![Co-Sign](assets/fr/50.webp)



Abre-se uma página web no nosso smartphone, pedindo-nos para introduzir o nosso código 2FA, o que fazemos graças ao Proton Authenticator.



![Co-Sign](assets/fr/51.webp)





Em seguida, digitalize o código QR que aparece na página Web, para autorizar o seu ColdCard a assinar a transação.


A transação é agora assinada pelas duas chaves e, portanto, válida.



Se o "Push Tx" estiver ativado no seu ColdCardQ, pode transmitir a transação diretamente para a rede com um simples toque na parte de trás do seu smartphone.



![Co-Sign](assets/fr/52.webp)




Se não tiver o "Push tx" ativado, prima o botão "QR" no seu ColdCardQ para visualizar a transação assinada como um código QR e importe-o para o Nunchuk, da mesma forma que no exemplo anterior.



![Co-Sign](assets/fr/53.webp)



Desta vez, verificamos que foram aplicadas 2 assinaturas, pelo que a transação está pronta para ser transmitida na rede Bitcoin.



![Co-Sign](assets/fr/54.webp)




Chegámos ao fim deste tutorial, que lhe dará uma visão geral das possibilidades oferecidas pela funcionalidade Co-Sign integrada nos dispositivos ColdCardQ e Mk4 da Coinkite, bem como a sua utilização através de carteiras como a Sparrow e a Nunchuk.