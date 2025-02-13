---
name: RGB CLI
description: Como é que posso criar e trocar contratos inteligentes no RGB?
---
![cover](assets/cover.webp)

Neste tutorial, vamos seguir o passo-a-passo do processo de escrita de um contrato, usando a ferramenta de linha de comando `rgb` criada pela associação LNP/BP. O objetivo é mostrar como instalar e manipular o CLI, compilar um Esquema, importar a Interface e a Implementação da Interface, e depois emitir um ativo RGB. Também veremos a lógica subjacente, incluindo a compilação e a validação de estado. No final deste tutorial, deverá ser capaz de reproduzir o processo e criar os seus próprios contratos RGB.

## Lembrete do protocolo RGB

O RGB é um protocolo que funciona sobre o Bitcoin e emula a funcionalidade de contratos inteligentes e a gestão de activos digitais, sem sobrecarregar a cadeia de blocos em que se baseia. Ao contrário dos contratos inteligentes on-chain convencionais (como no Ethereum, por exemplo), o RGB baseia-se num sistema de "validação do lado do cliente": a maioria dos dados e dos históricos de estado são trocados e armazenados exclusivamente pelos participantes envolvidos, enquanto a cadeia de blocos Bitcoin apenas aloja pequenos compromissos criptográficos (através de mecanismos como *Tapret* ou *Opret*). Por conseguinte, no protocolo RGB, a cadeia de blocos Bitcoin serve apenas como servidor de registo de tempo e sistema de proteção contra a dupla utilização.

Um contrato RGB está estruturado como uma máquina de estado evolutiva. Começa com uma Génese que define o estado inicial (descrevendo, por exemplo, a oferta, o ticker ou outros metadados) de acordo com um Esquema rigorosamente tipificado e compilado. As Transições de Estado e, se necessário, as Extensões de Estado são então aplicadas para modificar ou alargar este estado. Cada operação, quer se trate da transferência de activos fungíveis (RGB20) ou da criação de activos únicos (RGB21), envolve *Selos de utilização única*. Estes ligam os Bitcoin UTXOs a estados fora da cadeia e impedem a duplicação de gastos, assegurando simultaneamente a confidencialidade e a escalabilidade.

Para saber mais sobre o funcionamento do protocolo RGB, recomendo que faça este curso de formação abrangente:

https://planb.network/courses/csv402
A lógica interna do RGB é baseada em bibliotecas Rust que vocês, como programadores, podem importar para os vossos projectos para gerir a parte da *Validação do lado do cliente*. Além disso, a equipa LNP/BP está a trabalhar em ligações para outras linguagens, mas isto ainda não foi finalizado. Além disso, outras entidades, como a Bitfinex, estão a desenvolver as suas próprias pilhas de integração, mas falaremos sobre elas noutro tutorial. Por enquanto, o `rgb` CLI é a referência oficial, mesmo que permaneça relativamente pouco polido.

## Instalação e apresentação da ferramenta rgb CLI

O comando principal é simplesmente chamado `rgb`. Ele foi projetado para ser uma reminiscência do `git`, com um conjunto de sub-comandos para manipular contratos, invocá-los, emitir ativos e assim por diante. A Bitcoin Wallet não está integrada atualmente, mas estará em uma versão iminente (0.11). Esta próxima versão permitirá aos utilizadores criar e gerir as suas carteiras (através de descritores) diretamente a partir do `rgb`, incluindo a geração de PSBT, compatibilidade com hardware externo (por exemplo, uma carteira de hardware) para assinatura, e interoperabilidade com software como o Sparrow. Isto simplificará todo o cenário de emissão e transferência de activos.

### Instalação via Cargo

Instalamos a ferramenta em Rust com :

```bash
cargo install rgb-contracts --all-features
```

(Nota: o crate é chamado `rgb-contracts`, e o comando instalado será chamado `rgb`. Se uma crate chamada `rgb` já existia, pode ter havido uma colisão, daí o nome)

