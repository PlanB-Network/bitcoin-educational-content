---
name: Jade DIY
description: Transforme uma placa de desenvolvimento de 15 dólares em um hardware Bitcoin wallet totalmente funcional
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Construção para principiantes


**Público-alvo:** Construtores curiosos com pouca ou nenhuma experiência em sistemas integrados.


**Duração:** 2 horas (flexível)


**Resultados:** No final, os alunos irão:



- Reconhecer o modelo de segurança das carteiras de hardware "faça você mesmo" em relação aos dispositivos comerciais.
- Montar um dispositivo de assinatura baseado num microcontrolador.
- Faça o flash do firmware de código aberto e verifique a soma de verificação da compilação.
- Assinar e transmitir uma transação mainnet utilizando o seu novo dispositivo.


---

## Resumo


Este workshop de 2 horas ensina os principiantes a construir um hardware Bitcoin wallet funcional, colocando o firmware Jade de código aberto numa placa LilyGO T-Display de 15 dólares. Os alunos transformam um hardware de desenvolvimento genérico num dispositivo de assinatura comparável a carteiras comerciais que custam 150 dólares, aprendendo os fundamentos de segurança através da experiência prática e não apenas da teoria.


### Filosofia


Construir o seu próprio dispositivo de assinatura não se trata apenas de poupar dinheiro - trata-se de compreender a tecnologia que protege o seu Bitcoin. Este workshop abraça a "segurança através da compreensão" em vez da confiança na caixa negra. Ao adquirir componentes, fazer o flash de firmware de código aberto e gerar entropia, os alunos reduzem o risco da cadeia de fornecimento enquanto aprendem a avaliar criticamente as reivindicações de segurança. O objetivo é a autonomia informada: os alunos devem compreender tanto o poder como as limitações do seu dispositivo DIY em comparação com alternativas comerciais reforçadas.


---

## Conceito básico (15 min)


### O que é a autocustódia e porque é que é importante?


A Bitcoin foi criada para eliminar a necessidade de terceiros de confiança, como bancos e corporações, do nosso sistema monetário. Em vez de usar a confiança, a bitcoin usa a matemática, a física e a criptografia para permitir que qualquer pessoa tenha o poder de possuir e controlar o seu dinheiro sem precisar da permissão de ninguém.


A forma como isto funciona é que a bitcoin existe num registo digital global chamado blockchain, também conhecido como bitcoin timechain, que é um registo público e transparente gerido por computadores, em vez de um registo centralizado como uma conta bancária.


O importante é compreender que, para mover bitcoin de um local para outro, é necessário assinar essa transação com aquilo a que se chama uma chave privada. Pense nisso como desbloquear um cofre com uma senha e mover o bitcoin para o cofre de outra pessoa. O Bitcoin dá-lhe o poder de ter as chaves desse cofre, em vez de depender de um banco para movimentar o seu dinheiro por si.


Um grande poder traz consigo uma grande responsabilidade. Se perder as suas chaves, os seus fundos desaparecem para sempre. Desta forma, pode pensar nas chaves do cofre como o próprio dinheiro. Embora as chaves não sejam a mesma coisa que a bitcoin, são o mecanismo para movimentar os seus fundos e, por isso, é extremamente importante protegê-las. É por isso que dizemos "nem as tuas chaves, nem as tuas moedas".


O termo auto-custódia pode parecer confuso, mas tudo o que significa é ter as suas próprias chaves privadas e controlar a sua própria bitcoin. Se não detiver essa chave, está a confiar que outra pessoa a detenha por si. Se a sua bitcoin estiver num ETF ou numa bolsa (Mt. Gox, FTX, Coinbase, Binance, etc.), não possui a bitcoin, mas sim uma reivindicação da bitcoin. Isto introduz todo o tipo de riscos, como o de as bolsas serem pirateadas e perderem a sua bitcoin ou o de as empresas emprestarem o seu dinheiro e lhe darem apenas uma fração de reserva. Além disso, terceiros de confiança teriam controlo total sobre o seu dinheiro e poderiam limitar ou congelar os levantamentos.


![image](assets/fr/01.webp)


