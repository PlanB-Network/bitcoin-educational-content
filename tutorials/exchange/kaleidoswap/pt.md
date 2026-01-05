---
name: KaleidoSwap
description: Guia avançado para a negociação de activos RGB no Lightning Network com o KaleidoSwap
---

![cover](assets/cover.webp)


O KaleidoSwap é uma sofisticada aplicação de desktop de código aberto que faz a ponte entre o Protocolo RGB e o Lightning Network. Serve como uma interface abrangente para a gestão de nós RGB Lightning, interagindo com os fornecedores de serviços RGB Lightning (LSPs) através da especificação LSPS1 e executando trocas atómicas de activos RGB.


Como uma solução sem custódia, o KaleidoSwap permite que os utilizadores mantenham o controlo total sobre as suas chaves e dados. Ao alavancar o paradigma de validação do lado do cliente do RGB, ele permite contratos inteligentes privados e escaláveis em cima do Bitcoin. Este tutorial mergulha nos recursos avançados do KaleidoSwap, guiando-o através dos meandros do gerenciamento "colorido" do UTXO, canaliza a liquidez para ativos específicos e o modelo de negociação do tomador, garantindo que você possa utilizar totalmente esse poderoso protocolo de troca descentralizado.


## Instalação


O KaleidoSwap fornece binários pré-compilados para os principais sistemas operativos, mas para utilizadores avançados, a compilação a partir da fonte garante que está a executar o código mais recente com as suas configurações específicas.


### Descarregar binários


