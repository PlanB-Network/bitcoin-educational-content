---
name: BitcoinVoucherBot P2P
description: Como comprar e vender Bitcoin P2P com BitcoinVoucherBot
---

![image](assets/cover.webp)



Ainda ouvimos falar do BitcoinVoucherBot, um bot Telegram criado para comprar Bitcoin sem [KYC](https://planb.academy/resources/glossary/kyc-know-your-customer) via transferência bancária SEPA. Infelizmente, a partir de novembro de 2025, o BitcoinVoucherBot em sua forma centralizada não está mais disponível como um serviço sem KYC.



Neste guia, veremos como funciona a nova implementação que permite aos utilizadores comprar e vender Bitcoin diretamente no novo mercado P2P (Peer-To-Peer), sem KYC. Para contrariar as novas restrições que ameaçam cada vez mais a liberdade e a privacidade digitais, os programadores criaram esta extensão, dando aos utilizadores a possibilidade de comprar e vender Bitcoin com um elevado grau de anonimato através do P2P (Peer-To-Peer). Vamos ver juntos como funciona este novo método de troca.



Para utilizar o serviço, terá de efetuar transferências via Lightning Network. Por isso, certifique-se de que tem um wallet que suporta este protocolo e que lhe permite utilizar um "LNURL" ou um "Lightning Address" para receber e enviar fundos.



Entre as carteiras suportadas, podemos encontrar:





- [Sats.Mobi](https://planb.academy/tutorials/wallet/mobile/satsmobi-ea04e1cd-609a-4ea8-9c61-f9de1fe3a1fb) (Bot Telegram) (Custodial)
- [Wallet Of Satoshi](https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7) (Custodial with swap to Non-Custodial)
- [Breez](https://planb.academy/tutorials/wallet/mobile/breez-46a6867b-c74b-45e7-869c-10a4e0263c06) (Non-custodial)



Ou qualquer wallet que tenha um "Lightning Address" e gere uma fatura Bolt11. As carteiras que geram uma fatura Bolt12 não são atualmente suportadas. Para mais informações, consulte a definição de [Bolt](https://planb.academy/resources/glossary/bolt).



Para este tutorial, dada a sua facilidade de utilização imediata, utilizaremos o Wallet of Satoshi.



**Cuidado**: O Wallet of Satoshi, embora popular entre os principiantes, é custodial, com controlo limitado sobre os fundos; utilize-o apenas transitoriamente, transferindo-o imediatamente para um não-custodial para obter total soberania. A partir de outubro de 2025, inclui um modo autocustodial estável em todo o mundo no iOS/Android (atualize a aplicação), com chaves privadas autónomas, alternância entre modos, endereços Lightning personalizados e backup de 12 palavras seed. No entanto, continua a ser uma solução provisória até à consolidação, preferindo a maturidade sem custódia do wallet para a gestão a longo prazo.



Muito bem! Agora podemos começar a nossa viagem, que o guiará passo a passo na criação da sua conta, na gestão das correspondências de compras e vendas e na utilização da sua área restrita.



## Wallet e inscrição



Em primeiro lugar, se ainda não o tiver instalado no seu smartphone, descarregue o Wallet of Satoshi.





- [Google Play] (https://play.google.com/store/apps/details?id=com.livingroomofsatoshi.wallet&pli=1)
- [App Store](https://apps.apple.com/au/app/wallet-of-satoshi/id1438599608)



![image](assets/it/01.webp)



Se nunca utilizou o Wallet of Satoshi e quer perceber como funciona, sugiro que siga este tutorial para que possa activá-lo corretamente e fazer uma cópia de segurança.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Agora que o teu wallet está pronto, podes começar a enviar uma pequena quantidade de sats. Não se esqueça que, para completar a inscrição na plataforma P2P (Peer-To-Peer), terá de enviar 1000 sats como medida de controlo: isto é para criar uma barreira contra qualquer ataque do tipo phantom match (scam), evitando que alguém se inscreva sem qualquer filtro de spam.



![image](assets/it/02.webp)



Podemos agora abrir a plataforma P2P (Peer-To-Peer) para proceder ao registo. Pode iniciar sessão a partir de computadores de secretária ou navegadores em smartphones, através do Telegram BitcoinVoucherBot ou através de ligações .onion para proporcionar um nível de privacidade ainda maior.



se optar por utilizar o link Tor .onion, recomendo também o "Tor Browser". Se ainda não o conhece, pode aprender mais sobre ele neste link:



https://planb.academy/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb

Agora escolha como quer chegar à plataforma.





- [BitcoinVoucherBot](https://t.me/BitcoinVoucherBot?start=55360009) (Telegram)
- [Pc Desktop / Browser Smartphone](https://p2p.bitcoinvoucher.bot/?ref=55360009)
- [Tor .Onion](http://umembxtpokml6fkogemcfnpyt3qqvyw6u3hnvwinevo3gvoe6j7vfyad.onion/?ref=55360009)



Será redireccionado para a página principal.



prima "Get Starter" para começar de imediato



![image](assets/it/03.webp)



No ecrã seguinte, tem de escolher uma palavra-passe e introduzi-la (caixa A), e depois repeti-la (caixa B). Recomendo que guarde imediatamente esta palavra-passe num suporte de segurança, que pode ser um dispositivo digital seguro como o "Bitwarden":



https://planb.academy/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

ou guarde a sua palavra-passe num suporte de papel (**aviso**: esta não é uma boa solução, mas não faz mal se for uma solução temporária).



Marque a caixa de verificação onde declara que não é um robô (caixa C). Nota Não active a encriptação RSA a menos que saiba exatamente o que é e como funciona. Não é necessário fazer nada nesta fase. Clique em "Generate Avatar" ("Gerar Avatar") (caixa D).



![image](assets/it/04.webp)



Agora tem de pagar os 1000 sats para concluir a inscrição.



1. Começando pelo topo, vê primeiro o teu "Avatar ID", gerado aleatoriamente e extremamente importante Guarda-o cuidadosamente, tal como te aconselhei a fazer com a palavra-passe.


2. De seguida, deve introduzir o seu "Lightning Address" no campo abaixo. Isto permitir-lhe-á receber pagamentos se comprar Bitcoin, ou obter reembolsos. Se estiver a utilizar o Wallet ou o Satoshi, poderá copiar o seu Address clicando em receber.


3. Assinale a caixa de verificação onde declara que não é um robô.


4. Efectue o pagamento de 1000 sats para ter acesso à sua área restrita. Se não conseguir enquadrá-lo, clique nele com o rato (no PC) ou toque nele com o dedo (no browser/smartphones Telegram) para copiar o endereço que deve colar no Wallet of Satoshi e completar o pagamento da fatura.



![image](assets/it/05.webp)



Este é o vosso LNURL Address.



![image](assets/it/06.webp)



Parabéns!!! Criou o seu Avatar permanentemente e pode ver o resumo aqui. Mais uma vez, recomendo que guarde cuidadosamente o seu Avatar e a sua palavra-passe, como já sugeri anteriormente.



Clique em `I've saved my credentials, continue` (traduzido como: "Guardei as minhas credenciais, continue")



![image](assets/it/07.webp)



Encontra-se agora no centro da plataforma, onde pode ver todas as correspondências comerciais com os respectivos detalhes. Para uma visão mais clara, em baixo pode ver as imagens inerentes ao sítio Web a partir de computadores de secretária.





- "Tipo" ("Type") define se se trata de uma venda "Sell" ("vender") ou de uma compra "buy" ("comprar")
- "Amount" ("Montante"): indica quantos sats o utilizador está a vender, se a correspondência for do tipo "Sell", ou quantos Bitcoin o utilizador está disposto a comprar, se a correspondência for do tipo "Buy".
- "BTC Price with Margin" ("Preço BTC com margem"): mostra o preço tendo em conta a margem aplicada acima do valor marcado.
- "Margem" ("Margin") é a percentagem que é aplicada ao preço de mercado, Com um sinal de menos (-) obtém-se um desconto sobre o preço de mercado, Com um sinal de mais (+) aplica-se um prémio ao preço de mercado.
- o "Método" ("Método") indica o método de pagamento preferido pelo utilizador.
- "Criador" é o avatar único utilizado pelo utilizador na plataforma.
- "Rep" (Reputação) O nível de reputação do utilizador varia entre -5 pouco fiável e +5 extremamente fiável.
- "Status" ("Estado"): indica o estado da correspondência. Na imagem de ecrã de exemplo, todas as correspondências parecem estar "Open" ("Abertas").
- "Expiração" ("Expiration"): mostra quanto tempo falta para o jogo expirar e ser cancelado se não tiver sido escolhido por ninguém.



![image](assets/it/08.webp)



No canto superior direito, clique no seu Avatar para aceder ao seu perfil.



![image](assets/it/09.webp)



Aqui pode ver o nome do seu Avatar, ID de utilizador, data de criação e reputação, que se reflectirá positiva ou negativamente no seu comportamento nas negociações.



![image](assets/it/10.webp)



Na secção Definições, pode ver o seu "Lightning Address", introduzido durante o registo, e alterá-lo, se necessário. Também tem a opção de criar uma chave pública, que, como mencionado, só deve ser configurada se tiver as competências adequadas. Esta chave é utilizada para encriptar as mensagens que trocará com o seu interlocutor diretamente a partir do seu computador.



A funcionalidade de Notificação do Telegram é altamente recomendada. Ao activá-la, aparecerá um código QR para enquadrar na aplicação Telegram: desta forma, receberá notificações em tempo real sobre todas as acções relacionadas com os seus jogos, diretamente no chat do bot no Telegram.



![image](assets/it/11.webp)



Por fim, encontra a sua secção de referência, com os ganhos gerados pelos utilizadores que convidou. A partir daqui, pode utilizar o botão para partilhar a sua ligação ou código QR e, um pouco mais abaixo, ver uma lista de correspondências para acompanhar a sua reputação e a pontuação correspondente.



![image](assets/it/12.webp)



## Criar uma encomenda para Comprar Bitcoin



Entrar no Mercado: a partir da barra de navegação principal, clicar no símbolo do carrinho "Mercado" ("Mercado") para abrir o livro de encomendas. Em seguida, iniciar uma nova encomenda: premir o botão "Nova encomenda" ("Nova encomenda") para iniciar o processo.



![image](assets/it/13.webp)





- Definir detalhes da encomenda:
- Selecionar a opção "Comprar Bitcoin" ("Buy Bitcoin").
- Introduza a quantidade de sats que pretende.
- Definir a margem de preço (entre -20% e +20% do valor de mercado).
- Escolha o método de pagamento (Instantâneo SEPA, etc.).
- Indica a moeda preferida.
- Confirmar a encomenda: clicar em "Criar encomenda" ("Confirmar encomenda") para passar à fase de depósito.



![image](assets/it/14.webp)



Depósito exigido: é necessário um depósito igual a 10% do montante total, acrescido de uma taxa de serviço, para ativar a encomenda.




- Pagamento por depósito: quando a encomenda é criada, o sistema gera automaticamente uma fatura Lightning. O depósito é apenas temporário e é reembolsado quando a encomenda é concluída.
- Caraterísticas principais:
- Caução: 10% do valor da encomenda.
- Taxa de serviço: custo de utilização da plataforma.
- Limite de tempo: dispõe de 5 minutos para efetuar o pagamento, caso contrário a transação expira.



![image](assets/it/15.webp)



Após o pagamento bem sucedido, a ordem aparecerá no livro e será visível para todos os utilizadores, que a podem escolher e aceitar. Para criar uma ordem de venda, basta clicar em "Sell Bitcoin" ("Vender Bitcoin"), introduzir a quantidade de satoshi que pretende vender, definir a margem, selecionar o método de pagamento e a moeda e, em seguida, proceder ao depósito de 10% como caução. Uma vez concluída, a sua correspondência será visível na lista.



![image](assets/it/16.webp)



## Como aceitar uma encomenda



1. Os vendedores podem ver uma lista de todas as encomendas disponíveis no livro.


2. Verificar os pormenores: cada encomenda apresenta informações como:




  - Quantidade de Bitcoin,
  - Margem sobre o preço,
  - Forma de pagamento,
  - Reputação do utilizador.



![image](assets/it/17.webp)



3. Clique na encomenda para abrir a ficha completa com todas as informações.


4. Premir "Sell Bitcoin" ("Vender Bitcoin") para aceitar a proposta.



![image](assets/it/18.webp)



## Depósito exigido pelo vendedor



Quando a encomenda é aceite, o sistema gera uma fatura para pagamento. O depósito inclui:



- O montante total da encomenda,



- a comissão de serviço.



O pagamento do depósito deve ser efectuado dentro do prazo estipulado, caso contrário a transação não será confirmada.



![image](assets/it/19.webp)



## Envio de instruções de pagamento



Depois de efectuado o depósito, a transação aparecerá no painel de controlo pessoal do vendedor, que deverá fornecer os dados ao comprador para concluir o pagamento em moeda fiduciária.



1. O vendedor apresenta a transação ativa no seu painel.


2. Clique em "Apresentar instruções de pagamento"


3. Introduzir todas as informações necessárias para o pagamento fiduciário (IBAN, destinatário, endereço, motivo do pagamento, etc.).


4. Clicar em "Enviar mensagem" ("Send Message") para transmitir os dados ao comprador.



![image](assets/it/20.webp)



## Procedimento de pagamento



O comprador recebe, no chat da plataforma, uma mensagem com todos os dados necessários para efetuar o pagamento em moeda fiduciária:




- Dados bancários: IBAN com nome e endereço do titular da conta do vendedor.
- Montante exato: montante fiduciário exato a transferir.
- Causal/descrição: texto a incluir na transação.
- Prazo: data-limite para efetuar o pagamento.



A transferência é efectuada fora do sistema P2P e deve ser feita através da instituição bancária.



⚠️ **Nota importante:** a confirmação na plataforma só deve ser feita depois de ter efectuado a transferência ou o pagamento em moeda fiduciária através do seu banco.



![image](assets/it/21.webp)



## Confirmação do pagamento fiduciário



Este passo é crucial para o comprador e só deve ser efectuado depois de verificar se o pagamento foi efetivamente enviado.



1. Dados de receção: o comprador recebeu as instruções de pagamento do vendedor.


2. Execução do pagamento: a transferência fiduciária é efectuada a partir da conta bancária.


3. Verificação: verificar se a operação foi processada corretamente.


4. Confirmar na plataforma: clicar em "Confirmar pagamento fiduciário" ("Confirm fiat payment") na página de negociação.


O botão "Confirmar pagamento fiat" aparece na secção da transação e só deve ser utilizado depois de se verificar que o pagamento foi efetivamente enviado.



![image](assets/it/22.webp)



A última etapa do processo consiste em o vendedor confirmar a receção do pagamento em moeda fiduciária, após o que as satss são libertadas para o comprador.



![image](assets/it/23.webp)



## Conclusão



Na esperança de que este tutorial o ajude a utilizar um novo método para transacionar Bitcoins ou mesmo apenas comprá-los, seja para a sua própria reserva de valor ou para começar a dar vida aos pagamentos diários. Ainda assim, continua a ser uma porta a explorar para fazer face ao que está prestes a acontecer no nosso mundo digital.



O laço dos organismos que nos controlam está a apertar-se, para dar origem a uma Internet cada vez mais controlada. Ao comprar o P2P, manterá as suas compras em total anonimato, sem deixar rasto e sem repercussões de terceiros.