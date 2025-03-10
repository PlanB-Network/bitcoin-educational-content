---
name: Enviado
description: Configurar e utilizar um Passaporte com a aplicação Envoy
---
![cover](assets/cover.webp)

Envoy é uma aplicação de gestão de carteiras Bitcoin desenvolvida pela Foundation. Foi especialmente concebida para ser utilizada com a carteira de hardware Passport.

O Passport "*Batch 2*" que apresentamos neste tutorial com a aplicação Envoy é o sucessor do "*Founder's Edition*". Apresenta um design premium, um ecrã a cores de alta definição e um teclado físico ergonómico. Funciona em modo "*Air-Gap*", assegurando que as chaves privadas da sua carteira permanecem totalmente isoladas, com trocas possíveis através de um cartão MicroSD ou códigos QR. O dispositivo inclui uma bateria amovível de 1200 mAh.

Quanto à conetividade, o Passport está equipado com uma porta MicroSD, uma porta USB-C para carregamento e uma câmara traseira para leitura de códigos QR.

Em termos de segurança, o Passport incorpora um elemento seguro e o código-fonte do dispositivo é totalmente open-source. Ele oferece todas as caraterísticas esperadas de uma boa carteira de hardware Bitcoin. Note-se que o Passport ainda não suporta miniscript, mas esta funcionalidade está planeada para o segundo trimestre de 2025.

Com um preço de 199 dólares, o Passport posiciona-se como uma carteira de hardware topo de gama, competindo com o Coldcard Q, Jade Plus, Tezor Safe 5 e os modelos topo de gama da Ledger.

![Image](assets/fr/01.webp)

Para gerir a sua carteira segura num Passport, tem várias opções. Esta carteira de hardware é compatível com a maioria dos softwares de gestão de carteiras no mercado, incluindo Sparrow Wallet, Specter Desktop, Nunchuk, Keeper, entre outros.

Neste tutorial, destinado a utilizadores principiantes e intermédios, vamos descobrir como utilizar a aplicação Envoy com o seu Passport. É a forma mais fácil de tirar o máximo partido da sua carteira de hardware.

Se for um utilizador avançado e quiser explorar funcionalidades mais complexas, recomendo que consulte este outro tutorial onde configuramos o Passport com a Sparrow Wallet :

https://planb.network/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

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

## Descarregar a aplicação Envoy

Aceda à sua loja de aplicações para descarregar o Envoy :


