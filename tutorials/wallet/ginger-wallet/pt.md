---
name: Gengibre Wallet
description: Software Bitcoin Wallet de fonte aberta e auto-custódia, Fork do Wasabi Wallet, integrando Coinjoins
---
![cover](assets/cover.webp)



Ginger Wallet é um portfólio Bitcoin de código aberto, sem custódia, focado em confidencialidade e privacidade. Começou como Fork a partir do Wasabi Wallet (após a versão 2.0.7.2 - licença MIT).



O Ginger Wallet mantém a arquitetura técnica do Wasabi, acrescentando algumas caraterísticas específicas. De acordo com a [documentação do Ginger Wallet] (https://docs.gingerwallet.io/why-ginger/difference.html#gingerwallet), o Wasabi dá ênfase à **autonomia e ao controlo**, enquanto o Ginger se concentra na **facilidade de utilização, segurança e experiência simplificada**, tornando-o acessível aos menos familiarizados com aspectos técnicos.



O Ginger Wallet é um software Wallet apenas para computadores (sem aplicação móvel).



## O que é o CoinJoin?



O CoinJoin** é um tipo específico de estrutura de transação Bitcoin que reúne vários participantes numa única transação de colaboração. Este mecanismo mistura as entradas de diferentes utilizadores numa transação comum, tornando extremamente difícil - se não mesmo impossível, se for feito corretamente - rastrear os fundos. Como resultado, torna-se quase impossível para um observador externo identificar com certeza a origem e o destino dos bitcoins envolvidos, ao contrário do que acontece nas transacções Bitcoin convencionais.



Para si, o utilizador, o CoinJoin ajuda a preservar a sua confidencialidade. Por exemplo, se receber uma doação de 10 000 Sats num Bitcoin Address, o remetente pode rastrear estes fundos e, em alguns casos, deduzir que possui uma quantidade maior de bitcoins ou observar as suas actividades. Ao fazer um CoinJoin após esta doação de 10 000 Sats, quebra a rastreabilidade: o remetente deixará de poder deduzir qualquer informação sobre si a partir deste pagamento.



O Chaumian CoinJoin oferece um elevado nível de segurança, uma vez que os fundos permanecem sob o controlo exclusivo do utilizador em todos os momentos. Mesmo os operadores dos servidores de coordenação não podem desviar os bitcoins dos participantes em nenhuma circunstância. Nem os utilizadores nem os coordenadores precisam de confiar uns nos outros: cada um mantém o controlo das suas chaves privadas e permanece exclusivamente autorizado a validar transacções. Nenhum terceiro pode, portanto, apropriar-se dos seus bitcoins durante um CoinJoin, nem estabelecer uma ligação direta entre os seus inputs e outputs.



Para saber mais sobre o CoinJoin, consulte o curso BTC 204 da Plan ₿ Academy :



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Instalar o Ginger Wallet



Para instalar o Ginger Wallet, visite o sítio Web [Ginger Wallet] (https://gingerwallet.io).



Prima **Download** para descarregar a versão correta para o seu computador (Windows / MacOs / Linux).



![screen](assets/fr/03.webp)



Outra opção é ir ao [GitHub](https://github.com/GingerPrivacy/GingerWallet/releases) do projeto para o descarregar.



![screen](assets/fr/04.webp)



Em seguida, execute o programa de instalação.



![screen](assets/fr/05.webp)




## Definições dos parâmetros



### Configurações preliminares



Abra o Ginger Wallet e selecione o seu idioma preferido.



![screen](assets/fr/06.webp)



Logo desde o início, Ginger recorda-lhe os custos envolvidos no processo CoinJoin.



![screen](assets/fr/07.webp)



Em seguida, prima **Iniciar** e, depois, **Novo** para criar uma nova carteira.



![screen](assets/fr/08.webp)



Em seguida, guarde e confirme o seu seedphrase.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![screen](assets/fr/09.webp)



![screen](assets/fr/10.webp)



Para maior segurança, o Ginger Wallet dá-lhe a opção de adicionar um passphrase.



![screen](assets/fr/11.webp)



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Este passphrase, uma vez adicionado, será solicitado sempre que tentar aceder à sua carteira.



![screen](assets/fr/12.webp)



O Ginger ativa automaticamente a predefinição **CoinJoin** quando cria a sua carteira. É informado deste facto e pode personalizar a definição de acordo com as suas necessidades.



![screen](assets/fr/13.webp)




### Definições gerais



Quando tiveres criado o teu primeiro portefólio, serás levado para o Interface Wallet da Ginger.



![screen](assets/fr/14.webp)



Ativar o **Modo discreto**, se pretender ocultar os saldos das suas carteiras.



![screen](assets/fr/15.webp)



Pode criar vários portefólios no Ginger Wallet. Basta clicar em **Adicionar um portefólio**.



![screen](assets/fr/16.webp)



O Ginger suporta a utilização de carteiras de hardware através da norma Bitcoin core Interface, embora a integração direta de ou para uma carteira de hardware ainda não esteja disponível.



As carteiras de hardware compatíveis incluem (mas não estão limitadas a) :




- BLOCKSTREAM Jade
- Coldcard MK4
- Cartão frio Q
- Ledger Nano S Plus
- Ledger Nano X
- Trezor Modelo T
- Trezor Safe 3
- etc.



Agora clique em **Configurações**.



![screen](assets/fr/17.webp)



Estas definições são as da aplicação em geral e as configurações aí efectuadas aplicam-se a todos os portefólios.



Em **Definições**, tem os separadores :





- Geral**



![screen](assets/fr/18.webp)





- Aparência



Neste separador, é possível alterar o idioma, a moeda e a unidade de visualização da taxa (BTC/Satoshi), entre outros.



![screen](assets/fr/19.webp)





- Bitcoin**



Este separador permite-lhe ativar o Bitcoin Knots para ser executado quando a aplicação é iniciada, escolher a sua rede (Main/RegTest) e o seu fornecedor de taxas de carregamento (Mempool Space/BLOCKSTREAM info/Full node), etc.



![screen](assets/fr/20.webp)





- Caraterísticas de segurança**



No separador Segurança, pode ativar a autenticação de dois factores, ativar ou desativar o Tor e até desactivá-lo quando a aplicação Ginger for fechada.



![screen](assets/fr/21.webp)



**NB** :




- Para a autenticação de dois factores, certifique-se de que a sua aplicação de autenticação suporta o protocolo SHA256 e códigos de 8 dígitos. O Ginger Wallet requer um código 2FA de 8 dígitos para maior segurança. Este formato mais longo torna o código muito mais difícil de adivinhar ou comprometer, oferecendo uma maior proteção contra o acesso não autorizado.
- Por padrão, todo o tráfego de rede do Ginger passa pelo Tor, eliminando a necessidade de configuração manual. Se o Tor já estiver ativo no seu sistema, o Ginger dar-lhe-á automaticamente prioridade.



Mas assim que desativar o Tor nas definições, a sua privacidade permanece geralmente preservada, exceto em duas situações:




- durante um CoinJoin, o coordenador pode ligar as suas entradas e saídas ao seu IP Address;
- ao difundir uma transação, um nó malicioso ao qual se liga poderia associar a sua transação ao seu IP.



Não se esqueça de premir **Done** (no canto inferior direito do Coin) de cada vez, para guardar as suas definições. Algumas configurações requerem que o Ginger Wallet seja reiniciado para ter efeito.



Além disso, a barra de pesquisa no topo das carteiras permite-lhe procurar e aceder a qualquer parâmetro, etc...



![screen](assets/fr/22.webp)




### Configuração da carteira



Podem ser criadas várias carteiras na aplicação, pelo que cada carteira pode ser configurada de acordo com as suas necessidades. Para o fazer, clique nos **três pontos** à frente do nome da carteira e, em seguida, em **Configurações da carteira**.



![screen](assets/fr/23.webp)



Como pode ver, para além do parâmetro Wallet, poderá ver os seus UTXOs (lista de tokens que possui), estatísticas e informações Wallet (a chave pública alargada, por exemplo).



Para voltar à configuração da nossa carteira, depois de clicar em parâmetros da carteira, será levado para os seguintes separadores:




- Geral** (onde pode alterar o nome da carteira) ;



![screen](assets/fr/24.webp)





- CoinJoin** (onde pode personalizar as definições CoinJoin desta carteira) ;



![screen](assets/fr/25.webp)





- Ferramentas** (onde pode verificar o seu seedphrase, sincronizar novamente a sua carteira ou eliminá-la).



![screen](assets/fr/26.webp)




## Receber bitcoins



Para receber bitcoins no seu Wallet no Ginger Wallet :




- prima **Receber** ;



![screen](assets/fr/27.webp)





- Introduzir o nome da fonte à qual deseja associar o Address. Esta etiqueta serve para manter o controlo dos seus pagamentos. Isto não tem implicações para o On-Chain; trata-se simplesmente de informação de rastreabilidade armazenada localmente na sua aplicação;



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

![screen](assets/fr/28.webp)





- clicar na pequena seta à esquerda de **generate** para escolher o formato Address (**SegWit** /**Taproot**) e, em seguida, clicar em **generate**, para generate e Address e código QR.



![screen](assets/fr/29.webp)



Este código Address ou QR será utilizado pelo remetente para lhe enviar bitcoins.



![screen](assets/fr/30.webp)




## Enviar bitcoins



Vídeo tutorial sobre como enviar através do Ginger Wallet.



![Vidéo](https://youtu.be/2nf5aAimfhg)



Para o efeito :




- Prima o botão **Enviar**;
- introduzir o Address do destinatário, o montante a enviar e uma etiqueta;
- verificar a síntese da transação e confirmar o envio.



![screen](assets/fr/31.webp)




## Gastar bitcoins



É fácil comprar e vender Bitcoin com Ginger Wallet. Em apenas alguns passos, pode gastar os seus bitcoins.



### Comprar bitcoins



Os utilizadores do Ginger Wallet podem comprar bitcoins.





- Prima o botão **Comprar**. Este botão permanece visível mesmo que o Wallet esteja vazio.



![screen](assets/fr/32.webp)





- Selecione o seu país, ou mesmo o seu estado (em algumas regiões, como o Canadá), antes de proceder à compra de um Bitcoin. De facto, quando clicar na função **Comprar** pela primeira vez, também terá de especificar a sua região.



![screen](assets/fr/33.webp)



Prima **Continuar** para avançar no processo de compra.





- Em seguida, introduza o montante de bitcoins que pretende comprar no campo dedicado. Também pode escolher a moeda de transação.



![screen](assets/fr/34.webp)



Cada moeda tem um limite mínimo e máximo de compra. Por exemplo, em USD, o limite máximo é de $30.000.



Se já tiver efectuado uma compra, pode consultar o seu histórico de transacções clicando no botão **Pedidos anteriores**. Será apresentada uma lista das transacções anteriores e o respetivo estado.





- Escolha a oferta mais adequada para si.



Nesta altura, verá uma lista de todas as ofertas disponíveis. Para cada oferta, tem :




 - nome do fornecedor (1) ;
 - o número de bitcoins equivalente ao montante previamente introduzido, o método de pagamento e a taxa de compra (2) ;
 - o botão **Aceitar** (3).



![screen](assets/fr/35.webp)



As taxas indicadas na oferta não constituem um custo adicional. Já estão incluídas no montante total da oferta.



O canto superior direito Coin do ecrã com a etiqueta **Todos** permite-lhe filtrar as ofertas por método de pagamento. O método de pagamento selecionado será definido por defeito, mas pode ser alterado em qualquer altura.



![screen](assets/fr/36.webp)



Se encontrar uma oferta adequada, clique no botão **Aceitar** para prosseguir com a compra. Será então redireccionado para a página do vendedor, onde poderá finalizar a transação.



### Vender bitcoins



Os utilizadores do Ginger Wallet podem vender o Bitcoin. O botão **Vender** só é visível quando existem fundos disponíveis na carteira.





- Clique em **Vender**.



![screen](assets/fr/37.webp)





- Tal como acontece com a opção **Comprar**, quando utiliza a função Vender pela primeira vez, deve selecionar o seu país antes de proceder a uma venda do Bitcoin.





- De seguida, tem de introduzir o montante de Bitcoins que pretende vender. Pode introduzir este montante em BTC ou numa moeda fiduciária, como o dólar americano (USD).





- Depois de o ter feito, verá uma lista de ofertas disponíveis. Escolha uma oferta de venda que lhe convenha e clique em **Aceitar** para continuar.





- Agora é necessário finalizar a transação:
 - Depois de aceitar uma oferta, será redireccionado para a página do fornecedor;
 - Siga as instruções na página do fornecedor ;
 - A certa altura, receberá um destinatário Address e o montante exato a enviar;
 - De seguida, volte ao Ginger Wallet para continuar o processo;
 - Uma vez de volta ao Ginger Wallet, uma caixa de diálogo aparecerá, permitindo-lhe continuar clicando em **Enviar**.



Isto abrirá o ecrã **Enviar** com o Address do destinatário e o montante pré-preenchido. Também pode utilizar o botão **Enviar** no ecrã inicial. Embora possa enviar a transação manualmente, recomendamos que a complete através da caixa de diálogo para um processo optimizado.



## Criar um CoinJoin no Ginger Wallet



![Vidéo](https://youtu.be/AJe67RDfB1A)



Proteja a confidencialidade dos seus bitcoins com **CoinJoin**, integrado diretamente no Ginger Wallet. O Wallet utiliza o **WABISABI**, um protocolo Chaumian CoinJoin concebido para facilitar coinjoins mais acessíveis e eficientes.



Cabe-lhe a si escolher a estratégia CoinJoin (automática ou manual) que mais lhe convém.



O Ginger CoinJoin está pronto a utilizar assim que o descarregar (não são necessários passos adicionais). Automaticamente, o Ginger CoinJoin é executado em segundo plano para proteger a sua privacidade em cada transação. Na prática, o leitor CoinJoin aparecerá sempre que tiver um saldo que possa ser anonimizado.



Quanto ao arranque manual do CoinJoin, é uma operação de um clique. Inicie a ronda e aguarde que a transação do CoinJoin seja criada e confirmada. Verá a pontuação de anonimato no Interface.



Podem ser efectuadas várias misturas até se atingir o nível de anonimato desejado. Também é possível excluir determinadas partes da mistura.



Por defeito, a Ginger utiliza o seu próprio coordenador com todos os parâmetros pré-configurados e taxas garantidas. Coinjoins de tokens com valor superior a 0,03 BTC incorrem em uma taxa de coordenador de 0,3%, além da taxa Mining. Entradas de 0,03 BTC ou menos, bem como remixes, estão isentas de taxas de coordenador, mesmo após uma única transação. Por conseguinte, um pagamento efectuado com fundos CoinJoin permite que tanto o remetente como o destinatário remisturem as suas moedas sem incorrerem em taxas de coordenação.



Ginger prefere coinjoins com mais participantes a rondas mais pequenas e rápidas. Os coinjoins maiores oferecem mais anonimato, custos mais baixos e maior eficiência do espaço BLOCK.




## Segurança e boas práticas



O desejo de descentralização e a preservação da privacidade exigem a adoção de várias boas práticas:




- Guarde sempre o seu seedphrase num local seguro, fora de linha;
- Se perder o seu computador ou suspeitar de acesso não autorizado, crie imediatamente um novo Wallet. Transfira os seus fundos para esta nova carteira e elimine a antiga;
- Utilizar um Address diferente para cada receção para evitar a reutilização de endereços;
- Descarregue sempre as suas aplicações de portefólio exclusivamente a partir da conta oficial do GitHub ou do sítio Web oficial.



Agora já está familiarizado com a utilização da aplicação Ginger Wallet para enviar, receber e gastar os seus bitcoins.



Se achou este tutorial útil, por favor deixe-me um polegar Green abaixo. Sinta-se à vontade para partilhar este artigo através das suas plataformas de redes sociais. Muito obrigado!



Sugiro também que consulte este tutorial sobre como utilizar a aplicação informática Liana para enviar e receber bitcoins, bem como implementar um plano patrimonial automatizado.



https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04