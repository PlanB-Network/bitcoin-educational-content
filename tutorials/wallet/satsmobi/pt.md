---
name: Sats.mobi

description: Um Wallet de custódia acessível por telegrama
---

![cover](assets/cover.webp)


_Este tutorial foi escrito por_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)


## Sats.Mobi

O SatsMobi é um Wallet que opera no Telegram, apresentando todas as funcionalidades de um Lightning Network (custodial) Wallet, além de uma série de recursos muito divertidos. Originou-se de um Fork do extinto LightningTipBot, herdando todas as suas funcionalidades e acrescentando outras mais actuais, tornando-o assim mais moderno. Tal como o LNTipBot, o Sats.Mobi também adopta a filosofia open-source. O Wallet pode ser configurado e gerido de forma independente, clonando-o a partir deste [repositório](https://github.com/massmux/SatsMobiBot).


Se preferir utilizá-lo de forma simples, iniciar uma conversa no Telegram revelará que se trata de um bot.


## Definições

Na barra de pesquisa do Telegram, procure por "satsmobi" e aparecerá o link para o [bot] (@SatsMobiBot).


**Atenção**: Se não tiver a certeza de pesquisar através do Telegram, aceda ao bot de forma segura utilizando o seguinte [link](https://t.me/SatsMobiBot)


![image](assets/it/01.webp)


Tudo o que precisa de fazer para começar é premir _START_


![image](assets/it/02.webp)


Para explorar o Wallet, pode selecionar _Menu_ no canto inferior esquerdo.


![image](assets/it/03.webp)


Agora opta por _/help_ entre os comandos principais.


![image](assets/it/04.webp)


O Sats.Mobi dá-nos as boas-vindas mostrando uma mensagem, listando todas as principais funcionalidades. Ao iniciar, o bot criou também um LN Address, ligado ao identificador escolhido no Telegram (que é único por defeito). Os comandos para envio e recebimento de Sats com esse Wallet são visíveis, assim como outras funções que veremos mais adiante. É interessante ver também o menu _/avançado_


![image](assets/it/05.webp)


É de notar que o Sats.Mobi também criou um LN Address anónimo, para ser usado para ganhar privacidade. O bot funciona com comandos: basta clicar na palavra correspondente ou escrever a barra "/" na barra de mensagens, seguida do comando que se pretende executar. Mesmo que o Wallet tenha acabado de ser criado, escolha, por exemplo, _/transactions_


![image](assets/it/06.webp)


Este comando mostra a lista das últimas transacções, neste caso particular igual a zero.


![image](assets/it/07.webp)


## Receber Sats

O comando para criar um Invoice e receber Sats é _/factura_. O Sats.Mobi funciona exclusivamente em Satoshi, a unidade mais pequena do Bitcoin; por isso, para criar o Invoice, é necessário escrever o montante em Sats na barra de mensagens e depois enviá-lo no chat com o bot.

![image](assets/it/08.webp)


No exemplo seguinte, optou-se por receber um montante de 210 Sats.


![cover](assets/it/09.webp)


Após alguns instantes de espera pela preparação do Invoice, este está disponível sob a forma de texto e de código QR. Ao pagar o Invoice, o Wallet apresenta o saldo. Se, por qualquer razão, o total não for atualizado, escreva _/saldo_ e prima a tecla `enter`.


![image](assets/it/10.webp)


## Envio de Sats


Embora os Sats sejam um bem extremamente valioso, do qual não se deve separar de ânimo leve, o Sats.Mobi torna esta parte apelativa, a realização de alguns testes breves (ou seja, algumas transacções experimentais) não será um problema.


### Pagamento de um Invoice


A maneira mais simples de pagar um Invoice é copiar a string de mensagem `lnbc1xxxxx` e colá-la na barra de mensagens depois de digitar o comando _/pay_. **A sintaxe correta** requer que se deixe um espaço após o comando.


![image](assets/it/11.webp)


O Wallet envia uma mensagem a pedir confirmação. Ao clicar em _Pay_, o Invoice é pago.


![image](assets/it/12.webp)


O Sats.Mobi pode contar com um nó Lightning eficiente e bem ligado, raramente os pagamentos falham porque consegue sempre encontrar o encaminhamento correto.


### Pagar confortavelmente a partir do telemóvel


Navegando no Telegram, o Sats.Mobi também está disponível no telemóvel. A função mais conveniente para pagar com o telemóvel é a digitalização de um código QR, mas este Wallet não a possui por conceção, uma vez que não é uma aplicação autónoma, mas está contida numa rede social. Por conseguinte, o Sats.Mobi foi programado para facilitar ao máximo a experiência móvel: pode efetivamente descodificar uma imagem, como uma fotografia tirada do código QR do Invoice que pretende pagar.


Suponhamos, por exemplo, que quer pagar um Invoice de 50 Sats.


![image](assets/it/20.webp)


Quando isto nos é mostrado, podemos tirar uma fotografia do código QR correspondente.


![image](assets/it/21.webp)


Em seguida, abrimos o Telegram no telemóvel e, na conversa com o Sats.Mobi, anexamos a fotografia que acabámos de tirar do código QR


![cover](assets/it/22.webp)


Uma vez selecionado, enviamo-lo para o bot:


![image](assets/it/23.webp)

O Sats.Mobi descodifica a fotografia e **apresenta imediatamente o pedido de pagamento**, com a descrição correta. O chat pede confirmação, para prosseguir é necessário premir _/pay_

![image](assets/it/24.webp)


Aguarde um momento para que o pagamento seja processado.


![image](assets/it/25.webp)


O Invoice para 50 Sats foi pago, um resultado alcançado sem a utilização de uma câmara e a sua função de digitalização integrada.


### Sats.Mobi em Grupos de telegramas


![image](assets/it/27.webp)


Entre as caraterísticas que tornaram o LNTipBot famoso e que o Sats.Mobi traz para o Telegram, está a que torna a experiência divertida e interactiva para os membros de um grupo.

Os proprietários podem convidar o bot para se juntar ao chat do grupo e depois nomear o Sats.Mobi como administrador. A partir desse momento, a diversão começa, porque os membros podem começar a recompensar outros utilizadores pela sua contribuição para o grupo.


- _/tip_ adiciona uma dica ao responder a uma mensagem;
- _/send_ envia fundos especificando um LN Address ou um identificador de Telegrama como destinatário;
- _/faucet_ (no menu _/avançado_) permite criar uma série de dicas que os membros mais rápidos do grupo podem recolher clicando em _/colher_;
- _/tipjar_ (no menu _/avançado_) cria outro tipo de distribuição que pode ser enviado aos utilizadores do grupo.


Cada um destes comandos tem a sua sintaxe, que é explicada no menu principal de comandos.


E se não formos o proprietário de um grupo? Não há problema: basta pedir ao fundador para convidar o Sats.Mobi, adicioná-lo como administrador do grupo e está tudo pronto!


## Ponto de venda (POS)


Quando o Sats.Mobi é lançado pela primeira vez, o bot também cria outra funcionalidade para o utilizador: **o POS**. O "dispositivo" é ativado pelo utilizador com o comando _/pos_ ou clicando no botão relacionado da consola no canto inferior direito. Na verdade, o POS é uma aplicação web, que se abre como um pop-up no chat do Telegram


![image](assets/it/14.webp)


O Interface apresenta o identificador pessoal do Telegram do utilizador no canto superior esquerdo e é utilizado simplesmente como todos os POS: escrevendo o montante no teclado. Suponhamos que agora queremos cobrar 21 cêntimos de euro por um serviço. Sabendo que o Sats.Mobi apenas gere nativamente o Sats, não é fácil fazer a conversão na sua cabeça. Pelo contrário, o POS apresenta o euro como a unidade de conta, mostrando ao mesmo tempo o equivalente em Satoshi.


![image](assets/it/15.webp)

Ao clicar em _/OK_, é apresentado o Invoice que pode ser mostrado ao cliente através de um código QR ou que pode ser enviado como uma cadeia de caracteres através de mensagens instantâneas, para que possa ser pago.

![image](assets/it/16.webp)

![image](assets/it/17.webp)


Naturalmente, o POS também está disponível nos telemóveis, aos quais se acede da mesma forma que anteriormente.


![image](assets/it/18.webp)


Também é bem visualizado no ecrã do telemóvel:


![image](assets/it/19.webp)


## Caraterísticas adicionais


Há outras caraterísticas que completam a oferta do Sats.Mobi Wallet, que, como vimos, alarga o conceito de Wallet para além das operações de receção e envio de pagamentos:


- _/nostr_: para ligar o Wallet ao seu próprio utilizador Nostr para receber zaps;
- _/cashback_: mostra um código que pode ser apresentado a um comerciante para obter cashback numa compra;
- _/buy_: inicia um procedimento guiado dentro do bot, que permite comprar Sats por euros;
- _/activatecard_: para solicitar a ativação de um cartão de débito NFC, recarregável através do Sats.Mobi Wallet e para o qual podem ser activadas notificações;
- _/link_: cria um link para o seu próprio Zeus ou Blue Wallet, que pode ser utilizado como controlo remoto para este Wallet.


## Conclusão

O Sats.Mobi é um Wallet agradável e divertido de usar, que traz de volta as experiências vividas com o LNTipBot usando as funções mais avançadas do LNBits. No entanto, é importante lembrar que **é um serviço de custódia**. Por conseguinte, deve ser utilizado para guardar muito poucos Sats, não é um Wallet principal para os seus fundos Lightning Network. Existe também um limite de capacidade intrínseca, igual a 500 000 Sats, um limite que se aconselha a não ultrapassar.


Se estiver à procura de carteiras Lightning Network sem custódia, é definitivamente aconselhável procurar outros produtos.


---
### Documentação


- [Github](https://github.com/massmux/SatsMobiBot)
- Lista de reprodução de [vídeos](https://www.youtube.com/results?search_query=Sats.mobi) demo