Com a auto-custódia, a confiança é eliminada da equação. Ninguém pode congelar os seus fundos ou negar uma transação, pode enviar dinheiro através das fronteiras, para qualquer pessoa, em qualquer altura, e não precisa de uma conta bancária, de um BI ou da aprovação de ninguém. Ninguém o pode impedir, censurar ou roubar, desbloqueando todo o poder do bitcoin como dinheiro da liberdade. É por isso que dizemos que, com o bitcoin, pode ser o seu próprio banco.


O Bitcoin foi criado para resolver o problema da manipulação da confiança e do dinheiro, uma opção de saída do nosso sistema atual, mas a saída só funciona se levarmos as chaves. É por isso que a auto-custódia é tão importante.


### O que é um Wallet?


O termo wallet é um pouco impróprio e, por isso, pode ser confuso. Sim, é verdade que um wallet de bitcoin, tal como um wallet físico, armazena valor. Mas a principal diferença é que as carteiras de bitcoin não armazenam efetivamente qualquer bitcoin.


O Bitcoin só existe como registo na blockchain pública, ou dentro dos cofres metafóricos no ciberespaço. Lembre-se de que para mover o bitcoin você tem que usar suas chaves para desbloquear o cofre e mover as moedas para outro lugar, as chaves privadas são o que é usado para gastar bitcoin. Quando você faz uma transação com o seu wallet, você está realmente apenas usando suas chaves para assinar a transação. É assim que você mostra a prova de que possui o dinheiro e tem o direito de gastar essas moedas.


As carteiras Bitcoin apenas armazenam as suas chaves privadas, pelo que seria mais correto chamar-lhes porta-chaves.


### Carteiras Hot vs Cold


Um Hot wallet é uma aplicação de software no seu telemóvel ou computador. Está ligado à Internet, pelo que é mais fácil de utilizar e mais rápido para assinar transacções, mas isto também significa que está mais exposto a hackers, malware e phishing. Chama-se "quente" porque está ligado à Internet, está ligado à corrente e está ligado à corrente. Um exemplo seria um telemóvel wallet ou um browser wallet.


Por outro lado, uma wallet fria, ou wallet de hardware, é um dispositivo que cria e armazena a sua chave offline. Isto elimina a possibilidade de alguém piratear os seus fundos e é muito mais seguro para poupanças a longo prazo, no entanto, é um dispositivo que é necessário para assinar cada transação e pode ser menos conveniente.


### Modelo de ameaça Hardware Wallet


As carteiras de hardware existem para resolver um problema fundamental: como assinar transacções Bitcoin sem expor as suas chaves privadas a um computador ligado à Internet que pode ser comprometido por malware ou atacantes remotos? O modelo de ameaça principal assume que o seu computador portátil ou telemóvel do dia a dia é potencialmente hostil. Um wallet de hardware cria um ambiente isolado em que as chaves privadas nunca saem do dispositivo e a assinatura da transação ocorre num secure element ou microcontrolador que apenas comunica a assinatura de volta ao computador anfitrião, não a chave em si. Mesmo que o seu computador esteja completamente comprometido, um atacante não pode roubar o seu Bitcoin sem acesso físico ao dispositivo e ao seu PIN.


No entanto, as carteiras de hardware apresentam as suas próprias ameaças. É necessário confiar que o fabricante não introduziu backdoors, que a cadeia de fornecimento não foi adulterada e que a geração de números aleatórios é verdadeiramente aleatória. Os atacantes físicos podem extrair chaves através de ataques de canal lateral ou manipulação de chips, e alguém com acesso temporário pode modificar o seu dispositivo. Construir o seu próprio hardware wallet ajuda-o a compreender estes compromissos - tomará decisões sobre elementos seguros versus microcontroladores de uso geral, como verificar transacções num ecrã e como proteger contra ameaças remotas e físicas. O objetivo não é uma segurança perfeita, mas sim compreender quais as ameaças contra as quais se está a proteger e quais as que permanecem.


### Conceitos-chave



