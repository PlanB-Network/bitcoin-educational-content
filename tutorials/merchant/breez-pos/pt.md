---
name: Breez ponto de vendas

description: Guia para começar a aceitar bitcoin usando o Breez POS
---

![capa](assets/cover.jpeg)

# Breez Ponto de Vendas

_Este texto vem do site de documentação do Breez: https://doc.breez.technology/How-to-Get-Started-with-Breez-POS.html_

## O que é o Breez POS?

**Breez** é um aplicativo completo e não custodial da Lightning. Vamos entender isso:

- **Lightning** é uma rede de pagamento de bitcoin que reduz o tempo de transação de minutos para milissegundos e as taxas de transação de vários dólares para alguns centavos ou menos. A Lightning transforma o bitcoin de ouro digital em moeda digital, preservando todos os benefícios que tornam o bitcoin ótimo.
- **Não custodial** significa que o Breez não assume a posse do dinheiro dos usuários. Muitos aplicativos da Lightning assumem a posse do dinheiro de seus usuários. Eles são basicamente bancos de bitcoin. Com um aplicativo não custodial como o Breez, todos os usuários são seus próprios bancos.
- **Completo** significa que o Breez cuida de quase todas as operações técnicas automaticamente e em segundo plano. Coisas como criação de canal, liquidez de entrada e roteamento permanecem ocultas. (Mas o Breez também é de código aberto, então aqueles interessados em auditar a tecnologia são bem-vindos a fazê-lo!)

**Breez POS** é a abreviação do nosso modo de ponto de venda. Em outras palavras, o Breez funciona como uma caixa registradora digital para empresas e comerciantes que desejam aceitar pagamentos da Lightning (além de seu modo "padrão", que é como a versão digital de uma carteira de couro para bitcoin, e um player de podcast de próxima geração). Agora vamos ver como configurar o Breez como uma caixa registradora da Lightning para o seu negócio.

## Como começar com o Breez?

1. O primeiro passo é baixar o aplicativo. Ele está disponível para Android e iOS (instale o TestFlight e clique no link do seu dispositivo).
2. O Breez pode fazer backup automaticamente no Google Drive, iCloud ou em qualquer servidor WebDav.
   > Observe que cada dispositivo executa seu próprio nó da Lightning. Você pode executar o modo POS em quantos dispositivos desejar, mas os saldos permanecerão separados.
3. Com o aplicativo aberto, clique no ícone no canto superior esquerdo para encontrar o modo de Ponto de Venda.

## Configurando o POS

1. Clique nesse ícone no canto superior esquerdo e clique em Ponto de Venda > Configurações do POS.

### A Senha do Gerente

Nas Configurações do POS, você tem a opção de criar uma senha do gerente. A senha do gerente torna impossível enviar pagamentos do aplicativo Breez sem autorização. A equipe de vendas só poderá receber pagamentos do dispositivo. Observe que, se você estiver usando essa opção, também poderá querer impedir o acesso ao backup do Breez, portanto, é recomendável usar uma conta externa do WebDav (por exemplo, Nextcloud) para esse caso de uso.

### A Lista de Itens

A lista de itens é um catálogo de itens à venda e seus preços. Existem duas maneiras de adicionar itens à lista:

- Para inserir itens um de cada vez, clique em Itens perto do topo da visualização principal do POS e, em seguida, no sinal de "+" no canto inferior direito. Aqui você pode inserir o nome de um único tipo de item, o preço (exibido na moeda equivalente de sua escolha) e o SKU (um identificador interno exclusivo para esse tipo de item; é opcional).
- Para inserir vários itens de uma vez, clique no ícone da calculadora no canto superior esquerdo, depois em Ponto de Venda > Preferências > Configurações do PDV e, em seguida, clique nos três pontos à direita da Lista de Itens e, depois, em Importar de CSV. Isso permitirá que você importe um arquivo CSV que você preparou antecipadamente contendo os nomes, preços e SKUs dos seus itens.

### Tela de Moeda Fiat