Pode transferir a versão mais recente para o seu sistema operativo a partir do [site oficial](https://kaleidoswap.com/) ou da [página de versões do GitHub](https://github.com/kaleidoswap/desktop-app/releases).


### Métodos de instalação


1.  **Windows**: Descarregar o instalador `.exe` e executá-lo.

2.  **macOS**: Transfira o ficheiro `.dmg`, abra-o e arraste o KaleidoSwap para a pasta Aplicações.

3.  **Linux**: Baixe o arquivo `.AppImage` ou `.deb` e instale/execute-o.



## Opções de configuração do nó


Quando iniciar o KaleidoSwap pela primeira vez, ser-lhe-á apresentado o **Painel de ligação**. Este é o primeiro passo para configurar o seu ambiente.


![Node Selection Screen](assets/en/01.webp)


O utilizador deve escolher a forma de ligação ao RGB Lightning Network. Esta escolha tem impacto no seu nível de controlo e privacidade.


### Opção 1: Nó local (recomendado para auto-custódia)


**Para um controlo total e privacidade**, execute um nó diretamente na sua máquina, veja as vantagens abaixo:


- Auto-responsável**: O utilizador tem as chaves. Nenhum terceiro pode congelar os seus fundos ou censurar as suas transacções.
- Privacidade**: Os seus dados permanecem no seu dispositivo.
- Independência**: Não depende de prestadores de serviços externos.


Se selecionar **Nó local**, será levado para o ecrã de configuração onde pode criar um novo wallet ou restaurar um já existente.


![Local Node Setup Screen](assets/en/02.webp)


### Opção 2: Nó remoto


Conectar-se a um RGB Lightning Node remoto (auto-hospedado em um VPS ou em um provedor hospedado).


- Vantagens**: Sem utilização de recursos locais, disponibilidade 24/7.
- Compensação**: Requer a confiança no anfitrião ou a gestão de um servidor remoto.


![Remote Node Setup Screen](assets/en/03.webp)


**Recomendamos vivamente que corra o seu próprio nó - quer localmente (Opção 1), quer alojando um nó remoto - para tirar o máximo partido das propriedades resistentes à censura do Bitcoin e do RGB.


## Criar um Wallet


O KaleidoSwap gerencia os ativos Bitcoin e RGB. O processo de criação do wallet inicializa um keystore que protege os seus fundos on-chain e os estados do seu canal Lightning.


Eis o processo pormenorizado:

1. Abra o KaleidoSwap e selecione **Nó Local**.

2. Clique em **Criar novo Wallet**.

3. **Configuração de conta**: Introduza um **Nome da conta** e selecione a **Rede** (por exemplo, Bitcoin, Mainnet, Testnet, Signet).

4. **Configuração Avançada** (Opcional): Se for um utilizador avançado, pode configurar pontos finais RPC personalizados, URLs de indexador ou definições de proxy em "Definições avançadas".

5. Clique em **Continuar**.

6. **Password**: Defina uma palavra-passe forte para encriptar localmente o seu ficheiro wallet.

7. **Frase de recuperação**: Anote a sua frase seed e guarde-a em segurança.


    - Crítico**: Esta frase é necessária para recuperar os seus fundos on-chain e a identidade do nó.
    - Aviso**: **Os estados dos canais de relâmpago não podem ser totalmente recuperados apenas com o seed**. Também é necessário manter cópias de segurança estáticas dos canais (SCB) para recuperar os fundos bloqueados nos canais.


![Wallet Creation Screen](assets/en/04.webp)



## Visão geral do painel de controlo


Assim que o seu wallet for criado, será direcionado para o **Dashboard** principal.


![KaleidoSwap Dashboard](assets/en/05.webp)


nota: A captura de ecrã acima mostra um wallet que já foi financiado e tem canais activos. Um novo wallet apresentará saldos nulos e não terá canais activos até ser financiado


## Financiamento do seu Wallet


Para operar com activos RGB, é necessário financiar o seu wallet. O KaleidoSwap suporta o depósito de activos Bitcoin e RGB através de transacções on-chain ou Lightning Network.


### Depositar Bitcoin


1. Clique em **Depósito** no menu Acções rápidas.

2. Selecione **BTC** na lista de activos.


![Select BTC Asset](assets/en/06.webp)


3. Escolha o seu método de depósito: **On-chain** ou **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- Em cadeia**: Digitalize o código QR ou copie o endereço para enviar o Bitcoin a partir de outro wallet.
- Relâmpago**: Gerar uma fatura com o montante pretendido.


![BTC On-chain Deposit](assets/en/08.webp)


### Depositar activos RGB e UTXOs coloridos


Para receber activos RGB (como o USDT), são necessários UTXOs específicos disponíveis para serem "coloridos" (atribuídos a um ativo).


1. Clique em **Deposit** e selecione o ativo RGB (por exemplo, USDT). **Importante**: Se esta for a **primeira vez** que o seu nó está a receber este ativo específico, **deixe o campo ID do ativo vazio**. Introduzir um ID para um ativo desconhecido fará com que o nó retorne um erro, uma vez que ainda não o reconhece.

2. Escolha **Em cadeia** ou **Relâmpago**.


![USDT Deposit Options](assets/en/09.webp)


#### Modos de receção em cadeia: Testemunha vs. Cego


Ao receber activos RGB on-chain, existem dois modos de privacidade:



- Receção cega (recomendada para privacidade)**: O utilizador fornece um UTXO "blinded" ao remetente. Está a pedir ao remetente para enviar activos para um UTXO existente que possui, mas ofusca o identificador real do UTXO. Isto oferece uma melhor privacidade.
- Receção de testemunhas**: O utilizador fornece um endereço Bitcoin padrão. Está a pedir ao remetente que crie um *novo* UTXO para si, enviando os activos para esse endereço. Isto permite que os activos do RGB sejam anexados diretamente ao novo UTXO criado pela transação.


#### Depósito relâmpago


Para depósitos Lightning, basta generate uma fatura. O ativo RGB será encaminhado para si através dos seus canais abertos.


![USDT Lightning Invoice](assets/en/10.webp)



## Abrir canais com activos RGB


Para encaminhar os activos do RGB através do Lightning Network, é necessário um canal com liquidez e alocação de activos suficientes. A maneira mais fácil de começar é **Comprar um Canal** de um LSP (Lightning Service Provider).


### Comprar um canal ao Kaleido LSP


1. Vá para o separador **Canais**. Verá opções para "Abrir canal" (manual) ou "Comprar canal" (LSP).

2. Clique em **Canal de compra**.


![Channels Dashboard](assets/en/11.webp)


3. **Ligar ao LSP**: A aplicação ligar-se-á ao LSP Kaleido por defeito. Este fornecedor oferece liquidez de entrada e suporta o encaminhamento de activos RGB.


![Connect to LSP](assets/en/12.webp)


4. **Configurar canal**:


    - Capacidade**: Selecione a capacidade total de Bitcoin para o canal.
    - Atribuição do RGB**: Escolha o ativo RGB (por exemplo, USDT) que pretende receber ou enviar. O LSP assegurará que o canal está configurado para suportar este ativo.


![Configure Channel](assets/en/13.webp)



    - Atribuição do RGB**: Escolha o ativo RGB (por exemplo, USDT) que pretende receber ou enviar. O LSP assegurará que o canal está configurado para suportar este ativo.


![RGB Allocation](assets/en/14.webp)


5.  **Pagamento**: Deve pagar uma taxa ao LSP para abrir o canal e fornecer liquidez. Pode pagar usando **Lightning** ou **On-chain** Bitcoin. O pagamento pode ser efectuado a partir do seu KaleidoSwap wallet interno ou de um wallet externo.


![Complete Payment](assets/en/15.webp)


6. Assim que o pagamento for confirmado, o LSP iniciará a transação de abertura do canal. Aparecerá um ecrã **Ordem concluída**.


![Order Completed](assets/en/16.webp)


7. Após a confirmação na blockchain, o teu canal estará ativo e pronto para transferências RGB.



## Negociação: Modelo Taker-Maker


O motor de negociação do KaleidoSwap funciona num modelo **Taker-Maker**. Pode trocar activos manualmente com um par ou utilizar um Criador de Mercado (LSP).


### Troca com um criador de mercado (LSP)


Esta é a forma mais comum de negociar. O cliente actua como **Taker**, executando ordens contra a liquidez disponível fornecida pelo LSP (**Maker**).


1. Navegue até ao separador **Comércio** e selecione **Criador de mercado**.

2. **Introduzir o montante**: Introduza o montante de Bitcoin que pretende enviar (ou o ativo que pretende receber). A interface mostrará a taxa de câmbio e as taxas estimadas.


![Market Maker Swap](assets/en/17.webp)


3. **Confirmar troca**: Reveja os detalhes, incluindo a taxa de câmbio e o montante exato que irá receber. Clique em **Confirmar troca**.


![Confirm Swap](assets/en/18.webp)


4. **Processamento**: A troca é executada atomicamente no Lightning Network. É apresentado um ecrã de estado que indica que a troca está pendente.


![Swap Pending](assets/en/19.webp)


5. **Sucesso**: Uma vez que os HTLCs são liquidados, o swap está completo e os activos estão no seu canal.


![Swap Success](assets/en/20.webp)



## Programador API


Para os programadores que constroem com base no KaleidoSwap, a aplicação expõe um API que suporta:



- RGB LSPS1**: Para serviços de liquidez automatizados.
- Swap API**: Para negociação programática e criação de mercado.
- WebSocket**: Para subscrições de dados de mercado em tempo real.


Consulte a [Documentação API](https://docs.kaleidoswap.com/api/introduction) para obter informações completas sobre os pontos finais e as especificações.


## Conclusão


O KaleidoSwap permite-lhe aproveitar a privacidade e a escalabilidade dos activos do RGB no Lightning Network. Ao entender os UTXOs coloridos e a alocação de ativos de canal, você pode utilizar totalmente esse poderoso protocolo de troca descentralizado.