- Entropia e frases do seed:** O seu wallet é tão seguro quanto a aleatoriedade que o gera. Vamos misturar o gerador de números aleatórios do dispositivo com truques amigáveis para o ser humano, como o lançamento de dados, converter essa entropia numa [frase BIP39] de 12 ou 24 palavras (https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) e sair da sala com uma cópia de segurança escrita ou metálica em que confie.
- Higiene da frase-semente:** Trate o seed como as chaves mestras das suas poupanças. Nunca escreva as palavras num telemóvel ou computador - os keyloggers, as capturas de ecrã e as cópias de segurança na nuvem podem divulgá-las para sempre. Mantenha a frase offline, guarde-a num local a que só você possa aceder e pratique a sua leitura em voz alta antes de sair.
- Elemento seguro + microcontrolador:** Pense no secure element como o cofre e o microcontrolador como o cérebro. O secure element guarda as chaves privadas com resistência à violação, enquanto o microcontrolador trata do ecrã, dos botões e da lógica do firmware. Note que as carteiras de hardware que estamos a construir hoje não têm um secure element. Isto não significa que seja insegura, apenas que tem menos um nível de proteção.
- Confiar no firmware:** O firmware é o sistema operativo invisível do wallet. Descarregue sempre a partir de versões marcadas, verifique o hash publicado e compreenda que as compilações reproduzíveis permitem que várias pessoas compilem o mesmo código e cheguem exatamente ao mesmo binário. Se o checksum não corresponder, não assine.


---

## O que estamos a construir?


Nós estamos pegando um hardware genérico, o LilyGo T-Display, e colocando o firmware Jade SDK nele. O [Jade Plus] (https://blockstream.com/jade/jade-plus/) é um wallet de código aberto, que custa normalmente 150 dólares:


![image](assets/fr/02.webp)


Hoje, em vez disso, vamos fazer o flash do seu firmware para um hardware de 15 dólares.


### O que comprar


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB com shell, modelo K164)** - [Encomende diretamente à LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) por cerca de 15 dólares. Esta placa ESP32 fornece o ecrã, os botões e a interface USB que espelham o Jade Plus da Blockstream. O ESP32 integrado também inclui rádios Wi-Fi e Bluetooth; enviaremos um firmware que os mantém desactivados, mas eles moldam o seu modelo de ameaça porque um código malicioso pode voltar a ligá-los.
- Cabo USB-C** - Traga um cabo com capacidade para dados para que possa fazer o flash do firmware e alimentar a placa diretamente a partir do seu portátil (totalmente adequado para utilização em aulas).


### Porquê construir o seu próprio Hardware Wallet?



- Poupe cerca de 135 dólares em comparação com a compra de um dispositivo comercial.
- Desenvolver o conforto com a intermitência do firmware, elementos seguros e higiene do wallet.
- Crie dispositivos de assinatura adicionais para distribuir as poupanças por várias carteiras.
- Reduzir o risco da cadeia de fornecimento através do fornecimento e montagem de cada componente por si.
- Não esqueçamos o mantra de Lopp: a soberania e a conveniência estão sempre em conflito.


## Configuração física


### Preparar o seu caso


