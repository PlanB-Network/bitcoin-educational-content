---
name: Wallet of Satoshi - Auto-Custódia
description: Saiba como configurar o modo de auto-custódia de uma carteira Wallet of Satoshi
---

![cover](assets/cover.webp)



***Not your keys, not your coins* é mais do que um ditado, é um princípio fundamental do Bitcoin, o que significa que, se não controlar as **chaves privadas** que desbloqueiam as suas bitcoins, não é realmente dono delas.



Muitos utilizadores começam geralmente com um **custodial wallet**, depois migram para um **auto-custodial wallet**, onde controlam eles próprios as suas chaves privadas.


Neste tutorial, não vamos apresentar-lhe um novo wallet com autocustódia. Em vez disso, vamos apresentar-lhe uma nova funcionalidade dos wallet ***Wallet of Satoshi***: **o modo de auto-custódia**.



O objetivo desta nova integração é permitir que os utilizadores mantenham o controlo das suas chaves privadas, beneficiando simultaneamente da simplicidade e de uma experiência de utilização fluida.



Antes de chegarmos ao cerne da questão, vamos analisar o modo especial de auto-custódia oferecido pelo Wallet of Satoshi (WoS).



## A particularidade do modo de auto-custódia



A simplicidade e fluidez do modo de auto-custódia do WoS elimina a complexidade de abrir canais Lightning, administrar nós... Mas como é que isto é possível?



O modo de auto-custódia do Wallet of Satoshi é alimentado por **Spark**. Esta é uma solução Layer 2 para o Bitcoin, criada pela Lightspark, utilizando a tecnologia **statechains**.



Por conseguinte, as transacções não são efectuadas diretamente no Lightning Network. As interações entre a rede **LN** e o **Spark** realizam-se através de **trocas atómicas**.



Por exemplo, Bob deseja pagar uma fatura Lightning usando WoS. Ele transfere seus satoshis, mas em segundo plano, estes são encaminhados para um **Spark Service Provider (SSP)** no Spark, que por sua vez executa o pagamento na rede Lightning.



Por outro lado, o Alice deseja obter fundos diretamente da sua carteira WoS. Neste caso, o **SSP** recebe o sats através do LN e credita imediatamente a carteira do Alice.



Assim, é importante notar que, para beneficiar da simplicidade e fluidez do WoS, é necessário depender dos servidores do Spark. No entanto, em termos de segurança, se uma SSP se tornar maliciosa ou indisponível, dispõe do mecanismo de **saída unilateral**, uma medida de segurança que lhe permite recuperar os seus fundos no Bitcoin on-chain (mesmo que isso possa ser lento e dispendioso), garantindo uma experiência de auto-custódia comparável à de um nó Lightning privado.



Tendo em conta todos estes parâmetros, pode então decidir a quantidade de sats que pretende manter na sua autocustódia WoS.



Se é novo no Wallet of Satoshi, terá naturalmente de descarregar a aplicação móvel wallet. No entanto, se já estiver a utilizá-la e quiser saber como utilizar o **modo de auto-custódia**, vá diretamente para a secção **Configuração do modo de auto-custódia** deste tutorial.



## Começar a utilizar o Wallet of Satoshi



Aceda à sua loja de aplicações e descarregue o WoS.



![screen](assets/fr/03.webp)



Abra a aplicação quando a transferência estiver concluída e prima **Iniciar**.



![screen](assets/fr/04.webp)



Será redireccionado para a interface principal da aplicação. De facto, quando acede ao WoS pela primeira vez, a carteira já está funcional e abre sistematicamente em modo de custódia por defeito.



![screen](assets/fr/05.webp)



Mesmo que não pretenda utilizar o WoS em modo de custódia, recomendamos que o configure primeiro. Para o fazer, consulte este tutorial.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Passemos à configuração do nosso WoS em auto-custódia.



## Configuração do modo de auto-custódia



Clique no menu de hambúrguer (ícone de 3 barras) no canto superior direito da interface principal.



![screen](assets/fr/06.webp)



Em seguida, no menu que aparece, clicar no submenu **Open Self Custody Wallet**.



![screen](assets/fr/07.webp)



O WoS diz-te imediatamente que *o modo de auto-custódia vem com uma frase de recuperação. Além disso, és o único responsável pela segurança dos teus fundos*.



![screen](assets/fr/08.webp)



Assinalar o botão "**Compreendo**" (1) e, em seguida, premir o botão **Abrir auto-custódia Wallet** (2), que aparece a amarelo vivo.



![screen](assets/fr/09.webp)



### Criar uma carteira de autocustódia



Depois de clicar no botão **Abrir Wallet de autocuidado**, clique no botão **Criar um novo Wallet**.



![screen](assets/fr/10.webp)



O WoS criará então uma carteira de autocustódia para si, novamente dentro da mesma aplicação. Poderá alternar entre o modo **custodial** (disponível em determinadas regiões) e o modo **autocustodial** quando lhe for conveniente e em qualquer altura.



![screen](assets/fr/11.webp)



Uma vez criado, será redireccionado para a interface principal do WoS self-custody. Verificará que não existem diferenças entre a visão geral e as interfaces de uma carteira de custódia WoS e as de uma carteira de autocustódia WoS.



### Guardar a sua frase mnemónica



Toque no ícone **Keychain + Backup Wallet** situado na parte superior do ecrã, entre o nome Wallet of Satoshi e o menu de hambúrgueres.



![screen](assets/fr/12.webp)



