---
name: Wallet de Satoshi
description: O Wallet de custódia mais simples para começar
---
![cover](assets/cover.webp)

_Este tutorial foi escrito por_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Transferência, configuração e utilização do Wallet do Satoshi


O Wallet do Satoshi é um Lightning Network Wallet, de custódia, e muito simples de utilizar.

Para efeitos do curso [BTC105 - Finding Now] (https://planb.network/it/courses/trovarsi-ora-d1370810-63f6-4aba-b822-e3a66bf225a5), é utilizado para os cupões Redeem Lightning Network.


**Lembrem-se sempre**: _não as vossas chaves, não as vossas moedas_


As carteiras de custódia não permitem aos utilizadores um controlo total sobre os seus fundos. Normalmente não são recomendadas, exceto para principiantes. A WoS deve ser usada como um Wallet de transição ou para guardar dinheiro de bolso, não para acumulação de fundos a longo prazo.


---

O Wallet do Satoshi (WoS) é um produto de custódia, mas tem uma certa reputação. Podemos razoavelmente recorrer a uma ferramenta como o WoS, por exemplo, para aumentar a nossa capacidade de receber liquidez. Delegamos temporariamente ao WoS o "trabalho sujo" de gerir a liquidez dos canais por nós. Quando se atinge um determinado montante, esvaziamos o On-Chain do WoS para o nosso Wallet sem custódia.


**WARNING⚠️: Recomenda-se que leia o tutorial na sua totalidade antes de prosseguir**


### Descarregamento do Wallet do Satoshi


Vai à Play Store e descarrega o WoS


![image](assets/it/01.webp)


**Nota:** O WoS só pode ser descarregado de lojas oficiais. Se o sistema operativo do dispositivo estiver programado, antes de abrir o WoS há uma parte de verificação pelo próprio sistema operativo. Após a fase de verificação, selecione _Abrir_.


![image](assets/it/02.webp)


O Wallet do Satoshi abre-se com o seguinte ecrã, sendo necessário clicar em _Iniciar_


![image](assets/it/03.webp)


### Registar uma conta no WoS


Nesta altura, o Wallet já está operacional, mas para maior segurança, procedemos à configuração de um início de sessão: será necessário para recuperar fundos em caso de mau funcionamento ou perda do dispositivo. Por conseguinte, selecione o menu no canto superior esquerdo.


![image](assets/it/04.webp)


Abre-se toda a janela do menu, na qual deve definir exclusivamente a moeda (o Wallet do Satoshi apresenta, por defeito, o dólar americano como moeda de referência) e a cor do tema (claro/escuro), de acordo com o seu gosto. Não utilizar os outros comandos.


Sendo o WoS uma ferramenta de custódia, não podemos fazer o backup do Wallet com a frase Mnemonic, mas podemos permitir que o WoS recupere os nossos fundos, em caso de perda ou não utilização do dispositivo móvel, clicando em _Login/Register_

Aparece uma janela que nos pede para introduzir um e-mail Address. Pode ser **um e-mail Proton** (recomendado), mas deve ser funcional, pois permitirá recuperar os fundos no Wallet em caso de perda/roubo ou danificação do telemóvel.


![image](assets/it/08.webp)


O Wallet do Satoshi enviou uma mensagem para a caixa de correio eletrónico indicada.


![image](assets/it/09.webp)


Na caixa de correio, encontraremos duas palavras, que temos de introduzir, reescrevendo-as, no espaço fornecido pela aplicação.


- não ativar o tradutor: as palavras são e devem permanecer em inglês**
- reescrever as duas palavras prestando atenção às maiúsculas e minúsculas**


![image](assets/it/10.webp)


Depois de transcrever as duas palavras, clique em _OK_.


![image](assets/it/11.webp)


O resultado deve ser uma imagem que aparece na parte superior, com o símbolo da marca de verificação.


![image](assets/it/12.webp)


na secção de definições, a barra vermelha _Login/Registo_ apresenta agora o e-mail Address do utilizador.


![image](assets/it/13.webp)


### Receber pagamentos


Para receber no WoS, clique em _Receive_ e aparecerá uma série de comandos.


![image](assets/it/14.webp)


Pode receber


- via LN-Address **a**
- através do LN, definindo o Invoice **b**
- on chain (WoS apoia a rede Bitcoin, mas com trocas submarinas pagas) **c**
- através da leitura do código QR de um LNurl-p **d**


![image](assets/it/15.webp)


### Criar um Invoice


Clicar em _Receive_ e escolher o comando com o símbolo Lightning Network.


![image](assets/it/16.webp)


Aparece o menu de criação do Invoice, onde clicamos em _Adicionar montante_ para escrever o montante exato e adicionar uma descrição, neste exemplo, "O meu primeiro Invoice".


![image](assets/it/17.webp)


Com o teclado, definimos o montante.


![image](assets/it/18.webp)


para depois receber o pagamento do Invoice. O pagamento recebido tem o seguinte aspeto:


![image](assets/it/19.webp)


### Recolha no POS


O Wallet do Satoshi tem uma caraterística predefinida, que o torna particularmente adequado para os comerciantes: o POS. Vejamos como activá-lo.


No ecrã principal, selecione o menu no canto superior direito.


![image](assets/it/20.webp)


Em seguida, selecione _Ponto de venda_.


![image](assets/it/21.webp)


Com a última versão do WoS, certifique-se de que seleciona o _Keypad_.


![image](assets/it/22.webp)

e depois digitar o montante no teclado, no exemplo que se segue igual a 10 cêntimos / 118 Sats. Acrescentar uma descrição para a coleção, neste caso "a minha segunda com o POS". Um grande botão Green acende-se e deve ser clicado

![image](assets/it/23.webp)


para generate o Invoice e mostrá-lo - por exemplo - a um cliente.


![image](assets/it/24.webp)


Este pagamento também é cobrado!


![image](assets/it/25.webp)


### Envio de pagamentos


A simplicidade é um ponto forte do ecrã principal do WoS. Para pagar um Invoice, clicar em _Enviar_


![image](assets/it/26.webp)


Na primeira utilização, o WoS pede autorização para aceder à câmara


![image](assets/it/27.webp)


A partir deste momento, a câmara é activada


![image](assets/it/28.webp)


Enquadrando o Invoice, vemos que foi pedido um pagamento de 210 Sats. É também lida uma descrição, se o requerente a tiver definido. Este ecrã é o resumo e também um pedido de confirmação: O WoS "pede autorização" para enviar o pagamento, que é concedida clicando no botão _Enviar_ do Green


![image](assets/it/29.webp)


Quando o pagamento chega ao seu destino, o WoS notifica-o com este ecrã


![image](assets/it/30.webp)


No ecrã principal, clicando em _Histórico_ (logo abaixo do saldo), aparece a lista das transacções


![image](assets/it/31.webp)


#### Recuperar a conta WoS


Agora, vamos ver como instalar o WoS num novo dispositivo; isto também será útil em casos de roubo, perda ou incapacidade de operar o telemóvel no qual o Wallet estava previamente instalado. Uma vez reinstalado, é necessário refazer o procedimento de registo de conta que acabámos de explicar, com uma única variante: no final do pedido de início de sessão com o e-mail previamente definido, o WoS aparecerá assim:


![image](assets/it/33.webp)


Uma mensagem avisa-nos que foi enviado um e-mail com o procedimento para reativar a conta. Deve abrir a sua caixa de correio eletrónico.


**IMPORTANTE**: abra o e-mail a partir de um PC ou, em qualquer caso, de um dispositivo diferente daquele em que está prestes a recuperar a conta WoS. Na caixa de entrada, encontramos uma mensagem que nos mostra um código QR para enquadrar


![image](assets/it/34.webp)


Assim que o código QR for enquadrado, na página principal do WoS aparecerá a conta recuperada, com o saldo e o histórico.