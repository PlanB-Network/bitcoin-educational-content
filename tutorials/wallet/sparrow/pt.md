---
name: Pardal Wallet
description: Instalação, configuração e utilização do Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet é um software de gerenciamento de portfólio Bitcoin de autocustódia desenvolvido por Craig Raw. Este software de código aberto é apreciado pelos bitcoiners pelas suas muitas funcionalidades e Interface intuitivo.

Existem duas formas de utilizar o Sparrow:


- Como um Hot Wallet, em que as suas chaves privadas são armazenadas no seu PC.
- Como um gestor Cold Wallet, onde as chaves privadas são mantidas num Hardware Wallet. Neste modo, o Sparrow apenas manipula informações públicas do Wallet, rastreia fundos, gera endereços e cria transacções, mas a assinatura Hardware Wallet é necessária para tornar estas transacções válidas. Por conseguinte, pode substituir aplicações como o Ledger Live ou o Trezor Suite.

O Sparrow suporta carteiras de assinatura única e carteiras de assinatura múltipla e permite a gestão fluida de várias carteiras. Por exemplo, pode controlar simultaneamente um Wallet ligado a um Ledger, outro a um Trezor, e também ter um Hot Wallet.

O software também oferece funcionalidades avançadas de controlo de moedas, permitindo-lhe escolher com precisão quais os UTXOs a utilizar nas suas transacções para otimizar a sua confidencialidade.

Em termos de ligação, o Sparrow permite-lhe ligar-se ao seu próprio nó Bitcoin, quer remotamente através de um servidor Electrum, quer com o Bitcoin Core. Também é possível usar um nó público se ainda não tiveres o teu próprio nó. As conexões remotas são feitas via Tor.

## Instalar o Sparrow Wallet

