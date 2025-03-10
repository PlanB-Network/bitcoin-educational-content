---
name: Passaporte - Fundação
description: Configurar e utilizar a carteira de hardware Passport em modo manual
---
![cover](assets/cover.webp)

O Passport é uma carteira de hardware apenas para Bitcoin, concebida pela Foundation Devices, uma empresa americana fundada em abril de 2020 em Boston.

O Passport "*Batch 2*" que apresentamos neste tutorial é o sucessor do "*Founder's Edition*". Apresenta um design premium, um ecrã a cores de alta definição e um teclado físico ergonómico. Funciona em modo "*Air-Gap*", garantindo que as chaves privadas da sua carteira permanecem totalmente isoladas, sendo possível efetuar trocas através de um cartão MicroSD ou de códigos QR. O dispositivo inclui uma bateria amovível de 1200 mAh.

Quanto à conetividade, o Passport está equipado com uma porta MicroSD, uma porta USB-C para carregamento e uma câmara traseira para leitura de códigos QR.

Em termos de segurança, o Passport incorpora um elemento seguro e o código-fonte do dispositivo é totalmente open-source. Ele oferece todas as caraterísticas esperadas de uma boa carteira de hardware Bitcoin. Note-se que o Passport ainda não suporta miniscript, mas esta funcionalidade está planeada para o segundo trimestre de 2025.

Com um preço de 199 dólares, o Passport posiciona-se como uma carteira de hardware topo de gama, competindo com o Coldcard Q, Jade Plus, Tezor Safe 5 e os modelos topo de gama da Ledger.

![Image](assets/fr/01.webp)

Para gerir a sua carteira segura num Passport, tem várias opções. Esta carteira de hardware é compatível com a maioria dos softwares de gestão de carteiras do mercado, incluindo Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, entre outros. Neste tutorial, vamos aprender a usá-la com a Sparrow Wallet.

Se é um principiante, a opção mais fácil é utilizar o seu Passport com a aplicação nativa Envoy, desenvolvida pela Foundation. Para saber como utilizar o Envoy com o seu Passport, consulte este outro tutorial :

https://planb.network/tutorials/wallet/mobile/envoy-3ae5d6c7-623b-45b3-bb34-abcf9572b7cb

## Desembalar o Passaporte

Quando receber o seu Passport, certifique-se de que a caixa e o selo da embalagem estão intactos para confirmar que a embalagem não foi aberta. Será também efectuada uma verificação de software da autenticidade e integridade do dispositivo quando este for configurado.

![Image](assets/fr/02.webp)

O conteúdo da caixa inclui :


- Passaporte;
- Um pedaço de cartão para escrever a sua frase mnemónica;
- Um cabo USB-C para carregamento ;
- Cartão microSD ;
- Dois adaptadores MicroSD para Lightning ou USB-C ;
- Autocolantes.

No dispositivo, encontrará :


- Um teclado (1) ;
- Porta USB-C (2);
- Um botão de apagar (3);
- Um botão de retorno (4) ;
- Um botão de confirmação (5);
- Almofada direcional (6);
- Botão de ligar/desligar (7);
- Um indicador de estado (8);
- Porta microSD (9) ;
- Um botão para mudar de modo aA1 (10) ;
- Uma câmara traseira.

![Image](assets/fr/03.webp)

## Passaporte inicial

Prima o botão ligar/desligar na parte lateral do aparelho para o pôr a funcionar.

![Image](assets/fr/04.webp)

Prima o botão de confirmação para aceder ao menu seguinte.

![Image](assets/fr/05.webp)

Neste tutorial, vamos utilizar a Sparrow Wallet para gerir a carteira protegida por passaporte. Selecione "*Configuração manual*".

![Image](assets/fr/06.webp)

Em seguida, aceite as condições de utilização.

![Image](assets/fr/07.webp)

O passo seguinte consiste em verificar o seu dispositivo. Este procedimento confirma a autenticidade do seu passaporte e garante que este não foi adulterado durante o transporte. Ser-lhe-á pedido que digitalize um código QR.