O WoS oferece duas formas diferentes de guardar as suas 12 palavras (frase mnemónica): **backup via Google Drive** e **backup manual**.



Apesar de sugerirmos uma cópia de segurança manual, que é a mais segura, também lhe mostraremos como fazer uma cópia de segurança através do Google Drive.



#### Cópia de segurança através do Google Drive



Clique no botão **Cópia de segurança do Google Drive**.



![screen](assets/fr/13.webp)



Se optar por fazer uma cópia de segurança com o Google Drive, existe um risco elevado de a sua conta Google ser comprometida. Uma pessoa mal-intencionada teria acesso ao ficheiro que contém as suas 12 palavras e poderia, assim, obter acesso ao seu wallet.



Adicionar uma palavra-passe para encriptar o ficheiro que contém as suas 12 palavras é certamente uma boa forma de adicionar uma camada extra de segurança.



Por isso, active o botão **Encriptar com uma palavra-passe** nas opções avançadas.



![screen](assets/fr/14.webp)



Na nova interface que aparece, defina uma palavra-passe forte e confirme-a novamente.



![screen](assets/fr/15.webp)



É importante lembrar que, uma vez escolhida a palavra-passe, não deve esquecê-la nem perder o suporte em que a escreveu. Se a esquecer ou perder, nunca mais poderá aceder às suas 12 palavras e, consequentemente, aos seus fundos.



Depois de escolher a sua palavra-passe, selecione uma conta Google para a cópia de segurança e conceda os acessos exigidos pelo WoS.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Esperar alguns segundos. Bingo! A sua cópia de segurança foi concluída com êxito.



![screen](assets/fr/18.webp)



Tem sempre a opção de efetuar uma cópia de segurança adicional, escolhendo o segundo método de cópia de segurança: a cópia de segurança manual.


#### Cópia de segurança manual



Se optar pelo backup manual, recomendamos vivamente que consulte este tutorial, que explora as melhores práticas para fazer o backup da sua frase mnemónica de forma segura, para que não perca o acesso aos seus bitcoins.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Prima o botão **Cópia de segurança manual**.



![screen](assets/fr/19.webp)



Na interface seguinte, o WoS recorda-lhe algumas precauções de segurança a ter em conta antes de prosseguir com a cópia de segurança manual.



Ativar o botão **Compreendo** e premir o botão **Próximo**.



![screen](assets/fr/20.webp)



Ser-lhe-ão então apresentadas as suas 12 palavras. Guarde-as e, em seguida, clique no botão **Próximo**.



![screen](assets/fr/21.webp)



Nesta nova interface, prima as palavras pela ordem correta.



![screen](assets/fr/22.webp)



Por fim, clique no botão **Próximo**. Parabéns! A sua cópia de segurança está agora concluída.



![screen](assets/fr/23.webp)



## Restauro de carteiras sob auto-custódia



Se pretender recuperar ou restaurar o seu WoS self-custody wallet na sequência de uma mudança de telefone ou por qualquer outro motivo, eis os passos a seguir.



Para abrir a carteira WoS, clique no menu de hambúrgueres no canto superior direito da interface principal.


No menu que aparece, clicar no submenu **Open Self Custody Wallet**.


Na nova interface que aparece, prima o botão **Restaurar Wallet existente**.



![screen](assets/fr/24.webp)



Escolha um método de restauro e avance para o passo seguinte.



![screen](assets/fr/25.webp)



### Restaurar através do Google Drive



1. Prima o botão **Restaurar a partir do Google Drive**.


2. Selecione uma conta Google e deixe que o WoS recupere os dados de recuperação guardados no seu Google Drive.


3. Em seguida, introduza a sua palavra-passe de encriptação (se a tiver definido previamente, é claro) a partir do ficheiro que contém as suas 12 palavras.


4. Aguarde alguns momentos para que o restauro tenha efeito e poderá aceder novamente à sua carteira.



### Restauro manual



1. Prima o botão **Restaurar manualmente**.


2. Em seguida, introduza as 12 palavras da sua frase mnemónica, escrevendo cada palavra à frente do seu número inicial.


3. Aguarde alguns momentos para que o restauro tenha efeito e poderá aceder novamente à sua carteira.




### Transferência de bitcoins entre a custódia do WoS e a auto-custódia do WoS



Quando tiver bitcoins (sats) no seu WoS custody wallet e criar um WoS self-custody wallet, não perderá os seus fundos. Melhor ainda, pode transferi-los para a sua carteira de autocustódia e vice-versa.



Para o fazer :


Pode copiar o seu endereço de autocustódia WoS relâmpago ou uma fatura que tenha criado.



![screen](assets/fr/26.webp)



Abra agora o seu wallet de custódia e prima o botão **Envoyer**.



Em seguida, cole o endereço ou a fatura. Prima **Envoyer** uma segunda vez.



Volte à sua carteira sob custódia e verá que recebeu efetivamente os fundos.



![screen](assets/fr/27.webp)



## Enviar e receber bitcoins



Quanto ao envio e receção de bitcoins em modo de auto-custódia, tal como a visão geral e as interfaces, não são diferentes do envio e receção de bitcoins através de um wallet de custódia WoS.



Consulte o tutorial básico sobre a utilização do Wallet of Satoshi na rede Plan₿.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Agora é possível configurar e operar o Wallet of Satoshi no modo de auto-custódia.



Se achou este tutorial útil, por favor deixe-me um polegar verde abaixo. Muito obrigado!