- Na [Google Play Store] (https://play.google.com/store/apps/details?id=com.foundationdevices.envoy);
- Na [App Store] (https://apps.apple.com/us/app/envoy-by-foundation/id1584811818);
- Em [F-Cold](https://foundation.xyz/fdroid/).

![Image](assets/fr/50.webp)

Também pode descarregar o ficheiro APK diretamente [do repositório GitHub da Fundação] (https://github.com/Foundation-Devices/envoy/releases).

![Image](assets/fr/51.webp)

Quando a aplicação estiver aberta, selecione "*Manage Passport*" (Gerir passaporte).

![Image](assets/fr/52.webp)

Escolha se pretende ativar a ligação Tor para reforçar a confidencialidade e, em seguida, prima "*Continuar*".

![Image](assets/fr/53.webp)

Escolha "*Ligar um Passport existente*" se o seu Passport já estiver configurado ou "*Configurar um novo Passport*" se estiver a inicializar a sua carteira de hardware pela primeira vez.

![Image](assets/fr/54.webp)

Aceitar as condições de utilização.

![Image](assets/fr/55.webp)

De seguida, ser-lhe-á pedido que verifique a autenticidade do passaporte. Clique em "*Next*".

![Image](assets/fr/56.webp)

## Passaporte inicial

Prima o botão ligar/desligar na parte lateral do aparelho para o pôr a funcionar.

![Image](assets/fr/04.webp)

Prima o botão de confirmação para aceder ao menu seguinte.

![Image](assets/fr/05.webp)

Neste tutorial, utilizaremos o Envoy para gerir a carteira protegida por passaporte. Selecione "*Envoy App*".

![Image](assets/fr/57.webp)

Clicar em "*Continuar no Envoy*".

![Image](assets/fr/58.webp)

O passo seguinte consiste em verificar o seu dispositivo. Este procedimento confirma a autenticidade do seu passaporte e garante que este não foi adulterado durante o transporte. Ser-lhe-á pedido que digitalize um código QR.

![Image](assets/fr/08.webp)

Digitalize os códigos QR dinâmicos apresentados na aplicação com o seu passaporte. Quando a leitura estiver concluída, clique em "*Próximo*".

![Image](assets/fr/59.webp)

Em seguida, utilize o seu telemóvel para digitalizar o código QR apresentado no seu passaporte.

![Image](assets/fr/60.webp)

Se aparecer a mensagem "*Your Passport is secure*", isto confirma que a sua carteira de hardware é genuína. Pode agora utilizá-la para proteger uma carteira Bitcoin.

![Image](assets/fr/61.webp)

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

### Sem a aplicação Envoy

Para o fazer, utilize o cartão MicroSD incluído na caixa do Passport (ou outro) e insira-o no computador. Descarregue a versão mais recente do firmware a partir do [sítio de documentação da Fundação] (https://docs.foundation.xyz/firmware-updates/passport/) ou [do seu repositório GitHub] (https://github.com/Foundation-Devices/passport2/releases).

![Image](assets/fr/21.webp)

Antes de o instalar no seu dispositivo, aconselhamos vivamente que verifique a autenticidade e a integridade do firmware descarregado. Se precisar de ajuda para o fazer, consulte este tutorial :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

### Com a aplicação Envoy

A outra opção, mais simples, é utilizar diretamente a aplicação Envoy. Clique em "*Download Firmware*".

![Image](assets/fr/62.webp)

Utilize o adaptador fornecido com o Passport para ligar o cartão MicroSD ao telemóvel.

![Image](assets/fr/63.webp)

Selecione o cartão MicroSD no seu explorador de ficheiros para guardar o firmware.

![Image](assets/fr/64.webp)

O firmware está agora guardado. Retire o MicroSD do seu smartphone e insira-o no Passport.

![Image](assets/fr/65.webp)

Será aberto o explorador de ficheiros Passport. Selecione o arquivo `vN.N.N-passport.bin`.

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

## Configurar a carteira no Envoy

Neste tutorial, vou mostrar-lhe como utilizar o Passport com a aplicação Envoy. No entanto, esta carteira de hardware também é compatível com Sparrow Wallet, Keeper, BlueWallet, Nunchuk, Specter e muitos outros...

![Image](assets/fr/66.webp)

Utilize a aplicação Envoy para digitalizar o código QR apresentado no seu passaporte.

![Image](assets/fr/67.webp)

As suas chaves públicas são agora importadas para a aplicação. Clique em "*Validar endereço de receção*".

![Image](assets/fr/68.webp)

Utilize o seu passaporte para digitalizar o endereço apresentado no Envoy.

![Image](assets/fr/69.webp)

O seu passaporte confirmará se a carteira importada na Envoy é válida. Confirme-o na aplicação.

![Image](assets/fr/70.webp)

Pode agora aceder às informações públicas da sua carteira no Envoy, mas para gastar bitcoins, terá de utilizar o seu Passaporte.

![Image](assets/fr/71.webp)

## Descubra os menus do Passport

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

Também é possível introduzir uma frase-chave BIP39 ou utilizar uma semente temporária.

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

## Receber bitcoins

Agora que o seu Passaporte está configurado, está pronto para receber os seus primeiros sats na sua nova carteira Bitcoin. Para o fazer, no Envoy, clique na sua conta "*Primary 0*".

![Image](assets/fr/72.webp)

Clique no botão "*Receber*".

![Image](assets/fr/73.webp)

A sua aplicação Envoy apresenta o primeiro endereço em branco disponível na sua carteira. Antes de o utilizar, vamos verificar o endereço no ecrã do Passport para nos certificarmos de que pertence realmente à nossa carteira Bitcoin. No menu "*Account*" do seu Passport, selecione "*Account Tools*".

![Image](assets/fr/74.webp)

Clique em "*Verificar endereço*" e, em seguida, digitalize o código QR apresentado no Envoy.

![Image](assets/fr/75.webp)

Certifique-se de que o endereço indicado no passaporte corresponde exatamente ao indicado no Sparrow e de que aparece "*Verificado*".

![Image](assets/fr/76.webp)

Agora pode usá-lo para receber bitcoins. Quando a transação for transmitida na rede, aparecerá no Envoy. Aguarde até ter recebido confirmações suficientes para considerar a transação definitiva.

![Image](assets/fr/77.webp)

## Enviar bitcoins

Agora que já tens alguns sats na tua carteira, também podes enviar alguns. Para o fazer, clica no botão "*Enviar*".

![Image](assets/fr/78.webp)

Introduza o endereço do destinatário, quer colando-o diretamente, quer digitalizando o código QR com a câmara do seu smartphone.

![Image](assets/fr/79.webp)

Determine o montante que pretende enviar e, em seguida, clique em "*Confirmar*".

![Image](assets/fr/80.webp)

Selecione a taxa de transação de acordo com a situação atual do mercado e, em seguida, verifique as informações da transação. Se tudo estiver correto, clique em "*Assinar com passaporte*".

![Image](assets/fr/81.webp)

Adicione uma etiqueta à sua transação para manter um registo claro da sua finalidade.

![Image](assets/fr/82.webp)

O Envoy então exibe um PSBT (*Transação de Bitcoin Parcialmente Assinada*). O aplicativo construiu a transação, mas ainda falta a(s) assinatura(s) para desbloquear os bitcoins usados na entrada. Essas assinaturas só podem ser realizadas pelo Passport, que hospeda sua semente dando acesso às chaves privadas necessárias para assinar a transação.

![Image](assets/fr/83.webp)

No seu Passport, aceda ao menu "*Conta*" e clique em "*Assinar com código QR*".

![Image](assets/fr/84.webp)

Digitalize o PSBT (*Transação Bitcoin Parcialmente Assinada*) apresentado no Envoy.

![Image](assets/fr/85.webp)

Confirmar se o endereço de receção e o montante enviado estão corretos e, em seguida, premir o botão de confirmação.

![Image](assets/fr/86.webp)

Verificar o endereço de troca. No meu exemplo, não existe nenhum, uma vez que a transação inclui uma única saída.

![Image](assets/fr/87.webp)

Certifique-se de que a taxa é a que escolheu.

![Image](assets/fr/88.webp)

Se todas as informações estiverem corretas, clique no botão de confirmação para assinar a transação.

![Image](assets/fr/89.webp)

O seu passaporte mostra-lhe a transação assinada sob a forma de um código QR.

![Image](assets/fr/90.webp)

Na aplicação Envoy, clique no ícone do código QR e, em seguida, digitalize o PSBT apresentado no ecrã do seu passaporte.

![Image](assets/fr/91.webp)

Verifique os detalhes da sua transação uma última vez. Se tudo estiver correto, prima "*Enviar transação*" para a transmitir na rede Bitcoin.

![Image](assets/fr/92.webp)

A sua transação está agora a aguardar confirmação. Pode acompanhar o estado da mesma diretamente a partir da sua conta.

![Image](assets/fr/93.webp)

Parabéns, agora já sabe como configurar e utilizar o Passport com a aplicação Envoy. Se achou este tutorial útil, agradecia que deixasse um polegar verde abaixo. Sinta-se à vontade para partilhar este artigo nas suas redes sociais. Obrigado por partilhar!

Para mais informações, consulte o nosso tutorial sobre o software Liana:

https://planb.network/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04
