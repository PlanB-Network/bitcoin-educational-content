---
name: passphrase BIP39 Trezor
description: Como é que adiciono um passphrase à minha carteira Trezor?
---
![cover](assets/cover.webp)



Um passphrase BIP39 é uma palavra-passe opcional que, combinada com a frase Mnemonic, fornece um Layer adicional de segurança para carteiras Bitcoin determinísticas e hierárquicas. Neste tutorial, vamos descobrir juntos como configurar um passphrase no seu Bitcoin Wallet seguro num Trezor (Safe 3, Safe 5 e Model One).



![Image](assets/fr/01.webp)



Antes de começares este tutorial, se não estás familiarizado com o conceito de passphrase, como funciona e as suas implicações para o teu Bitcoin Wallet, recomendo-te vivamente que consultes este outro artigo teórico onde explico tudo (isto é muito importante, pois usar um passphrase sem perceber bem como funciona pode colocar as tuas bitcoins em risco) :



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

O passphrase no Trezor é tratado da forma clássica se tiver optado pela norma BIP39 durante a configuração (o que eu recomendo se não precisar de *Multi-share Backup*). A particularidade do Trezor é que pode introduzir o passphrase diretamente no Hardware Wallet ou através do teclado do seu computador utilizando o software Trezor Suite. Esta segunda opção é consideravelmente menos segura, uma vez que o computador tem uma superfície de ataque imensamente maior do que o Hardware Wallet. No entanto, a digitação de um passphrase complexo pode ser mais rápida num teclado convencional do que no Hardware Wallet, o que pode encorajar a utilização de palavras-passe fortes. Portanto, é sempre melhor usar um passphrase, mesmo que tenha que ser digitado, do que não usar nenhum. É importante, no entanto, estar ciente do aumento do risco de ataques numéricos que isso implica.



Estas opções não estão disponíveis em todos os softwares de gestão de carteiras compatíveis com o Trezor. Por exemplo, para o Model One, o passphrase pode ser introduzido através do teclado no Sparrow Wallet. Para os modelos Model T, Safe 3 e Safe 5, é necessário utilizar o Trezor Suite ou introduzir o passphrase diretamente no Hardware Wallet, uma vez que a opção de introdução através do Sparrow foi desactivada pela HWI há alguns anos.



![Image](assets/fr/02.webp)



No Trezor Suite, existem duas formas diferentes de gerir a procura do passphrase. Pode ativar a opção "*passphrase*" no separador "*Device*". Se estiver activada, o Trezor Suite e todos os outros softwares de gestão de carteiras pedem-lhe sistematicamente que introduza o seu passphrase sempre que o inicia. Se preferir uma abordagem mais discreta à utilização de um passphrase, pode manter a definição em "*Standard*". Neste caso, terá de aceder manualmente ao menu do seu Hardware Wallet no canto superior esquerdo e clicar no botão "*+ passphrase*" sempre que o iniciar.



Antes de iniciar este tutorial, certifique-se de que já inicializou o seu Trezor e gerou a sua frase Mnemonic. Se não o fez e o seu Trezor é novo, siga o tutorial específico do modelo disponível no Plan ₿ Network. Quando tiver concluído este passo, pode voltar a este tutorial.



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## Adicionar um passphrase a um Safe 3 ou Safe 5



Depois de ter criado o seu Wallet, guardado o seu Mnemonic e definido um PIN, será levado para o menu inicial do Trezor Suite. No canto superior esquerdo, deve aparecer uma janela que o convida a ativar o passphrase BIP39.



![Image](assets/fr/03.webp)



Se esta janela não for apresentada, terá de ativar manualmente a opção "*passphrase*" no separador de definições "*Dispositivo*".



![Image](assets/fr/04.webp)



Esta janela pede-lhe para introduzir o seu passphrase. Escolha um passphrase forte e faça imediatamente uma cópia de segurança física, num suporte como papel ou metal. Neste exemplo, eu escolhi o passphrase: `fH3&kL@9mP#2sD5qR!82`. Este é um exemplo; no entanto, recomendo que escolha um passphrase um pouco mais longo. Entre 30 e 40 caracteres seria o ideal (como uma boa palavra-passe).



é claro que nunca deve partilhar o seu passphrase na Internet, como eu faço neste tutorial. Este exemplo de Wallet só será utilizado no Testnet e será apagado no final do tutorial