Aceda à [página oficial de transferência do Sparrow Wallet] (https://sparrowwallet.com/download/) e escolha a versão do software que corresponde ao seu sistema operativo.

![Image](assets/fr/01.webp)

É importante verificar a integridade e a autenticidade do software antes de o instalar. Se não sabe como o fazer, encontrará um tutorial completo aqui :

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Uma vez instalado o Sparrow, pode saltar os ecrãs explicativos iniciais e ir diretamente para o ecrã de gestão da ligação.

![Image](assets/fr/02.webp)

## Ligação à rede Bitcoin

Para interagir com a rede Bitcoin e transmitir as suas transacções, o Sparrow deve estar ligado a um nó Bitcoin. Existem três formas principais de estabelecer esta ligação:


- usando um nó público, ou seja, conectando-se a um nó de terceiros que permite tais conexões. Se não tiver o seu próprio nó Bitcoin, esta opção permite-lhe começar a utilizar o Sparrow rapidamente. No entanto, o nó ao qual se liga verá todas as suas transacções, o que pode comprometer a sua confidencialidade. Ter controlo sobre as suas chaves é essencial, mas ter o seu próprio nó é ainda melhor. Por isso, use esta opção apenas se estiver a começar, tendo em conta os riscos para a sua privacidade.
- ligação a um nó Bitcoin Core. Se tiver o seu próprio nó Bitcoin Core, pode ligá-lo ao Sparrow Wallet, quer localmente, se o Bitcoin Core estiver instalado na mesma máquina, quer remotamente.
- ligação através de um servidor Electrum. Se o seu nó Bitcoin estiver equipado com Electrum, como é o caso das soluções node-in-a-box como o Umbrel ou o Start9, pode ligar-se a ele remotamente a partir do Sparrow.

**É preferível utilizar uma ligação via Electrs ou Bitcoin Core no seu próprio nó para reduzir a necessidade de confiar em terceiros e otimizar a sua confidencialidade**

### Ligar a um nó público 🟡

A ligação a um nó público é muito simples. Clique no separador "*Servidor público*".

![Image](assets/fr/03.webp)

Selecione um nó na lista pendente.

![Image](assets/fr/04.webp)

Em seguida, clique em "*Testar ligação*".

![Image](assets/fr/05.webp)

Uma vez ligado, o Sparrow Wallet apresentará um visto amarelo no canto inferior direito do Interface para indicar que está ligado a um nó público.

![Image](assets/fr/06.webp)

### Ligação a um núcleo Bitcoin 🟢

O segundo método de ligação a um nó Bitcoin é ligar o Sparrow a um Bitcoin Core. Se o Bitcoin Core estiver instalado na mesma máquina, a autenticação será feita através do arquivo cookie. Se o Bitcoin Core estiver em uma máquina remota, será necessário utilizar a senha definida no arquivo `Bitcoin.conf`.

Por favor, note que se você usar um nó Bitcoin Core podado, você não será capaz de restaurar um Wallet contendo transações anteriores aos blocos armazenados localmente. No entanto, para um novo Wallet criado no Sparrow, isso não será um problema: suas novas transações serão visíveis, mesmo com um nó podado.

Para configurar um nó Bitcoin Core, pode consultar um dos seguintes tutoriais, dependendo do seu sistema operativo:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3
https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed
No Sparrow, aceda ao separador "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Com o Bitcoin Core local:**

Se o Bitcoin Core estiver instalado no seu computador, localize o ficheiro `Bitcoin.conf` entre os ficheiros de software. Se esse arquivo não existir, é possível criá-lo. Abra-o com um editor de texto e insira a seguinte linha:

```ini
server=1
```

Em seguida, guarde as suas alterações.

Também o pode fazer através do gráfico Interface do Bitcoin-QT, navegando para "*Settings*" > "*Options...*" e activando a opção "*Enable RPC server*".

Não se esqueça de reiniciar o software depois de efetuar estas alterações.

![Image](assets/fr/08.webp)

Em seguida, retorne ao Sparrow Wallet e digite o caminho para o seu arquivo de cookie, geralmente localizado na mesma pasta que `Bitcoin.conf`, dependendo do seu sistema operacional:

| **macOS** | ~/Biblioteca/Apoio a aplicações/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Deixe os outros parâmetros como padrão, URL `127.0.0.1` e porta `8332`, depois clique em "*Testar conexão*".

![Image](assets/fr/10.webp)

A ligação é estabelecida. Aparecerá um visto Green no canto inferior direito para indicar que está ligado a um nó Bitcoin Core.

![Image](assets/fr/11.webp)

**Com Bitcoin Core remote:**

Se o Bitcoin Core estiver instalado noutra máquina ligada à mesma rede, primeiro localize o ficheiro `Bitcoin.conf` entre os ficheiros de software. Se este ficheiro ainda não existir, pode criá-lo. Abra este ficheiro com um editor de texto e adicione a seguinte linha:

```ini
server=1
```

Depois de editar o ficheiro, certifique-se de que o guarda na pasta adequada ao seu sistema operativo:

| **macOS** | ~/Biblioteca/Apoio a aplicações/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

Esta operação também pode ser efectuada através do Bitcoin-QT Interface gráfico Interface. Vá ao menu "*Settings*", depois "*Options...*", e active a opção "*Enable RPC server*" marcando a caixa correspondente. Se o ficheiro `Bitcoin.conf` não existir, pode criá-lo diretamente a partir deste Interface, clicando em "*Open Configuration File*".

![Image](assets/fr/12.webp)

Encontre o IP Address da máquina que aloja o Bitcoin Core na sua rede local. Para fazer isso, você pode usar uma ferramenta como [Angry IP Scanner] (https://angryip.org/). Vamos assumir, para fins de argumentação, que o IP Address do seu nó é `192.168.1.18`.

No ficheiro `Bitcoin.conf`, adicione as seguintes linhas, definindo `rpcbind=192.168.1.18` para corresponder ao IP Address do seu nó.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

No arquivo `Bitcoin.conf`, adicione um nome de usuário e senha para conexões remotas. Certifique-se de substituir `loic` pelo seu nome de usuário e `my_password` por uma senha forte:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Depois de modificar e guardar o ficheiro, reinicie o software Bitcoin-QT.

Pode agora regressar ao Sparrow Wallet. Vá para a aba "*User / Pass*". Digite o nome de usuário e senha que você configurou no arquivo `Bitcoin.conf`. Deixe os outros parâmetros como padrão, ou seja, URL `127.0.0.1` e porta `8332`. Em seguida, clique em "*Test Connection*".

![Image](assets/fr/15.webp)

A ligação é estabelecida. Aparecerá um visto Green no canto inferior direito para indicar que está ligado a um nó Bitcoin Core.

![Image](assets/fr/16.webp)

### Ligar a um servidor Electrum 🔵

A última opção para se conectar é usar um servidor Electrum remoto. Este método permite-lhe ligar-se ao seu nó via Tor a partir de outro dispositivo, e tira partido de um indexador para navegar mais rapidamente nos seus portfólios no Sparrow. É particularmente adequado se tiver uma solução node-in-a-box como Umbrel ou Start9, que lhe permite instalar Electrum com um único clique.

Para fazer isso, obtenha o Tor `.onion' Address do seu servidor Electrum. Com Umbrel, por exemplo, você vai encontrá-lo na aplicação Electrs.

![Image](assets/fr/17.webp)

No Sparrow Wallet, aceder ao separador "*Private Electrum*".

![Image](assets/fr/18.webp)

Introduza o seu Tor Address no espaço fornecido. As outras definições podem manter-se predefinidas. Em seguida, clique em "*Testar ligação*".

![Image](assets/fr/19.webp)

A ligação é confirmada. Se fechar esta janela, aparecerá um visto azul no canto inferior direito, indicando que está ligado a um servidor Electrum.

![Image](assets/fr/20.webp)

## Criar uma carteira quente

Agora que o Sparrow Wallet está configurado para comunicar com a rede Bitcoin, está pronto para criar o seu primeiro Wallet. Esta secção guia-o através da criação de um Hot Wallet, ou seja, um Wallet cujas chaves privadas estão armazenadas no seu computador. Uma vez que o seu computador é uma máquina complexa ligada à Internet, apresenta uma superfície de ataque muito grande. Por conseguinte, um Hot Wallet só deve ser utilizado para quantidades limitadas de bitcoins. Para armazenar quantidades maiores, opte por um Wallet seguro com um Hardware Wallet. Se é isto que procura, pode passar à secção seguinte.

Para criar um Hot Wallet, no ecrã inicial do Sparrow Wallet, clique no separador "*File*" e, em seguida, em "*New Wallet*".

![Image](assets/fr/21.webp)

Introduza um nome para a sua carteira e clique em "*Criar Wallet*".

![Image](assets/fr/22.webp)

No topo do Interface, pode escolher se pretende criar uma carteira "*Single Signature*" ou "*Multi Signature*". Logo abaixo, selecione o tipo de script para bloquear os seus UTXOs. Recomendo que utilize o padrão mais recente: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Em seguida, clique em "*New or Imported Software Wallet*" (Software Wallet novo ou importado).

![Image](assets/fr/24.webp)

Escolha a norma BIP39, uma vez que é suportada por praticamente todo o software da carteira Bitcoin. De seguida, escolha o comprimento da sua frase de recuperação. Atualmente, uma frase de 12 palavras é suficiente, uma vez que ambas oferecem uma segurança semelhante, mas a frase de 12 palavras é mais simples de guardar.

![Image](assets/fr/25.webp)

Clica no botão "*generate New*" para generate a frase Mnemonic do teu Wallet. Esta frase dá acesso total e irrestrito a todos os seus bitcoins. Qualquer pessoa que possua esta frase pode roubar os seus fundos, mesmo sem acesso físico ao seu computador.

A frase de 12 palavras restaura o acesso aos seus bitcoins em caso de perda, roubo ou avaria do seu computador. Por isso, é muito importante guardá-la cuidadosamente e guardá-la num local seguro.

Pode gravá-lo em papel ou, para maior segurança, gravá-lo em aço inoxidável para o proteger de incêndios, inundações ou desmoronamentos. A escolha do suporte para o seu Mnemonic dependerá da sua estratégia de segurança, mas se estiver a utilizar o Sparrow como um Wallet de gasto quente contendo quantidades moderadas, o papel deverá ser suficiente.

Para mais informações sobre a forma correta de guardar e gerir a sua frase Mnemonic, recomendo vivamente que siga este outro tutorial, especialmente se for um principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270
![Image](assets/fr/26.webp)

**Obviamente, nunca se deve partilhar estas palavras na Internet, como faço neste tutorial. Este exemplo Wallet será utilizado apenas no Testnet e será eliminado no final do tutorial

Também pode optar por adicionar um passphrase BIP39 clicando na caixa "*Usar passphrase*". Atenção: a utilização de um passphrase pode ser muito útil, mas se não compreender o seu funcionamento, pode ser muito arriscado. É por isso que aconselho vivamente a leitura deste pequeno artigo teórico sobre o assunto:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Depois de ter guardado o seu Mnemonic e qualquer passphrase num suporte físico, clique em "*Confirmar cópia de segurança*".

![Image](assets/fr/27.webp)

Volte a introduzir as suas 12 palavras para confirmar que foram guardadas corretamente e, em seguida, clique em "*Create Keystore*".

![Image](assets/fr/28.webp)

Em seguida, clique em "*Import Keystore*" para generate as chaves da sua carteira a partir da frase Mnemonic.

![Image](assets/fr/29.webp)

Clique em "*Aplicar*" para finalizar a criação da carteira.

![Image](assets/fr/30.webp)

Defina uma palavra-passe forte para garantir o acesso à sua carteira Sparrow. É uma boa ideia guardar esta palavra-passe num gestor de palavras-passe, para que não se esqueça dela. Note que esta palavra-passe não desempenha qualquer papel na derivação das suas chaves. Ela só é usada para aceder ao seu Wallet através do Sparrow Wallet. Assim, mesmo sem esta palavra-passe, a sua frase Mnemonic será suficiente para aceder aos seus bitcoins a partir de qualquer aplicação compatível com o BIP39.

![Image](assets/fr/31.webp)

O teu Hot Wallet está agora criado. Podes saltar para a secção *Receber Bitcoins* deste tutorial se não planeares usar um Hardware Wallet com o Sparrow.

## Gerir uma carteira Cold

A segunda maneira de usar o Sparrow Wallet é configurá-lo como um gerenciador de portfólio com um Hardware Wallet. Nesta configuração, as chaves privadas do seu Bitcoin Wallet permanecem exclusivamente no Hardware Wallet, enquanto o Sparrow acede apenas à informação pública. Esta abordagem oferece um maior nível de segurança do que as carteiras Hot discutidas acima, uma vez que as chaves privadas são mantidas num dispositivo especializado, muitas vezes com um chip seguro, que não está ligado à Internet e, portanto, apresenta uma superfície de ataque muito menor do que um computador tradicional.

Existem duas formas principais de ligar o Hardware Wallet ao Sparrow:


- Por cabo, normalmente utilizado com modelos de entrada de gama como o Trezor Safe 3 ou o Ledger Nano S Plus ;
- No modo Air-Gap, ou seja, sem uma ligação direta com fios, através de um cartão MicroSD ou do código QR Exchange.

O Sparrow suporta todos estes métodos de comunicação e é compatível com a maioria das carteiras de hardware existentes no mercado.

Para este tutorial, vou utilizar um Ledger Nano S com um cabo, mas o procedimento é semelhante no modo Air-Gap. Encontrará detalhes específicos para o seu Hardware Wallet no seu tutorial dedicado ao Plan ₿ Network.

Antes de começar, certifique-se de que o Wallet já está configurado no seu Hardware Wallet. Se estiver a utilizar uma ligação com fios, ligue-o ao seu computador através do cabo.

Para importar o chamado "*Keystore*" (a informação pública necessária para gerir a carteira) para o Sparrow Wallet, clique no separador "*File*" e depois em "*New Wallet*".

![Image](assets/fr/32.webp)

Dê um nome à sua carteira e clique em "*Criar Wallet*". Aconselho-o a introduzir o nome do seu Hardware Wallet para o identificar facilmente mais tarde.

![Image](assets/fr/33.webp)

Na parte superior do Interface, escolha entre uma carteira "*Single Signature*" ou "*Multi Signature*". Para o nosso exemplo, vamos configurar uma carteira de assinatura única.

Logo abaixo, selecione o tipo de script para bloquear os seus UTXOs. Se o seu Hardware Wallet o suportar, sugiro que escolha "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

Em seguida, o procedimento difere consoante o método de ligação. Se estiver a utilizar um método Air-Gap, selecione "*Airgapped Hardware Wallet*". Depois, siga as instruções específicas para o seu dispositivo.

![Image](assets/fr/35.webp)

Se estiver a utilizar uma ligação por cabo, como no meu caso, escolha "*Connected Hardware Wallet*".

![Image](assets/fr/36.webp)

Clique em "*Verificar*" para que o Sparrow detecte o seu dispositivo. Certifique-se de que ele está conectado e desbloqueado. Para alguns modelos, como o Ledger, terá de abrir a aplicação "*Bitcoin*" para ativar a deteção.

![Image](assets/fr/37.webp)

Selecione "*Importar armazenamento de chaves*".

![Image](assets/fr/38.webp)

Clique em "*Aplicar*" para finalizar a criação da carteira.

![Image](assets/fr/39.webp)

Defina uma palavra-passe forte para proteger o acesso ao seu Sparrow Wallet. Esta senha protegerá suas chaves públicas, endereços e histórico de transações. Recomendamos que a guarde num gestor de senhas. Note que esta palavra-passe não desempenha qualquer papel na derivação das suas chaves. Mesmo sem ela, pode recuperar o acesso aos seus bitcoins com o seu Mnemonic através de qualquer software compatível com o BIP39.

![Image](assets/fr/40.webp)

O seu portefólio de gestão está agora configurado no Sparrow.

![Image](assets/fr/41.webp)

## Receber bitcoins

Agora que o seu Wallet está configurado no Sparrow, pode receber bitcoins. Basta aceder ao menu "*Receber*".

![Image](assets/fr/42.webp)

O Sparrow apresentará o primeiro Address não utilizado no seu Wallet. Pode adicionar um "*Label*" a este Address para o lembrar da origem destes satoshis no futuro.

![Image](assets/fr/43.webp)

Se estiver a utilizar um Hot Wallet, o Address apresentado pode ser utilizado imediatamente, quer copiando-o quer digitalizando o código QR associado.

Se estiver a utilizar um Hardware Wallet, é muito importante verificar o Address no ecrã do dispositivo antes de o utilizar. Para dispositivos com fios, ligue e desbloqueie o Hardware Wallet e, em seguida, no Sparrow, clique em "*Display Address*". Certifique-se de que o Address apresentado no seu Hardware Wallet corresponde ao apresentado no Sparrow.

![Image](assets/fr/44.webp)

Para os utilizadores do Hardware Wallet Air-Gap, a verificação do Address varia consoante o modelo do dispositivo. Consulte o tutorial dedicado ao Plan ₿ Network para obter instruções precisas.

Quando a transação tiver sido transmitida pelo pagador, aparecerá no separador "*Transacções*". Pode clicar nela para obter mais pormenores, como o txid.

![Image](assets/fr/45.webp)

No separador "*Endereços*", encontra uma lista de todos os seus endereços de caixa de entrada. Pode ver se já foram utilizados e se foi adicionada uma etiqueta. *Os endereços "Receive*" são aqueles que o Sparrow mostra quando clica em "*Receive*" e destinam-se a pagamentos recebidos. Os endereços "*Change*" são utilizados para o Exchange nas suas transacções, ou seja, para recuperar a parte não utilizada dos seus UTXOs nas entradas.

![Image](assets/fr/46.webp)

O separador "*UTXOs*" mostra-lhe todos os seus UTXOs, ou seja, os fragmentos de Bitcoin que detém. Pode ver a quantidade de cada UTXO e a etiqueta associada.

![Image](assets/fr/47.webp)

## Enviar bitcoins

Agora que tens alguns satoshis no teu Wallet, tens também a opção de enviar alguns. Embora existam várias formas de o fazer, recomendo que utilize o menu "*UTXOs*" para um controlo mais preciso das moedas que gasta (*controlo de moedas*), em vez de ir diretamente para o menu "*Enviar*" (embora este último possa ser suficiente se for um principiante).

![Image](assets/fr/48.webp)

Selecione os UTXOs que pretende utilizar como entradas para esta transação e, em seguida, clique em "*Enviar selecionados*". Esta abordagem permite-lhe selecionar as fontes mais adequadas de entre os seus UTXOs, em função das suas despesas e das etiquetas aplicadas aquando da sua receção, de forma a otimizar a confidencialidade dos seus pagamentos. Certifique-se de que a soma dos UTXOs selecionados é superior ao montante que pretende enviar.

![Image](assets/fr/49.webp)

Introduza o Address do destinatário no campo "*Pagar a*". Também pode digitalizar o Address com a sua webcam, clicando no ícone da câmara. O botão "*+Adicionar*" permite-lhe pagar vários endereços numa única transação.

![Image](assets/fr/50.webp)

Adicione uma etiqueta à sua transação para o lembrar do seu objetivo. Esta etiqueta também será associada ao seu eventual Exchange.

![Image](assets/fr/51.webp)

Introduzir o montante a enviar para este Address.

![Image](assets/fr/52.webp)

Ajustar a taxa de honorários de acordo com as condições actuais do mercado. Pode fazê-lo introduzindo um valor de taxa absoluto ou ajustando a taxa de taxa com o cursor.

![Image](assets/fr/53.webp)

Na parte inferior do Interface, é possível escolher entre "*Eficiência*" e "*Privacidade*". No meu caso, a opção "*Privacidade*" não está disponível, pois só tenho um UTXO nesta carteira. "*Eficiência*" corresponde a uma transação clássica, enquanto "*Privacidade*" é uma transação do tipo Stonewall, uma estrutura de transação que reforça a sua confidencialidade simulando um mini-CoinJoin, o que torna a análise em cadeia mais complexa.

![Image](assets/fr/54.webp)

O Sparrow apresenta um diagrama de resumo que mostra as suas entradas, saídas e taxas de transação (note que as taxas não são realmente uma saída, ao contrário do que este diagrama sugere). Se estiver satisfeito com tudo, clique em "*Criar transação*".

![Image](assets/fr/55.webp)

É apresentada uma página com os detalhes do Elements da sua transação. Verifique se todas as informações estão corretas e, em seguida, clique em "*Finalizar transação para assinatura*".

![Image](assets/fr/56.webp)

É importante manter o Sighash por defeito. Para perceber porquê, dê uma vista de olhos a este curso de formação, no qual explico tudo o que precisa de saber sobre o Sighash:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f
No ecrã seguinte, as opções variam de acordo com o tipo de Wallet que está a utilizar:


- Para um Air-Gap Hardware Wallet, clique em "*Mostrar QR*" para exibir um PSBT que pode assinar com o seu dispositivo e, em seguida, carregue o PSBT assinado no Sparrow usando "*Digitalizar QR*". A opção "*Guardar transação*" funciona de forma semelhante, mas com trocas num microSD ;
- Para um Hot Wallet, basta clicar em "*Sign*" e introduzir a palavra-passe do Wallet para assinar;
- Para um Hardware Wallet com fios, clique também em "*Assinar*" para enviar a transação não assinada para o seu dispositivo.

![Image](assets/fr/57.webp)

No seu Hardware Wallet, verifique o Address do destinatário, o montante enviado e as despesas. Se tudo estiver correto, proceda à assinatura.

Uma vez assinada a transação, ela reaparecerá no Sparrow, pronta para ser transmitida na rede Bitcoin para posterior inclusão em um bloco. Se tudo estiver correto, clique em "*Broadcast Transaction*".

![Image](assets/fr/58.webp)

A sua transação é agora transmitida e aguarda confirmação.

![Image](assets/fr/59.webp)

## Gerir e configurar carteiras no Sparrow

No separador "*Configurações*", encontrará informações detalhadas sobre a sua carteira, tais como :


- Tipo de carteira (single-sig ou multi-sig) ;
- Tipo de guião utilizado ;
- O nome que atribuiu à carteira ;
- Impressão de chave mestra;
- O caminho de desvio ;
- A chave pública alargada da conta.

![Image](assets/fr/60.webp)

O botão "*Exportar*" permite-lhe exportar a informação da sua carteira para que possa utilizá-la noutro software, mantendo a informação configurada no Sparrow.

O botão "*Adicionar conta*" permite-lhe adicionar uma conta adicional à sua carteira. Uma conta corresponde a um conjunto separado de endereços de caixa de entrada. Esta funcionalidade pode ser útil, por exemplo, se pretender separar uma conta pessoal e uma conta profissional, com uma única frase Mnemonic.

O botão "*Avançado*" dá acesso a definições avançadas, como a personalização da pesquisa Address do Sparrow e a alteração da palavra-passe da carteira.

![Image](assets/fr/61.webp)

Ao fechar o Sparrow Wallet, o Wallet é bloqueado automaticamente. Na próxima vez que abrir o software, uma janela solicitará que desbloqueie o Wallet com sua senha.

![Image](assets/fr/62.webp)

Se esta janela não abrir, ou se pretender abrir outra carteira no Sparrow, clique no separador "*File*" e selecione "*Open Wallet*".

![Image](assets/fr/63.webp)

Isto abrirá o seu Gestor de Ficheiros na pasta onde o Sparrow guarda as suas carteiras. Basta selecionar o Wallet que deseja abrir e digitar a senha para desbloqueá-lo.

![Image](assets/fr/64.webp)

No menu "*Arquivo*", em "*Configurações*", encontram-se os parâmetros de ligação à rede do Bitcoin já explorados nas secções anteriores. Também é possível ajustar vários parâmetros, como a unidade utilizada, a moeda fiduciária para conversões e as fontes de informação.

![Image](assets/fr/65.webp)

O separador "*Ver*" oferece opções de personalização e acesso a alguns comandos úteis, como "*Refresh Wallet*", que actualiza a pesquisa de transacções da sua carteira.

![Image](assets/fr/66.webp)

O separador "*Ferramentas*" agrupa várias ferramentas avançadas, incluindo :


- "*Sign/Verify Message*" permite-lhe provar a posse de um Address recetor ou verificar uma assinatura.
- a opção "*Enviar para muitos*" oferece um Interface simplificado para efetuar transacções para vários endereços de receção de uma só vez, o que é conveniente para despesas em lote.
- o "*Sweep Private Key*" permite-lhe recuperar bitcoins protegidos por uma simples chave privada e transferi-los para o seu Sparrow Wallet. Isto pode ser particularmente útil para aqueles com bitcoins que datam do início dos anos 2010, antes da era das carteiras HD.
- "Verificar transferência" verifica a integridade e autenticidade do software descarregado antes de o instalar no seu dispositivo.
- o "*Restart In*" permite-lhe mudar para as suas carteiras nas redes Testnet ou Signet. Isto pode ser útil se desejar aceder a redes de teste com moedas sem valor real.

![Image](assets/fr/67.webp)

Agora já sabe tudo sobre o software Sparrow Wallet, uma excelente ferramenta para gerir diariamente as suas carteiras Bitcoin.

Se achou este tutorial útil, ficaria muito grato se deixasse um polegar Green abaixo. Sinta-se à vontade para o partilhar nas suas redes sociais. Muito obrigado!

Recomendo também este outro tutorial em que explico como configurar o Hardware Wallet COLDCARD Q com o Sparrow Wallet :

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3