Tem duas opções para alojar a sua placa LilyGO T-Display: uma caixa impressa em 3D ou a caixa oficial LilyGO. A caixa impressa pode ser encontrada e impressa a partir de [este modelo] (https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Oferece um invólucro leve e personalizável para o seu dispositivo.


![image](assets/fr/04.webp)


Em alternativa, pode utilizar a capa oficial da LilyGO, que proporciona um ajuste e acabamento ligeiramente diferentes, oferecendo uma proteção mais robusta e um aspeto polido.


![image](assets/fr/05.webp)


Note que as caixas impressas e oficiais diferem ligeiramente em termos de design e montagem. Qualquer que seja a opção escolhida, certifique-se de que a placa está corretamente colocada dentro da caixa para evitar ligações soltas ou danos.


### Inspecionar a placa


Antes de prosseguir, inspeccione cuidadosamente a sua placa LilyGO T-Display para detetar quaisquer defeitos ou detritos visíveis. Verifique se o ecrã, os botões e a porta USB-C estão limpos e sem pó ou salpicos de solda. Manuseie a placa com cuidado e observe a segurança da descarga eletrostática (ESD), aterrando-se ou usando uma pulseira ESD para evitar danos aos componentes sensíveis.


### Ligar ao computador portátil


Usando um cabo USB-C com capacidade de dados, conecte a placa LilyGO ao seu laptop. Esta ligação fornecerá energia e permitir-lhe-á fazer o flash do firmware.


No arranque, é apresentado o seguinte ecrã:


![image](assets/fr/06.webp)



Quando ligado, o LilyGO exibirá uma tela de teste de cores passando por cores sólidas. Isto confirma que o visor e a placa estão a funcionar corretamente antes de fazer o flash do firmware.


Quando o teste de cor estiver concluído, o ecrã ficará num estado predefinido, indicando que a placa está pronta para os passos seguintes do processo de construção.


![image](assets/fr/07.webp)


## A maneira fácil ou a maneira Hard


Existem duas abordagens principais para flashear o firmware do seu hardware wallet: a maneira fácil e a maneira difícil. A maneira fácil utiliza ferramentas pré-configuradas ou flashes baseados na web que carregam automaticamente o firmware no seu dispositivo com o mínimo de entrada. Este método é ideal para iniciantes que querem uma vitória rápida ou preferem evitar as complexidades de depuração e interações de linha de comando. Simplifica o processo e coloca-o em funcionamento mais rapidamente, tornando-o acessível para os principiantes em desenvolvimento incorporado ou carteiras de hardware.


A maneira mais difícil, por outro lado, envolve o uso manual de ferramentas de linha de comando para fazer o flash do firmware. Esta abordagem requer a verificação de assinaturas de firmware e somas de verificação para garantir a autenticidade e integridade, dando-lhe uma compreensão mais profunda do processo de flashing e da forma como o firmware interage com o hardware. Embora exija mais esforço e familiaridade com os comandos do terminal, oferece maior controlo, transparência e confiança na segurança do dispositivo.


Cada método tem as suas desvantagens: o método fácil sacrifica um certo grau de confiança e compreensão em prol da rapidez e da conveniência, enquanto o método difícil requer mais tempo e competências técnicas, mas recompensa-o com flexibilidade e uma maior compreensão da tecnologia subjacente. Os instrutores devem incentivar os alunos a escolher o caminho que melhor se adapta ao seu nível de conforto e curiosidade, promovendo a confiança e a exploração.


## A maneira fácil


A maneira mais fácil de flashear um ESP32



- Ir para o Github oficial da Blockstream: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Pode descarregar o ficheiro fonte e executar o sítio Web localmente, mas o GitHub já o aloja em [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). O GitHub fornece o HTML, CSS, JavaScript, etc. diretamente ao seu browser para que possa fazer o flash do dispositivo sem instalar ferramentas de desenvolvimento.


![image](assets/fr/09.webp)



- Abra o menu suspenso (provavelmente o padrão é `M5Stack Core2`) e selecione sua placa de desenvolvimento - para esta aula, escolha `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Quando clicar em flash, vai aparecer isto. Para saber qual o dispositivo que é o LILYGO, desligue o lilygo e volte a ligá-lo. A porta COM do lilygo vai aparecer e desaparecer. Clique na porta COM em que o Jade está conectado


![image](assets/fr/11.webp)



- É isso, deve aparecer uma barra de progresso e, quando terminar, está pronto para o configurar


## Configurar o Jade Wallet


Uma vez que o firmware é atualizado com sucesso, seu LilyGO T-Display é agora um hardware Jade wallet totalmente funcional. Esta secção irá guiá-lo através do processo de configuração inicial, desde a geração da sua frase seed até à ligação do dispositivo com o software wallet, como o Sparrow ou a aplicação móvel Blockstream Green.


### Arranque inicial e configuração do dispositivo



- Ligar o dispositivo:** Com o LilyGO ainda ligado ao seu portátil através de USB-C, o firmware Jade deve arrancar automaticamente. Verá o logótipo Jade aparecer no ecrã.



- Entrar no modo de configuração:** O dispositivo apresenta-lhe um menu inicial. Utilize os dois botões físicos da placa para navegar:
 - Botão esquerdo:** Mover para cima/para trás
 - Botão direito:** Mover para baixo/para a frente
 - Ambos os botões em simultâneo:** Selecionar/confirmar



- Selecione "Setup":** Navegue até à opção Setup e prima ambos os botões para confirmar. O dispositivo guiá-lo-á através do processo de configuração inicial.


### Criar o seu Wallet



- Escolher "Begin Setup":** O dispositivo irá pedir-lhe para iniciar o processo de criação do wallet. Confirme a sua seleção.



- Selecione "Criar novo Wallet":** Ser-lhe-ão apresentadas duas opções:
 - Criar novo Wallet:** Gera uma nova frase seed (escolha esta para o workshop)
 - Restaurar Wallet:** Recuperar um wallet existente a partir de uma frase seed (para utilizadores avançados)



- Selecionar "Create New Wallet" e confirmar.



- Gerar entropia:** O dispositivo utilizará o seu gerador de números aleatórios para criar entropia criptográfica. Este processo demora alguns segundos, uma vez que o dispositivo recolhe a aleatoriedade de várias fontes.


### Gravar a sua frase-semente



- Escreva a sua frase seed:** O aparelho apresentará agora uma frase BIP39 seed de 12 palavras, uma palavra de cada vez. Este é o passo mais crítico de todo o processo.


**Práticas de segurança importantes:**


- Escrever cada palavra claramente num papel (utilizar os cartões de frases seed fornecidos, se disponíveis)
- Verificar duas vezes cada palavra à medida que a escreve
- Nunca fotografe a frase seed com o seu telemóvel
- Nunca digitar as palavras em nenhum computador ou telemóvel
- Mantenha a sua frase seed privada - não partilhe o seu ecrã nem mostre a outras pessoas



- Verificar a frase do seed:** Depois de escrever as 12 palavras, o dispositivo pede-lhe que confirme várias palavras da frase para garantir que as gravou corretamente. Utilize os botões para selecionar a palavra correta para cada pedido.


**Dica profissional:** Antes de avançar, pratique a leitura da sua frase seed em voz alta (em silêncio, para que os outros não possam ouvir). Isto ajuda a detetar quaisquer erros de escrita ou ambiguidades.


### Método de ligação



- Selecionar o tipo de ligação:** O firmware Jade suporta dois métodos de ligação:
 - USB:** Ligação com fios através de um cabo USB-C (recomendado para esta oficina)
 - Bluetooth:** Ligação sem fios a dispositivos móveis



- Selecione **USB** por agora, uma vez que é a opção mais simples para o software wallet de secretária e não introduz vectores de ataque sem fios.



- Nomeação do dispositivo:** O Jade apresentará um identificador único como "Connect Jade A7D924". Este identificador ajuda-o a distinguir entre várias carteiras de hardware, caso acabe por construir mais do que uma. Tome nota deste identificador, se desejar.


### Ligação ao software Wallet


Tem agora duas opções principais para interagir com o seu recém-criado hardware wallet: a aplicação móvel Blockstream Green (para utilização em movimento) ou o Sparrow Wallet (para utilização em ambiente de trabalho com funcionalidades mais avançadas). Para este workshop, vamos concentrar-nos no Sparrow Wallet, uma vez que oferece uma melhor visibilidade dos detalhes técnicos das transacções Bitcoin.


#### Opção 1: Aplicação móvel Blockstream Green (Início rápido)


Se quiser testar rapidamente o seu dispositivo com um dispositivo móvel:



- Descarregar a aplicação **Blockstream Green** da App Store (iOS) ou do Google Play (Android)
- Abrir a aplicação e selecionar "Ligar Hardware Wallet"
- Selecionar "Jade" na lista de dispositivos suportados
- Ligue o Jade ao seu telemóvel utilizando um cabo USB-C para USB-C (ou um adaptador USB-C para Lightning para iPhone 15+)
- Siga as instruções no ecrã para ligar e criar o seu primeiro wallet


**Nota sobre o Liquid:** A aplicação Blockstream Green suporta tanto o Bitcoin como o Liquid (uma cadeia lateral do Bitcoin). Se estiver a utilizar as funcionalidades do Liquid, poderá ser-lhe pedido para "Exportar chave mestra" - isto permite que a aplicação veja os montantes das transacções na rede Liquid, que de outra forma são confidenciais. Para este workshop, pode ignorar as funcionalidades Liquid e concentrar-se nas transacções Bitcoin padrão.


#### Opção 2: Sparrow Wallet (Recomendado para a oficina)


Sparrow O Wallet é uma poderosa aplicação de ambiente de trabalho que lhe permite um controlo pormenorizado das suas transacções Bitcoin e estabelece uma ligação perfeita com o seu hardware Jade wallet.


**Instalação



- Descarregar o Sparrow Wallet a partir do sítio Web oficial: [sparrowwallet.com](https://sparrowwallet.com)
- Verifique a assinatura do download (consulte a documentação do Sparrow para obter detalhes)
- Instalar e lançar a aplicação


**Ligar o seu Jade ao Sparrow:**



- No Sparrow, ir para **File → New Wallet**
- Dê um nome ao seu wallet (por exemplo, "My Jade Wallet")
- Clique em **Ligado Hardware Wallet**
- O Sparrow deve detetar automaticamente o dispositivo Jade ligado
- Se lhe for pedido, confirme a ligação no ecrã Jade premindo os dois botões
- Selecione o tipo de script pretendido:
 - Native Segwit (P2WPKH):** Recomendado para iniciantes - taxas mais baixas, maior compatibilidade com carteiras modernas
 - Segwit aninhado (P2SH-P2WPKH):** Para compatibilidade com serviços mais antigos
 - Taproot (P2TR):** Mais avançado, oferece a melhor privacidade e taxas mais baixas, mas requer suporte wallet de ponta
- Clique em **Importar Keystore** para concluir a ligação


**Configuração da ligação do servidor do Sparrow:**


Antes de poder ver o seu saldo ou transmitir transacções, o Sparrow precisa de se ligar a um nó Bitcoin para obter dados da cadeia de blocos. Existem várias opções, cada uma com diferentes compromissos entre conveniência, privacidade e confiança:



- Electrum Server público (mais fácil, menos privado):** Liga-se a um servidor público operado por um terceiro. Rápido de configurar, mas o servidor pode ver os endereços do seu wallet e potencialmente ligá-los ao seu endereço IP. Bom para testes em testnet.
 - No Sparrow, vá para **Ferramentas → Preferências → Servidor**
 - Selecione **Servidor público** e escolha um servidor da lista
 - Clique em **Testar ligação** para verificar



- Bitcoin Core ou Knots Node (Mais privado, mais trabalho):** Executar o seu próprio nó Bitcoin completo. Este é o padrão ouro para privacidade e verificação, já que você mesmo valida cada transação e não confia no servidor de ninguém. No entanto, requer o download de todo o blockchain (~600GB) e manter seu nó sincronizado.
 - Instalar e sincronizar o núcleo ou os nós Bitcoin
 - No Sparrow, vá para **Ferramentas → Preferências → Servidor**
 - Selecione **Bitcoin Core ou Knots** e introduza os detalhes de ligação do seu nó



- Electrum Server Privado (Bom equilíbrio):** Hospede seu próprio servidor Electrum (como Fulcrum ou Electrs) conectado ao seu nó Bitcoin Core ou Knots. Oferece total privacidade sem a necessidade de executar o Sparrow na mesma máquina do seu nó.
 - Configure um servidor Electrum apontando para o seu Bitcoin Core ou nó Knots
 - No Sparrow, vá para **Ferramentas → Preferências → Servidor**
 - Selecione **Private Electrum** e introduza o URL do seu servidor


Para este workshop, utilizar um **Electrum Server público** é perfeitamente adequado para transacções de testnet. Num ambiente de produção com fundos reais, é melhor considerar a possibilidade de executar o seu próprio nó ou utilizar um servidor privado de confiança para obter o máximo de privacidade.


#### Opção 3: Aplicação de ambiente de trabalho Blockstream Green (Início rápido)


O Blockstream Green é o software para terminar a configuração da JadeDIY e deve ser utilizado com a versão para computador



- Obtenha a aplicação oficial da Blockstream - esta é a ligação para a mesma a partir do seu sítio Web. Quando estiveres lá, clica em [Descarregar agora] (https://blockstream.com/app/).


![image](assets/fr/12.webp)



- Dependendo do local para onde vão os seus downloads, o mais provável é que o ficheiro esteja na sua pasta Downloads. Verifique essa pasta e faça duplo clique no ficheiro executável para instalar o software.


![image](assets/fr/13.webp)



- Poderá ter de conceder direitos de administrador para executar o instalador. Assim que o fizer, aparecerá uma janela com o aspeto da seguinte imagem - clique em **Next**.


![image](assets/fr/14.webp)



- Escolha o local onde pretende que a aplicação instalada resida (um local com os outros programas ou um local fácil de encontrar) e, em seguida, clique em **Próximo**.


![image](assets/fr/15.webp)



- O instalador pedirá um nome para o atalho. Introduza um ou mantenha o nome predefinido e, em seguida, clique em **Próximo**.


![image](assets/fr/16.webp)



- Se pretender um atalho para o ambiente de trabalho, assinale a caixa; caso contrário, clique em **Próximo**.


![image](assets/fr/17.webp)



- Por fim, clique em **Instalar** e aguarde alguns minutos até a instalação estar concluída.


![image](assets/fr/18.webp)



- A barra de progresso deve encher-se até ao fim.


![image](assets/fr/19.webp)



- Quando terminar, aparecerá uma nova página - clique em **Finalizar**.


![image](assets/fr/20.webp)



- Localize a aplicação Blockstream recentemente instalada (exemplo apresentado no menu Iniciar do Windows 11).


![image](assets/fr/21.webp)



- Quando o encontrar, clique para iniciar - deve aparecer um ecrã inicial.


### Verificar a configuração


Uma vez ligado ao Sparrow (ou a outra aplicação wallet):



- Verifique os seus endereços:** O Sparrow apresentará os endereços de receção derivados da sua frase seed. Pode verificar um endereço no seu dispositivo Jade indo ao separador "Receive" (Receber) no Sparrow e clicando em "Display Address" (Mostrar Address) - o endereço deve aparecer tanto no ecrã do seu computador como no ecrã do Jade.



- Gerar um endereço de receção:** Clique no separador **Receber** no Sparrow e copie o seu primeiro endereço de receção do Bitcoin.



- Pronto para transacções:** O seu hardware wallet está agora totalmente configurado e pronto para receber e assinar transacções Bitcoin. Avance para a secção seguinte para praticar a assinatura de uma transação testnet.



---

### Lista de verificação de configuração rápida



- O firmware Jade arranca com êxito
- Novo wallet criado com a frase de 12 palavras seed
- Frase-semente escrita de forma clara e verificada
- Modo de ligação USB selecionado
- Software Wallet (Sparrow) instalado e ligado
- Ligação ao servidor configurada (Electrum público para mainnet)
- Primeiro endereço de receção gerado e verificado no dispositivo



---

**Licença do MIT


**Direitos de autor (c) 2025 The Bitcoin Network NYC**


É concedida permissão, sem custos, a qualquer pessoa que obtenha uma cópia deste software e dos ficheiros de documentação associados (o "Software"), para negociar o Software sem restrições, incluindo, sem limitação, os direitos de utilizar, copiar, modificar, fundir, publicar, distribuir, sublicenciar e/ou vender cópias do Software, e para permitir que as pessoas a quem o Software é fornecido o façam, sujeito às seguintes condições:


O aviso de direitos de autor acima e este aviso de permissão devem ser incluídos em todas as cópias ou partes substanciais do Software.


O SOFTWARE É FORNECIDO "TAL COMO ESTÁ", SEM QUALQUER TIPO DE GARANTIA, EXPRESSA OU IMPLÍCITA, INCLUINDO MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM DETERMINADO FIM E NÃO INFRACÇÃO. EM NENHUMA CIRCUNSTÂNCIA OS AUTORES OU DETENTORES DE DIREITOS DE AUTOR SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE, SEJA NUMA ACÇÃO DE CONTRATO, DELITO OU OUTRA, DECORRENTE DE, FORA DE OU EM LIGAÇÃO COM O SOFTWARE OU A UTILIZAÇÃO OU OUTRAS TRANSACÇÕES COM O SOFTWARE.


---