A instalação compila um grande número de dependências (por exemplo, análise de comandos, integração Electrum, gestão de provas de conhecimento zero, etc.).

Quando a instalação estiver concluída, o ficheiro :

```bash
rgb
```

Executando `rgb` (sem argumentos) mostra uma lista de sub-comandos disponíveis, tais como `interfaces`, `schema`, `import`, `export`, `issue`, `invoice`, `transfer`, etc. Você pode mudar o diretório de armazenamento local (um esconderijo que guarda todos os logs, esquemas e implementações), escolher a rede (testnet, mainnet) ou configurar seu servidor Electrum.

![RGB-CLI](assets/fr/01.webp)

### Primeira visão geral dos controlos

Quando executar o seguinte comando, verá que uma interface `RGB20` já está integrada por defeito:

```bash
rgb interfaces
```

Se esta interface não estiver integrada, clone o ficheiro :

```bash
git clone https://github.com/RGB-WG/rgb-interfaces
```

Compilar:

```bash
cargo run
```

Em seguida, importe a interface da sua escolha:

```bash
rgb import interfaces/RGB20.rgb
```

![RGB-CLI](assets/fr/02.webp)

No entanto, dizem-nos que ainda não foi importado nenhum esquema para o software. Também não existe nenhum contrato na reserva. Para o ver, execute o comando :

```bash
rgb schemata
```

Pode então clonar o repositório para obter determinados esquemas:

```bash
git clone https://github.com/RGB-WG/rgb-schemata
```

![RGB-CLI](assets/fr/03.webp)

Este repositório contém, no seu diretório `src/`, vários ficheiros Rust (por exemplo `nia.rs`) que definem esquemas (NIA para "*Non Inflatable Asset*", UDA para "*Unique Digital Asset*", etc.). Para compilar, pode então executar :

```bash
cd rgb-schemata
cargo run
```

Isso gera vários arquivos `.rgb` e `.rgba` correspondentes aos esquemas compilados. Por exemplo, você encontrará `NonInflatableAsset.rgb`.

### Importação de esquema e implementação de interface

Agora é possível importar o esquema para o `rgb` :

```bash
rgb import schemata/NonInflatableAssets.rgb
```

![RGB-CLI](assets/fr/04.webp)

Isto adiciona-o ao stock local. Se executarmos o seguinte comando, vemos que o esquema aparece agora:

```bash
rgb schemata
```

## Criação de contratos (emissão)

Existem duas abordagens para criar um novo ativo:


- Ou utilizamos um script ou código em Rust que constrói um Contrato preenchendo os campos do esquema (estado global, Estados Próprios, etc.) e produz um ficheiro `.rgb` ou `.rgba`;
- Ou use o sub-comando `issue` diretamente, com um arquivo YAML (ou TOML) descrevendo as propriedades do token.

Pode encontrar exemplos em Rust na pasta `examples`, que ilustram como construir um `ContractBuilder`, preencher o `estado global` (nome do ativo, ticker, abastecimento, data, etc.), definir o Estado de Propriedade (a que UTXO está atribuído), e depois compilar tudo isto numa *consignação de contrato* que pode exportar, validar e importar para um esconderijo.

A outra maneira é editar manualmente um arquivo YAML para personalizar o `ticker`, o `nome`, o `fornecimento`, e assim por diante. Suponha que o arquivo se chame `RGB20-demo.yaml`. Você pode especificar :


- `spec`: ticker, nome, precisão ;
- `terms`: um campo para avisos legais ;
- `issuedSupply` : a quantidade de fichas emitidas ;
- `assignments`: indica o selo de utilização única (*definição do selo*) e a quantidade desbloqueada.

Eis um exemplo de um ficheiro YAML a criar:

```yaml
interface: RGB20Fixed
globals:
spec:
ticker: PBN
name: Plan B Network
details: "Pay attention: the asset has no value"
precision: 2
terms:
text: >
SUBJECT TO, AND WITHOUT IN ANY WAY LIMITING, THE REPRESENTATIONS AND WARRANTIES OF ANY SELLER. PROPERTY IS BEING SOLD “AS IS”...
media: ~
issuedSupply: 100000000
assignments:
assetOwner:
seal: tapret1st:b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1
amount: 100000000 # this is 1 million (we have two digits for cents)
```

