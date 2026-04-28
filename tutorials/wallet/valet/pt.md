---
name: Manobrista Bitcoin
description: O Valet traz o Lightning node sem custódia para o seu bolso
---

![cover_valet](assets/cover.webp)



## Introdução


O Valet é um Bitcoin e Lightning wallet leve e auto-custodial que oferece um processo de integração fácil e conveniente para iniciantes. Foi especificamente concebido para servir as comunidades Bitcoin e as economias circulares, especialmente em zonas remotas.


Trata-se de um fork do **Simple Bitcoin Wallet (SBW)**, com uma funcionalidade avançada de canal Lightning alojado denominada **Fiat Channels**, concebida para permitir que qualquer pessoa aceite pagamentos Lightning sem riscos de volatilidade.


Atualmente, o Valet só está disponível para dispositivos Android e pode ser descarregado e instalado a partir de várias lojas de aplicações de código aberto. No entanto, o Valet **não** está alojado na **Google Play Store** devido a preocupações com a privacidade do programador e com o KYC.



## Descarregar e instalar o Valet


O Valet pode ser descarregado como um ficheiro APK a partir da página GitHub da Standard Sats'. a [Standard Sats] (https://standardsats.github.io/) é a empresa que desenvolveu o Valet.


para descarregar o Valet, visite a página Standard Sats [GitHub page] (https://github.com/standardsats/valet/releases) e localize a versão **mais recente** (geralmente é a mais alta).


vá a **Assets** e clique no ficheiro com apenas uma extensão **.apk**. O teu download começará automaticamente.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


quando o download estiver concluído, vá para o **Gerenciador de arquivos** > **Downloads** do seu dispositivo e selecione o arquivo apk Valet.


![Select_valet_apk](assets/en/002.webp)


instale-a e, em poucos segundos, a sua aplicação estará pronta e aparecerá no seu ecrã inicial.


![valet_icon_on_homescreen](assets/en/003.webp)


Em alternativa, pode também descarregar o Valet a partir da loja de aplicações **F-Droid**. Se não tiver a aplicação F-Droid no seu dispositivo, pode descarregá-la e instalá-la [aqui] (https://f-droid.org/en/).


no seu ecrã inicial, abra o F-Droid e procure **Valet**. Selecionar a primeira opção com um ícone **roxo e branco** das duas opções que aparecerão e clicar em **Download**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


após o download, clique em **Instalar** e siga as instruções no ecrã. Quando a instalação estiver concluída, pode iniciar o Valet a partir do F-Droid, clicando em **Abrir**, ou iniciá-lo a partir do ecrã inicial do seu dispositivo.



## Criar um Bitcoin Wallet


Pode configurar um Bitcoin wallet no Valet em dois passos simples.


inicie o Valet a partir do ecrã inicial do seu dispositivo ou da aplicação F-Droid. Aparecerá um ecrã de configuração do wallet, com duas opções: **Criar novo Wallet** e **Restaurar Wallet existente**.


selecione **Criar novo Wallet** e, instantaneamente, será criado um novo wallet e será redireccionado para a página inicial.


![set_up_a\_new_wallet](assets/en/006.webp)



## Cópia de segurança da sua frase-semente


na página inicial do wallet, clique no cartão **Green** que tem uma inscrição **"Toque para guardar a frase de recuperação do wallet no caso de alguma vez perder ou substituir o seu dispositivo"


![seed_phrase_green_card](assets/en/007.webp)


é apresentado um conjunto de 12 palavras inglesas. Escreve-as num papel, pela ordem de 1 a 12, e guarda-as bem.


![the_seed_phrase](assets/en/008.webp)


### Prestar atenção ⚠️:


Preste atenção aos seguintes elementos:


- Como já sabe, o Valet é um wallet autocustodial, pelo que a sua frase seed é o único acesso para recuperar o seu Wallet.
- Se alguma vez perder a sua frase seed, **nunca** terá acesso ao seu wallet.
- Se alguém obtiver a sua frase seed, pode roubar irremediavelmente todos os seus Bitcoin.


Por isso, terá de escrever a sua frase seed de 12 palavras e guardá-la num local seguro. Nunca deve fazer uma captura de ecrã, guardá-la como rascunho no seu e-mail ou guardá-la em qualquer dispositivo eletrónico que tenha estado ligado à Internet.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Receção e envio de Bitcoins em Valet


O Valet é um wallet auto-custodial com capacidade para on-chain e Lightning Bitcoin. Isto significa que pode receber e enviar Bitcoin a partir do Valet através de um **On-chain** ou de um **Lightning Network**.


No entanto, para poder receber ou enviar Bitcoin através do Lightning, é necessário criar um canal Lightning utilizando os seus on-chain Bitcoins como Liquidity. Ou pode adquirir a liquidez de um canal Lightning junto dos vendedores.



## Geração de um Bitcoin Address em cadeia


Para receber o Bitcoin através do on-chain, é necessário gerar um endereço Bitcoin.


na página inicial do wallet, verá um cartão **Laranja** e um **Púrpura**, respetivamente designados por **Bitcoin** e **Lightning**.


clique no cartão laranja com a designação **Bitcoin**. Será redireccionado para um ecrã que apresenta um endereço Bitcoin.


![click_on_Bitcoin_card](assets/en/009.webp)


pode **copiar** o endereço e enviá-lo para a pessoa que lhe está a enviar Bitcoins, ou clicar no botão **partilhar** para enviar o código QR para a pessoa através das redes sociais ou outros canais de comunicação.


também pode clicar no botão **Editar** para definir a quantidade de Bitcoins que devem ser enviados para esse endereço.


**Atenção:** Tal como uma fatura, a função de edição é útil em cenários em que se pretende receber uma quantidade específica de Bitcoins para um endereço num determinado momento; no entanto, isto não significa que o endereço não possa receber quantidades superiores ou inferiores.


clicar em **Mais endereços novos**, para gerar novos endereços aleatórios.


![generating_a\_bitcoin_add](assets/en/010.webp)


também pode gerar um endereço on-chain Bitcoin clicando no botão **Receber** no fundo da sua página inicial do wallet. Depois seleciona **Receber para endereço bitcoin** e continua com o mesmo processo acima.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Envio de Bitcoin via On-chain


O envio do Bitcoin a partir do Valet wallet através do on-chain é uma tarefa simples.


na parte inferior da página inicial do seu wallet, clique no botão **Enviar**, introduza o endereço do Bitcoin ou clique em **Digitalizar**, para digitalizar o código QR do endereço e, em seguida, clique em **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


introduza o montante em Bitcoin que pretende enviar. Pode introduzir manualmente um montante em termos de Sats ou em termos de moeda Fiat, ou pode clicar em **Max** para utilizar todo o seu saldo de on-chain.


também pode ajustar as taxas que pretende pagar pela transação, clicando na pequena caixa verde denominada **taxa** e, em seguida, deslizando o ponto branco para a direita ou para a esquerda para aumentar ou diminuir as taxas, respetivamente. Clique em **Ok** para enviar a transação.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Configuração de um canal Lightning Network


Como mencionado acima, o Valet é um Bitcoin e Lightning wallet auto-custodial; assim, para poder enviar e receber Bitcoin através da rede Lightning, terá de configurar primeiro um canal Lightning, seguindo estes passos:


no ecrã inicial, clique no **cartão roxo** com a designação **Raios**. Será encaminhado para uma página com as seguintes opções:



- Digitalizar Nó QR
- Comprar em LNBIG.COM
- Comprar em BITREFILL.COM
- Pedido de re-sincronização do gráfico LN.


Ao selecionar **Comprar em lnbig.com** ou **Comprar em bitrefill.com**, será redireccionado para os sítios Web destas empresas, onde poderá adquirir uma liquidez de entrada de várias capacidades. Ignore a última opção **Request LN graph resync** por enquanto.


Portanto, a nossa escolha é **Digitalizar um Nó QR**. Nesta altura, deve ter decidido e obtido o **código QR** do nó para o qual pretende abrir um canal. Podes abrir canais para qualquer nó público à tua escolha. Consulta [1ML] (https://1ml.com/) ou [Amboss] (https://amboss.space/), seleciona qualquer nó público à tua escolha e digitaliza o código QR associado ao nó que escolheste.


![channel_opening_options](assets/en/016.webp)


será automaticamente redireccionado para a página seguinte, onde deverá financiar o seu canal. Mais uma vez, o uso da rede Lightning autocustodial exige que você use seus Bitcoins para financiar um canal. Isso significa que você deve ter Bitcoins em seu on-chain wallet para financiar o canal Lightning. Consulte este artigo de [Hacken] (https://hacken.io/discover/lightning-network/) para saber mais sobre a rede Lightning.


![fund_channel](assets/en/017.webp)


introduza a **quantidade** de Bitcoins com que pretende financiar o canal, ou clique em **Max** para utilizar todo o seu saldo de on-chain Bitcoin. Pode ajustar a **taxa**, ou deixar a taxa predefinida e clicar em **Ok**.


**Atenção:** O montante com que financia o canal será a capacidade do seu novo canal (ou seja, o volume total de Sats que pode ser transaccionado de e para esse canal)


Também é importante que utilizes mais de **100.000 Sats** como montante de financiamento ao abrir um canal. Isso ocorre porque muitos Lightning nodes exigem um mínimo de 100.000 Sats de capacidade para abrir um canal para eles. Portanto, para evitar tentativas e erros, basta usar valores superiores a esse intervalo.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


nesta altura, quando consultar a sua página inicial do wallet, verá que o seu montante de financiamento foi transferido do **cartão Bitcoin** para o **cartão Lightning**. No seu histórico de transacções, verá a transação de financiamento a ser processada.


![channel_funding_processing](assets/en/020.webp)


se clicar no cartão Lightning, verá informações que mostram que o seu canal Lightning está a abrir. Você também verá a **transação de financiamento do canal** na sua lista de transações. Aguarde a confirmação da transação de financiamento no blockchain e seu canal Lightning estará pronto.


![channel_opening](assets/en/021.webp)


assim que a transação de financiamento for confirmada, clique no **Cartão Lightning** na sua página inicial, e verá as informações sobre o seu canal Lightning da seguinte forma:



- CONJUNTO ALEATÓRIO DE NÚMEROS SEPARADOS POR PONTOS:** Estes são os endereços IP dos nós. (IPV4 e IPV6, respetivamente)
- CAPACIDADE:** Este é o volume total de Sats que pode ser enviado e recebido através deste canal
- CAN SEND:** Esta é a quantidade de Sats que pode enviar nesta altura. Verá que é quase o mesmo valor que a **Capacidade**. Isto deve-se ao facto de não ter enviado quaisquer pagamentos através do canal.
- CAN RECEIVE:** Este é o número de Sats que pode receber neste canal neste momento. (Será pouco ou nada nesta altura porque para poder receber, tem de enviar primeiro alguns Sats para criar um Liquidity de entrada)
- REEMBOLSÁVEL:** Isto mostra o montante que é pago de volta para o seu endereço on-chain quando fecha o seu canal. Isto também é referido como o **Saldo local do seu canal**. Note que é um pouco menor do que a capacidade do canal, e isso é porque ao fechar um canal, você deve pagar uma taxa para publicar a transação de fechamento no blockchain, assim como você fez ao financiar o canal. Assim, o sistema deduziu o valor mais baixo aproximado que irá pagar)
- VALUE IN FLIGHT:** Quando alguém envia algum sats para o seu canal, ou quando tenta enviar algum sats para alguém, e por qualquer razão, a transação é atrasada, é frequentemente mostrado neste campo.


![channel_info](assets/en/022.webp)


## Enviar Sats através do seu canal


O envio do Sats através do Lightning Network é uma tarefa simples.


na parte inferior da página inicial, clique em **Enviar**, e **cole** a fatura Lightning (deve tê-la copiado) no campo fornecido, ou clique em **Digitalizar** para digitalizar o código QR da fatura Lightning.


![click_send_or_scan](assets/en/023.webp)


A maioria das facturas Lightning vem com um montante pré-inserido a pagar. Mas, em alguns casos, pode ser uma fatura aberta em que é necessário preencher o valor.


introduza o montante em **Dólares** ou **Sats**, ou clique em **Max**, para utilizar todo o saldo do seu canal Lightning, e depois clique em **Ok**. Assim que um bom caminho for encontrado, seu pagamento será enviado e concluído em alguns segundos. Fique de olho na página inicial para ver se o pagamento foi concluído. Ele terá uma marca de verificação verde quando for concluído.


![enter_the_amount](assets/en/024.webp)


## Receber o Sats através do seu canal


Receber pagamentos no seu canal Lightning depende muito do facto de ter ou não um Liquidity de entrada. Depois de abrir um canal, você não poderá receber pagamentos até que tenha enviado pelo menos alguns Sats para **criar liquidez de entrada** na outra extremidade da conexão do canal. Para confirmar se podes receber Sats e a quantidade de Sats que podes receber, verifica o campo **Pode Receber** nas informações do teu canal. Isto mostrar-te-á quantos Sats recebes em cada momento.


Agora, vamos supor que enviou alguns Sats do seu canal, tem agora liquidez de entrada e pode receber Sats.


Para receber no canal Lightning, é necessário gerar uma fatura. Ao contrário do Bitcoin on-chain, que utiliza endereços, a rede Lightning utiliza facturas. Existem duas vias para gerar uma fatura no Valet.


#### OPÇÃO 1


na parte inferior da página inicial, clicar em **Receber**, selecionar **Receber para fatura relâmpago**. Preencha o valor a ser recebido na fatura e clique em **Ok**. Copie a fatura ou compartilhe o código QR com o pagador.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### OPÇÃO 2


clique no cartão Lightning roxo na página inicial do wallet. Toque em qualquer lugar do seu canal e uma lista de opções aparecerá. Selecione **Receber no canal** e introduza o montante que está a receber (em Sats ou em dólares). Também verás quantos Sats podes receber (capacidade de entrada) quando estiveres a preencher a fatura. Clique em **Ok** e copie a fatura ou partilhe o código QR com o pagador.


![receive_to_channel](assets/en/028.webp)


**Atenção:** A primeira opção é uma opção universal, o que significa que se tiver mais do que um canal ativo e utilizar a primeira opção, o sistema selecionará automaticamente um dos seus canais para receber o Sats.


Assim, neste cenário, a segunda opção é a melhor a utilizar se pretender receber Sats para um determinado canal.


### Explicação das opções de pop-up do seu canal


Quando toca no seu canal, são apresentados os seguintes campos de opções:


![channel_pop_ups](assets/en/029.webp)


**PARTILHAR DETALHES DO CANAL LIGHTNING:** Permite-lhe partilhar os detalhes do seu canal, como o ID do par remoto, o ID do canal local, a transação de financiamento, a data de criação, etc.


**FECHAR O CANAL PARA A CARTEIRA:** Pode fechar o seu canal relâmpago sempre que quiser. Para fechar o seu canal, o sistema verifica o saldo de Bitcoin que você tem no seu próprio lado do canal (lembre-se do campo **"Pode enviar "**, também conhecido como seu saldo local) e envia-o de volta para você. No Valet, pode escolher para onde quer que o Bitcoin seja enviado quando o canal é fechado. Portanto, **Fechar canal para wallet** é uma das suas duas opções.


clique nesta opção e selecione **Bitcoin**. O encerramento do canal será iniciado e o saldo do seu canal Bitcoin será enviado de volta para o endereço on-chain do seu wallet.


![close_channel_to_wallet](assets/en/030.webp)


**Fechar canal para ADDRESS:** Esta é a segunda opção para fechar um canal. Ao escolher esta opção, ser-lhe-á pedido que introduza um endereço wallet para onde será enviado o saldo Bitcoin do seu canal. Tem em atenção que, nesta opção, apenas podes digitalizar o código QR do endereço Bitcoin para o qual pretendes fechar o canal. Atualmente, não existe a opção de colar manualmente o endereço.


clique nesta opção, digitalize o endereço do Bitcoin e clique em **Ok**. O encerramento do canal será iniciado e o seu saldo do Lightning Bitcoin será enviado para o endereço que digitalizou.


![scan_address_and_Ok](assets/en/031.webp)


**RECEBER AO CANAL:** É a mesma coisa que gerar uma fatura, mas em alguns casos, pode ter mais do que um canal, incluindo canais Fiat (um tipo único de canal Lightning que pode ser obtido no Valet wallet). Assim, se tiver vários canais abertos, esta opção garante que pode receber o pagamento num canal específico.


**RECARREGAR A PARTIR DE OUTROS CANAIS:** Esta opção é uma funcionalidade que lhe permite recarregar um canal a partir de outros canais existentes. Por exemplo, se tiver 2 canais Lightning diferentes (A e B), e o saldo do Bitcoin no canal A se tiver esgotado, com esta opção, pode facilmente e automaticamente recarregar o saldo do canal A a partir do canal B.


**RECEBIMENTO NÃO PRIVADO: Esta é também uma opção para gerar uma fatura para receber o pagamento, mas quando utiliza esta opção, o remetente paga-lhe diretamente. Isto significa que o pagamento não passa por diferentes nós antes de chegar a si, como acontece com um pagamento Lightning normal. Portanto, em essência, o remetente sabe que foi você quem pagou, conhece sua ID de canal etc. Esta opção pode ser usada frequentemente quando está a receber o pagamento de uma fonte em que confia e não precisa de manter a sua privacidade.


## Canais alojados e Fiat


Como muitos outros Bitcoin wallets, o Valet é um Bitcoin e Lightning wallet simples e leve. Mas ele tem um recurso Lightning exclusivo que o diferencia da maioria dos outros Bitcoin wallets. Esse recurso é chamado de **Canais hospedados e Fiat**.


Os canais Fiat são um tipo de implementação Lightning que permite uma fácil integração e utilização da rede Lightning. É uma solução de custódia que permite o anonimato total, tal como acontece com um canal Lightning normal. A tecnologia dos canais Fiat também permite a criação de derivados Bitcoin na rede Lightning. Um exemplo é que, com os canais Fiat, os comerciantes podem aceitar pagamentos Bitcoin de valor estável sem se preocuparem com a volatilidade do Bitcoin.


A implementação atual dos canais Fiat no Valet permite a criação de moedas Fiat sintéticas estáveis apoiadas pelo Sats. Utiliza uma relação anfitrião-cliente em que o anfitrião é qualquer nó Lightning que ofereça este serviço e o cliente é o utilizador do Valet. É uma solução de custódia porque todos os Sats estão do lado do host; no entanto, a geração de faturas, o roteamento de tor e a geração de pré-imagem ainda acontecem no lado do cliente, como em um canal Lightning normal.


A abertura de um canal Fiat segue o mesmo processo que a abertura de um canal Lightning. A única diferença significativa é que, neste caso, o cliente (utilizador Valet) não tem de comprometer qualquer liquidez on-chain para criar a capacidade do canal. O Host define a capacidade do canal e encaminha todos os pagamentos para o cliente.


para abrir um canal Fiat, clique no cartão roxo **Lightning** na página inicial do wallet. Selecione **Scan Node QR** (Neste ponto, deve ter identificado um Host para o qual pretende abrir um canal e obtido o QR do nó. Um exemplo de um nó Host para o qual se pode abrir um canal Fiat é o nó SATM do Standard Sats)


**Atenção:** É importante notar que qualquer pessoa pode ser um Host. Tudo o que é necessário é executar um nó Lightning com o plugin **Fiat channel** e um **Hedging service**. Os canais Fiat são um projeto de código aberto do *Standard Sats*. Leia mais sobre ele [aqui](https://github.com/standardsats/fiat-channels-rfc) e [aqui](https://standardsats.github.io/).


Nó SATM QR abaixo:


![SATM_node_QR](assets/en/032.webp)


depois de digitalizar o nó QR, clique em **Pedir canal fiat USD** ou **Pedir canais fiat EUR** (Esta é a denominação fiat em que os seus saldos Fiat serão cotados). Por enquanto, escolha USD e clique em **OK**. O canal será aberto automaticamente e poderá começar a receber o Sats imediatamente. É simples assim!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


vá à página inicial do seu wallet, verá um cartão **verde claro** com a etiqueta **USD**, que é o seu **canal Fiat**.


![fiat_channel_card](assets/en/035.webp)


**Atenção:** Quando recebe Sats num canal Fiat, o valor fiat do Sats que recebeu será bloqueado como um saldo estável, enquanto o volume de Sats flutua com o preço do Bitcoin. Esta solução foi concebida principalmente para os comerciantes que querem aceitar o Sats como pagamento, mas não querem enfrentar os desafios da volatilidade do Bitcoin. Isto ajuda-os a manter um valor estável em todos os momentos, enquanto continuam a poder efetuar transacções na rede Lightning, desfrutando do alcance global e da rápida liquidação do Bitcoin como meio de troca no Lightning Network.


Quando o seu canal Fiat é criado, eis os seguintes campos de valor que verá e o que cada um deles significa:


![fiat_channel_info](assets/en/036.webp)



- CONJUNTO ALEATÓRIO DE NÚMEROS SEPARADOS POR PONTOS:** Estes são os endereços IP dos nós. (IPV4 e IPV6, respetivamente)
- TAXA DO SERVIDOR:** Este é o preço de mercado Bitcoin a que o Anfitrião lhe oferece os serviços. Muitas vezes, este preço será ligeiramente diferente do preço de mercado predominante, porque um Anfitrião pode acrescentar um pequeno prémio. Cabe inteiramente a um Anfitrião decidir esta taxa; por conseguinte, esta também varia de Anfitrião para Anfitrião.
- SALDO FIAT:** Este é o valor fiat estável bloqueado de cada sat que receberes neste canal. Lembra-te, como explicado anteriormente, sempre que receberes Sats no teu canal Fiat, o valor fiat do Sats no momento da receção é imediatamente bloqueado como um valor fiat sintético estável neste campo. O teu **Saldo Fiat** não varia com o preço de mercado do Bitcoin. Sempre que quiser efetuar pagamentos a partir deste canal, só pode enviar o equivalente em Sats deste saldo Fiat. Pense nisso como uma moeda fiduciária digital apoiada pelo Sats.
- CAPACIDADE:** Este é o volume total de Sats que pode ser enviado e recebido através deste canal. (Isto também é definido pelo Host. E, ao contrário de um canal Lightning normal, esta capacidade pode ser ajustada pelo Host, conforme o caso)
- PODE ENVIAR:** Este é o volume de Sats que pode enviar em cada ponto com base no seu saldo fiat. Isto é completamente diferente do que se tem num canal Lightning normal, porque este valor flutua com o preço do Bitcoin. Por isso, o que vês aqui é o valor em Sats do teu saldo Fiat em qualquer altura com base na **Taxa do Servidor**.
- CAN RECEIVE:** Este é o número de Sats que pode receber neste canal neste momento. Depois de criar o seu canal, este valor deve ser o mesmo que a capacidade do canal.
- VALOR EM VOO:** Quando alguém envia algum sats para o seu canal, ou quando tenta enviar algum sats para alguém e, por qualquer razão, a transação se atrasa, é frequentemente apresentado neste campo.


Eis alguns aspectos importantes a ter em conta sobre os canais Fiat:



- Ao contrário de um canal Lightning normal, quando abres um canal fiat, podes começar imediatamente a receber Sats, mas não podes enviar. Só podes enviar Sats quando tiveres recebido Sats.
- Em todos os momentos, o ativo que está a ser enviado de e para é o Sats. O *Saldo Fiat* é apenas uma representação IOU sintética de um valor Bitcoin recebido em qualquer altura. Portanto, não é uma criação do token ou uma nova criptomoeda.
- O canal Fiat é sobretudo útil para os comerciantes/empresas que estão cépticos quanto à aceitação de pagamentos em Bitcoin devido a preocupações com a volatilidade. Pode também ser útil para as empresas que pretendem pagar os salários dos seus trabalhadores em Bitcoin sem terem de suportar as consequências da volatilidade do Bitcoin, que pode tornar o seu capital salarial instável. Também pode ser útil para indivíduos que vivem numa área com uso predominante de Bitcoin, mas têm custos de vida fixos.
- Repara que não existe nenhum campo com a indicação **REFUNDABLE**. Isto é porque, tecnicamente, não podes fechar um canal Fiat. Só podes deixar de usar um canal Fiat drenando o seu saldo para o teu canal Lightning normal.


### As opções do seu Fiat Channel Pop-Up explicadas


Quando toca no seu canal Fiat Lightning, são apresentados os seguintes campos:


![fiat_channel_pop_up](assets/en/037.webp)


**SHARE HOSTED CHANNEL DETAILS:** Isto permite-lhe partilhar os detalhes do seu canal Fiat, como o ID do par remoto, o ID do canal local, a data de criação, etc.


**EXPORT CHANNEL STATE:** Isto permite-te exportar o estado de um canal em qualquer altura. Isto é geralmente útil para corrigir erros de canal, e um Host pode pedir que você compartilhe isso se houver necessidade.


**Como mencionado anteriormente, tecnicamente não é possível fechar um canal Fiat, mas é possível drenar o saldo do seu canal para o seu canal Lightning normal existente. Isso automaticamente move o equivalente em Sat do seu saldo Fiat para o seu canal Lightning normal.


**RECEBER AO CANAL:** É a mesma coisa que gerar uma fatura, mas em alguns casos, um utilizador pode ter mais do que um canal Fiat com Hosts diferentes, incluindo canais Lightning normais. Assim, se um utilizador tiver vários canais abertos, esta opção garante que pode receber o pagamento num canal específico.


**RECARREGAR A PARTIR DE OUTROS CANAIS:** Esta opção é uma funcionalidade que permite ao utilizador recarregar um canal a partir de outros canais existentes. Assim, com esta opção, podes encher o teu canal Fiat a partir de um canal normal ou de outros canais Fiat que tenhas, da mesma forma que podes drenar.


**Esta opção também permite gerar uma fatura para receber o pagamento, mas quando utiliza esta opção, o remetente paga-lhe diretamente. Isto significa que o pagamento não passa por diferentes nós antes de chegar a si. Assim, na essência, o remetente sabe que foi você quem pagou, conhece o seu ID de canal, etc. Esta opção pode ser frequentemente utilizada quando está a receber um pagamento de uma fonte em que confia e não precisa de manter a sua privacidade.


## Definições do arrumador:


Como qualquer outra aplicação, o Valet tem definições de aplicação que podem ser ajustadas a seu gosto. Pode aceder à página de definições a partir do ecrã inicial.


no ecrã inicial, clique no ícone **Gear** localizado no canto superior direito do ecrã para aceder às definições. Abaixo estão os componentes da secção de definições.


![settings_icon](assets/en/038.webp)


**Se esta opção estiver **Desactivada**, deve activá-la porque esta é a única forma de recuperar os seus canais Lightning normais se desinstalar e reinstalar o Valet. Explicaremos isso mais tarde. Portanto, clique aqui e dê permissão ao Valet para o seu **armazenamento de mídia**, pois é onde o arquivo de backup é salvo.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**ONDE ARMAZENAR A CÓPIA DE SEGURANÇA LOCAL:** Desde que tenha dado permissão ao Valet para o seu armazenamento, este campo será automaticamente definido para armazenar cópias de segurança locais na pasta **Downloads**. Mas pode alterá-lo clicando aqui e selecionando qualquer pasta à sua escolha.


**GERIR CARTEIRAS DE CADEIA** Isto é um pouco técnico e não precisa de se preocupar com isto, a menos que tenha experiência suficiente. A predefinição aqui é óptima.


**ADD HARDWARE WALLET:** Também não deve preocupar-se com isto, a menos que tenha um Hardware wallet que queira ligar e monitorizar. Com esta definição, pode digitalizar e ligar o seu hardware wallet, como o Trezor ou o cartão Cold, e monitorizar as suas actividades. Esta é uma funcionalidade apenas de observação, o que significa que não é possível efetuar transacções no Hardware wallet a partir daqui. Apenas pode observar e monitorizar as actividades, saldos, etc. do wallet.


**DEFINIR NÓDULO PERSONALIZADO ELECTRUM:** Isto também é técnico e, a menos que tenha conhecimentos suficientes, não se deve preocupar com isto. A predefinição é suficientemente boa.


**Unidades de Bitcoin:** Esta é a forma como pretende que o seu saldo Bitcoin seja apresentado. A primeira opção apresenta o seu saldo em termos Satoshi, por exemplo, 1.000.000 Sats, enquanto a segunda opção o apresenta em pontos decimais BTC. por exemplo, 0,01BTC


**Utilizar autenticação por PIN** Se selecionar esta caixa, terá de definir um PIN ou uma impressão digital que deverá introduzir para iniciar sessão no seu wallet e autenticar as transacções.


**USAR CONEXÃO TOR:** Se marcar esta caixa, as suas transacções serão encaminhadas através da rede Tor. Acrescenta uma camada extra de privacidade, mas pode resultar num atraso no processamento do pagamento, especialmente para pagamentos Lightning.


**VISUALIZAR A FRASE DE RECUPERAÇÃO BIP39:** É aqui que pode aceder à sua frase de 12 palavras do seed para backup. Por isso, se não a escreveu antes, ou não consegue encontrar onde a escreveu, desde que ainda tenha acesso ao seu Wallet, pode copiá-la daqui.


**ESTATÍSTICAS DE UTILIZAÇÃO:** Mostra-lhe um resumo de todas as suas transacções e actividades desde a criação do wallet


![usage_stats](assets/en/041.webp)


## Recuperação do Wallet


O Valet é um wallet sem custódia, por isso, se perder o seu dispositivo ou desinstalar a aplicação wallet, terá de efetuar uma recuperação do wallet para recuperar os seus Bitcoins e canais Lightning. No início deste tutorial, mencionámos a importância de anotar a sua **frase seed de 12 palavras** porque é a chave para recuperar o seu wallet. Não há representantes de atendimento ao cliente que possam ajudá-lo a voltar ao seu wallet.


Existem duas ferramentas importantes necessárias para recuperar o seu Valet wallet, dependendo se tinha ou não um canal Lightning ativo. Para um utilizador que não tinha um canal Lightning normal ativo, só precisa da sua **frase seed de 12 palavras**, seguindo os passos simples abaixo:


instalar uma nova aplicação Valet e lançar/iniciar a aplicação.


selecionar **Restaurar Wallet existente**


![restore_existing_wallet](assets/en/042.webp)


selecionar **Frase de recuperação apenas**.


![select_recovery_phrase](assets/en/043.webp)


introduza a sua frase de recuperação de 12 palavras e clique em **OK**.


![input_12_words](assets/en/044.webp)


O seu wallet será recuperado. Neste caso, apenas o saldo do on-chain Bitcoin será recuperado.


No entanto, se tiveres um canal de Relâmpago normal ativo e recuperares o teu wallet apenas com a frase de recuperação, o teu canal de Relâmpago será fechado à força e qualquer saldo de Bitcoin que tenhas nele será automaticamente enviado para o teu saldo de on-chain.


A outra forma de recuperar o seu Valet wallet, especialmente se tinha um canal Lightning normal aberto antes de desinstalar o Valet, é **utilizar o ficheiro de cópia de segurança local guardado no seu dispositivo, juntamente com a sua frase de 12 palavras seed**. Se utilizar estes dois, o estado do seu canal Lightning será restaurado, pelo que o seu canal Lightning não será fechado à força.


Eis os passos a seguir:


instalar uma nova aplicação Valet e lançar/iniciar a aplicação.


selecione **Restaurar Wallet existente**.


👉 Selecione **Frase de cópia de segurança + recuperação**.


![select_backup_and_recovery_seed](assets/en/045.webp)


selecione o ficheiro de cópia de segurança no gestor de ficheiros do seu telefone. (Por predefinição, é sempre guardado na pasta **Downloads**)


![local_backup_file_in_download_folder](assets/en/046.webp)


Uma vez selecionado o ficheiro de cópia de segurança correto, será apresentada uma mensagem a confirmar que um **"ficheiro de cópia de segurança está presente "** e ser-lhe-á pedido que introduza a sua frase seed de 12 palavras.


![enter_12_words](assets/en/047.webp)


introduza a sua frase de recuperação de 12 palavras e clique em **OK**. Será encaminhado para a sua página inicial do wallet.


aguarde a sincronização da rede do Bitcoin (**SYNC**) e a sincronização do nó do Lightning (**LN Sync**) serem concluídas e seu wallet será totalmente restaurado, incluindo seus canais do Lightning.


![LN_sync](assets/en/048.webp)


## Conclusão


O Valet é uma solução wallet interessante, com caraterísticas que o tornam adequado para a integração de novos utilizadores. Dispõe igualmente de um canal Fiat, uma tecnologia não tão recente que assegura a integração de empresas geridas por fiat na norma Bitcoin.


Descarregue o Valet hoje mesmo e experimente-o!!! 🧡