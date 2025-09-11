---
name: BitcoinVoucherBot
description: Um bot do Telegram para comprar Bitcoin em confidencialidade
---
![image](assets/cover.webp)

_Este tutorial foi escrito por_ [Bitcoin Campus](https://linktr.ee/bitcoincampus_)

## Introdução

O BitcoinVoucherBot é uma ferramenta com a qual os Bitcoins podem ser comprados em Exchange por euros.

### Luz KYC

A ação de trocar euros por Bitcoin é o primeiro e mais fundamental passo para começar a estudar este tema, mas é aparentemente também o mais difícil e complexo. As opções podem ser muitas: oferecer Bitcoin através de Exchanges centralizadas, encontros temáticos de Bitcoin, amigos, conhecidos, entre outros. Nós juntamo-nos à comunidade Bitcoiner e **recomendamos absolutamente a utilização de Exchanges centralizadas** de forma a salvaguardar uma maior atenção à privacidade de cada um.

Embora esta opção possa ser menos conveniente, é importante compreender que as bolsas aplicam o regulamento "Know Your Cutomer" (KYC), atribuindo assim uma identidade, bem como uma localização física, a cada Satoshi comprado nelas. a "conveniência" tem alguns efeitos secundários surpreendentes.

### Como o fazer?

Aqui está o serviço [BitcoinVoucherBot:](https://t.me/BitcoinVoucherBot), um bot do Telegram que actua como um canal entre as nossas transferências SEPA e as compras Sats.

### Pré-requisitos

Para começar a usar o BitcoinVoucherBot, não há necessidade de divulgar informações pessoais sensíveis para a equipa do Bot. **Não é necessária nenhuma autorização**.

Tudo o que é necessário é uma conta Telegram já ativa e uma conta bancária. **Nota**: Uma conta aberta nos Correios Italianos (para os clientes italianos) ou, de um modo mais geral, referente a um cartão recarregável não é adequada.

No chat do Telegram preparamos uma encomenda, pagamo-la com uma transferência bancária e, finalmente, através do bot, recebemos um vale emitido por uma empresa terceira que não conhece o objeto da compra.

### Ativação do bot e menu

A ativação é uma operação simples e única. A partir do Telegram, procure por _@BitcoinVoucherBot_ e assim que chegar ao chat do Bot, um grande botão _Start/Start_ se destaca na parte inferior. A operação provoca a resposta do Bot, que apresenta um menu com os principais comandos disponíveis. Aparecem também as primeiras mensagens de boas-vindas, para as quais recomendamos uma leitura atenta.

**Atenção**: existem vários golpistas que se fazem passar pelo VoucherBot original. Se não tiver certeza da pesquisa via Telegram, acesse o link do BitcoinVoucherBot a partir do [site oficial](https://www.bitcoinvoucherbot.com/)

![image](assets/it/01.webp)

As opções aparecem clicando no botão _Menu_ no canto inferior esquerdo: pode clicar na palavra correspondente ao comando, ou digitar na caixa de mensagem a barra `/` seguida do comando digitado.

![image](assets/it/02.webp)

As principais operações incluem:


- _/purchase_: é o procedimento de compra propriamente dito. Quando a transação é concluída, o código QR é gerado automaticamente pelo bot, pronto para ser resgatado.
- _/refill_: disponível no momento da redação deste tutorial, mas não a abordaremos porque - por razões técnicas - esta opção pode ser removida mais tarde.
- _/swap_: abre o procedimento de troca, disponível com um prático bot do Telegram ou através da Web.
- _/ap_: plano de acumulação, que lhe permite criar um **Plano de acumulação constante (PAC)**.
- _/lnaddress_: com o qual nos pedem para ligar um LN Address próprio, para um procedimento específico que veremos mais tarde.
- _/credits_: para verificar quanto crédito resta para os cupões generate.
- _/myorders_: mostra as encomendas efectuadas com o bot (**Aviso** o sistema só regista as últimas 10 encomendas efectuadas e não todo o histórico).
- _/fees_: um comando para verificar as taxas de rede. Para as avaliar, é sempre melhor confiar no Mempool.space.
- _/support_: em caso de necessidade, abre contactos para comunicar problemas à equipa de apoio.

## Procedimento de compra de Bitcoin

### Preparação do pedido

Clicar em _/comprar_ no menu de comando

![image](assets/it/03.webp)

Aparecem várias oportunidades, mas escolhemos _BTC Vouchers_

![image](assets/it/04.webp)

O BitcoinVoucherBot permite-lhe comprar Bitcoin onchain, Lightning e Liquid.

Nesta fase, escolher _Onchain & Lightning 🔗⚡️_

![image](assets/it/05.webp)

O ecrã muda rapidamente e o VoucherBot propõe denominações de compra. Começam com um mínimo de 100,00 euros e vão até 900,00 euros.

No caso de uma primeira compra, apenas são oferecidas as denominações 100,00 €, Onchain e Lightning. Para aumentar a confidencialidade, sugerimos que escolha _Lightning ⚡️_

![image](assets/it/06.webp)

O VoucherBot avisa-nos que foi feita uma primeira escolha e que, para a confirmar, temos de escolher _Proceed_

![image](assets/it/07.webp)

É agora uma questão de escolher o método de pagamento. A transferência é feita por transferência bancária **(aceite apenas SEPA)**. O VoucherBot propõe como destinatário uma empresa que disponibiliza duas contas bancárias, uma no Reino Unido e outra na Suíça. O banco suíço foi escolhido para efetuar este tutorial

![image](assets/it/08.webp)

Nesta altura, é-nos pedido que introduzamos o nosso IBAN, aquele a partir do qual se iniciará a transferência para o banco escolhido. Estas informações vão compor um puzzle que permitirá ao bot, ou seja, a uma máquina, juntar algumas informações para que o processo de compra flua sem necessidade de intervenção humana.

O IBAN deve ser escrito na barra de mensagens, verificado e enviado para o bot.

![image](assets/it/09.webp)

Aparece agora uma mensagem de controlo na conversa com o VoucherBot.

Se tudo estiver correto, continue clicando em _Proceder_.

![image](assets/it/10.webp)

### Pagamento

Após alguns instantes, necessários para processar os dados, o VoucherBot responde com uma mensagem que contém todos os pormenores necessários para concluir a encomenda. Dependendo do que o seu banco exige, as informações relevantes são:


- o `IBAN`, que é essencial para o depósito, bem como o Address do destinatário;
- o valor escolhido anteriormente através do limite, que deve ser cumprido para que o VoucherBot reconheça a encomenda quando o pagamento for recebido;
- "Motivo do pagamento", que é o motivo do pagamento. **Deve ser copiado e colado sem retirar ou acrescentar nada no campo apropriado da sua transferência. Qualquer "." ou "-" presente no motivo do pagamento pode ser substituído por "espaço em branco "**.
- um `OrderID` único para referir quando solicitar qualquer assistência.

Pode então proceder ao pagamento, através da sua aplicação ou banco. Quando o pagamento tiver sido aceite pelo banco, é importante não esquecer de premir _Notificar pagamento_ no chat com o VoucherBot. Esta simples operação avisa-o de que um pagamento está a caminho.

![image](assets/it/11.webp)

O VoucherBot responde com uma mensagem que contém um aviso muito importante: **não apague o chat**, pelo menos até receber o voucher, porque é o único meio de reconstruir a encomenda e de a manter em funcionamento.

![image](assets/it/12.webp)

---
Atenção:


- só são aceites transferências electrónicas SEPA;
- os tempos de espera estão exclusivamente relacionados com a forma como os bancos (que não funcionam 24 horas por dia, 7 dias por semana, 365 dias por ano, como o Bitcoin) processam o vale. A receção do vale pode demorar entre algumas horas e 3 dias úteis;
- para qualquer necessidade, o Bitcoin VoucherBot tem um excelente serviço de [apoio](https://t.me/BitcoinVoucherGroup) no Telegram.

---
### Resgate

Assim que o pagamento é bem sucedido, o Bitcoin VoucherBot envia o voucher diretamente para o chat. O voucher relâmpago tem a forma de um código QR, impresso num fundo laranja.

![image](assets/it/31.webp)

Existem todos os dados necessários para o levantar:


- o montante em Sats, equivalente ao enviado por transferência eletrónica, excluindo as taxas de serviço e de rede;
- uma identificação de referência do vale;
- a data até à qual o vale deve ser resgatado, sob pena de perda de fundos, ou seja, 25 dias após a emissão.

Pode levantar o vale enquadrando o código QR com a função de leitura de um Wallet Lightning Network compatível, ou através do LNURL, também indicado abaixo do código QR.

Para este tutorial usamos o Wallet Of Satoshi, utilizando a função de leitura ativada pelo botão _Send_.

![image](assets/it/32.webp)

Com a câmara do telemóvel activada, enquadrar o código QR no chat, abrindo o Telegram a partir do PC

![image](assets/it/34.webp)

Antes de prosseguir, o Wallet Of Satoshi exibe uma tela de verificação que inclui o valor, que corresponde exatamente ao indicado no voucher, e como descrição, BitcoinVoucherBot. Para resgatar o voucher, basta clicar em _Receive_.

![image](assets/it/35.webp)

Wallet Of Satoshi processa por alguns instantes.

![image](assets/it/36.webp)

e, finalmente, a coleta é comunicada e fica imediatamente disponível no saldo do Wallet.

**Wallet of Satoshi é um aplicativo custodial: logo após o resgate do voucher é recomendável mover os sats para uma carteira não-custodial.**

![image](assets/it/37.webp)

### Como trocar um vale de desconto onchain

Como vimos na preparação da encomenda, o VoucherBot permite que o Sats seja comprado diretamente na cadeia, com a escolha do voucher com o mesmo nome.

**Nota**: A preparação da encomenda e o pagamento não mudam, são sempre os mesmos. O que muda é a forma como um talão onchain é descontado.

Após completar a encomenda, efetuar o pagamento, premir _Notificar pagamento_ e aguardar o tempo técnico dos bancos para transferir a transferência, o VoucherBot responderá enviando o voucher diretamente para o chat.

Este vale também tem a forma de um código QR, mas a cor principal é o amarelo canário e - o que é mais importante - na descrição está bem explicado que se trata de um vale onchain, que se retira diretamente na sua onchain Wallet e, para iniciar o procedimento de retirada, tem de clicar em _Redeem on Telegram_. O voucher onchain também contém as informações já vistas para o voucher lightning:


- o montante em Sats, equivalente ao enviado por transferência eletrónica, excluindo as taxas de serviço e de rede;
- um código de voucher;
- uma identificação de referência do vale;
- a data até à qual o vale deve ser resgatado, sob pena de perda de fundos, ou seja, 25 dias após a emissão.

![image](assets/it/22.webp)

**WARNING ⚠️:** clicado como explicado, abre-se o pop-up de outro bot: **Voucher RedeemBot.**

O Voucher RedeemBot é a ferramenta disponibilizada para o efeito. Quer seja a primeira utilização ou existam encomendas anteriores, cada vez que é efectuado um novo resgate é sempre necessário clicar em _START_.

![image](assets/it/23.webp)

Nesta altura, o RedeemBot carrega o voucher onchain, facilmente reconhecido pelo Voucher Code e pelo ID de referência. Também desbloqueia a barra para escrever mensagens e começar a conversar com o bot, que de facto nos convida a dizer-lhe um Address onchain do nosso Wallet.

**Nota**: Este Address deve ser do tipo SegWit.

![image](assets/it/24.webp)

Nesta altura, abrimos o nosso Wallet e o generate e o SegWit Address

![image](assets/it/25.webp)

copiamo-lo

![image](assets/it/26.webp)

e colá-lo na conversa com o RedeemBot

![image](assets/it/27.webp)

Temos agora um ecrã de verificação, para verificar se o código do vale está correto, bem como o Address que comunicámos ao RedeemBot. Vamos verificar bem porque, ao clicar em _Proceed_, a transação começa e não haverá forma de a encontrar novamente se tivermos, por exemplo, comunicado o Address errado.

![image](assets/it/28.webp)

A transação foi iniciada e o procedimento Redeem do voucher onchain termina assim.

![image](assets/it/29.webp)

enquanto o montante pode ser visto na história do nosso Wallet.

![image](assets/it/30.webp)