![RGB-CLI](assets/fr/05.webp)

Em seguida, basta executar o comando :

```bash
rgb issue '<SchemaID>' ssi:<Issuer> rgb20-demo.yaml
```

![RGB-CLI](assets/fr/06.webp)

No meu caso, o identificador único do esquema (que deve ser colocado entre aspas simples) é `RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k` e não coloquei nenhum emitente. Portanto, o meu pedido é :

```txt
rgb issue 'RDYhMTR!9gv8Y2GLv9UNBEK1hcrCmdLDFk9Qd5fnO8k' ssi:anonymous rgb20-demo.yaml
```

Se não souber o ID do esquema, execute o comando :

```bash
rgb schemata
```

O CLI responde que um novo contrato foi emitido e adicionado ao stash. Se digitarmos o seguinte comando, vemos que existe agora um contrato adicional, correspondente ao que acabou de ser emitido:

```bash
rgb contracts
```

![RGB-CLI](assets/fr/07.webp)

Em seguida, o comando seguinte apresenta os estados globais (nome, ticker, oferta...) e a lista de Estados Próprios, ou seja, as atribuições (por exemplo, 1 milhão de fichas `PBN` definidas no UTXO `b449f7eaa3f98c145b27ad0eeb7b5679ceb567faef7a52479bc995792b65f804:1`).

```bash
rgb state '<ContractId>'
```

![RGB-CLI](assets/fr/08.webp)

## Exportação, importação e validação

Para partilhar este contrato com outros utilizadores, pode ser exportado do esconderijo para um ficheiro :

```bash
rgb export '<ContractId>' myContractPBN.rgb
```

![RGB-CLI](assets/fr/09.webp)

O arquivo `myContractPBN.rgb` pode ser passado para outro usuário, que pode adicioná-lo ao seu estoque com o comando :

```bash
rgb import myContractPBN.rgb
```

Aquando da importação, se se tratar de uma simples *contratação de consignação*, será apresentada a mensagem "`Importing consignment rgb`". Se se tratar de uma *consignação de transição de estado* de maior dimensão, o comando será diferente (`rgb accept`).

Para garantir a validade, também é possível utilizar a função de validação local. Por exemplo, é possível executar :

```bash
rgb validate myContract.rgb
```

### Utilização, verificação e visualização de stocks

Para relembrar, o stash é um inventário local de esquemas, interfaces, implementações e contratos (Genesis + transições). Cada vez que executa "import", adiciona um elemento ao stash. Este stash pode ser visualizado em pormenor com o comando :

```bash
rgb dump
```

![RGB-CLI](assets/fr/10.webp)

Isto irá gerar uma pasta com detalhes de todo o stock.

## Transferência e PSBT

Para efetuar uma transferência, é necessário manipular uma carteira Bitcoin local para gerir os compromissos `Tapret` ou `Opret`.

### Gerar uma fatura

Na maioria dos casos, a interação entre os participantes num contrato (por exemplo, Alice e Bob) ocorre através da geração de uma fatura. Se a Alice quiser que o Bob execute algo (uma transferência de fichas, uma reemissão, uma ação num DAO, etc.), a Alice cria uma fatura que detalha as suas instruções ao Bob. Assim, temos :


- Alice** (o emitente da fatura) ;
- Bob** (que recebe e executa a fatura).

Ao contrário de outros ecossistemas, uma fatura RGB não se limita à noção de pagamento. Pode incluir qualquer pedido ligado ao contrato: revogar uma chave, votar, criar uma gravação (*gravação*) num NFT, etc. A operação correspondente pode ser descrita na interface do contrato. A operação correspondente pode ser descrita na interface do contrato.

O seguinte comando gera uma fatura RGB:

