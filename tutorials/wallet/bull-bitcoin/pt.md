---
name: Bull Bitcoin Wallet
description: Saiba como utilizar o Wallet Bull Bitcoin
---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=6b0xTB2sE8E)


*Este tutorial em vídeo da BTC Sessions acompanha-o no processo de configuração e utilização do Bull Bitcoin Wallet!


Este guia leva-o através da instalação, configuração e utilização do Bull Bitcoin Wallet. Aprenderá a enviar e receber fundos nas redes Bitcoin On-Chain, Liquid e Lightning, bem como a mover o Bitcoin entre elas. As extensas funcionalidades do wallet fazem dele uma ferramenta poderosa e completa para gerir o seu Bitcoin. Vamos começar.


## Introdução


Bull Bitcoin Wallet, desenvolvido por [Bull Bitcoin](https://www.bullbitcoin.com/), é um **self-custodial** Bitcoin wallet, o que significa que tem controlo total sobre as suas chaves privadas e, portanto, sobre os seus fundos, sem depender de terceiros. De código aberto e enraizado numa filosofia Cypherpunk, este Wallet combina simplicidade, confidencialidade e funcionalidades avançadas, como swaps entre redes e suporte PayJoin. Permite-lhe gerir os seus bitcoins em três redes: **Bitcoin onchain**, **Liquid** e **Lightning**, cada uma adaptada a utilizações específicas. No [BullBitcoin GitHub] (https://github.com/orgs/SatoshiPortal/projects/49), pode consultar os tópicos actuais e os próximos desenvolvimentos. Como o projeto é 100% open-source e "construído em público", pode também enviar as suas sugestões e quaisquer erros que encontre. Embora algumas carteiras suportem agora múltiplas redes, o Bull Bitcoin Wallet destaca-se por integrar profundamente as caraterísticas de privacidade em todas elas, tornando-o uma ferramenta poderosa para gerir o seu Bitcoin em todas as principais redes


## 1️⃣ Pré-requisitos


Antes de começar a utilizar o **Bull Bitcoin Wallet**, certifique-se de que possui os seguintes itens:



- Smartphone compatível**: Um dispositivo **iOS** (iPhone ou iPad) ou **Android**
- Ligação à Internet
- Suportes de cópia de segurança seguros**: Escreva a sua **frase de recuperação** (12 palavras) em papel ou metal e guarde-a num local seguro.
- Conhecimentos básicos**: É útil ter um conhecimento mínimo dos conceitos do Bitcoin (endereços, transacções, taxas), embora este tutorial explique cada passo para os principiantes.


## 2️⃣ Instalação


Pode instalar a aplicação através de:



- [Apple App Store](https://apps.apple.com/app/bull-bitcoin/id6743380972)[ ](https://apps.apple.com/us/app/bitchat-mesh/id6748219622)(para dispositivos iOS)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bullbitcoin.mobile&hl=en) (para dispositivos Android)


Os utilizadores do Android também têm opções alternativas:



- Baixe o APK diretamente da página [GitHub Releases](https://github.com/SatoshiPortal/bullbitcoin-mobile/releases) ou
- Instalar através da [Zapstore] compatível com o Nostr (https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqtxxmmd9e382mrvvf5hgcm0d9hzumt0vf5kcegnah0ap)


Depois de instalar a aplicação, siga o ecrã de boas-vindas para configurar a sua conta.


## 3️⃣ Configuração inicial


Ao abrir, são-lhe apresentadas as seguintes opções:



- `Criar novo Wallet`
- `Recover Wallet` e
- `Opções avançadas`


Comecemos por tocar em `Opções avançadas`.


Aqui, podemos configurar as definições avançadas antes de criar ou recuperar um wallet:


1. Habilite o `Tor proxy` para rotear o tráfego através da rede Tor.

1. a [aplicação Orbot] (https://orbot.app/en/) tem de estar instalada e a funcionar antes de ser activada

2. O Tor Proxy só se aplica ao Bitcoin (não ao Liquid) e pode resultar numa ligação mais lenta.

2. Configurar um `Electrum Server personalizado`, ou

3. Ajustar as definições do `Recover Bull`. Iremos aprender mais sobre o [Recover Bull](https://recoverbull.com/) mais tarde.


Depois de efetuar todos os ajustes opcionais, toque em "Concluído". Se desejar reutilizar um Wallet existente, clique em `Recuperar Wallet` e preencha as 12 palavras da sua frase de recuperação.


Caso contrário, clique em `Criar um novo Wallet`.


![image](assets/en/01.webp)


## 4️⃣ Ecrã inicial


Antes de nos aprofundarmos, vamos dar uma vista de olhos ao `Home Screen` para nos orientarmos:



- o menu `síntese das transacções` e `configurações` está localizado no topo.
- O "Saldo disponível" tem uma opção de privacidade que pode ser "activada ou desactivada".
- Aceder ao `Bitcoin Bull Exchange` para `Comprar, Vender ou Pagar` (isto depende da jurisdição e pode exigir KYC).
- `Transferência` de fundos entre carteiras
- `Secure Bitcoin` igual a Onchain Bitcoin Wallet
- `Pagamentos instantâneos` via Lightning- / Liquid Network *(Nota: Bull Bitcoin Wallet permite efetuar e receber pagamentos via Lightning. Os fundos recebidos via Lightning são armazenados na rede [*Liquid](https://liquid.net/) (nos pagamentos instantâneos Wallet) graças a uma troca automática via [*Boltz exchange](https://boltz.exchange/). Isto permite-lhe interagir com Lightning sem ter de gerir canais de liquidez, mantendo-se em auto-custódia.)*
- `Emissão` e `Recebimento` de fundos


![image](assets/en/02.webp)


Primeiro, vamos fazer algumas configurações importantes e começar com o `Backup`.


## 5️⃣ Cópia de segurança


Para iniciar o processo de cópia de segurança, toque no `ícone da engrenagem (⚙)` no canto superior direito da aplicação e selecione `Wallet Backup`. Ser-lhe-ão apresentados dois métodos para proteger o seu wallet: `Encrypted Vault` e `Physical Backup`. Vamos explorar cada um deles.


![image](assets/en/03.webp)


### Cópia de segurança física


Toque em `Physical Backup` para ver uma lista de 12 palavras que representam a sua frase de recuperação ou seed. Por favor, considere o seguinte:



- Escreva a sua "frase de recuperação" com o máximo cuidado. Escreva-a em papel ou metal e guarde-a num local seguro (cofre, local offline). Esta frase é o único meio de aceder aos seus bitcoins em caso de perda do seu dispositivo ou de eliminação da aplicação.
- Também é importante notar que qualquer pessoa com esta frase pode roubar todos os seus bitcoins. Nunca as armazene digitalmente:
- Sem captura de ecrã
- Sem cópias de segurança na nuvem, por correio eletrónico ou por mensagens
- Sem copiar/colar (risco de guardar na área de transferência)


![image](assets/en/25.webp)


No ecrã seguinte, terá de colocar as palavras na ordem correta para se certificar de que a frase seed está correta. Receberá uma confirmação quando o teste estiver concluído e for bem sucedido.


! **Este ponto é crítico**. Para mais assistência :


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

### Cofre encriptado


Existe também a opção de uma cópia de segurança encriptada e anónima na nuvem. Mas não mencionámos no último parágrafo que as cópias de segurança na nuvem são arriscadas e devem ser evitadas? No entanto, a equipa do Bull Bitcoin desenvolveu uma forma inteligente de tornar o processo seguro. Eis como funciona:


o `Recoverbull` é um protocolo de backup que simplifica a segurança do seu Bitcoin wallet, dividindo o backup em duas partes. Primeiro, o ficheiro de backup do seu wallet é encriptado no seu dispositivo usando uma chave de encriptação forte. Pode guardar este ficheiro encriptado onde quiser, como o Google Drive ou o seu dispositivo. Em segundo lugar, a chave de criptografia necessária para desbloquear o arquivo é armazenada pelo Recoverbull Key Server. Para recuperar o seu wallet, precisa tanto do ficheiro de backup encriptado como da chave, à qual acede com o seu PIN ou palavra-passe. Este design garante que o seu backup na nuvem, por si só, é inútil e que o servidor de chaves, por si só, é inútil sem o seu ficheiro de backup específico. Isto mantém os seus fundos seguros mesmo que uma parte seja comprometida.


Pense nisto como um cofre de segurança. O ficheiro de cópia de segurança encriptado é a *caixa*, que pode armazenar em qualquer lugar (como o Google Drive). O seu PIN de recuperação é a *chave*, que é armazenada separadamente pelo servidor de chaves do Recoverbull. Um ladrão teria de obter tanto a sua caixa específica como a sua chave específica para a abrir. Este design garante que mesmo que alguém obtenha o seu ficheiro de backup, este é inútil sem a chave do servidor, e a chave do servidor é inútil sem o seu ficheiro de backup único.


Saiba mais sobre o protocolo de backup `Recoverbull` wallet [aqui] (https://recoverbull.com/).


Toque em `Cofre encriptado` e depois em `Continuar` para confirmar a utilização do servidor predefinido. A ligação será encaminhada através da rede `Tor` para garantir a privacidade e o anonimato.


**Compreender os seus PINs



- `PIN de desbloqueio da aplicação`**:** O PIN opcional definido em `Configurações > PIN de segurança` para bloquear a aplicação no telemóvel.
- `PIN de recuperação`**:** O PIN obrigatório criado durante o processo de backup do `Encrypted Vault`, utilizado para desencriptar o seu ficheiro de backup durante a recuperação.


Estes são dois PINs separados. Não se esqueça do seu PIN de recuperação, pois é essencial para restaurar o seu wallet."


**Configuração do PIN de recuperação:**



- Deve criar um PIN ou uma palavra-passe para recuperar o acesso ao seu wallet.
- O PIN / Palavra-passe deve ter pelo menos 6 dígitos (por exemplo, evite sequências simples como 123456, que não são aceites).
- Sem este PIN, a recuperação do wallet é impossível.


Em seguida, selecione um fornecedor de cofre:



- `Google Drive` ou
- uma "localização personalizada" (por exemplo, o seu dispositivo)


![image](assets/en/04.webp)


Agora, guarde o "ficheiro de cópia de segurança". Em seguida, toque em `Test Recovery`, selecione o ficheiro de cópia de segurança ou o cofre guardado e, em seguida, toque em `Decrypt Vault`. Introduza o seu `PIN` ou `Password`. Se tudo tiver funcionado, aparecerá o ecrã `Teste concluído com êxito`.


### Etiquetas de importação/exportação


Agora que criámos a nossa cópia de segurança, vamos dar uma vista de olhos em "Etiquetas".  O Bull Bitcoin wallet aumenta a privacidade e a organização ao permitir que os utilizadores criem etiquetas personalizadas para os seus endereços de receção e transacções. Estas etiquetas ajudam-no a categorizar os seus fundos, uma vez que as transacções enviadas para um endereço etiquetado herdarão essa etiqueta, e também pode etiquetar as transacções de saída para acompanhar a sua mudança. O wallet suporta totalmente a norma [BIP-329](https://bip329.org/), o que significa que pode exportar todas as suas etiquetas para um ficheiro e importá-las para outro wallet. Esta caraterística assegura que pode fazer cópias de segurança do seu histórico de transacções e categorizações, ou migrá-las entre diferentes instâncias do wallet, sem perder a sua organização personalizada.


![image](assets/en/05.webp)


## 6️⃣ Definições


Com a sua cópia de segurança principal protegida, vamos explorar as outras funcionalidades disponíveis nas definições.


### A - Garantir o acesso


Para proteger a aplicação, navegue para `Configurações` e escolha `PIN de segurança` para selecionar o Código PIN. Crie um PIN forte para bloquear o acesso ao seu wallet. Embora este passo seja opcional, é altamente recomendado para evitar o acesso não autorizado se outra pessoa utilizar o seu telemóvel.


![image](assets/en/06.webp)


### B - Ligação a um nó pessoal (opcional)


O BullBitcoin Wallet liga-se aos servidores Electrum por defeito: o primeiro gerido pelo Bull Bitcoin e um servidor secundário da Blockstream, ambos considerados como não guardando registos, o que reduz o risco de rastreio.


Para uma maior confidencialidade, é possível ligar a aplicação ao seu próprio nó Bitcoin através de um servidor Electrum. Para o fazer, toque em `Configurações` > `Configurações Bitcoin` > `Configurações Electrum Server` e, em seguida, toque em `+ Adicionar servidor personalizado` para introduzir o endereço e as credenciais do seu servidor.


![image](assets/en/07.webp)


### C - Moeda


O saldo disponível é apresentado no ecrã principal em `sats` e `USD`. Para alterar isso, navegue até `Configurações` > `Moeda`. Aí, pode alternar entre `sats/BTC` e selecionar a sua `moeda fiduciária predefinida`.


![image](assets/en/08.webp)


### D - Definições do Bitcoin


O menu `Bitcoin Settings` oferece um acesso profundo às principais configurações e dados do seu wallet. Aqui, pode inspecionar os detalhes fundamentais do seu `Secure Bitcoin` e `Instant payments wallets`, dando-lhe total transparência e controlo. As principais caraterísticas deste menu incluem:



- Detalhes do Wallet:** Navegue para o seu Secure Bitcoin ou Instant payments wallet para ver informações específicas.
- Impressão digital do Wallet:** Um identificador único para o seu wallet.
- Chave pública (Pubkey):** A chave utilizada para os endereços de receção generate do Bitcoin.
- Descriptor:** Um resumo técnico da estrutura do seu wallet.
- Caminho de derivação:** O caminho específico utilizado para generate todos os endereços da sua chave mestra privada.
- Address View:** Aceder a uma lista dos seus endereços de receção não utilizados e alterar endereços (brevemente)


Além disso, tem a opção de:



- configurações de "Ativar transferência automática" para definir um saldo máximo instantâneo do wallet, que será automaticamente transferido para o seguro bitcoin wallet.
- Importar carteiras genéricas através da frase `Mnemonic` ou importar `watch-only`
- Ligar `Hardware wallets`: os dispositivos atualmente suportados são ColdcardQ, SeedSigner, Specter, Krux, Blockstream Jade e Foundation Passport


## 7️⃣ Bull Bitcoin Exchange


Diretamente a partir do wallet, tem acesso à [bolsa Bull Bitcoin] (https://www.bullbitcoin.com/), permitindo-lhe comprar, vender e pagar Bitcoin sem sair da aplicação. Esta integração fornece uma solução conveniente para gerir as suas necessidades de Bitcoin. Esteja ciente de que o acesso à bolsa e aos seus serviços pode ser restrito com base na sua jurisdição, e a verificação do Know Your Customer (KYC) pode ser necessária para cumprir os padrões regulatórios e usar todos os recursos da plataforma.


Para começar, toque em `Exchange` no canto inferior direito e, em seguida, em `Assinar` ou `Login` na sua conta.


A bolsa oferece as seguintes [caraterísticas] (https://www.bullbitcoin.com/):



- Comprar Bitcoin com auto-custódia a partir da sua conta bancária
- Sem custódia
- Pessoas singulares ou colectivas
- Levantamento imediato
- Sem taxas ocultas
- Lightning Network disponível
- Sem limites de transação
- Opções de compra recorrentes


![image](assets/en/09.webp)


Para saber mais, consulte este tutorial:


https://planb.academy/en/tutorials/exchange/centralized/bull-bitcoin-europe-0ccf713e-efcd-44ec-8205-211f49ac7d53

## 8️⃣ Receção de fundos


A receção de fundos com o **Bull Bitcoin Wallet** é simples e flexível, suportando três redes distintas adaptadas a diferentes casos de utilização:



- A rede `Bitcoin (onchain)` para um armazenamento seguro e a longo prazo.
- A rede `Liquid` para transacções rápidas e mais confidenciais.
- A rede `Lightning` para pagamentos instantâneos e de baixo custo.


A aplicação gera automaticamente o endereço ou a fatura adequados com base na rede selecionada. Eis como proceder para cada rede.


### Receção via Onchain (rede Bitcoin)


Para receber fundos do on-chain, pode selecionar `Secure Bitcoin Wallet` no ecrã inicial e tocar em `Receber`, ou tocar no botão principal `Receber` e depois escolher a `Rede Bitcoin`.


Existem dois modos principais para gerar um endereço de receção:


**Modo predefinido (URI com parâmetros de entrada adicionais)


Por defeito, o wallet gera um [BIP21 URI] (https://bips.dev/21/). Trata-se de um formato normalizado que inclui mais informações do que um simples endereço, incluindo um montante, uma nota pessoal e parâmetros PayJoin para aumentar a privacidade. Este URI abrangente é codificado num código QR e disponibilizado para cópia. O formato é o seguinte: `bitcoin:<address>?<parameter1>=<value1>&<parameter2>=<value2>`.



- Parâmetros de entrada adicionais:**
    - Montante:** Especifique um montante solicitado em BTC, sats ou numa moeda fiduciária.
    - Mensagem:** Adicionar uma nota pessoal que será visível para o remetente.
    - PayJoin:** Ativar esta opção para melhorar a privacidade, combinando as entradas do remetente e do destinatário na transação.


Exemplo de URI:


```
bitcoin:bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54xxxxx?amount=0.0005&message=Tip+for+tutorial&pj=HTTPS%3A%2F%2FPAYJO.IN%2F78UH9WZUP8KKJ%23RK1Q2H30FASCU9WW09DQY2LK0K8P2DPRJ99V72CA78ACQAEL675QYTMQ+OH1QYP87E2AVMDKXDTU6R25WCPQ5ZUF02XHNPA65JMD8ZA2W4YRQN6UUWG+EX1L0LYV6G
```


*Nota importante: Não envie quaisquer fundos para os endereços indicados neste tutorial, pois o wallet será eliminado


![image](assets/en/10.webp)


**Opção de copiar ou digitalizar apenas Address activada


Com a opção `Copiar ou digitalizar apenas Address` activada, a aplicação gera um endereço Bitcoin simples no formato SegWit (bech32).


Exemplo:


```javascript
bc1q0vv86t2sj7daduvdc50njms6u6jzh2y54x3g56
```


Mesmo que introduza um montante ou uma nota, estes não serão incluídos no código QR ou no endereço copiado.


![image](assets/en/11.webp)


### Receção através do Liquid Network


É possível receber um pagamento no Liquid Network. Uma vez no ecrã "Receber", existem as mesmas duas opções para gerar um pedido de pagamento:


**1. Address simples:** Copiar o endereço padrão `Liquid`. Este é um identificador único para o seu wallet na rede Liquid e não inclui qualquer montante ou mensagem específica.


Exemplo Address:


```javascript
lq1qq05k3vmnvbullbitcoinjujn6h04z9jtw53xuyktqf9mam2zpfz05j2fe2x8xhejgkga3nvmp4yyp35qynkcw2xqmy7xxxxxxx
```


**2. Pedido de pagamento pormenorizado (URI):** Para um pedido mais estruturado, pode especificar um montante e uma nota pessoal. Estas informações são automaticamente codificadas num URI partilhável e no código QR correspondente.



- Montante:** Pode definir o montante em Bitcoin (BTC), Satoshis (Sats) ou numa moeda fiduciária.
- Nota:** Adicionar uma mensagem pessoal para identificar a transação.


**Exemplo de URI:**


```javascript
liquidnetwork:lq1qqdhgs7w537nun55a5sdy4gxkd08pclk3d7v4qz36sy4xp0cq6gvl52fcfv7kdgkgzmfycrud0zsygqgyjclycckpasxxxxxx?amount=0.00001&message=Test&assetid=6f0279e9ed041c3d710a9f57d0c02928416460c4b722ae3457a11eec381c526d
```


Para concluir a transação, forneça ao remetente o `endereço` ou `URI`. Pode fazê-lo copiando-o para a sua área de transferência ou pedindo ao remetente que digitalize o código QR diretamente a partir do seu ecrã.


![image](assets/en/12.webp)


### Receber via Lightning



O Bull Bitcoin Wallet também lhe permite enviar e receber pagamentos através do Lightning Network. Uma caraterística chave é que os fundos recebidos via Lightning são automaticamente trocados e armazenados no `Liquid Network` dentro do seu `Instant Payments Wallet`. Este serviço é alimentado pelo `Boltz`. Esse design permite que você aproveite a velocidade e o baixo custo do Lightning sem a complexidade de gerenciar canais de liquidez, mantendo a autocustódia total de seus fundos. Embora esta abordagem híbrida seja autocustodial e evite a complexidade da gestão de canais, introduz um serviço de terceiros (Boltz), uma pequena taxa de swap e a dependência da federação de funcionários do Liquid Network como detentores de chaves, o que é diferente de um Lightning wallet tradicional, sem custódia, em que gere os seus próprios canais. Pode saber mais sobre o Liquid e o seu modelo de governação aqui:


https://planb.academy/en/courses/e17ee350-41d4-49fa-b270-29e4d26d22f8/overview-of-liquid-architecture-and-governance-model-17650c4b-cd1f-4bc6-b490-708f92dc9306


- Limites:**
    - Montante mínimo:** É necessário um montante mínimo de faturação. Consulte a aplicação para obter o limite atual
    - Taxas:** Você, o destinatário, é responsável por uma pequena taxa de troca. Esta taxa é deduzida do montante que o remetente transfere e está sujeita a alterações
- Benefícios:**
    - Auto-Custódia:** Os seus fundos estão sempre sob o seu controlo, protegidos na rede Liquid.
    - Evite as elevadas taxas On-Chain:** Ao utilizar o Lightning e armazenar no Liquid, evita as taxas on-chain associadas à abertura de um canal Lightning tradicional. Pode optar por transferir fundos para um canal on-chain mais tarde, quando o montante acumulado justificar a despesa.
    - Sugestão:** Para uma transação mais económica entre dois utilizadores do Bull Bitcoin, utilize diretamente a rede **Liquid** para evitar totalmente as taxas de troca do Lightning.


Para receber um pagamento, é necessário generate uma "fatura relâmpago":


1. `Digite um valor`**:** Especifique o valor que deseja receber em Bitcoin (BTC), Satoshis (Sats) ou uma moeda fiduciária.

2. `Adicionar uma nota` **(Opcional):** Incluir um memorando ou nota. Esta será incorporada na fatura e apresentada no seu histórico de transacções quando o pagamento estiver concluído, facilitando a sua identificação.

3. a fatura Lightning é sensível ao tempo e expira após **12 horas**. Se não for paga dentro deste período, torna-se inválida e terá de efetuar uma nova fatura.


Forneça a fatura ao remetente copiando-a para a sua área de transferência ou permitindo que ele leia o código QR apresentado no seu ecrã.


![image](assets/en/13.webp)


## 9️⃣ Envio de fundos


Pode aceder ao ecrã de envio diretamente a partir da página inicial ou a partir de qualquer uma das suas carteiras. O Bull Bitcoin Wallet simplifica o processo, detectando automaticamente a rede de destino - `Bitcoin`, `Liquid` ou `Lightning` - com base no endereço ou na fatura que introduzir, quer seja colada ou digitalizada através de um código QR.


### On-Chain Transmissão através da rede Bitcoin


O envio de fundos on-chain significa que a sua transação é registada diretamente na cadeia de blocos Bitcoin. Este método é melhor para transferências maiores ou transferências não sensíveis ao tempo. Para começar, pode tocar no `Botão Enviar` em baixo à direita, e digitalizar ou introduzir um `endereço Bitcoin padrão`.


Se o endereço fornecido não incluir um montante específico, ser-lhe-á pedido que preencha os detalhes no ecrã de envio. Pode especificar o montante na sua unidade preferida, como BTC, satoshis ou um equivalente fiduciário. Também tem a opção de adicionar uma nota pessoal, que é um memorando privado para sua própria referência para o ajudar a identificar a transação mais tarde. Esta nota não é partilhada com o destinatário.


Em contrapartida, se o pedido de pagamento que digitalizar ou colar já contiver todos os dados necessários, como um BIP21 URI com um montante pré-definido, o wallet ignorará o ecrã de introdução de dados e levá-lo-á diretamente ao ecrã de confirmação para autorizar o pagamento.


![image](assets/en/14.webp)


Antes de a sua transação ser transmitida, ser-lhe-á apresentado um ecrã de confirmação. É crucial reservar um momento e rever cuidadosamente todos os parâmetros, prestando muita atenção ao endereço do destinatário, ao montante que está a ser enviado e às taxas de rede. Este ecrã também fornece ferramentas poderosas para personalizar a sua transação.


É possível controlar as taxas de duas formas principais. O primeiro método consiste em selecionar uma velocidade de transação desejada, como baixa, média ou alta, e o wallet calculará automaticamente a taxa adequada. O segundo método permite um controlo mais preciso, permitindo-lhe definir uma taxa específica, quer como um total absoluto em satoshis, quer como uma taxa relativa por byte, que depois fornece um tempo de confirmação estimado.


Para utilizadores avançados, o wallet oferece várias definições para afinar a transação. o `Replace-by-Fee` (RBF) está ativado por defeito, o que é uma caraterística valiosa que lhe permite acelerar uma transação se esta ficar presa no mempool, retransmitindo-a com uma taxa mais elevada. Também é possível selecionar manualmente quais as `Unspent Transaction Outputs` (UTXOs) a partir das quais gastar. Esta é uma ferramenta poderosa para a consolidação UTXO, uma estratégia em que se combinam várias entradas pequenas numa única maior. Embora isso possa custar mais em taxas para a transação atual, pode reduzir significativamente as taxas em transações futuras, especialmente se houver previsão de aumento das taxas de rede.


![image](assets/en/15.webp)


O PayJoin é automaticamente ativado quando digitaliza o pedido de pagamento de um destinatário (um URI BIP21) que inclui um parâmetro `pj=`. Se simplesmente colar um endereço simples, sem parâmetros adicionais, esta funcionalidade não será activada. Este método colaborativo melhora a privacidade ao combinar os dados do remetente e do destinatário, quebrando a heurística da propriedade de dados comuns e permitindo um melhor escalonamento e poupança de taxas em algumas circunstâncias.


### Envio para o Liquid Network


O `Liquid Network` foi concebido para transacções rápidas e confidenciais com taxas mínimas. Quando envia fundos através do Liquid, estes são retirados do seu `Instant Payments Wallet`. O processo é simples: basta introduzir ou digitalizar o `endereço Liquid` do destinatário.


Se o endereço não especificar um montante, ser-lhe-á pedido que indique um montante no ecrã de envio. Pode introduzir o montante em BTC, satoshis ou fiat. Uma das principais vantagens do Liquid é o seu baixo limite mínimo. Tal como nas transacções on-chain, pode adicionar uma nota pessoal opcional para os seus próprios registos. Se o pedido de pagamento já incluir um montante, o wallet passará diretamente para o ecrã de confirmação.


No ecrã de confirmação de uma transação Liquid, poderá rever os detalhes. As taxas são notavelmente baixas e são calculadas com base na complexidade da transação. Normalmente, são de cerca de 0,1 sat/vB, o que, para uma transação simples, equivale a apenas 20-40 satoshis (por exemplo, 26 satoshis em 21 de dezembro de 2025).


![image](assets/en/16.webp)


### Envio para o Lightning Network


Pode digitalizar um Lightning Address (por exemplo, `runningbitcoin@rizful.com`), que lhe permite definir o montante e uma nota opcional para o destinatário, ou digitalizar uma fatura com um montante predefinido, que o leva diretamente para o ecrã de confirmação.


*Note-se que se aplicam montantes mínimos e taxas.*


O Bull Bitcoin Wallet envia pagamentos Lightning retirando fundos do seu `Instant Payments Wallet` (no Liquid) e trocando-os através do `Boltz`. Essa abordagem híbrida é totalmente autocustodial e evita as altas taxas on-chain de gerenciamento de um canal Lightning dedicado, mas exige o pagamento de uma `taxa de troca`. Para obter o menor custo, envie diretamente para o endereço Liquid de um destinatário se ele também usar um Bull Bitcoin wallet.


## transferir fundos entre as suas carteiras


O Bull Bitcoin permite mover seu Bitcoin entre seu `Secure Bitcoin` wallet e seu `Instant Payments Wallet` no Liquid Network ou para um `externo Wallet`. Para realizar uma transferência, basta navegar até a seção `Transferência`, selecionar as carteiras de origem e destino, digitar o valor que deseja mover e confirmar a transação.


![image](assets/en/17.webp)


## 1️⃣1️⃣ Recuperando seu Bull Bitcoin Wallet


Esta secção explica como recuperar o acesso aos seus fundos Bull Bitcoin Wallet se perder o seu dispositivo, desinstalar a aplicação ou simplesmente precisar de mudar para um novo dispositivo. Como já foi explicado, existem dois métodos principais de recuperação: utilizando o método exclusivo `Recoverbull` e utilizando uma `frase BIP39 seed` padrão.


### Método 1: Recoverbull


Recapitulação: As cópias de segurança do Wallet são encriptadas localmente. O ficheiro encriptado pode ser armazenado no armazenamento em nuvem ou noutro dispositivo. A chave de encriptação é armazenada pelo Servidor de Chaves Recoverbull. Ambos são mantidos separados e devem ser combinados para recuperar um wallet.


Para começar, vou apagar o Wallet com todos os fundos e reinstalar o wallet. Vamos chegar novamente ao "ecrã de boas-vindas". Desta vez, selecione a opção `Recover Wallet`. Depois, navegue até ao método `Encrypted Vault`, confirme a utilização do `Default Key server` e selecione a localização ou `Vault provider` onde guardou o ficheiro de cópia de segurança.


![image](assets/en/18.webp)


O ecrã indica que o cofre foi importado com sucesso. Toque no botão `Decriptar Cofre` e introduza o `PIN`. O ecrã seguinte mostrará os seus `saldos` e o `número de transacções` que foram recuperadas.


![image](assets/en/19.webp)


### Método 2: Frase-semente


Este método utiliza a frase de recuperação principal do seu wallet, uma lista padrão de 12 palavras que serve como a melhor cópia de segurança para os seus fundos. É a forma mais universal de recuperar um Bitcoin wallet, uma vez que não está ligada a nenhum serviço ou servidor específico. Desde que tenha esta frase, pode restaurar o seu wallet em qualquer dispositivo compatível, mesmo sem acesso ao servidor de chaves Bull Bitcoin.


No ecrã de boas-vindas, selecione `Recover Wallet`. Desta vez, escolha o método `Physical backup`. A aplicação apresentará uma grelha de palavras. Selecione cuidadosamente cada palavra da sua frase de 12 palavras seed na ordem correta. Seja meticuloso, pois um único erro resultará num wallet incorreto.


## 1️⃣2️⃣ Ligação de um Hardware Wallet


Para o mais alto nível de segurança, muitos utilizadores do Bitcoin optam por guardar os seus fundos em `armazenamento a frio`. Isto significa manter as `chaves privadas` que controlam o seu Bitcoin num dispositivo que nunca está ligado à Internet. Um `hardware wallet` (ou dispositivo de assinatura) é um dispositivo físico especializado concebido exatamente para este fim. Funciona como um cofre digital para as suas chaves, assegurando que nunca são expostas às potenciais ameaças de um computador ou smartphone online.


Ao ligar um hardware wallet à aplicação Bull Bitcoin, obtém o melhor de dois mundos: a segurança intransigente do armazenamento a frio para as suas chaves privadas, combinada com as caraterísticas poderosas e a interface de fácil utilização do Bull Bitcoin wallet para visualizar saldos e gerir transacções. Neste capítulo final, mostrar-lhe-emos como ligar um hardware wallet, tal como um [Coldcard Q](https://coldcard.com/q), ao seu Bull Bitcoin wallet. Este tutorial não abordará a configuração de um Coldcard Q em profundidade; pode aprender sobre isso aqui:


https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

https://planb.academy/en/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

### Importação de um Wallet


![image](assets/en/26.webp)


Em primeiro lugar, no menu principal do seu Coldcard Q, selecione `Exportar Wallet` e, em seguida, escolha `Bull Wallet`. O seu Coldcard irá generate um código QR.


![image](assets/en/20.webp)


Abra o Bull Bitcoin Wallet e navegue até `Configurações` > `Configurações Bitcoin` > `Importar wallet` e selecione `Coldcard Q` no seu telefone e toque em `Abrir a câmara` para digitalizar este código QR e importar as chaves públicas do seu hardware wallet.


![image](assets/en/21.webp)


### Receber com Coldcard Q


Para receber o Bitcoin utilizando o seu Coldcard Q ligado, não é necessário que o dispositivo esteja fisicamente ligado ao seu telefone. O Bull Bitcoin Wallet já importou as chaves públicas necessárias, permitindo-lhe receber endereços generate por si só.


1. Toque no seu dispositivo de assinatura Coldcard Q importado e selecione `Receber`.

2. A aplicação apresentará automaticamente um novo endereço Bitcoin a partir do wallet do seu Coldcard.

3. Utilize este endereço para receber fundos. O Bitcoin será protegido diretamente com as chaves do hardware wallet, mesmo que o dispositivo esteja offline durante o processo.


![image](assets/en/22.webp)


### Envio com Coldcard Q


O envio do Bitcoin com o seu Coldcard Q requer a sua confirmação física para autorizar qualquer transação. Embora a aplicação Bull Wallet seja utilizada para criar a transação, a assinatura final só pode ser criada no próprio hardware wallet.


Para começar, abra o seu `Coldcard Q` wallet e toque em `Enviar`. Em seguida, "abra a câmara" para digitalizar o código QR do endereço de receção. Após a leitura, introduza o `montante` que pretende enviar e ajuste a `prioridade da taxa` conforme necessário.


Para mais opções, pode consultar as Definições avançadas. Aqui encontrará a opção `Substituir por taxa` (RBF), que está activada por defeito e permite-lhe acelerar uma transação bloqueada mais tarde. Também tem a opção `Coin Control`, que lhe permite selecionar manualmente os UTXOs específicos que pretende gastar.


Depois de ter revisto todos os detalhes, toque em `Mostrar PSBT` para preparar a transação.


![image](assets/en/23.webp)


Toque no botão `Scan` do seu Coldcard Q e utilize a sua câmara para digitalizar o código QR apresentado no seu telefone. O ecrã Coldcard mostra-lhe então todos os detalhes da transação. Verifique cuidadosamente o montante, o endereço do destinatário e o seu endereço de mudança. Se tudo estiver correto, prima o botão `Enter` no Q da Coldcard para assinar a transação. Em seguida, aparecerá no ecrã um código QR da transação assinada.


![image](assets/en/24.webp)


No Bull wallet, toque em "Terminei", depois toque no botão "Câmara" para digitalizar o código QR da "transação assinada" do seu Coldcard Q. O Bull Wallet apresentará agora um ecrã de resumo da transação assinada. Reveja-a uma última vez e depois toque em `Broadcast` Transaction. Isto finaliza o processo, enviando a transação para a rede Bitcoin, e os seus fundos seguirão o seu caminho.


## 🎯 Conclusão


Concluiu a sua viagem através do Bull Bitcoin Wallet. A aplicação coloca poderosas ferramentas de privacidade e segurança na ponta dos seus dedos, tornando as funcionalidades avançadas simples de utilizar. Ajuda a manter a privacidade com recursos como `PayJoin`, que esconde suas transações no blockchain, e `Tor integration`, que mascara sua atividade de rede de olhos curiosos. Para aqueles que querem o controlo final, pode ligar-se ao seu `nó pessoal Bitcoin` para deixar de depender de servidores de terceiros, e usar um `Hardware wallet` para manter as suas chaves privadas completamente offline e seguras. Com opções de backup inteligentes e suporte contínuo para Bitcoin, Liquid e Lightning, o Bull Bitcoin Wallet é uma escolha forte e completa para quem quer manter os seus fundos privados, seguros e totalmente sob o seu próprio controlo.


## 📚 Recursos do Bull Wallet


[Github](https://github.com/SatoshiPortal/bullbitcoin-mobile) | [Website ](https://www.bullbitcoin.com/)| [Recoverbull](https://recoverbull.com/)