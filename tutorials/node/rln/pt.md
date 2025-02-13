---
name: Nó de relâmpago RGB
description: Como é que lanço um nó Lightning compatível com RGB com RLN?
---
![cover](assets/cover.webp)

Neste tutorial passo a passo, você aprenderá a configurar um nó RGB do Lightning em um ambiente Regtest. Veremos como criar tokens RGB e circulá-los em canais.

## O projeto RLN

A equipa RGB da Bitfinex tem vindo a trabalhar desde 2022 para enriquecer o ecossistema RGB, desenvolvendo uma pilha de tecnologia completa. Em vez de visar um único produto comercial, seus esforços estão focados em disponibilizar tijolos de software de código aberto, contribuindo para as especificações do protocolo RGB e criando referências de implementação.

Entre as contribuições notáveis da Bitfinex para o ecossistema RGB está [a biblioteca *RGBlib*](https://github.com/RGB-Tools/rgb-lib), escrita em Rust e acessível através de ligações em Kotlin e Python, o que simplifica muito o desenvolvimento de aplicações RGB, encapsulando mecanismos complexos de validação e envolvimento.

A equipa da Bitfinex também concebeu uma carteira móvel RGB, denominada "[*Iris Wallet*](https://iriswallet.com/)", disponível para Android. Esta carteira integra a utilização de um servidor proxy RGB para gerir facilmente as trocas de dados fora da cadeia (*consignments*) para *Client-side Validation* em RGB.

A Bitfinex também desenvolveu o projeto `rgb-lightning-node` (RLN). Este é um daemon Rust baseado num fork do `rust-lightning` (LDK), modificado para ter em conta a existência de activos RGB num canal. Quando um canal é aberto, a presença de tokens RGB pode ser especificada, e cada vez que o estado do canal é atualizado, é criada uma transição de estado que reflete a distribuição de tokens nas saídas do Lightning. Isso permite que :


- Abrir canais Lightning em USDT, por exemplo;
- Encaminhar estes tokens através da rede, desde que os caminhos de encaminhamento tenham liquidez suficiente;
- Explorar a lógica de punição e bloqueio de tempo do Lightning sem modificação: basta ancorar a transição RGB numa saída adicional da transação de compromisso.

O código RLN ainda está em fase alfa: recomendamos a sua utilização apenas em **regtest** ou na **testnet**.

## Lembrete do protocolo RGB

O RGB é um protocolo que funciona sobre o Bitcoin e emula a funcionalidade de contratos inteligentes e a gestão de activos digitais, sem sobrecarregar a cadeia de blocos em que se baseia. Ao contrário dos contratos inteligentes on-chain convencionais (como no Ethereum, por exemplo), o RGB baseia-se num sistema de "validação do lado do cliente": a maioria dos dados e dos históricos de estado são trocados e armazenados exclusivamente pelos participantes envolvidos, enquanto a cadeia de blocos Bitcoin apenas aloja pequenos compromissos criptográficos (através de mecanismos como *Tapret* ou *Opret*). Por conseguinte, no protocolo RGB, a cadeia de blocos Bitcoin serve apenas como servidor de registo de tempo e sistema de proteção contra a dupla utilização.

Um contrato RGB está estruturado como uma máquina de estado evolutiva. Começa com uma Génese que define o estado inicial (descrevendo, por exemplo, a oferta, o ticker ou outros metadados) de acordo com um Esquema rigorosamente tipificado e compilado. As Transições de Estado e, se necessário, as Extensões de Estado são então aplicadas para modificar ou alargar este estado. Cada operação, quer se trate da transferência de activos fungíveis (RGB20) ou da criação de activos únicos (RGB21), envolve *Selos de utilização única*. Estes ligam os Bitcoin UTXOs a estados fora da cadeia e impedem a duplicação de gastos, assegurando simultaneamente a confidencialidade e a escalabilidade.

Para saber mais sobre o funcionamento do protocolo RGB, recomendo que faça este curso de formação abrangente:

https://planb.network/courses/csv402
## Instalação de nó Lightning compatível com RGB

Para compilar e instalar o binário `rgb-lightning-node`, começamos por clonar o repositório e seus sub-módulos, depois executamos o comando :

```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```

![RLN](assets/fr/01.webp)


- A opção `--recurse-submodules` também clona os sub-dispositivos necessários (incluindo a versão modificada do `rust-lightning`);
- A opção `--shallow-submodules` restringe a profundidade do clone para acelerar o download, enquanto ainda fornece acesso aos commits essenciais.

A partir da raiz do projeto, execute o seguinte comando para compilar e instalar o binário :

```bash
cargo install --locked --debug --path .
```

![RLN](assets/fr/02.webp)


- `--locked` garante que a versão das dependências seja respeitada;
- o `--debug` não é obrigatório, mas pode ajudá-lo a concentrar-se (pode utilizar o `--release` se preferir) ;
- `--path .` diz ao `cargo install` para instalar a partir do diretório atual.

No final deste comando, um executável `rgb-lightning-node` estará disponível no seu `$CARGO_HOME/bin/`. Certifique-se que este caminho está no seu `$PATH` para que você possa invocar o comando de qualquer diretório.

## Pré-requisitos

Para funcionar, o daemon `rgb-lightning-node` precisa da presença e configuração do :


- Um nó `bitcoind`**

Cada instância RLN precisará se comunicar com `bitcoind` para transmitir e monitorar suas transações on-chain. Autenticação (login/password) e URL (host/porta) terão de ser fornecidos ao daemon.


- Um indexador** (Electrum ou Esplora)

O daemon deve ser capaz de listar e explorar transacções na cadeia, em particular para encontrar o UTXO no qual um ativo foi ancorado. Terá de especificar o URL do seu servidor Electrum ou Esplora.


- Um proxy RGB**

O servidor proxy é um componente (opcional, mas altamente recomendado) para simplificar a troca de *consignações* RGB entre pares Lightning. Mais uma vez, um URL deve ser especificado.

Os IDs e URLs são introduzidos quando o daemon é *desbloqueado* através da API.

## Lançamento do Regtest

Para uso simples, há um script `regtest.sh` que inicia automaticamente, via Docker, um conjunto de serviços: `bitcoind`, `electrs` (indexador), `rgb-proxy-server`.

![RLN](assets/fr/03.webp)

Isto permite-lhe lançar um ambiente local, isolado e pré-configurado. Cria e destrói contentores e diretórios de dados em cada reinicialização. Começaremos iniciando o arquivo :

```bash
./regtest.sh start
```

Este script irá :


- Crie um diretório `docker/` para armazenar ;
- Execute o `bitcoind` no regtest, bem como o indexador `electrs` e o `rgb-proxy-server` ;
- Esperar até que tudo esteja pronto a utilizar.

![RLN](assets/fr/04.webp)

De seguida, vamos lançar vários nós RLN. Em shells separados, execute, por exemplo (para lançar 3 nós RLN) :

```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```

![RLN](assets/fr/05.webp)


- O parâmetro `--network regtest` indica a utilização da configuração regtest;
- `--daemon-listening-port` indica em qual porta REST o Lightning node escutará as chamadas de API (JSON);
- `--ldk-peer-listening-port` especifica qual porta Lightning p2p deve ser escutada;
- `dataldk0/`, `dataldk1/` são os caminhos para os diretórios de armazenamento (cada nó armazena a sua informação separadamente).

Agora pode executar comandos nos seus nós RLN a partir do seu browser, graças à API. Em particular, é aqui que pode *desbloquear* daemons. Basta abrir um browser no mesmo computador que os seus nós e introduzir o URL :

```url
https://rgb-tools.github.io/rgb-lightning-node/
```

Para que um nó possa abrir um canal, deve primeiro ter bitcoins num endereço gerado com o seguinte comando (para o nó n.º 1, por exemplo):

```bash
curl -X POST http://localhost:3001/address
```

A resposta fornecer-lhe-á um endereço.

![RLN](assets/fr/06.webp)

No Regtest `bitcoind`, nós vamos minerar alguns bitcoins. Executar :

```bash
./regtest.sh mine 101
```

![RLN](assets/fr/07.webp)

Enviar os fundos para o endereço do nó gerado acima:

```bash
./regtest.sh sendtoaddress <address> <amount>
```

![RLN](assets/fr/08.webp)

Em seguida, extrai um bloco para confirmar a transação:

```bash
./regtest.sh mine 1
```

![RLN](assets/fr/09.webp)

## Lançamento da Testnet (sem Docker)

Se quiser testar um cenário mais realista, pode lançar nós RLN na Testnet em vez de no Regtest, apontando para serviços públicos ou serviços que controla:

```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```

Por defeito, se não for encontrada nenhuma configuração, o daemon tentará utilizar o ficheiro :


- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`

Com o login :


- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`

Também é possível personalizar estes elementos através da API `init`/`unlock`.

## Emissão de um token RGB

Para emitir um token, começaremos por criar UTXOs "coloríveis":

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```

![RLN](assets/fr/10.webp)

Pode, evidentemente, adaptar a encomenda. Para confirmar a transação, extraímos um :

```bash
./regtest.sh mine 1
```

Agora, podemos criar um ativo RGB. O comando dependerá do tipo de ativo que pretende criar e dos respectivos parâmetros. Aqui estou a criar um token NIA (*Non Inflatable Asset*) chamado "PBN" com um fornecimento de 1000 unidades. O parâmetro `precision` permite-lhe definir a divisibilidade das unidades.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```

![RLN](assets/fr/11.webp)

A resposta inclui o ID do ativo recentemente criado. Não se esqueça de anotar este identificador. No meu caso, é :

```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```

![RLN](assets/fr/12.webp)

Pode então transferi-lo para a cadeia ou alocá-lo num canal Lightning. É exatamente isso que vamos fazer na próxima secção.

## Abrir um canal e transferir um ativo RGB

Você deve primeiro conectar seu nó a um par na rede Lightning usando o comando `/connectpeer`. No meu exemplo, eu controlo ambos os nós. Então, vou recuperar a chave pública do meu segundo nó do Lightning com este comando:

```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```

O comando devolve a chave pública do meu nó n.º 2:

```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```

![RLN](assets/fr/13.webp)

Em seguida, abriremos o canal especificando o ativo relevante (`PBN`). O comando `/openchannel` permite-lhe definir o tamanho do canal em satoshis e optar por incluir o ativo RGB. Depende do que se pretende criar, mas no meu caso, o comando é :

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```

Saiba mais aqui:


- `peer_pubkey_and_opt_addr`: Identificador do par ao qual nos queremos ligar (a chave pública que encontrámos anteriormente);
- `capacity_sat`: Capacidade total do canal em satoshis ;
- `push_msat`: Quantidade em milisatoshis inicialmente transferida para o par quando o canal é aberto (aqui eu transfiro imediatamente 10.000 sats para que ele possa fazer uma transferência RGB mais tarde) ;
- `asset_amount`: Quantidade de activos RGB a afetar ao canal;
- `asset_id` : Identificador único do ativo RGB envolvido no canal;
- `public`: Indica se o canal deve ser tornado público para encaminhamento na rede.

![RLN](assets/fr/14.webp)

Para confirmar a transação, são extraídos 6 blocos:

```bash
./regtest.sh mine 6
```

![RLN](assets/fr/15.webp)

O canal Lightning está agora aberto e também contém 500 tokens `PBN` do lado do nó nº 1. Se o nó nº 2 desejar receber tokens `PBN`, deve gerar uma fatura. Veja como fazer isso:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```

Com :


- `amt_msat`: Montante da fatura em milisatoshis (mínimo 3000 sats) ;
- `expiry_sec` : Tempo de expiração da fatura em segundos ;
- `asset_id` : Identificador do ativo RGB associado à fatura ;
- `montante_do_activo`: Montante do ativo RGB a ser transferido com esta fatura.

Em resposta, receberá uma fatura RGB:

```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```

![RLN](assets/fr/16.webp)

Vamos agora pagar esta fatura a partir do primeiro nó, que detém o dinheiro necessário com o token `PBN`:

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```

![RLN](assets/fr/17.webp)

O pagamento foi efectuado. Este facto pode ser verificado através da execução do comando :

```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```

![RLN](assets/fr/18.webp)

Eis como implementar um nó Lightning modificado para transportar activos RGB. Esta demonstração é baseada em :


- Um ambiente regtest (via `./regtest.sh`) ou testnet ;
- Um nó Lightning (`rgb-lightning-node`) baseado num `bitcoind`, um indexador e um `rgb-proxy-server` ;
- Uma série de APIs REST JSON para abrir/fechar canais, emitir tokens, transferir activos através do Lightning, etc.

Graças a este processo :


- As transacções de envolvimento de relâmpagos incluem uma saída adicional (OP_RETURN ou Taproot) com a ancoragem de uma transição RGB;
- As transferências são efectuadas exatamente da mesma forma que os pagamentos Lightning tradicionais, mas com a adição de um token RGB;
- Vários nós RLN podem ser ligados para encaminhar e experimentar pagamentos em vários nós, desde que haja liquidez suficiente em bitcoins e activos RGB no caminho.

Se achou este tutorial útil, ficarei muito grato se colocar um polegar verde abaixo. Por favor, não hesite em partilhar este artigo nas suas redes sociais. Muito obrigado!

Recomendo também este outro tutorial em que explico como utilizar a ferramenta RGB CLI desenvolvida pela associação LNP/BP para criar um contrato RGB:

https://planb.network/tutorials/node/rgb/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4