![Image](assets/fr/08.webp)

Aceda ao [sítio oficial de verificação] (https://validate.foundationdevices.com/) e selecione "*Passport*".

![Image](assets/fr/09.webp)

Utilize a câmara do seu passaporte para digitalizar o código QR apresentado no sítio.

![Image](assets/fr/10.webp)

O seu dispositivo apresentará 4 palavras.

![Image](assets/fr/11.webp)

Introduza estas palavras no sítio Web para confirmar a autenticidade do seu passaporte e clique em "*Validate*".

![Image](assets/fr/12.webp)

Se aparecer a mensagem "*Passed*", a sua carteira de hardware é genuína. Pode agora utilizá-la para proteger uma carteira Bitcoin.

![Image](assets/fr/13.webp)

Confirme o resultado do teste no seu passaporte.

![Image](assets/fr/14.webp)

## Definir o código PIN

Segue-se o passo do código PIN. O código PIN desbloqueia o seu passaporte. Por conseguinte, proporciona proteção contra o acesso físico não autorizado. O código PIN não está envolvido na derivação das chaves criptográficas da sua carteira. Assim, mesmo sem acesso ao código PIN, a posse da sua frase mnemónica de 12 ou 24 palavras permitir-lhe-á recuperar o acesso aos seus bitcoins.

![Image](assets/fr/15.webp)

Recomendamos que escolha um código PIN que seja o mais aleatório possível. Além disso, certifique-se de que guarda este código num local diferente daquele onde o seu Passaporte está guardado (por exemplo, num gestor de palavras-passe).

Pode escolher um código PIN entre 6 e 12 dígitos. Aconselho-o a ser o mais longo possível.

Utilize o teclado para introduzir os seus números PIN. Quando tiver terminado, clique no botão de confirmação.

![Image](assets/fr/16.webp)

Confirme o seu PIN uma segunda vez.

![Image](assets/fr/17.webp)

O seu código PIN foi registado.

![Image](assets/fr/18.webp)

## Atualizar o firmware do Passport

A sua carteira de hardware sugere que actualize o firmware. Recomendo que actualize imediatamente para beneficiar das melhorias e correcções introduzidas pelas versões mais recentes. Para continuar, clique no botão de confirmação à direita.

![Image](assets/fr/19.webp)

O Passport está pronto para receber o novo firmware através de um cartão MicroSD.

![Image](assets/fr/20.webp)

Para o fazer, utilize o cartão MicroSD incluído na caixa do Passport (ou outro) e insira-o no computador. Descarregue a versão mais recente do firmware a partir do [sítio de documentação da Fundação] (https://docs.foundation.xyz/firmware-updates/passport/) ou [do seu repositório GitHub] (https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Antes de o instalar no seu dispositivo, aconselhamos vivamente que verifique a autenticidade e a integridade do firmware descarregado. Se precisar de ajuda para o fazer, consulte este tutorial :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Depois de verificar o arquivo `.bin`, coloque-o no seu MicroSD e insira-o no Passport. O explorador de arquivos do Passport será aberto. Selecione o ficheiro `vN.N.N-passport.bin`.

![Image](assets/fr/22.webp)

Clique em "*Selecionar*".

![Image](assets/fr/23.webp)

Em seguida, confirmar a instalação do firmware.

![Image](assets/fr/24.webp)

Aguarde que a atualização seja concluída.

![Image](assets/fr/25.webp)

Quando a atualização estiver concluída, introduza o seu código PIN para desbloquear o dispositivo e continuar a configuração.

![Image](assets/fr/26.webp)

## Criar uma nova carteira Bitcoin

Agora é altura de criar uma nova carteira Bitcoin. Clique no botão de confirmação.

![Image](assets/fr/27.webp)

Para criar uma nova carteira, clique em "*Criar nova semente*".

![Image](assets/fr/28.webp)

Pode escolher entre uma frase mnemónica de 12 ou 24 palavras. A segurança oferecida por ambas as opções é semelhante, pelo que pode optar pela que for mais fácil de guardar, ou seja, 12 palavras.

![Image](assets/fr/29.webp)

Clique em "*Continuar*".

![Image](assets/fr/30.webp)

O seu Passport irá agora gerar o seu "*Backup Code*". Trata-se de uma série de números que podem ser utilizados para desencriptar uma cópia de segurança da sua carteira armazenada num MicroSD. Este sistema de backup, específico para dispositivos Foundation, constitui um backup adicional à sua frase mnemónica, mas não é compatível com outro software Bitcoin.

Se decidir utilizar este "*Código de Backup*", certifique-se de que o guarda num local diferente do seu MicroSD que contém o backup encriptado da sua carteira. Pode, no entanto, optar por não utilizar este sistema se considerar que uma boa cópia de segurança da sua frase mnemónica é suficiente.

![Image](assets/fr/31.webp)

Introduza o seu "*Código de cópia de segurança*" para confirmar que o guardou corretamente.

![Image](assets/fr/32.webp)

Se tiver sido inserido um MicroSD, a cópia de segurança encriptada da sua carteira foi aí guardada.

![Image](assets/fr/33.webp)

O seu passaporte apresentará a sua frase mnemónica de 12 palavras. Esta mnemónica dá-lhe acesso total e sem restrições a todos os seus bitcoins. Qualquer pessoa na posse desta frase pode roubar os seus fundos, mesmo sem acesso físico ao seu Passaporte.

A frase de 12 palavras restaura o acesso aos seus bitcoins em caso de perda, roubo ou quebra do seu passaporte. Por isso, é muito importante guardá-lo cuidadosamente e armazená-lo num local seguro.

Pode gravá-lo no cartão fornecido na caixa ou, para maior segurança, recomendo que o grave numa base de aço inoxidável para o proteger de incêndios, inundações ou desmoronamentos.

Clique no botão de confirmação para ver a sua frase mnemónica.

![Image](assets/fr/34.webp)

Para mais informações sobre a forma correta de guardar e gerir a sua frase mnemónica, recomendo vivamente que siga este outro tutorial, especialmente se for um principiante:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

é claro que nunca deve partilhar estas palavras na Internet, como eu estou a fazer neste tutorial. Este exemplo de portefólio será utilizado apenas na Testnet e será eliminado no final do tutorial

Fazer uma cópia de segurança física desta frase.

![Image](assets/fr/35.webp)

O seu Passaporte foi configurado com sucesso. Clique no botão de confirmação para continuar.

![Image](assets/fr/36.webp)

## Descoberta do menu

A interface do Passport tem três menus principais:


- "*Conta*";
- "*Mais*";
- "*Configurações*".

Para navegar entre estes menus, utilize as setas esquerda e direita do teclado direcional.

### *Menu "Conta*

No menu "*Account*", encontra as principais funcionalidades da sua carteira Bitcoin. Pode assinar uma transação através da câmara ou da porta MicroSD.

![Image](assets/fr/37.webp)

O submenu "*Ferramentas de conta*" oferece opções como a verificação de um endereço, a assinatura de uma mensagem ou a consulta dos endereços da sua carteira.

![Image](assets/fr/38.webp)

No submenu "*Manage Account*" (Gerir conta*), pode ligar a sua carteira Bitcoin a um software de gestão de carteiras (que abordaremos nos próximos passos deste tutorial), ou ver e mudar o nome da sua conta.

![Image](assets/fr/39.webp)

### Mais" menu

No menu "*Mais*", pode criar uma nova conta na sua carteira, associada à mesma frase mnemónica.

![Image](assets/fr/40.webp)

Também pode introduzir uma frase-chave BIP39 (ver secção seguinte) ou utilizar uma semente temporária.

![Image](assets/fr/41.webp)

### Menu "Definições

No menu "*Definições*", encontrará todas as definições da sua carteira e do seu dispositivo.

![Image](assets/fr/42.webp)

O submenu "*Dispositivo*" dá-lhe opções para personalizar o brilho do ecrã, definir o atraso antes do bloqueio automático, alterar o código PIN ou mudar o nome do dispositivo.

![Image](assets/fr/43.webp)

O submenu "*Backup*" permite-lhe exportar a sua cópia de segurança encriptada da carteira, verificar a validade de uma cópia de segurança existente ou procurar novamente o seu "*Código de cópia de segurança*".

![Image](assets/fr/44.webp)

O submenu "*Firmware*" serve para atualizar o firmware do Passport. Recomendamos que efectue estas actualizações regularmente para beneficiar das últimas correcções e funcionalidades.

![Image](assets/fr/45.webp)

O sub-menu "*Bitcoin*" permite-lhe alterar a unidade apresentada (BTC ou satoshis), gerir uma possível carteira Multisig ou mudar para o modo "*Testnet*".

![Image](assets/fr/46.webp)

Em "*Avançado*", pode ver as palavras da sua frase mnemónica, realizar acções no MicroSD inserido, repor as definições de fábrica do Passport ou realizar uma verificação de autenticidade, tal como foi feito anteriormente.

![Image](assets/fr/47.webp)

Pode ativar "*Palavras de segurança*", uma função que acrescenta uma camada de segurança, apresentando duas palavras específicas ao desbloquear o dispositivo depois de introduzir os primeiros quatro dígitos do código PIN. Estas palavras, que devem ser guardadas durante a configuração, garantem que o Passport não foi substituído ou adulterado. Em caso de discrepância numa data posterior, aconselhamos a não utilizar o dispositivo. Aconselho-o a ativar esta opção para evitar a maioria dos riscos de comprometimento físico do dispositivo.

![Image](assets/fr/48.webp)

Por fim, o sub-menu "*Extensões*" permite ativar funções específicas para determinadas utilizações do aparelho, como o protocolo coinjoin da Whirlpool.

![Image](assets/fr/49.webp)

## Adicionar uma frase-passe BIP39

Antes de continuar, se desejar, pode acrescentar uma frase-passe BIP39. Uma frase-passe BIP39 é uma palavra-passe opcional que pode escolher livremente e que é adicionada à sua frase mnemónica para reforçar a segurança da carteira. Com esta funcionalidade activada, o acesso à sua carteira Bitcoin requer tanto a mnemónica como a frase-chave. Sem ambos, seria impossível recuperar a carteira.

Antes de configurar esta opção no seu Passport, recomenda-se vivamente a leitura deste artigo para compreender totalmente o funcionamento teórico da frase-chave e evitar erros que possam levar à perda das suas bitcoins:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Para o ativar, vá ao menu "*Mais*" e clique em "*Enter Passphrase*".

![Image](assets/fr/50.webp)

Introduza a sua frase-chave utilizando o teclado aA1 e certifique-se de que a guarda uma ou mais vezes num suporte físico (papel ou metal). Para o exemplo, estou a utilizar uma frase-chave muito fraca, mas deve escolher uma frase-chave forte e aleatória, incluindo todos os tipos de caracteres e suficientemente longa (como uma palavra-passe forte).

![Image](assets/fr/51.webp)

Tenha em atenção que as frases-passe BIP39 são sensíveis a maiúsculas e minúsculas. Se introduzir uma frase-chave ligeiramente diferente da inicialmente configurada, o Passport não comunicará um erro, mas obterá outro conjunto de chaves criptográficas que não serão as da sua carteira inicial.

Portanto, é importante, ao configurar, anotar em algum lugar a impressão digital da chave mestra que será dada no próximo passo. Por exemplo, com a minha frase-passe `Plan B Network`, a impressão digital da minha chave-mestra é `745D526B`.

![Image](assets/fr/52.webp)

Sempre que desbloquear o Passport, terá de regressar a este menu para introduzir a frase-chave e aplicá-la à sua carteira. O Passport não guarda a frase-chave.

Cada vez que desbloquear, depois de escrever a frase-chave, verifique neste ecrã de confirmação se a impressão digital fornecida é a mesma que escreveu durante a configuração. Se for, a sua frase-chave está correta e está a aceder à carteira Bitcoin correta. Se não for, está na carteira errada e tem de tentar novamente, tendo o cuidado de não cometer erros de introdução.

Antes de receberes os teus primeiros bitcoins na tua carteira, **aconselho-te vivamente a fazeres um teste de recuperação vazio**. Tome nota de algumas informações de referência, como o seu xpub ou o primeiro endereço de receção, e depois apague a sua carteira no Passport enquanto ainda está vazia (`Configurações -> Avançado -> Apagar Passport`). Em seguida, tente restaurar a sua carteira utilizando as cópias de segurança em papel da frase mnemónica e de qualquer frase-chave. Verifique se a informação do cookie gerada após o restauro corresponde à que escreveu originalmente. Se corresponder, pode ter a certeza de que as suas cópias de segurança em papel são fiáveis. Para saber mais sobre como efetuar uma recuperação de teste, consulte este outro tutorial :

https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

![Image](assets/fr/53.webp)

## Configurar a carteira na Sparrow Wallet

Neste tutorial, vou mostrar-vos uma utilização avançada do Passport com a Sparrow Wallet. No entanto, esta carteira de hardware também é compatível com Envoy (a aplicação Foundation), Keeper, BlueWallet, Nunchuk, Specter, e muitos outros...

Comece por descarregar e instalar a Sparrow Wallet [a partir do site oficial] (https://sparrowwallet.com/) no seu computador, caso ainda não o tenha feito.

![Image](assets/fr/54.webp)

Certifique-se de que verifica a autenticidade e a integridade do software antes da instalação. Se não souber como o fazer, consulte este tutorial:

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Quando a Sparrow Wallet estiver aberta, clique no separador "*Arquivo*" e depois em "*Nova carteira*".

![Image](assets/fr/55.webp)

Dê um nome à sua carteira e, em seguida, clique em "*Criar carteira*".

![Image](assets/fr/56.webp)

Selecione "*Airgapped Hardware Wallet*".

![Image](assets/fr/57.webp)

Clique em "*Scan...*" junto à opção "*Passaporte*". Isto irá abrir a sua câmara Web.

![Image](assets/fr/58.webp)

Na sua carteira de hardware, aceda ao menu "*Conta*", selecione o submenu "*Gerir conta*" e clique em "*Ligar carteira*".

![Image](assets/fr/59.webp)

Na lista pendente que aparece, selecione "*Sparrow*".

![Image](assets/fr/60.webp)

Em seguida, selecione "*Single-sig*" para uma configuração normal, sem multisig.

![Image](assets/fr/61.webp)

Selecionar a opção "*Código QR*".

![Image](assets/fr/62.webp)

O seu Passaporte irá então gerar códigos QR dinâmicos. Utilize a câmara Web do seu computador para os digitalizar para o software Sparrow.

![Image](assets/fr/63.webp)

Deve ver agora o seu xpub e a impressão digital da sua chave mestra, que deve corresponder à que aparece no seu Passaporte quando introduz a sua frase-chave. Clique no botão "*Aplicar*".

![Image](assets/fr/64.webp)

Defina uma palavra-passe forte para proteger o acesso à sua Sparrow Wallet. Esta senha protegerá suas chaves públicas, endereços, etiquetas e histórico de transações de acessos não autorizados. É uma boa ideia guardar esta palavra-passe num gestor de palavras-passe, para que não se esqueça dela.

![Image](assets/fr/65.webp)

O Passport pede-lhe então que digitalize o primeiro endereço de receção para confirmar que a importação foi bem sucedida.

![Image](assets/fr/66.webp)

No Sparrow, vá ao separador "*Receber*" e digitalize o código QR do primeiro endereço.

![Image](assets/fr/67.webp)

Se a operação for bem sucedida, o seu passaporte apresentará a indicação "*Verificado*".

![Image](assets/fr/68.webp)

Isto confirma que a importação foi bem sucedida.

![Image](assets/fr/69.webp)

## Receber bitcoins

Agora que o seu Passport está configurado, está pronto para receber os seus primeiros sats na sua nova carteira Bitcoin. Para isso, no Sparrow, clique no menu "*Receive*".

![Image](assets/fr/70.webp)

O Sparrow mostrará o primeiro endereço de recibo em branco no seu portefólio. Pode adicionar uma etiqueta.

![Image](assets/fr/71.webp)

Antes de o utilizar, vamos verificar o endereço no ecrã do Passport para nos certificarmos de que pertence à nossa carteira Bitcoin. No Sparrow, podes ampliar o código QR do endereço clicando nele, se necessário. No menu "*Account*" do Passport, selecione "*Account Tools*".

![Image](assets/fr/72.webp)

Clique em "*Verificar endereço*" e, em seguida, digitalize o código QR apresentado na Sparrow Wallet.

![Image](assets/fr/73.webp)

Certifique-se de que o endereço indicado no passaporte corresponde exatamente ao indicado no Sparrow e de que aparece "*Verificado*".

![Image](assets/fr/74.webp)

Agora pode usá-lo para receber bitcoins. Quando a transação for transmitida na rede, aparecerá no Sparrow. Aguarde até ter recebido confirmações suficientes para considerar a transação definitiva.

![Image](assets/fr/75.webp)

## Enviar bitcoins

Agora que já tens alguns sats na tua carteira, também podes enviar alguns. Para o fazer, clique no menu "*UTXOs*".

![Image](assets/fr/76.webp)

Selecione os UTXOs que pretende utilizar como entradas para esta transação e, em seguida, clique em "*Enviar selecionados*".

![Image](assets/fr/77.webp)

Introduza o endereço do destinatário, uma etiqueta para recordar o objetivo da transação e o montante que pretende enviar para esse endereço.

![Image](assets/fr/78.webp)

Ajuste a taxa de honorários de acordo com as condições actuais do mercado e, em seguida, clique em "*Criar transação*".

![Image](assets/fr/79.webp)

Verifique se todos os parâmetros da transação estão corretos e, em seguida, clique em "*Finalizar transação para assinatura*".

![Image](assets/fr/80.webp)

Clique em "*Show QR*" para exibir a PSBT (*Partially Signed Bitcoin Transaction*). O Sparrow construiu a transação, mas ainda faltam as assinaturas para desbloquear os bitcoins usados na entrada. Essas assinaturas só podem ser realizadas pelo Passport, que hospeda sua semente dando acesso às chaves privadas necessárias para assinar a transação.

![Image](assets/fr/81.webp)

No seu Passport, aceda ao menu "*Conta*" e clique em "*Assinar com código QR*".

![Image](assets/fr/82.webp)

Digitalize o PSBT (*Transação Bitcoin Parcialmente Assinada*) apresentado na Sparrow Wallet.

![Image](assets/fr/83.webp)

Confirmar se o endereço de receção e o montante enviado estão corretos e, em seguida, premir o botão de confirmação.

![Image](assets/fr/84.webp)

Verificar o endereço de troca. No meu exemplo, não existe nenhum, uma vez que a transação inclui uma única saída.

![Image](assets/fr/85.webp)

Certifique-se de que a taxa é a que escolheu.

![Image](assets/fr/86.webp)

Se todas as informações estiverem corretas, clique no botão de confirmação para assinar a transação.

![Image](assets/fr/87.webp)

Na Sparrow Wallet, clique em "*Scan QR*" e digitalize o código QR apresentado no seu Passaporte.

![Image](assets/fr/88.webp)

A sua transação assinada está agora pronta para ser transmitida na rede Bitcoin e incluída num bloco por um mineiro. Se tudo estiver correto, clique em "*Broadcast Transaction*".

![Image](assets/fr/89.webp)

A sua transação foi transmitida e está a aguardar confirmação.

![Image](assets/fr/90.webp)

Parabéns, agora já sabe como configurar e utilizar o Passport. Se achou este tutorial útil, agradecia que deixasse um polegar verde abaixo. Não hesite em partilhar este artigo nas suas redes sociais. Obrigado por partilhar!

Para mais informações, consulte o nosso tutorial sobre o software Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