Para recomendações mais específicas sobre a escolha do seu passphrase, convido-o mais uma vez a consultar este outro artigo:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Se pretender introduzir o seu passphrase através do teclado do seu computador, introduza-o no campo fornecido e, em seguida, clique em "*Acessar passphrase Wallet*".



![Image](assets/fr/05.webp)



O Hardware Wallet apresentará então o passphrase. Certifique-se de que corresponde à sua cópia de segurança física (papel ou metal) antes de clicar no ecrã para continuar.



![Image](assets/fr/06.webp)



Isto dar-lhe-á acesso à sua carteira protegida pelo passphrase.



![Image](assets/fr/07.webp)



Se preferir aumentar a segurança introduzindo o seu passphrase apenas no seu Trezor, quando lhe for pedido, clique em "*Enter passphrase on Trezor*".



![Image](assets/fr/08.webp)



Aparecerá um teclado T9 no seu Trezor, permitindo-lhe introduzir o seu passphrase. Uma vez terminada a introdução, clique no visto Green para aplicar o passphrase ao seu Wallet.



![Image](assets/fr/09.webp)



Terá então acesso ao seu passphrase seguro Wallet.



![Image](assets/fr/10.webp)



Para utilizar o Sparrow Wallet, o procedimento é semelhante, mas para os modelos T, Safe 3 e Safe 5, o passphrase deve ser introduzido no Hardware Wallet e não através do teclado do computador.



Sempre que o Sparrow Wallet requerer acesso ao seu Trezor e o passphrase ainda não tiver sido aplicado desde o último arranque, terá de o introduzir utilizando o teclado T9.



![Image](assets/fr/11.webp)



## Adicionar um passphrase a um Model One



No Model One, a utilização de um passphrase BIP39 é quase indispensável. Como este dispositivo não incorpora um elemento seguro, é relativamente fácil extrair informações sensíveis. Por conseguinte, não é resistente a ataques físicos. No entanto, como o passphrase não é retido no dispositivo depois de este ter sido desligado, a utilização de um passphrase forte (não-brutável) pode protegê-lo contra a maioria dos ataques físicos conhecidos neste modelo.



No Model One, não é possível introduzir o passphrase diretamente no Hardware Wallet. Terá de o introduzir através do teclado do seu computador.



Depois de ter criado o seu Wallet, guardado o seu Mnemonic e definido um PIN, será levado para o menu inicial do Trezor Suite. No canto superior esquerdo, deve aparecer uma janela que o convida a ativar o passphrase BIP39.



![Image](assets/fr/12.webp)



Se esta janela não for apresentada, é necessário ativar a opção "*passphrase*" no separador "*Device*" das definições.



![Image](assets/fr/13.webp)



Esta janela pede-lhe para introduzir o seu passphrase. Escolha um passphrase forte e faça imediatamente uma cópia de segurança física, num suporte como papel ou metal. Neste exemplo, eu escolhi o passphrase: `fH3&kL@9mP#2sD5qR!82`. Este é apenas um exemplo; no entanto, recomendo que escolha um passphrase um pouco mais longo. Entre 30 e 40 caracteres seria o ideal (como uma boa palavra-passe).



Para recomendações mais específicas sobre a escolha do seu passphrase, convido-o mais uma vez a consultar este outro artigo:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Introduza o seu passphrase no campo fornecido e, em seguida, clique no botão "*Accessar passphrase Wallet*".



![Image](assets/fr/14.webp)



O seu Hardware Wallet apresentará o seu passphrase. Certifique-se de que corresponde à sua cópia de segurança física (papel ou metal) e, em seguida, clique no botão do lado direito para continuar.



![Image](assets/fr/15.webp)



Isto levá-lo-á à sua carteira protegida pelo passphrase.



![Image](assets/fr/16.webp)



Para usar o Sparrow Wallet depois disso, o procedimento permanece o mesmo. Sempre que o Sparrow requerer acesso ao seu Hardware Wallet, e o passphrase não tiver sido introduzido desde que o dispositivo foi iniciado pela última vez, terá de o introduzir.



![Image](assets/fr/17.webp)



Parabéns, agora está a par da utilização do passphrase BIP39 nas carteiras de hardware Trezor. Se quiser levar a sua segurança Wallet um passo mais além, veja este tutorial sobre os sistemas de backup *Multi-share* da Trezor (*Shamir's Secret Sharing Scheme*):



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

Se achou este tutorial útil, agradecia que deixasse um polegar Green abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Muito obrigado!