```bash
$ rgb invoice $CONTRACT -i $INTERFACE $ACTION $STATE $SEAL
```

Com :


- `$CONTRACT`: Identificador do contrato (*ContractId*) ;
- `$INTERFACE`: a interface a utilizar (por exemplo, `RGB20`) ;
- `$ACTION`: o nome da operação especificada na interface (para uma simples transferência de token fungível, poderia ser "Transfer"). Se a interface já fornecer uma ação por defeito, não é necessário introduzi-la novamente aqui;
- `$STATE`: os dados de estado a transferir (por exemplo, um montante de fichas se for transferida uma ficha fungível);
- `$SEAL`: o selo de utilização única do beneficiário (Alice), ou seja, uma referência explícita a um UTXO. O Bob utilizará esta informação para construir a transação testemunha, e o resultado correspondente pertencerá então à Alice (em *UTXO oculto* ou não encriptado).

Por exemplo, com os seguintes comandos

```bash
alice$ CONTRACT='iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY'
alice$ MY_UTXO=4960acc21c175c551af84114541eace09c14d3a1bb184809f7b80916f57f9ef8:1
alice$ rgb invoice $CONTRACT -i RGB20 --amount 100 $MY_UTXO
```

O CLI gerará uma fatura como :

```bash
rgb:iZgIN9EL-2H21UgQ-x!A3uJc-WwXhCSm-$9Lwcc1-v!mUkKY/RGB20/100+utxob:zlVS28Rb-...
```

Pode ser transmitida ao Bob através de qualquer canal (texto, código QR, etc.).

### Efetuar uma transferência

Para transferir a partir desta fatura :


- Bob (que tem os tokens no seu stash) tem uma carteira Bitcoin. Ele precisa de preparar uma transação Bitcoin (sob a forma de um PSBT, por exemplo, `tx.psbt`) que gasta os UTXOs onde se encontram os tokens RGB necessários, mais um UTXO para a moeda (câmbio) ;
- O Bob executa o seguinte comando:

```bash
bob$ rgb transfer tx.psbt $INVOICE consignment.rgb
```


- Isto gera um ficheiro `consignment.rgb` que contém :
 - O historial de transição prova à Alice que os tokens são genuínos;
 - A nova transição que transfere fichas para o selo de utilização única da Alice ;
 - Uma transação de testemunha (não assinada).
- Bob envia este ficheiro `consignment.rgb` a Alice (por correio eletrónico, um servidor de partilha ou um protocolo RGB-RPC, Storm, etc.);
- Alice recebe `consignment.rgb` e aceita-o na sua própria reserva :

```bash
alice$ rgb accept consignment.rgb
```


- O CLI verifica a validade da transição e adiciona-a ao esconderijo da Alice. Se for inválido, o comando falha com mensagens de erro detalhadas. Caso contrário, ele é bem-sucedido e informa que a transação de amostra ainda não foi transmitida na rede Bitcoin (Bob está aguardando a luz verde de Alice);
- A título de confirmação, o comando `accept` devolve uma assinatura (*payslip*) que Alice pode enviar a Bob para lhe mostrar que validou a *consignação* ;
- Bob pode então assinar e publicar (`--publish`) sua transação Bitcoin:

```bash
bob$ rgb check <sig> && wallet sign --publish tx.psbt
```


- Assim que esta transação é confirmada na cadeia, a propriedade do ativo é considerada transferida para Alice. A carteira de Alice, que monitoriza a extração da transação, vê o novo Estado de Propriedade aparecer no seu esconderijo.

Agora já sabe como emitir e transferir um contrato RGB. Se este tutorial lhe foi útil, ficar-lhe-ia muito grato se colocasse um polegar verde abaixo. Não hesite em partilhar este artigo nas suas redes sociais. Muito obrigado!

Também recomendo este outro tutorial no qual explico como lançar um nó Lightning compatível com RGB para trocar tokens quase instantaneamente:

https://planb.network/tutorials/node/rgb/rln-ffc02528-329b-4e16-bd83-873d0299feea