O Breez envia e recebe apenas bitcoin e, para a maioria das transações no Lightning, que tendem a ser de quantias menores, a soma é geralmente exibida em Satoshis, também conhecidos como sats (1 BTC = 100.000.000 sats). No entanto, muitos comerciantes acham prático poder ver (e informar aos clientes) o valor da compra exibido na moeda fiat local.

Na visualização principal do PDV, a moeda atualmente exibida é visível no lado direito (o padrão é SAT). Há também uma lista suspensa de outras moedas disponíveis para exibição. Para adicionar ou remover moedas desta lista suspensa, clique em Ponto de Venda > Preferências > Moedas Fiat. Em seguida, basta marcar as moedas que você gostaria de ter no seu menu suspenso e desmarcar aquelas que você gostaria de omitir.

Os valores exibidos são provenientes do yadio, uma fonte respeitada de dados de taxa de câmbio, e são atualizados em tempo quase real. Mas lembre-se: independentemente do valor da moeda que está sendo exibido atualmente, o pagamento em si é em bitcoin.

### Cobrando um Pedido

Para compor o pedido, adicione itens da lista de itens ou simplesmente insira uma soma no teclado. Em seguida, clique em Cobrar no topo da visualização principal do PDV. Você verá um código QR que o cliente pode escanear com seu aplicativo Lightning, que você pode compartilhar diretamente de outro aplicativo em seu dispositivo ou que você pode copiar e colar onde for necessário.

Ao escanear esse código ou clicar na fatura compartilhada/colada, o cliente verá a fatura em seu aplicativo Lightning e terá a opção de pagá-la e liquidar a transação imediatamente.

Assim que você ver a animação Pagamento aprovado! no aplicativo Breez no dispositivo do comerciante, você pode clicar no ícone da impressora para gerar um recibo para o cliente. Para usar uma impressora de recibos no Android, tente usar este driver. Observe que você também pode imprimir transações anteriores por meio da tela de Transações.

### Relatório de Vendas

Para visualizar um relatório diário/semanal/mensal de suas vendas (para fins contábeis ou outros), clique no ícone no canto superior esquerdo e, em seguida, clique em Transações. Clique no ícone de Relatório para exibir o relatório e no ícone de Calendário para alterar o período de datas selecionado.

### Exportando Transações

Para visualizar uma lista dos pagamentos recebidos no Breez, clique no ícone no canto superior esquerdo e, em seguida, clique em Transações. Clique nos três pontos no canto superior direito e, em seguida, em Exportar para exportar uma lista de pagamentos recebidos no formato CSV. Para restringir a lista a um determinado período de tempo, clique no ícone do calendário para definir um intervalo de datas.

### Imprimindo Recibos

Para imprimir um recibo de venda, clique no ícone de impressão no canto superior direito da caixa de diálogo de confirmação de pagamento. Alternativamente, clique no ícone no canto superior esquerdo e, em seguida, clique em Transações. Localize a venda a ser impressa, abra-a e clique no ícone de impressão no canto superior direito.

> Observação: use este driver para imprimir em uma impressora térmica portátil de 58mm/80mm Bluetooth/USB.

## Quero aprender mais

- Para obter mais informações sobre o Lightning e o Breez, confira nosso [blog](https://breez.technology/blog).
- Para obter mais dicas técnicas sobre como aproveitar ao máximo o aplicativo e realizar operações comuns, consulte nossa [documentação](https://breez.technology/documentation).
- Se você ficar preso e não conseguir encontrar a resposta em nenhum de nossos materiais de ajuda, você pode nos encontrar no [Telegram](https://t.me/breez_labs) ou nos enviar um [email](mailto:support@breez.technology).
- Se você quiser ver alguns vídeos de demonstração do modo Breez POS em ação feitos por nossos fãs e usuários, [aqui](https://www.youtube.com/watch?v=xxxx) está um ótimo vídeo curto, e [aqui](https://www.youtube.com/watch?v=xxxx) está um vídeo mais longo e detalhado.
